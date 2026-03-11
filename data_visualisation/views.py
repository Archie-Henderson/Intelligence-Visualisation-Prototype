from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from data_processing.models import *
from data_visualisation.forms import *
from django.db.models import Count
from django.db.models.lookups import GreaterThan, LessThan

import os
import json

# Create your views here.
def graph_view(request):
    form_data = request.POST if request.method == "POST" else request.GET
    filter_form = FiltersForm(form_data or None)

    ents = Entity.objects.all()
    filtered_ents = Entity.objects.all()
    links = EntityLink.objects.all()
    filtering = False

    context = {
        'unlinked': [],
        'linked': [],
        "cur_url": reverse('data_visualisation:graph'),
        "form": filter_form,
    }

    json_path = os.path.abspath("./static/graph_data.json")
    data = {'nodes': [], 'links': []}

    if filter_form.is_valid():
        filters = filter_form.cleaned_data

        if filters["node_id"] is not None:
            filtered_ents = filtered_ents.filter(entityID=filters["node_id"])
            filtering = True

        if filters["entity_type"]:
            filtered_ents = filtered_ents.filter(type=filters["entity_type"])
            filtering = True

        if filters["entity_name"]:
            filtered_ents = filtered_ents.filter(name__icontains=filters["entity_name"])
            filtering = True

        if filters["report_id"] is not None:
            report_entity_ids = (
                EntityIntelligenceReport.objects
                .filter(
                    report_id=filters["report_id"],
                    isDeleted=False,
                    entity__isDeleted=False,
                    report__isDeleted=False,
                )
                .values_list("entity_id", flat=True)
            )
            filtered_ents = filtered_ents.filter(entityID__in=report_entity_ids)
            filtering = True

        if filters["creation_date_start"] is not None:
            report_entity_ids = (
                EntityIntelligenceReport.objects
                .filter(
                    report__createdAt__date__gte=filters["creation_date_start"].date(),
                    isDeleted=False,
                    entity__isDeleted=False,
                    report__isDeleted=False,
                )
                .values_list("entity_id", flat=True)
            )
            filtered_ents = filtered_ents.filter(entityID__in=report_entity_ids)
            filtering = True

        if filters["creation_date_end"] is not None:
            report_entity_ids = (
                EntityIntelligenceReport.objects
                .filter(
                    report__createdAt__date__lte=filters["creation_date_end"].date(),
                    isDeleted=False,
                    entity__isDeleted=False,
                    report__isDeleted=False,
                )
                .values_list("entity_id", flat=True)
            )
            filtered_ents = filtered_ents.filter(entityID__in=report_entity_ids)
            filtering = True

    if filtering:
        data = add_data(
            ents=filtered_ents,
            show_unlinked_nodes=True,
            links=links,
            data=data
        )
    else:
        data = add_data(
            ents=ents,
            show_unlinked_nodes=False,
            links=links,
            data=data
        )

    context = add_context(filtered_ents if filtering else ents, filtering, context)

    with open(json_path, "w") as f:
        json.dump(data, f)

    return render(request, 'data_visualisation/graph.html', context=context)

def add_context(ents, filtering, context):
    for ent in ents:
            if (not filtering) and EntityLink.objects.filter(entity1 = ent).count() +  EntityLink.objects.filter(entity2 = ent).count() == 0:
                context['unlinked'].append({'id':ent.entityID, 'name':ent.name})
            else:
                context['linked'].append({'id':ent.entityID, 'name':ent.name})
    return context

def add_data(ents, show_unlinked_nodes, links, data):
    mention_counts_qs = (
        EntityIntelligenceReport.objects
        .filter(entity__in=ents, isDeleted=False, entity__isDeleted=False)
        .values("entity_id")
        .annotate(count=Count("id"))
    )
    mention_counts = {row["entity_id"]: row["count"] for row in mention_counts_qs}

    for ent in ents:
        if show_unlinked_nodes or EntityLink.objects.filter(entity1=ent).count() + EntityLink.objects.filter(entity2=ent).count() > 0:
            freq = mention_counts.get(ent.entityID, 0)
            data["nodes"].append({"id": ent.entityID, "name": ent.name, "freq": freq})

    for link in links:
        if link.entity1 in ents and link.entity2 in ents:
            level = link.relationLevel if link.relationLevel is not None else 1
            freq1 = mention_counts.get(link.entity1_id, 0)
            freq2 = mention_counts.get(link.entity2_id, 0)
            importance = freq1 + freq2
            data["links"].append(
                {
                    "source": link.entity1.entityID,
                    "target": link.entity2.entityID,
                    "level": level,
                    "importance": importance,
                }
            )

    return data
    
def walk_tree(ent_id):
    start_node = Entity.objects.get(entityID=ent_id)
    nodes = [start_node]
    discovered_nodes = {start_node.entityID}

    while nodes:
        node = nodes.pop()

        linked_edges = EntityLink.objects.filter(entity1=node) | EntityLink.objects.filter(entity2=node)

        for link in linked_edges:
            if link.entity1.entityID not in discovered_nodes:
                discovered_nodes.add(link.entity1.entityID)
                nodes.append(link.entity1)

            if link.entity2.entityID not in discovered_nodes:
                discovered_nodes.add(link.entity2.entityID)
                nodes.append(link.entity2)

    return discovered_nodes

def entity_details(request, ent_id):
    entity = Entity.objects.get(entityID=ent_id)

    # All reports where this entity is mentioned (respecting soft delete flags)
    report_links = []
    eir_qs = (
        EntityIntelligenceReport.objects
        .select_related("report", "entity")
        .filter(entity=entity, isDeleted=False, report__isDeleted=False)
        .order_by("report__reportID")
    )

    for eir in eir_qs:
        report = eir.report
        # All other entities in the same report
        other_entities = (
            Entity.objects.filter(
                entityintelligencereport__report=report,
                entityintelligencereport__isDeleted=False,
                isDeleted=False,
            )
            .exclude(entityID=entity.entityID)
            .distinct()
            .order_by("name")
        )
        report_links.append(
            {
                "report": report,
                "other_entities": list(other_entities),
            }
        )

    context = {
        "entity": entity,
        "report_links": report_links,
    }
    return render(request, "data_visualisation/entity_details.html", context=context)