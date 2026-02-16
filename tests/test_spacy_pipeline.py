from __future__ import annotations

import os
import unittest

try:
    import spacy
    from spacy.language import Language
except ModuleNotFoundError:
    spacy = None
    Language = None

try:
    from main import regex_entities
except Exception:
    regex_entities = None


def read_logs_text() -> str:
    #Integration tests

    repo_root = os.path.dirname(os.path.dirname(__file__))
    candidates = ["Logs.txt", "logs.txt", "LOGS.txt"]
    for name in candidates:
        path = os.path.join(repo_root, name)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()

    raise FileNotFoundError(
        f"Could not find Logs.txt in repo root ({repo_root}). "
        f"Tried: {', '.join(candidates)}"
    )

@unittest.skipIf(spacy is None, "spaCy not installed in this environment")
class LogsPipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load model or create a blank pipeline with English
        try:
            cls.nlp = spacy.load("en_core_web_sm")
        except Exception:
            cls.nlp = spacy.blank("en")

        # EntityRuler patterns
        ruler = cls.nlp.add_pipe(
            "entity_ruler",
            before="ner" if "ner" in cls.nlp.pipe_names else None,
        )

        COLORS = ["black", "white", "silver", "grey", "gray", "red", "blue", "yellow", "green"]
        GENERIC_VEHICLES = ["car", "vehicle", "van", "truck", "lorry", "motorbike", "motorcycle", "scooter", "bike"]
        MAKES = ["bmw", "audi", "toyota", "ford", "vauxhall", "mercedes", "volkswagen", "vw", "nissan", "honda", "hyundai", "kia", "tesla", "range", "rover"]
        DRUGS = ["heroin", "cocaine", "ketamine", "cannabis", "ecstasy", "mdma"]

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
            {"label": "VEHICLE", "pattern": [{"LOWER": {"IN": MAKES}}, {"TEXT": {"REGEX": r"^[A-Za-z0-9\-]{1,4}$"}, "OP": "?"}, {"LOWER": {"IN": ["series", "rover", "jeep"]}, "OP": "?"}]},
            {"label": "VEHICLE", "pattern": [{"LOWER": {"IN": COLORS}}, {"LOWER": {"IN": MAKES}}, {"TEXT": {"REGEX": r"^[A-Za-z0-9\-]{1,4}$"}, "OP": "?"}, {"LOWER": {"IN": ["series", "rover", "jeep"]}, "OP": "?"}]},

            # ITEM
            {"label": "ITEM", "pattern": [{"LOWER": "wheelie"}, {"LOWER": "bins"}]},
            {"label": "ITEM", "pattern": [{"LOWER": {"IN": ["package", "packages", "knife", "knives", "bat", "hammer", "hammers"]}}]},

            # DRUG
            {"label": "DRUG", "pattern": [{"LOWER": {"IN": DRUGS}}]},
            {"label": "DRUG", "pattern": [{"LOWER": "controlled"}, {"LOWER": "drugs"}]},
        ])

        # Add regex_entities component if it exists
        if regex_entities is not None:
            if Language is not None and not Language.has_factory("regex_entities"):
                Language.component("regex_entities")(regex_entities)
            if "regex_entities" not in cls.nlp.pipe_names:
                cls.nlp.add_pipe("regex_entities", last=True)

        cls.logs_text = read_logs_text()
        cls.doc = cls.nlp(cls.logs_text)

    # helpers
    def ents(self):
        return [(e.text, e.label_) for e in self.doc.ents]

    def assert_has_label(self, label: str):
        self.assertTrue(any(l == label for _, l in self.ents()), f"Expected at least one {label} entity")

    def assert_has_contains(self, label: str, substring: str):
        self.assertTrue(
            any(l == label and substring.lower() in t.lower() for t, l in self.ents()),
            f"Expected {label} containing '{substring}'",
        )

    # basic
    def test_pipeline_runs_on_full_logs(self):
        self.assertGreater(len(self.logs_text), 1000)

    def test_detects_some_people(self):
        self.assert_has_label("PERSON")

    def test_detects_some_addresses(self):
        self.assert_has_label("ADDRESS")

    def test_detects_some_postcodes(self):
        self.assert_has_label("POSTCODE")

    def test_detects_some_dobs(self):
        self.assert_has_label("DOB")

    def test_detects_some_vehicle_regs(self):
        self.assert_has_label("VEHICLE_REG")

    def test_detects_some_crime_groups(self):
        self.assert_has_label("CRIME_GROUP")

    def test_detects_some_items(self):
        self.assert_has_label("ITEM")

    def test_detects_some_drugs(self):
        self.assert_has_label("DRUG")

    # specific checks based on known content of Logs.txt
    def test_scott_bamber_present_as_person(self):
        self.assertTrue(
            any(l == "PERSON" and "scott" in t.lower() and "bamber" in t.lower() for t, l in self.ents())
            or any(l == "PERSON" and "bamber" in t.lower() for t, l in self.ents()),
            "Expected a PERSON entity for Scott BAMBER (or at least BAMBER)",
        )

    def test_specific_vehicle_reg_present(self):
        self.assert_has_contains("VEHICLE_REG", "SF13DDR")

    def test_specific_postcode_present(self):
        self.assert_has_contains("POSTCODE", "G207QB")

    def test_detects_some_dobs_with_date_shape(self):
        dobs = [t for t, l in self.ents() if l == "DOB"]
        self.assertTrue(dobs, "Expected at least one DOB entity")
        self.assertTrue(any("/" in t for t in dobs), f"DOB entities look odd: {dobs[:10]}")

    def test_detects_some_addresses_from_known_streets(self):
        self.assertTrue(
            any(l == "ADDRESS" and "maryhill road" in t.lower() for t, l in self.ents())
            or any(l == "ADDRESS" and "skirsa street" in t.lower() for t, l in self.ents())
            or any(l == "ADDRESS" and "sandbank street" in t.lower() for t, l in self.ents()),
            "Expected at least one ADDRESS containing a known street from Logs.txt",
        )

    def test_detects_at_least_one_phone(self):
        self.assertTrue(any(l == "PHONE" for _, l in self.ents()), "Expected at least one PHONE entity in Logs.txt")

    def test_detects_aliases(self):
        self.assertTrue(
            any(l == "ALIAS_CERTAIN" and "tadpole" in t.lower() for t, l in self.ents()),
            "Expected ALIAS_CERTAIN containing Tadpole",
        )
        self.assertTrue(
            any(l == "ALIAS_UNCERTAIN" and "dapper" in t.lower() for t, l in self.ents()),
            "Expected ALIAS_UNCERTAIN containing DAPPER",
        )

    def test_detects_crime_groups(self):
        self.assertTrue(
            any(l == "CRIME_GROUP" and "pollock" in t.lower() for t, l in self.ents()),
            "Expected CRIME_GROUP containing POLLOCK",
        )
        self.assertTrue(
            any(l == "CRIME_GROUP" and "wilkinson" in t.lower() for t, l in self.ents()),
            "Expected CRIME_GROUP containing WILKINSON",
        )

    def test_detects_multiple_vehicle_regs(self):
        self.assert_has_contains("VEHICLE_REG", "SF13DDR")
        regs = {t.strip().upper() for t, l in self.ents() if l == "VEHICLE_REG"}
        self.assertTrue(len(regs) >= 2 or ("SG19GGT" in regs), f"VEHICLE_REG entities were: {sorted(regs)}")

    def test_detects_vehicle_make(self):
        self.assertTrue(
            any(l == "VEHICLE" and "bmw" in t.lower() for t, l in self.ents()),
            "Expected VEHICLE containing BMW",
        )

    def test_detects_items(self):
        self.assertTrue(
            any(l == "ITEM" and "wheelie bins" in t.lower() for t, l in self.ents()),
            "Expected ITEM containing wheelie bins",
        )
        self.assertTrue(
            any(l == "ITEM" and "hammer" in t.lower() for t, l in self.ents()),
            "Expected ITEM containing hammer/hammers",
        )
        self.assertTrue(
            any(l == "ITEM" and "knife" in t.lower() for t, l in self.ents()),
            "Expected ITEM containing knife/knives",
        )

    def test_detects_drugs(self):
        self.assertTrue(
            any(l == "DRUG" and ("heroin" in t.lower() or "controlled drugs" in t.lower()) for t, l in self.ents()),
            "Expected DRUG containing heroin or controlled drugs",
        )

    def test_detects_group_and_role(self):
        self.assertTrue(any(l == "GROUP" for _, l in self.ents()), "Expected at least one GROUP entity")
        self.assertTrue(any(l == "ROLE" for _, l in self.ents()), "Expected at least one ROLE entity")

    def test_pipeline_robustness_empty_and_unicode(self):
        doc1 = self.nlp("")
        doc2 = self.nlp("Hugh ‘Shug’ MORRISON — test")
        self.assertIsNotNone(doc1)
        self.assertIsNotNone(doc2)

    def test_vehicle_reg_extracts_when_reg_prefix_present(self):
        doc = self.nlp("Vehicle: Reg No. AB12CDE")
        self.assertTrue(any(e.label_ == "VEHICLE_REG" for e in doc.ents), [(e.text, e.label_) for e in doc.ents])

    def test_dob_extracts_dd_mm_yyyy(self):
        doc = self.nlp("Bn.12/03/2005")
        dobs = [e.text for e in doc.ents if e.label_ == "DOB"]
        self.assertTrue(any("12/03/2005" in t for t in dobs), f"DOB ents: {dobs}")

    def test_phone_extracts_uk_mobile_shape(self):
        doc = self.nlp("Call 07889303555 now")
        phones = [e.text for e in doc.ents if e.label_ == "PHONE"]
        self.assertIn("07889303555", phones)

    def test_postcode_extracts_uk_postcode_shape(self):
        doc = self.nlp("Address: Glasgow G11 5LL")
        pcs = [e.text for e in doc.ents if e.label_ == "POSTCODE"]
        self.assertTrue(any("G11" in t.upper() for t in pcs), f"POSTCODE ents: {pcs}")

    def test_alias_certainty_labels(self):
        doc1 = self.nlp("Aka Tadpole")
        doc2 = self.nlp("possibly aka Ghost")
        self.assertTrue(any(e.label_ == "ALIAS_CERTAIN" for e in doc1.ents), [(e.text, e.label_) for e in doc1.ents])
        self.assertTrue(any(e.label_ == "ALIAS_UNCERTAIN" for e in doc2.ents), [(e.text, e.label_) for e in doc2.ents])

    def test_entities_do_not_overlap(self):
        ents = sorted(self.doc.ents, key=lambda e: (e.start_char, e.end_char))
        for prev, cur in zip(ents, ents[1:]):
            self.assertFalse(
                prev.start_char < cur.end_char and cur.start_char < prev.end_char,
                f"Overlapping ents: ({prev.text},{prev.label_}) and ({cur.text},{cur.label_})",
            )

    def test_only_expected_labels_produced(self):
        custom_labels = {
            "GROUP", "ROLE", "VEHICLE", "VEHICLE_REG", "ITEM", "DRUG",
            "CRIME_GROUP", "ALIAS_UNCERTAIN", "ALIAS_CERTAIN",
            "PHONE", "POSTCODE", "DOB", "ADDRESS",
        }
        produced = {e.label_ for e in self.doc.ents}
        unexpected_custom = {
            l for l in produced
            if l.startswith(("ALIAS", "VEHICLE", "CRIME", "POST", "DOB", "ADDRESS", "GROUP", "ROLE", "ITEM", "DRUG"))
            and l not in custom_labels
        }
        self.assertFalse(
            unexpected_custom,
            f"Unexpected custom-like labels produced: {sorted(unexpected_custom)}. Produced labels: {sorted(produced)}",
        )

    def test_no_empty_entities(self):
        for e in self.doc.ents:
            self.assertTrue(e.text.strip(), f"Empty/blank entity: {repr(e.text)} label={e.label_}")

if __name__ == "__main__":
    unittest.main()
