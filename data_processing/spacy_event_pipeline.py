# data_processing/services/spacy_event_pipeline.py
from __future__ import annotations

import re
from typing import List, Dict, Any, Optional, Set, Tuple

import spacy
from spacy.language import Language
from spacy.pipeline import EntityRuler
from spacy.tokens import Span
from spacy.util import filter_spans

from data_processing.models import (
    IntelligenceReport,
    Entity,
    EntityIntelligenceReport,
)
from data_processing.services.relationLevelCalculator import relationLevelCalculator

# -----------------------------
# 1) EVENT TRIGGERS (rule-based)
# -----------------------------
EVENT_TRIGGERS = {
    "DRUG_DEALING": [
        r"\bdeal(?:ing)?\b",
        r"\bsell(?:ing)?\b",
        r"\bsupp(?:ly|lying)\b",
        r"\bhand(?:ing)?\s+packages?\b",
        r"\bwraps?\b",
    ],
    "ASSAULT": [
        r"\bassault(?:ed)?\b",
        r"\battack(?:ed)?\b",
        r"\bstabb(?:ed|ing)\b",
        r"\bpunch(?:ed|ing)\b",
        r"\bhit\b",
    ],
    "WEAPON_POSSESSION": [
        r"\bknife\b",
        r"\bmachete\b",
        r"\bfirearm\b",
        r"\bgun\b",
        r"\bweapon\b",
        r"\bpossession\b",
    ],
    "VEHICLE_SIGHTING": [
        r"\bseen\b",
        r"\bobserved\b",
        r"\bdriving\b",
        r"\bvehicle\b",
        r"\breg(?:istration)?\b",
        r"\bplate\b",
    ],
    "PRISON_RELEASE": [
        r"\breleased\s+on\s+licen[cs]e\b",
        r"\breleased\s+from\s+prison\b",
    ],
    "ASSOCIATION": [
        r"\bassociat(?:ing|ed)\s+with\b",
        r"\bseen\s+with\b",
        r"\bmeeting\b",
    ],
}

def split_into_blocks(text: str) -> List[str]:
    return [b.strip() for b in re.split(r"\n\s*\n+", text) if b.strip()]

def ents_in_span(doc, start_char: int, end_char: int, labels: Optional[Set[str]] = None):
    out = []
    for e in doc.ents:
        if e.start_char >= start_char and e.end_char <= end_char:
            if labels is None or e.label_ in labels:
                out.append(e)
    return out

def last_person_before(ents, trigger_abs_start: int) -> Optional[str]:
    persons = [e for e in ents if e.label_ == "PERSON" and e.end_char <= trigger_abs_start]
    return persons[-1].text if persons else None

def _pick_texts(block_ents, sent_ents, labels: Set[str], limit: int = 2) -> List[str]:
    s = [e.text for e in sent_ents if e.label_ in labels]
    if s:
        return s[:limit]
    b = [e.text for e in block_ents if e.label_ in labels]
    return b[:limit]

