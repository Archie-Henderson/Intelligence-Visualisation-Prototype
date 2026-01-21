import re
import spacy
from spacy.pipeline import EntityRuler
from spacy.util import filter_spans
from spacy.language import Language


REG_VEHICLE_REG = re.compile(r"\bReg(?:istration)?\s*(?:No\.?|Number|#)?\s*[:\-]?\s*([A-Z0-9]{2,7})\b", re.I)

REG_CRIME_GROUP_NAME = re.compile(r"\b(?!the\b)([A-Za-z]+)\s+crime\s+(?:group|family|gang)\b", re.I)

REG_DOB = re.compile(r"\bBn\.?\s*(\d{2}/\d{2}/\d{4})\b", re.I)

REG_POSTCODE = re.compile(r"\b([A-Z]{1,2}\d{1,2}[A-Z]?\s*\d[A-Z]{2})\b", re.I)

REG_PHONE = re.compile(r"\b(07\d{9})\b")

#Currently not sure what to do with uncertain info. (trustworthy score to be thought about later)
REG_ALIAS = re.compile(
    r"\b(?P<uncertain>may\s+be|possibly|believed\s+to\s+be|thought\s+to\s+be|reported\s+to\s+be)?\s*"
    r"(?P<intro>aka|a\.k\.a\.|known\s+as|male\s+known\s+as)\s*"
    r"[:\-]?\s*"
    r"(?P<alias>[A-Z][A-Z0-9'’\-]{2,})\b",
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

    for m in REG_VEHICLE_REG.finditer(text):
        add_span(m.start(1), m.end(1), "VEHICLE_REG")

    for m in REG_CRIME_GROUP_NAME.finditer(text):
        add_span(m.start(1), m.end(1), "CRIME_GROUP")

    for m in REG_DOB.finditer(text):
        start, end = m.start(1), m.end(1)
        remove_overlaps(start, end) 
        add_span(start, end, "DOB")

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


    cleaned = []
    for e in new_ents:
        if e.label_ == "PERSON" and e.text.strip().lower() in {"glasgow", "paisley"}:
            continue
        if e.label_ == "PERSON" and e.text.strip().lower() == "bn":
            continue
        cleaned.append(e)

    doc.ents = filter_spans(cleaned)
    return doc



def main():
    nlp = spacy.load("en_core_web_sm")

    ruler = nlp.add_pipe("entity_ruler", before="ner")

    #car
    COLORS = ["black","white","silver","grey","gray","red","blue","yellow","green"]
    GENERIC_VEHICLES = ["car","vehicle","van","truck","lorry","motorbike","motorcycle","scooter","bike"]
    MAKES = ["bmw","audi","toyota","ford","vauxhall","mercedes","volkswagen","vw","nissan","honda","hyundai","kia","tesla","range","rover"]

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

    ])


    nlp.add_pipe("regex_entities", last=True)


    with open("logs.txt", "r", encoding="utf-8") as f:
        text = f.read()

    doc = nlp(text)

    # print entities
    KEEP = {
        "PERSON", "GPE", "LOC", "FAC", "DATE", "TIME", "ORG",
        "GROUP", "ROLE", "VEHICLE", "VEHICLE_REG", "ITEM", "DRUG", "CRIME_GROUP","ALIAS_UNCERTAIN", "PHONE", "POSTCODE", "DOB",
    }

    print("Pipeline:", nlp.pipe_names)
    print("-" * 60)
    print("ENTITIES (text | label):")
    for ent in doc.ents:
        if ent.label_ in KEEP:
            print(f"{ent.text} | {ent.label_}")


if __name__ == "__main__":
    main()
