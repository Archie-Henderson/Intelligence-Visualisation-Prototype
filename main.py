import re
import spacy
from spacy.pipeline import EntityRuler
from spacy.util import filter_spans
from spacy.language import Language
from spacy.tokens import Span
from data_processing.event_extractor import extract_events_from_text as llm_extract_events

import json
from typing import List, Dict, Any, Optional, Set

# SIMPLE EVENT EXTRACTION (Variant A)
# Works like: NER (spaCy + your rulers/regex) + trigger patterns + nearest-entity arguments.

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
    """Split the input into blocks using blank lines (simple but effective for police logs)."""
    blocks = [b.strip() for b in re.split(r"\n\s*\n+", text) if b.strip()]
    return blocks

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
    """Pick entity texts: first from the sentence; if empty, from the whole block."""
    s = [e.text for e in sent_ents if e.label_ in labels]
    if s:
        return s[:limit]
    b = [e.text for e in block_ents if e.label_ in labels]
    return b[:limit]

def extract_events_from_block(doc) -> List[Dict[str, Any]]:
    """Extract events from a single spaCy Doc (one block)."""
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

            subject = last_person_before(sent_ents, trigger_abs_start) or block_last_person

            date_ents = [e.text for e in sent_ents if e.label_ == "DATE"]
            time_ents = [e.text for e in sent_ents if e.label_ == "TIME"]
            location = _pick_texts(block_ents, sent_ents, {"GPE", "LOC", "FAC"}, limit=1)
            home_addr = _pick_texts(block_ents, sent_ents, {"ADDRESS"}, limit=1)

            vehicle = _pick_texts(block_ents, sent_ents, {"VEHICLE"}, limit=2)
            reg_plate = _pick_texts(block_ents, sent_ents, {"VEHICLE_REG"}, limit=2)
            gang = _pick_texts(block_ents, sent_ents, {"CRIME_GROUP", "ORG"}, limit=2)
            drugs = _pick_texts(block_ents, sent_ents, {"DRUG"}, limit=3)
            items = _pick_texts(block_ents, sent_ents, {"ITEM"}, limit=3)

            ev = {
                "event_type": etype,
                "trigger": trigger_text,
                "subject": subject,
                "date": date_ents[0] if date_ents else None,
                "time": time_ents[0] if time_ents else None,
                "location": location[0] if location else None,
                "home_address": home_addr[0] if home_addr else None,
                "vehicle": vehicle,
                "reg_plate": reg_plate,
                "gang": gang,
                "drugs": drugs,
                "items": items,
                "evidence_text": sent_text.strip(),
            }

            score = 0
            if ev["subject"]: score += 1
            if ev["date"]: score += 1
            if ev["time"]: score += 1
            if ev["location"]: score += 1
            if ev["vehicle"]: score += 1
            if ev["reg_plate"]: score += 1
            if ev["gang"]: score += 1
            if score >= 2:
                events.append(ev)

            break  # 1 event per sentence

    return events

def extract_events(text: str, nlp) -> List[Dict[str, Any]]:
    """Full pass: split text into blocks -> run nlp -> extract events."""
    all_events: List[Dict[str, Any]] = []
    for i, block in enumerate(split_into_blocks(text)):
        doc = nlp(block)
        evs = extract_events_from_block(doc)
        for ev in evs:
            ev["block_id"] = i
        all_events.extend(evs)
    return all_events



REG_VEHICLE_REG = re.compile(
    r"\bReg(?:istration)?\s*\.?\s*(?:No\.?|Number|#)?\s*[:\-]?\s*([A-Z0-9]{2,7})\b", re.I)

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
REG_ADDRESS = re.compile(r"(?m)^\s*(\d{1,4}\s+[A-Z][A-Za-z'\-]*(?:\s+[A-Z][A-Za-z'\-]*)*\s+(?:Road|Street|Drive|Avenue|Lane|Place|Crescent|Court|Terrace))\s*$")


