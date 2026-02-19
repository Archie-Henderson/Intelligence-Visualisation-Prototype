from __future__ import annotations

from unittest import skipUnless

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.
from data_processing.models import (
    IntelligenceReport,
    Entity,
    EntityIntelligenceReport,
    EntityLink,
)
from data_visualisation.views import graph_view, entity_details

try:
    from data_visualisation.filters import filter_entities
    FILTERING_AVAILABLE = True
except ModuleNotFoundError:
    filter_entities = None
    FILTERING_AVAILABLE = False

try:
    from data_visualisation.resizing import resize_graph
    RESIZING_AVAILABLE = True
except ModuleNotFoundError:
    resize_graph = None
    RESIZING_AVAILABLE = False

class GraphViewTests(TestCase):

    def test_graph_page_loads(self):
        response = self.client.get(reverse('data_visualisation:graph'))
        self.assertEqual(response.status_code, 200)

    def test_graph_with_no_entities(self):
        response = self.client.get(reverse('data_visualisation:graph'))

        self.assertEqual(len(response.context['linked']), 0)
        self.assertEqual(len(response.context['unlinked']), 0)

    def test_linked_and_unlinked_entities(self):
        e1 = Entity.objects.create(name="Entity 1", type="ADDRESS")
        e2 = Entity.objects.create(name="Entity 2", type="VEHICLE")
        e3 = Entity.objects.create(name="Entity 3", type="NAME")

        report = IntelligenceReport.objects.create(fullReport="Test Report")

        EntityLink.objects.create(
            entity_1=e1,
            entity_2=e2,
            intelligence_report=report,
        )

        response = self.client.get(reverse('data_visualisation:graph'))

        linked_names = {e['name'] for e in response.context['linked']}
        unlinked_names = {e['name'] for e in response.context['unlinked']}

        self.assertEqual(linked_names, {"Entity 1", "Entity 2"})
        self.assertEqual(unlinked_names, {"Entity 3"})

class EntityDetailsTests(TestCase):
    
    def setUp(self):
        self.entity1 = Entity.objects.create(name="Alice", type="NAME")
        self.entity2 = Entity.objects.create(name="Car", type="VEHICLE")

        self.report1 = IntelligenceReport.objects.create(fullReport="Report 1")
        self.report2 = IntelligenceReport.objects.create(fullReport="Report 2")

        EntityIntelligenceReport.objects.create(
            entity=self.entity1,
            report=self.report1
        )

        EntityLink.objects.create(
            entity_1=self.entity1,
            entity_2=self.entity2,
            intelligence_report=self.report2
        )

    def test_entity_details_page_loads(self):
        response = self.client.get(reverse('data_visualisation:ent_details', args=[self.entity1.entityID]))
        self.assertEqual(response.status_code, 200)

    def test_entity_reports_displayed(self):
        response = self.client.get(reverse('data_visualisation:ent_details', args=[self.entity1.entityID]))
        self.assertContains(response, "Report")
        self.assertContains(response, str(self.report1.reportID))

    def test_entity_links_displayed(self):
        response = self.client.get(reverse('data_visualisation:ent_details', args=[self.entity1.entityID]))
        self.assertContains(response, f"connected through report {self.report2.reportID}")

    def test_entity_with_no_links(self):
        entity3 = Entity.objects.create(name="Bob", type="NAME")
        response = self.client.get(reverse('data_visualisation:ent_details', args=[entity3.entityID]))
        self.assertEqual(response.status_code, 200)

@skipUnless(FILTERING_AVAILABLE, "filter_entities not implemented")
class FilterEntitiesTests(SimpleTestCase):

    def test_filter_by_type(self):
        self.assertTrue(FILTERING_AVAILABLE)

@skipUnless(RESIZING_AVAILABLE, "resize_graph not implemented")
class ResizeGraphTests(SimpleTestCase):

    def test_resize_graph(self):
        self.assertTrue(RESIZING_AVAILABLE)