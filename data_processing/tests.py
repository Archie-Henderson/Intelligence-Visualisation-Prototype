from django.test import SimpleTestCase
from data_processing.text_analysis import detect_entities

class SpacyEntityDetectionTests(SimpleTestCase):

    def test_detects_address(self):
        text = "She moved to New York."
        entities = detect_entities(text)

        self.assertTrue(
            any(e["label"] == "ADDRESS" for e in entities)
        )

    def test_detects_vehicle(self):
        text = "John bought a Toyota Camry."
        entities = detect_entities(text)

        self.assertTrue(
            any(e["label"] == "VEHICLE" for e in entities)
        )

    def test_detects_multiple_entities(self):
        text = "John Smith drove his Ford F-150 to Los Angeles."
        entities = detect_entities(text)

        labels = {e["label"] for e in entities}

        self.assertIn("NAME", labels)
        self.assertIn("VEHICLE", labels)
        self.assertIn("ADDRESS", labels)

    def test_detects_multiple_names(self):
        text = "John Smith and Sarah Johnson attended the meeting."
        entities = detect_entities(text)

        name_count = sum(
            1 for e in entities if e["label"] == "NAME"
        )

        self.assertGreaterEqual(name_count, 2)

    def test_no_false_positives(self):
        text = "Nothing"
        entities = detect_entities(text)

        self.assertEqual(
            len(entities),
            0
        )
    
    def test_detects_name_and_address(self):
        text = "John Smith lives in Chicago."
        entities = detect_entities(text)

        labels = {e["label"] for e in entities}

        self.assertIn("NAME", labels)
        self.assertIn("ADDRESS", labels)


    def test_detects_name_and_vehicle(self):
        text = "Sarah Johnson bought a Honda Civic."
        entities = detect_entities(text)

        labels = {e["label"] for e in entities}

        self.assertIn("NAME", labels)
        self.assertIn("VEHICLE", labels)


    def test_detects_address_and_vehicle(self):
        text = "A Ford Mustang was seen in Los Angeles."
        entities = detect_entities(text)

        labels = {e["label"] for e in entities}

        self.assertIn("VEHICLE", labels)
        self.assertIn("ADDRESS", labels)