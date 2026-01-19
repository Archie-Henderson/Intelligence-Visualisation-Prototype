from django.test import TestCase
from data_processing.models import (IntelligenceReport, Entity, Users, EntityIntelligenceReport,
EntityLink, AccessLog)
from django.core.exceptions import ValidationError
from data_processing.services.relationLevelCalculator import relationLevelCalculator
from django.db import IntegrityError

class BasicDatabaseExistenceTests(TestCase):

    def test_intelligence_report_exists(self):
        IntelligenceReport.objects.create(fullReport="Test report")
        self.assertTrue(IntelligenceReport.objects.exists())

    def test_entity_exists(self):
        Entity.objects.create(name="Scott BAMBER", type=Entity.PEOPLE)
        self.assertEqual(Entity.objects.count(), 1)

    def test_user_exists(self):
        Users.objects.create(name="Alice", rank="Constable")
        self.assertTrue(Users.objects.exists())

    def test_entity_intelligence_report_exists(self):
        e = Entity.objects.create(name="SG19GGT", type=Entity.VEHICLE)
        r = IntelligenceReport.objects.create(fullReport="Vehicle spotted")
        EntityIntelligenceReport.objects.create(entity=e, report=r)

        self.assertTrue(EntityIntelligenceReport.objects.exists())

    def test_entity_link_exists(self):
        e1 = Entity.objects.create(name="Scott", type=Entity.PEOPLE)
        e2 = Entity.objects.create(name="SG19GGT", type=Entity.VEHICLE)

        EntityLink.objects.create(
            entity1=e1,
            entity2=e2,
            relationLevel=1,
        )

        self.assertEqual(EntityLink.objects.count(), 1)

    def test_access_log_exists(self):
        u = Users.objects.create(name="Bob", rank="Sergeant")
        r = IntelligenceReport.objects.create(fullReport="Report")

        AccessLog.objects.create(
            user=u,
            report=r,
            actionType="view",
        )

        self.assertTrue(AccessLog.objects.exists())

class IntelligenceReportModelTests(TestCase):
    def test_create_report(self):
        r = IntelligenceReport.objects.create(
            fullReport="Some report text",
            intelligenceSource="Test source",
        )
        self.assertIsNotNone(r.reportID)
        self.assertEqual(r.fullReport, "Some report text")
        self.assertEqual(r.intelligenceSource, "Test source")
        self.assertIsNotNone(r.creationTime)

    def test_report_str(self):
        r = IntelligenceReport.objects.create(fullReport="X")
        self.assertIn("Report", str(r))


class EntityModelTests(TestCase):
    def test_create_entity_valid_type(self):
        e = Entity.objects.create(name="Scott", type=Entity.PEOPLE)
        self.assertIsNotNone(e.entityID)
        self.assertEqual(e.name, "Scott")
        self.assertEqual(e.type, Entity.PEOPLE)

    def test_entity_invalid_type_fails_full_clean(self):
        e = Entity(name="Bad", type="not-a-real-type")
        with self.assertRaises(ValidationError):
            e.full_clean()

    def test_entity_str(self):
        e = Entity.objects.create(name="SG19GGT", type=Entity.VEHICLE)
        s = str(e)
        self.assertIn("SG19GGT", s)
        self.assertIn("vehicle", s)  # because your type constants are lowercase


class UsersModelTests(TestCase):
    def test_create_user_valid_rank(self):
        u = Users.objects.create(name="Alice", rank="Constable")
        self.assertIsNotNone(u.userID)
        self.assertEqual(u.rank, "Constable")
        self.assertEqual(u.rank_level, 1)

    def test_user_invalid_rank_fails_full_clean(self):
        u = Users(name="Bob", rank="NotARank")
        with self.assertRaises(ValidationError):
            u.full_clean()

    def test_rank_level_property(self):
        u = Users.objects.create(name="Carol", rank="Commissioner")
        self.assertEqual(u.rank_level, 11)

    def test_user_str(self):
        u = Users.objects.create(name="Dave", rank="Inspector")
        self.assertIn("Dave", str(u))
        self.assertIn("Inspector", str(u))