def extract_events_from_block(doc) -> List[Dict[str, Any]]:
    events: List[Dict[str, Any]] = []
    block_ents = list(doc.ents)
    block_persons = [e.text for e in block_ents if e.label_ == "PERSON"]
    block_last_person = block_persons[-1] if block_persons else None

    compiled = []
    for etype, patterns in EVENT_TRIGGERS.items():
        for p in patterns:
            compiled.append((etype, re.compile(p, re.I)))

    for sent in doc.sents:
        sent_text = sent.text
        sent_start = sent.start_char
        sent_end = sent.end_char
        sent_ents = ents_in_span(doc, sent_start, sent_end)

        for etype, creg in compiled:
            m = creg.search(sent_text)
            if not m:
                continue

            trigger_text = m.group(0)
            trigger_abs_start = sent_start + m.start()

            suspect = last_person_before(sent_ents, trigger_abs_start) or block_last_person

            # DOB
            suspect_dob = None
            if suspect:
                suspect_ents = [e for e in block_ents if e.label_ == "PERSON" and e.text.strip() == suspect]
                if suspect_ents:
                    suspect_end = suspect_ents[0].end_char
                    dob_candidates = [e for e in block_ents if e.label_ == "DOB" and e.start_char >= suspect_end]
                    if dob_candidates:
                        dob_candidates.sort(key=lambda e: e.start_char)
                        suspect_dob = dob_candidates[0].text

            # Address
            suspect_home_addr = None
            if suspect:
                suspect_ents = [e for e in block_ents if e.label_ == "PERSON" and e.text.strip() == suspect]
                if suspect_ents:
                    suspect_end_pos = min(e.end_char for e in suspect_ents)
                    addr_ents = [e for e in block_ents if e.label_ == "ADDRESS" and e.start_char >= suspect_end_pos]
                    if addr_ents:
                        addr_ents.sort(key=lambda e: e.start_char)
                        suspect_home_addr = addr_ents[0].text

            # Date/time
            date_ents = [e.text for e in sent_ents if e.label_ == "DATE"]
            time_ents = [e.text for e in sent_ents if e.label_ == "TIME"]

            location = _pick_texts(block_ents, sent_ents, {"GPE", "LOC", "FAC", "ADDRESS"}, limit=1)
            vehicle = _pick_texts(block_ents, sent_ents, {"VEHICLE"}, limit=2)
            reg_plate = _pick_texts(block_ents, sent_ents, {"VEHICLE_REG"}, limit=2)

            # build
            ev = {
                "event_type": etype,
                "trigger": trigger_text,
                "suspect": suspect,
                "suspect_dob": suspect_dob,
                "date": date_ents[0] if date_ents else None,
                "time": time_ents[0] if time_ents else None,
                "location": location[0] if location else None,
                "home_address": suspect_home_addr,
                "vehicle": vehicle,
                "reg_plate": reg_plate,
                "evidence_text": sent_text.strip(),
            }

            score = 0
            if ev["suspect"]: score += 1
            if ev["date"]: score += 1
            if ev["time"]: score += 1
            if ev["location"]: score += 1
            if ev["vehicle"]: score += 1
            if ev["reg_plate"]: score += 1

            if score >= 2:
                events.append(ev)

            break

    return events

def extract_events(text: str, nlp) -> List[Dict[str, Any]]:
    all_events: List[Dict[str, Any]] = []
    for i, block in enumerate(split_into_blocks(text)):
        doc = nlp(block)
        evs = extract_events_from_block(doc)
        for ev in evs:
            ev["block_id"] = i
        all_events.extend(evs)
    return all_events

# -----------------------------
# 2) REGEX ENTITY COMPONENT
# -----------------------------
REG_VEHICLE_REG = re.compile(
    r"\bReg(?:istration)?\s*\.?\s*(?:No\.?|Number|#)?\s*[:\-]?\s*([A-Z0-9]{2,7})\b", re.I
)
REG_CRIME_GROUP_NAME = re.compile(r"\b(?!the\b)([A-Za-z]+)\s+crime\s+(?:group|family|gang)\b", re.I)
REG_OCG = re.compile(r"\b([A-Z]{3,})\s+OCG\b")
REG_DOB = re.compile(r"\bBn\.?\s*[:\-]?\s*(\d{2}/\d{2}/\d{4})\b", re.I)
REG_POSTCODE = re.compile(r"\b([A-Z]{1,2}\d{1,2}[A-Z]?\s*\d[A-Z]{2})\b", re.I)
REG_PHONE = re.compile(r"\b(07\d{9})\b")

REG_BLOCK_PERSON = re.compile(
    r"(?m)^\s*([A-Z][a-z]+)"
    r"(?:\s+(?:['‘’][^'‘’]{1,30}['‘’]))?"
    r"(?:\s+[A-Z][a-z]+)?"
    r"\s+([A-Z]{2,})\s*$"
)

REG_ADDRESS = re.compile(
    r"(?m)^\s*(\d{1,4}\s+[A-Z][A-Za-z'\-]*(?:\s+[A-Z][A-Za-z'\-]*)*\s+"
    r"(?:Road|Street|Drive|Avenue|Lane|Place|Crescent|Court|Terrace))\s*$"
)

REG_ALIAS = re.compile(
    r"\b(?P<uncertain>may\s+be|possibly|believed\s+to\s+be|thought\s+to\s+be|reported\s+to\s+be)?\s*"
    r"(?P<intro>aka|a\.k\.a\.|known\s+as|male\s+known\s+as)\s*"
    r"[:\-]?\s*"
    r"(?P<alias>[A-Za-z][A-Za-z0-9'’\-]{1,})\b",
    re.I,
)