#Currently not sure what to do with uncertain info. (trustworthy score to be thought about later)
REG_ALIAS = re.compile(
    r"\b(?P<uncertain>may\s+be|possibly|believed\s+to\s+be|thought\s+to\s+be|reported\s+to\s+be)?\s*"
    r"(?P<intro>aka|a\.k\.a\.|known\s+as|male\s+known\s+as)\s*"
    r"[:\-]?\s*"
    r"(?P<alias>[A-Za-z][A-Za-z0-9'’\-]{1,})\b",
    re.I
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
                # keep only all-caps surnames
                if surname.isupper() and surname.isalpha():
                    surname_set.add(surname)



    #!!currently overwriting org to person, etc, check needed just in case 
    cleaned = []
    for e in new_ents:
        if e.label_ == "PERSON" and e.text.strip().lower() in {"glasgow", "paisley"}:
            continue
        if e.label_ == "PERSON" and e.text.strip().lower() == "bn":
            continue
        #ORG→ PERSON
        if e.label_ == "ORG":
            txt = e.text.strip()
            if txt in surname_set:
                cleaned.append(Span(doc, e.start, e.end, label="PERSON"))
                continue
        cleaned.append(e)

    doc.ents = filter_spans(cleaned)
    return doc

def build_entity_index(doc) -> dict:
    """
    Group spaCy entities into buckets we care about for checking LLM events.
    """
    idx = {
        "persons": set(),
        "vehicles": set(),
        "locations": set(),
        "orgs": set(),
    }
    for ent in doc.ents:
        txt = ent.text.strip()
        if not txt:
            continue

        if ent.label_ in {"PERSON", "GROUP", "CRIME_GROUP", "ALIAS_CERTAIN", "ALIAS_UNCERTAIN"}:
            idx["persons"].add(txt)
        if ent.label_ in {"VEHICLE", "VEHICLE_REG"}:
            idx["vehicles"].add(txt)
        if ent.label_ in {"GPE", "LOC", "FAC", "ADDRESS"}:
            idx["locations"].add(txt)
        if ent.label_ in {"ORG", "CRIME_GROUP"}:
            idx["orgs"].add(txt)

    return idx


def _count_fuzzy_matches(values, entity_set) -> int:
    """
    Count how many strings in 'values' loosely match anything in entity_set
    (substring / case-insensitive). Simple but works well for our use-case.
    """
    hits = 0
    for v in values:
        v_norm = v.strip().lower()
        if not v_norm:
            continue
        for ent in entity_set:
            e_norm = ent.lower()
            if v_norm in e_norm or e_norm in v_norm:
                hits += 1
                break
    return hits


def score_llm_event_against_spacy(event: dict, ent_idx: dict) -> dict:
    """
    Compare one LLM event to spaCy entities and return simple alignment scores.
    """
    people = event.get("people") or []
    participants = event.get("participants") or people
    vehicles = event.get("vehicles") or []
    location = (event.get("location") or "").strip()

    p_hits = _count_fuzzy_matches(participants, ent_idx["persons"])
    v_hits = _count_fuzzy_matches(vehicles, ent_idx["vehicles"])

    loc_hit = None
    if location:
        loc_hit = any(
            (location.lower() in e.lower()) or (e.lower() in location.lower())
            for e in ent_idx["locations"]
        )

    return {
        "participant_match_ratio": (p_hits / len(participants)) if participants else None,
        "vehicle_match_ratio": (v_hits / len(vehicles)) if vehicles else None,
        "location_matched": loc_hit,
    }

def should_accept_llm_event(ev: dict, scores: dict) -> bool:
    """
    Decide whether to accept an LLM event based on spaCy alignment.
    - Participants / vehicles are strong signals.
    - Location is weak; we never reject *only* because location_matched is False.
    """
    p = scores.get("participant_match_ratio")
    v = scores.get("vehicle_match_ratio")

    # If we have at least some alignment on participants or vehicles, accept.
    if p is not None and p >= 0.3:
        return True
    if v is not None and v >= 0.3:
        return True

    # If the AI gave *no* participants/vehicles at all, but did give a location,
    # we can still accept the event (just less confidently).
    if not ev.get("participants") and not ev.get("vehicles") and ev.get("location"):
        return True

    # Otherwise, reject as too weak / unsupported.
    return True

def main():
    nlp = spacy.load("en_core_web_sm")

    ruler = nlp.add_pipe("entity_ruler", before="ner")

    #car
    COLORS = ["black","white","silver","grey","gray","red","blue","yellow","green"]
    GENERIC_VEHICLES = ["car","vehicle","van","truck","lorry","motorbike","motorcycle","scooter","bike"]
    MAKES = ["bmw","audi","toyota","ford","vauxhall","mercedes","volkswagen","vw","nissan","honda","hyundai","kia","tesla","range","rover"]

    #DRUGS
    DRUGS = ["heroin", "cocaine", "ketamine", "cannabis", "ecstasy", "mdma"]


    #Custom entity patterns
    ruler.add_patterns([

        # GROUP
        {"label": "GROUP", "pattern": [{"LOWER": "group"}, {"LOWER": "of"}, {"LOWER": {"IN": ["teenagers", "males", "men", "women", "boys", "girls", "people"]}}]},
        {"label": "GROUP", "pattern": [{"LOWER": {"IN": ["different", "several", "multiple", "large"]}}, {"LOWER": {"IN": ["groups", "group"]}, "OP": "?"}, {"LOWER": {"IN": ["of"]}, "OP": "?"}, {"LOWER": {"IN": ["males", "men", "women", "teenagers", "people"]}}]},
        {"label": "GROUP", "pattern": [{"LIKE_NUM": True}, {"LOWER": "or"}, {"LIKE_NUM": True}, {"LOWER": {"IN": ["males", "men", "women", "teenagers", "people"]}}]},

        # ROLE
        {"label": "ROLE", "pattern": [{"LOWER": {"IN": ["driver", "passenger", "owner", "enforcer", "courier"]}}]},

        # VEHICLE
        {"label": "VEHICLE", "pattern": [{"LOWER": {"IN": GENERIC_VEHICLES}}]},
        {"label": "VEHICLE", "pattern": [{"LOWER": {"IN": COLORS}}, {"LOWER": {"IN": GENERIC_VEHICLES}}]},
        {"label": "VEHICLE", "pattern": [{"LOWER": {"IN": MAKES}}]},
        {"label": "VEHICLE", "pattern": [{"LOWER": {"IN": MAKES}},{"TEXT": {"REGEX": r"^[A-Za-z0-9\-]{1,4}$"}, "OP": "?"},{"LOWER": {"IN": ["series", "rover", "jeep"]}, "OP": "?"}]},
        {"label": "VEHICLE", "pattern": [{"LOWER": {"IN": COLORS}}, {"LOWER": {"IN": MAKES}},{"TEXT": {"REGEX": r"^[A-Za-z0-9\-]{1,4}$"}, "OP": "?"},{"LOWER": {"IN": ["series", "rover", "jeep"]}, "OP": "?"}]},

        # ITEM
        {"label": "ITEM", "pattern": [{"LOWER": "wheelie"}, {"LOWER": "bins"}]},
        {"label": "ITEM", "pattern": [{"LOWER": {"IN": ["package", "packages", "knife", "knives", "bat", "hammer", "hammers"]}}]},

        #DRUG
        {"label": "DRUG", "pattern": [{"LOWER": {"IN": DRUGS}}]},
        {"label": "DRUG", "pattern": [{"LOWER": "controlled"}, {"LOWER": "drugs"}]},


    ])


    nlp.add_pipe("regex_entities", last=True)


    with open("Logs.txt", "r", encoding="utf-8") as f:
        text = f.read()

    doc = nlp(text)

    # print entities
    KEEP = {
        "PERSON", "GPE", "LOC", "FAC", "DATE", "TIME", "ORG",
        "GROUP", "ROLE", "VEHICLE", "VEHICLE_REG", "ITEM", "DRUG", "CRIME_GROUP","ALIAS_UNCERTAIN","ALIAS_CERTAIN", "PHONE", "POSTCODE", "DOB","ADDRESS",
    }

    print("Pipeline:", nlp.pipe_names)
    print("-" * 60)
    print("ENTITIES (text | label):")
    for ent in doc.ents:
        if ent.label_ in KEEP:
            print(f"{ent.text} | {ent.label_}")



    # EVENT EXTRACTION (Variant A) 
    events = extract_events(text, nlp)
    print("\n" + "=" * 60)
    print("EVENTS (JSON)")
    print(json.dumps(events, indent=2))

    print("\nRULE-BASED EVENTS (summary)")
    for i, ev in enumerate(events, 1):
        print(f"#{i}")
        print(f"  type:      {ev.get('event_type')}")
        print(f"  date:      {ev.get('date')}")
        print(f"  time:      {ev.get('time')}")
        print(f"  location:  {ev.get('location')}")
        print(f"  subject:   {ev.get('subject')}")
        print()

    # save to file (optional)
    with open("events.json", "w", encoding="utf-8") as f:
        json.dump(events, f, indent=2, ensure_ascii=False)

            # LLM-BASED EVENT EXTRACTION (Variant B)
    print("\n" + "=" * 60)
    print("LLM EVENTS + ALIGNMENT WITH SPACY")
    print("=" * 60)

    llm_events = []
    for i, block in enumerate(split_into_blocks(text)):
        try:
            res = llm_extract_events(block)
            events_block = res.get("events", [])
            for ev in events_block:
                ev["block_id"] = i
            llm_events.extend(events_block)
        except Exception as e:
            print(f"Error on block {i}: {e}")

    print(f"\nLLM returned {len(llm_events)} events.\n")

    # 2) Build spaCy entity index from the full doc
    ent_idx = build_entity_index(doc)

    for i, ev in enumerate(llm_events, 1):
        scores = score_llm_event_against_spacy(ev, ent_idx)
        accept = should_accept_llm_event(ev, scores)

        print(f"--- LLM Event {i} ---")
        print(f"Type:        {ev.get('event_type', 'unknown')}")
        print(f"Title:       {ev.get('title', '')}")
        print(f"Participants:{ev.get('participants') or ev.get('people', [])}")
        print(f"Vehicles:    {ev.get('vehicles', [])}")
        print(f"Location:    {ev.get('location', None)}")
        print(f"datetime_start: {ev.get('datetime_start')}")
        print(f"home_address:   {ev.get('home_address')}")
        print(f"Source span: {ev.get('source_text_span', '')[:120]}")
        print("Alignment with spaCy:")
        print(f"  participant_match_ratio: {scores['participant_match_ratio']}")
        print(f"  vehicle_match_ratio:     {scores['vehicle_match_ratio']}")
        print(f"  location_matched:        {scores['location_matched']}")
        print()

if __name__ == "__main__":
    main()