class EntityIntelligenceReportModelTests(TestCase):
    def setUp(self):
        self.e1 = Entity.objects.create(name="Scott BAMBER", type=Entity.PEOPLE)
        self.r1 = IntelligenceReport.objects.create(fullReport="Report 1")

    def test_create_join_row(self):
        join = EntityIntelligenceReport.objects.create(entity=self.e1, report=self.r1)
        self.assertIsNotNone(join.id)
        self.assertEqual(join.entity, self.e1)
        self.assertEqual(join.report, self.r1)

    def test_unique_together_prevents_duplicates(self):
        EntityIntelligenceReport.objects.create(entity=self.e1, report=self.r1)
        with self.assertRaises(Exception):
            # IntegrityError on database level
            EntityIntelligenceReport.objects.create(entity=self.e1, report=self.r1)

    def test_cascade_delete_report_deletes_join_rows(self):
        EntityIntelligenceReport.objects.create(entity=self.e1, report=self.r1)
        self.r1.delete()
        self.assertEqual(EntityIntelligenceReport.objects.count(), 0)

    def test_join_str(self):
        join = EntityIntelligenceReport.objects.create(entity=self.e1, report=self.r1)
        self.assertIn("in Report", str(join))


class EntityLinkModelTests(TestCase):
    def setUp(self):
        self.e1 = Entity.objects.create(name="Scott", type=Entity.PEOPLE)
        self.e2 = Entity.objects.create(name="SG19GGT", type=Entity.VEHICLE)
        self.r1 = IntelligenceReport.objects.create(fullReport="Report 1")

    def test_unique_together_prevents_duplicates_when_reportlink_is_set(self):
        EntityLink.objects.create(entity1=self.e1, entity2=self.e2, reportLink=self.r1, relationLevel=1)
        with self.assertRaises(IntegrityError):
            EntityLink.objects.create(entity1=self.e1, entity2=self.e2, reportLink=self.r1, relationLevel=2)
            
class AccessLogModelTests(TestCase):
    def setUp(self):
        self.user = Users.objects.create(name="Alice", rank="Sergeant")
        self.report = IntelligenceReport.objects.create(fullReport="Report 1")

    def test_create_access_log(self):
        log = AccessLog.objects.create(
            user=self.user,
            report=self.report,
            actionType="view",
        )
        self.assertIsNotNone(log.logID)
        self.assertEqual(log.actionType, "view")
        self.assertIsNotNone(log.actionTime)

    def test_accesslog_str(self):
        log = AccessLog.objects.create(user=self.user, report=self.report, actionType="edit")
        s = str(log)
        self.assertIn("edit", s)


class RelationLevelCalculatorIntegrationTests(TestCase):
   
    def setUp(self):
        self.e1 = Entity.objects.create(name="Scott BAMBER", type=Entity.PEOPLE)
        self.e2 = Entity.objects.create(name="SG19GGT", type=Entity.VEHICLE)

    def _make_report_with_entities(self, text, entities):
        report = IntelligenceReport.objects.create(fullReport=text)
        for e in entities:
            EntityIntelligenceReport.objects.create(entity=e, report=report)
        return report

    def test_calculator_creates_link_level_1(self):
        self._make_report_with_entities("R1", [self.e1, self.e2])

        relationLevelCalculator()

        link = EntityLink.objects.get(entity1=self.e1, entity2=self.e2, reportLink=None)
        self.assertEqual(link.relationLevel, 1)

    def test_calculator_caps_at_10(self):
        for i in range(12):
            self._make_report_with_entities(f"R{i}", [self.e1, self.e2])

        relationLevelCalculator()

        link = EntityLink.objects.get(entity1=self.e1, entity2=self.e2, reportLink=None)
        self.assertEqual(link.relationLevel, 10)

    def test_calculator_running_twice_does_not_duplicate(self):
        self._make_report_with_entities("R1", [self.e1, self.e2])
        self._make_report_with_entities("R2", [self.e1, self.e2])

        relationLevelCalculator()
        relationLevelCalculator()

        self.assertEqual(EntityLink.objects.filter(reportLink=None).count(), 1)
        link = EntityLink.objects.first()
        self.assertEqual(link.relationLevel, 2)