@Language.component("regex_entities")
def regex_entities(doc):
    new_ents = list(doc.ents)
    text = doc.text

    def remove_overlaps(start, end):
        nonlocal new_ents
        new_ents = [e for e in new_ents if not (e.start_char < end and start < e.end_char)]

    def add_span(start, end, label):
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span:
            new_ents.append(span)

    for m in REG_BLOCK_PERSON.finditer(text):
        start, end = m.start(1), m.end(2)
        remove_overlaps(start, end)
        add_span(start, end, "PERSON")

    for m in REG_VEHICLE_REG.finditer(text):
        add_span(m.start(1), m.end(1), "VEHICLE_REG")

    for m in REG_CRIME_GROUP_NAME.finditer(text):
        add_span(m.start(1), m.end(1), "CRIME_GROUP")

    for m in REG_OCG.finditer(text):
        start, end = m.start(1), m.end(1)
        remove_overlaps(start, end)
        add_span(start, end, "CRIME_GROUP")

    for m in REG_DOB.finditer(text):
        start, end = m.start(1), m.end(1)
        remove_overlaps(start, end)
        span = doc.char_span(start, end, label="DOB", alignment_mode="expand")
        if span:
            new_ents.append(span)

    for m in REG_POSTCODE.finditer(text):
        add_span(m.start(1), m.end(1), "POSTCODE")

    for m in REG_PHONE.finditer(text):
        start, end = m.start(1), m.end(1)
        remove_overlaps(start, end)
        add_span(start, end, "PHONE")

    for m in REG_ALIAS.finditer(text):
        start, end = m.start("alias"), m.end("alias")
        remove_overlaps(start, end)
        label = "ALIAS_UNCERTAIN" if m.group("uncertain") else "ALIAS_CERTAIN"
        add_span(start, end, label)

    for m in REG_ADDRESS.finditer(text):
        start, end = m.start(1), m.end(1)
        remove_overlaps(start, end)
        add_span(start, end, "ADDRESS")

    surname_set = set()
    for ent in new_ents:
        if ent.label_ == "PERSON":
            parts = ent.text.strip().split()
            if len(parts) >= 2:
                surname = parts[-1]
                if surname.isupper() and surname.isalpha():
                    surname_set.add(surname)

    cleaned = []
    for e in new_ents:
        if e.label_ == "PERSON" and e.text.strip().lower() in {"glasgow", "paisley"}:
            continue
        if e.label_ == "PERSON" and e.text.strip().lower() == "bn":
            continue
        if e.label_ == "ORG":
            txt = e.text.strip()
            if txt in surname_set:
                cleaned.append(Span(doc, e.start, e.end, label="PERSON"))
                continue
        cleaned.append(e)

    doc.ents = filter_spans(cleaned)
    return doc

# -----------------------------
# 3) spaCy pipeline builder (cached)
# -----------------------------
_NLP = None

