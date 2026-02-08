import unittest
import spacy

# import your custom component from main.py
from main import regex_entities  # this imports the @Language.component("regex_entities")


def build_nlp():
    #build the same pipeline as main() but dont read the logs so the tests focuses on the entity extraction
    nlp = spacy.load("en_core_web_sm")

    ruler = nlp.add_pipe("entity_ruler", before="ner")

    #car
    COLORS = ["black","white","silver","grey","gray","red","blue","yellow","green"]
    GENERIC_VEHICLES = ["car","vehicle","van","truck","lorry","motorbike","motorcycle","scooter","bike"]
    MAKES = ["bmw","audi","toyota","ford","vauxhall","mercedes","volkswagen","vw","nissan","honda","hyundai","kia","tesla","range","rover"]

    #DRUGS
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
        {"label": "VEHICLE", "pattern": [{"LOWER": {"IN": MAKES}},{"TEXT": {"REGEX": r"^[A-Za-z0-9\-]{1,4}$"}, "OP": "?"},{"LOWER": {"IN": ["series", "rover", "jeep"]}, "OP": "?"}]},
        {"label": "VEHICLE", "pattern": [{"LOWER": {"IN": COLORS}}, {"LOWER": {"IN": MAKES}},{"TEXT": {"REGEX": r"^[A-Za-z0-9\-]{1,4}$"}, "OP": "?"},{"LOWER": {"IN": ["series", "rover", "jeep"]}, "OP": "?"}]},

        # ITEM
        {"label": "ITEM", "pattern": [{"LOWER": "wheelie"}, {"LOWER": "bins"}]},
        {"label": "ITEM", "pattern": [{"LOWER": {"IN": ["package", "packages", "knife", "knives", "bat", "hammer", "hammers"]}}]},

        #DRUG
        {"label": "DRUG", "pattern": [{"LOWER": {"IN": DRUGS}}]},
        {"label": "DRUG", "pattern": [{"LOWER": "controlled"}, {"LOWER": "drugs"}]},


    ])

    # ensuring custom regex component exists in pipeline
    if "regex_entities" not in nlp.pipe_names:
        nlp.add_pipe("regex_entities", last=True)

    return nlp

def has_ent(doc, label: str, text: str) -> bool:
    #True if there is an entity with this label whose text contains 'text'
    return any(ent.label_ == label and text in ent.text for ent in doc.ents)

def get_ents(doc, label: str):
    return [ent.text for ent in doc.ents if ent.label_ == label]


def ents_as_tuples(doc):
    #Helper: list of (text,label) in order
    return [(e.text, e.label_) for e in doc.ents]


class PipelineSanityTests(unittest.TestCase):
    def test_pipeline_contains_expected_components(self):
        nlp = build_nlp()
        self.assertIn("entity_ruler", nlp.pipe_names)
        self.assertIn("ner", nlp.pipe_names)
        self.assertIn("regex_entities", nlp.pipe_names)

    def test_regex_entities_runs_last(self):
        nlp = build_nlp()
        self.assertEqual(nlp.pipe_names[-1], "regex_entities")


