from django.test import TestCase

from data_processing.models import (
    Entity,
    IntelligenceReport,
    EntityIntelligenceReport,
    EntityLink,
)

from data_processing.services.relationLevelCalculator import relationLevelCalculator


class RelationLevelCalculatorTests(TestCase):
    def setUp(self):
        self.e1 = Entity.objects.create(name="Scott BAMBER", type="people")
        self.e2 = Entity.objects.create(name="SG19GGT", type="vehicle")
        self.e3 = Entity.objects.create(name="Glasgow", type="location")

    def _make_report_with_entities(self, text, entities):
        """Helper: create a report and connect it to entities via EntityIntelligenceReport."""
        report = IntelligenceReport.objects.create(fullReport=text)
        for e in entities:
            EntityIntelligenceReport.objects.create(entity=e, report=report)
        return report

    def test_creates_link_with_level_1_for_single_cooccurrence(self):
        self._make_report_with_entities("R1", [self.e1, self.e2])

        relationLevelCalculator()

        link = EntityLink.objects.get(entity1=self.e1, entity2=self.e2, reportLink=None)
        self.assertEqual(link.relationLevel, 1)

    def test_relation_level_equals_number_of_reports_capped_at_10(self):
        for i in range(12):
            self._make_report_with_entities(f"R{i}", [self.e1, self.e2])

        relationLevelCalculator()

        link = EntityLink.objects.get(entity1=self.e1, entity2=self.e2, reportLink=None)
        self.assertEqual(link.relationLevel, 10)

    def test_does_not_create_reverse_duplicate(self):
        # same report but entities inserted in reverse order
        self._make_report_with_entities("R1", [self.e2, self.e1])

        relationLevelCalculator()

        links = EntityLink.objects.filter(reportLink=None)
        self.assertEqual(links.count(), 1)

        link = links.first()
        # should always store smaller id as entity1, larger as entity2
        self.assertEqual(link.entity1_id, min(self.e1.entityID, self.e2.entityID))
        self.assertEqual(link.entity2_id, max(self.e1.entityID, self.e2.entityID))

    def test_only_pairs_in_same_report_are_counted(self):
        self._make_report_with_entities("R1", [self.e1, self.e2])
        self._make_report_with_entities("R2", [self.e1, self.e3])

        relationLevelCalculator()

        self.assertTrue(
            EntityLink.objects.filter(entity1=self.e1, entity2=self.e2, reportLink=None).exists()
        )
        self.assertTrue(
            EntityLink.objects.filter(entity1=self.e1, entity2=self.e3, reportLink=None).exists()
        )
        self.assertFalse(
            EntityLink.objects.filter(entity1=self.e2, entity2=self.e3, reportLink=None).exists()
        )

    def test_running_twice_does_not_duplicate_links(self):
        self._make_report_with_entities("R1", [self.e1, self.e2])
        self._make_report_with_entities("R2", [self.e1, self.e2])

        relationLevelCalculator()
        relationLevelCalculator()  # run again

        links = EntityLink.objects.filter(reportLink=None)
        self.assertEqual(links.count(), 1)

        link = links.first()
        self.assertEqual(link.relationLevel, 2)