def get_nlp():
    global _NLP
    if _NLP is not None:
        return _NLP

    nlp = spacy.load("en_core_web_sm")

    ruler: EntityRuler = nlp.add_pipe("entity_ruler", before="ner")

    COLORS = ["black","white","silver","grey","gray","red","blue","yellow","green"]
    GENERIC_VEHICLES = ["car","vehicle","van","truck","lorry","motorbike","motorcycle","scooter","bike"]
    MAKES = ["bmw","audi","toyota","ford","vauxhall","mercedes","volkswagen","vw","nissan","honda","hyundai","kia","tesla","range","rover"]
    DRUGS = ["heroin", "cocaine", "ketamine", "cannabis", "ecstasy", "mdma"]

    ruler.add_patterns([
        {"label": "GROUP", "pattern": [{"LOWER": "group"}, {"LOWER": "of"}, {"LOWER": {"IN": ["teenagers", "males", "men", "women", "boys", "girls", "people"]}}]},
        {"label": "GROUP", "pattern": [{"LOWER": {"IN": ["different", "several", "multiple", "large"]}}, {"LOWER": {"IN": ["groups", "group"]}, "OP": "?"}, {"LOWER": {"IN": ["of"]}, "OP": "?"}, {"LOWER": {"IN": ["males", "men", "women", "teenagers", "people"]}}]},
        {"label": "GROUP", "pattern": [{"LIKE_NUM": True}, {"LOWER": "or"}, {"LIKE_NUM": True}, {"LOWER": {"IN": ["males", "men", "women", "teenagers", "people"]}}]},
        {"label": "ROLE", "pattern": [{"LOWER": {"IN": ["driver", "passenger", "owner", "enforcer", "courier"]}}]},
        {"label": "VEHICLE", "pattern": [{"LOWER": {"IN": GENERIC_VEHICLES}}]},
        {"label": "VEHICLE", "pattern": [{"LOWER": {"IN": COLORS}}, {"LOWER": {"IN": GENERIC_VEHICLES}}]},
        {"label": "VEHICLE", "pattern": [{"LOWER": {"IN": MAKES}}]},
        {"label": "VEHICLE", "pattern": [{"LOWER": {"IN": MAKES}}, {"TEXT": {"REGEX": r"^[A-Za-z0-9\-]{1,4}$"}, "OP": "?"}, {"LOWER": {"IN": ["series", "rover", "jeep"]}, "OP": "?"}]},
        {"label": "VEHICLE", "pattern": [{"LOWER": {"IN": COLORS}}, {"LOWER": {"IN": MAKES}}, {"TEXT": {"REGEX": r"^[A-Za-z0-9\-]{1,4}$"}, "OP": "?"}, {"LOWER": {"IN": ["series", "rover", "jeep"]}, "OP": "?"}]},
        {"label": "ITEM", "pattern": [{"LOWER": "wheelie"}, {"LOWER": "bins"}]},
        {"label": "ITEM", "pattern": [{"LOWER": {"IN": ["package", "packages", "knife", "knives", "bat", "hammer", "hammers"]}}]},
        {"label": "DRUG", "pattern": [{"LOWER": {"IN": DRUGS}}]},
        {"label": "DRUG", "pattern": [{"LOWER": "controlled"}, {"LOWER": "drugs"}]},
    ])

    nlp.add_pipe("regex_entities", last=True)

    _NLP = nlp
    return _NLP

# -----------------------------
# 4) Store extracted entities into DB for a report
# -----------------------------
def _get_or_create_entity(name: str, entity_type: str) -> Entity:
    name = (name or "").strip()
    if not name:
        raise ValueError("Empty entity name")
    obj, _ = Entity.objects.get_or_create(name=name, type=entity_type)
    return obj

def _link_entity_to_report(entity: Entity, report: IntelligenceReport) -> None:
    EntityIntelligenceReport.objects.get_or_create(entity=entity, report=report)

def extract_and_store_spacy_for_report(report_id: int) -> Dict[str, Any]:
    """
    Main entry for Django:
    - Takes IntelligenceReport.fullReport
    - Runs spaCy + regex entities + simple rule events
    - Stores Entities and links them to the report
    """
    report = IntelligenceReport.objects.get(pk=report_id)
    text = report.fullReport or ""

    nlp = get_nlp()
    doc = nlp(text)

    # 1) Store entities
    people = set()
    vehicles = set()
    telecom = set()
    locations = set()

    for ent in doc.ents:
        t = ent.text.strip()
        if not t:
            continue

        if ent.label_ in {"PERSON", "ALIAS_CERTAIN", "ALIAS_UNCERTAIN"}:
            people.add(t)
        if ent.label_ in {"VEHICLE", "VEHICLE_REG"}:
            vehicles.add(t)
        if ent.label_ in {"PHONE"}:
            telecom.add(t)
        if ent.label_ in {"GPE", "LOC", "FAC", "ADDRESS", "POSTCODE"}:
            locations.add(t)

    created_counts = {"people": 0, "vehicle": 0, "telecom": 0, "location": 0}

    for name in sorted(people):
        e = _get_or_create_entity(name, Entity.PEOPLE)
        _link_entity_to_report(e, report)
        created_counts["people"] += 1

    for name in sorted(vehicles):
        e = _get_or_create_entity(name, Entity.VEHICLE)
        _link_entity_to_report(e, report)
        created_counts["vehicle"] += 1

    for name in sorted(telecom):
        e = _get_or_create_entity(name, Entity.TELECOM)
        _link_entity_to_report(e, report)
        created_counts["telecom"] += 1

    for name in sorted(locations):
        e = _get_or_create_entity(name, Entity.LOCATION)
        _link_entity_to_report(e, report)
        created_counts["location"] += 1

    # extract rule-events (not stored in DB yet)
    rule_events = extract_events(text, nlp)

    # Update global entity-to-entity relation graph so the visualisation reflects entities from this and all reports.
    relationLevelCalculator()

    return {
        "report_id": report.pk,
        "entity_counts": created_counts,
        "rule_events_found": len(rule_events),
    }