class RegexEntitiesComponentTests(unittest.TestCase):
    def setUp(self):
        self.nlp = build_nlp()

    def test_block_person_detects_firstname_surname(self):
        text = "Scott BAMBER\nBn.12/03/2005\n"
        doc = self.nlp(text)
        ents = ents_as_tuples(doc)
        self.assertIn(("Scott BAMBER", "PERSON"), ents)

    def test_vehicle_reg_detected(self):
        text = "Vauxhall Astra Reg No. SF13DDR"
        doc = self.nlp(text)
        ents = ents_as_tuples(doc)
        self.assertIn(("SF13DDR", "VEHICLE_REG"), ents)

    def test_crime_group_name_detected(self):
        text = "POLLOCK crime family"
        doc = self.nlp(text)
        ents = ents_as_tuples(doc)
        self.assertIn(("POLLOCK", "CRIME_GROUP"), ents)

    def test_ocg_detected(self):
        text = "WILKINSON OCG"
        doc = self.nlp(text)
        ents = ents_as_tuples(doc)
        self.assertIn(("WILKINSON", "CRIME_GROUP"), ents)

    def test_dob_detected(self):
      doc = self.nlp("Scott BAMBER Bn.12/03/2005")
      dob_ents = get_ents(doc, "DOB")
      self.assertTrue(
            any("12/03/2005" in t for t in dob_ents),
            f"DOB ents were: {dob_ents}",
      )

    def test_postcode_detected(self):
        text = "Glasgow\nG207QB"
        doc = self.nlp(text)
        ents = ents_as_tuples(doc)
        self.assertIn(("G207QB", "POSTCODE"), ents)

    def test_phone_detected(self):
        text = "Contact: 07889303555"
        doc = self.nlp(text)
        ents = ents_as_tuples(doc)
        self.assertIn(("07889303555", "PHONE"), ents)

    def test_alias_certain_detected(self):
        text = "Kevin GRANDER Aka Tadpole"
        doc = self.nlp(text)
        ents = ents_as_tuples(doc)
        self.assertIn(("Tadpole", "ALIAS_CERTAIN"), ents)

    def test_alias_uncertain_detected(self):
        text = "He may be known as DAPPER"
        doc = self.nlp(text)
        ents = ents_as_tuples(doc)
        self.assertIn(("DAPPER", "ALIAS_UNCERTAIN"), ents)

    def test_address_detected(self):
        text = "80 Maryhill Road"
        doc = self.nlp(text)
        ents = ents_as_tuples(doc)
        self.assertIn(("80 Maryhill Road", "ADDRESS"), ents)

    def test_filters_glasgow_paisley_as_person(self):
        # If model tries to label these as PERSON, cleanup should remove them
        text = "Glasgow\nPaisley\n"
        doc = self.nlp(text)
        ents = ents_as_tuples(doc)
        self.assertNotIn(("Glasgow", "PERSON"), ents)
        self.assertNotIn(("Paisley", "PERSON"), ents)

    def test_filters_bn_as_person(self):
        text = "bn\n"
        doc = self.nlp(text)
        ents = ents_as_tuples(doc)
        self.assertNotIn(("bn", "PERSON"), ents)
        self.assertNotIn(("Bn", "PERSON"), ents)

    def test_overlap_handling_prefers_regex_person(self):
        # ensuring overlaps are removed and regex entity survives
        text = "Scott BAMBER\n"
        doc = self.nlp(text)
        ents = ents_as_tuples(doc)
        self.assertIn(("Scott BAMBER", "PERSON"), ents)


class EntityRulerPatternTests(unittest.TestCase):
    def setUp(self):
        self.nlp = build_nlp()

    def test_group_detected(self):
        doc = self.nlp("A group of teenagers were present.")
        self.assertIn(("group of teenagers", "GROUP"), ents_as_tuples(doc))

    def test_role_detected(self):
        doc = self.nlp("The driver stayed in the car.")
        self.assertIn(("driver", "ROLE"), ents_as_tuples(doc))

    def test_vehicle_generic_detected(self):
        doc = self.nlp("A vehicle was seen.")
        self.assertIn(("vehicle", "VEHICLE"), ents_as_tuples(doc))

    def test_vehicle_color_generic_detected(self):
        doc = self.nlp("A black car was parked.")
        self.assertIn(("black car", "VEHICLE"), ents_as_tuples(doc))

    def test_vehicle_make_detected(self):
      doc = self.nlp("BMW was parked outside.")
      self.assertTrue(has_ent(doc, "VEHICLE", "BMW"), f"VEHICLE ents were: {get_ents(doc, 'VEHICLE')}")


    def test_vehicle_make_model_detected(self):
        doc = self.nlp("A black BMW 3 series was parked.")
        # depends on tokenization, it might be "BMW 3 series" or "black BMW 3 series"
        ents = ents_as_tuples(doc)
        self.assertTrue(any(label == "VEHICLE" for _, label in ents))

    def test_item_wheelie_bins_detected(self):
        doc = self.nlp("They knocked over wheelie bins.")
        self.assertIn(("wheelie bins", "ITEM"), ents_as_tuples(doc))

    def test_item_hammer_detected(self):
        doc = self.nlp("He had hammers in the unit.")
        self.assertIn(("hammers", "ITEM"), ents_as_tuples(doc))

    def test_drug_detected(self):
        doc = self.nlp("He was selling heroin.")
        self.assertIn(("heroin", "DRUG"), ents_as_tuples(doc))

    def test_controlled_drugs_detected(self):
        doc = self.nlp("Police seized controlled drugs.")
        self.assertIn(("controlled drugs", "DRUG"), ents_as_tuples(doc))


if __name__ == "__main__":
    unittest.main()
