import re
import spacy
from spacy.pipeline import EntityRuler
from spacy.util import filter_spans
from spacy.language import Language


REG_VEHICLE_REG = re.compile(
    r"\bReg(?:istration)?\s*(?:No\.?|Number|#)?\s*[:\-]?\s*([A-Z0-9]{2,7})\b",
    re.I
)
REG_CRIME_GROUP_NAME = re.compile(
    r"\b([A-Za-z]+)\s+crime\s+(?:group|family|gang)\b",
    re.I
)

@Language.component("regex_entities")
def regex_entities(doc):
    new_ents = list(doc.ents)
    text = doc.text

    for m in REG_VEHICLE_REG.finditer(text):
        span = doc.char_span(m.start(1), m.end(1), label="VEHICLE_REG", alignment_mode="contract")
        if span:
            new_ents.append(span)

    for m in REG_CRIME_GROUP_NAME.finditer(text):
        span = doc.char_span(
            m.start(1), m.end(1),
            label="CRIME_GROUP",
            alignment_mode="contract"
        )
        if span:
            new_ents.append(span)

    doc.ents = filter_spans(new_ents)
    return doc


def main():
    nlp = spacy.load("en_core_web_sm")

    ruler = nlp.add_pipe("entity_ruler", before="ner")

    #Custom entity patterns
    ruler.add_patterns([
        # GROUP
        {"label": "GROUP", "pattern": [{"LOWER": "group"}, {"LOWER": "of"}, {"LOWER": {"IN": ["teenagers", "males", "men", "women", "boys", "girls", "people"]}}]},
        {"label": "GROUP", "pattern": [{"LOWER": {"IN": ["different", "several", "multiple", "large"]}}, {"LOWER": {"IN": ["groups", "group"]}, "OP": "?"}, {"LOWER": {"IN": ["of"]}, "OP": "?"}, {"LOWER": {"IN": ["males", "men", "women", "teenagers", "people"]}}]},
        {"label": "GROUP", "pattern": [{"LIKE_NUM": True}, {"LOWER": "or"}, {"LIKE_NUM": True}, {"LOWER": {"IN": ["males", "men", "women", "teenagers", "people"]}}]},

        # ROLE
        {"label": "ROLE", "pattern": [{"LOWER": {"IN": ["driver", "passenger", "owner", "enforcer", "courier"]}}]},

        # VEHICLE_DESC
        {"label": "VEHICLE_DESC", "pattern": [{"LOWER": {"IN": ["black", "white", "silver", "grey", "gray", "red", "blue", "yellow", "green"]}}, {"LOWER": {"IN": ["bmw", "audi", "toyota", "ford", "vauxhall", "mercedes"]}}]},

        # ITEM
        {"label": "ITEM", "pattern": [{"LOWER": "wheelie"}, {"LOWER": "bins"}]},
        {"label": "ITEM", "pattern": [{"LOWER": {"IN": ["package", "packages", "knife", "knives", "bat", "hammer", "hammers"]}}]},

    ])


    nlp.add_pipe("regex_entities", last=True)


    with open("logs.txt", "r", encoding="utf-8") as f:
        text = f.read()

    doc = nlp(text)

    # print entities
    KEEP = {
        "PERSON", "GPE", "LOC", "FAC", "DATE", "TIME", "ORG",
        "GROUP", "ROLE", "VEHICLE_DESC", "VEHICLE_REG", "ITEM", "CRIME_GROUP"
    }

    print("Pipeline:", nlp.pipe_names)
    print("-" * 60)
    print("ENTITIES (text | label):")
    for ent in doc.ents:
        if ent.label_ in KEEP:
            print(f"{ent.text} | {ent.label_}")


if __name__ == "__main__":
    main()
