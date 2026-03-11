from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from data_processing.models import *
from data_visualisation.forms import *
from django.db.models.lookups import GreaterThan, LessThan

import os
import json

# Create your views here.
def graph_view(request, node_id = None):
    filters = {'node_id':None,
                   'entity_type':"",
                   'entity_name':"",
                   'creation_data_end':None,
                   'creation_date_start':None,
                   'report_id':None,
                   'form_behaviour':False}

    ents = Entity.objects.all()
    filtered_ents = Entity.objects.all()
    links = EntityLink.objects.all()
    filter_data = False
    filtering = False
    
    json_path = os.path.abspath("./static/graph_data.json")

    data = {'nodes':[],
            'links':[]}

    if request.method == "POST":
        filter_form = FiltersForm(request.POST)

        if filter_form.is_valid():
            filters = filter_form.cleaned_data
            print(filters['form_behaviour'])

            if filters['node_id'] != None:
                filtered_ents = filtered_ents.filter(entityID__in = walk_tree(filters['node_id']))
                filtering = True
            if filters['entity_type'] != "":
                filtered_ents = filtered_ents.filter(type = filters['entity_type'])
                filtering = True
            if filters['entity_name'] != "":
                filtered_ents = filtered_ents.filter(name__contains = filters['entity_name'])
                filtering = True
            # if filters['creation_date_end'] != None:
            #     filtered_ents = filtered_ents.filter(entry_date__lt = filters['creation_date_end'])
            #     filtering = True
            # if filters['creation_date_start'] != None:
            #     filtered_ents = filtered_ents.filter(entry_date__gt = filters['creation_date_start'])
            #     filtering = True
            if filters['report_id'] != None:
                filtered_ents = filtered_ents.filter(entityID__in = EntityIntelligenceReport.objects.filter(report_id = filters['report_id']).values_list())
                filtering = True
            if filters['form_behaviour']:
                filter_data = True
                print("Filtering graph")

    if filter_data:
        data = add_data(ents=filtered_ents, show_unlinked_nodes=True, links=links, data=data)
    else:
        data = add_data(ents=ents, show_unlinked_nodes=False, links=links, data=data)


    context = {'unlinked':[],
               'linked':[],
               "cur_url": reverse('data_visualisation:graph'),
               "form":filters}
    context = add_context(filtered_ents, filtering, context)

    with open(json_path, "w") as f:
        json.dump(data, f)

    return render(request, 'data_visualisation/graph.html', context = context)

def add_context(ents, filtering, context):
    for ent in ents:
            if (not filtering) and EntityLink.objects.filter(entity_1 = ent).count() +  EntityLink.objects.filter(entity_2 = ent).count() == 0:
                context['unlinked'].append({'id':ent.entityID, 'name':ent.name})
            else:
                context['linked'].append({'id':ent.entityID, 'name':ent.name})
    return context

def add_data(ents, show_unlinked_nodes, links, data):
    for ent in ents:
        if show_unlinked_nodes or EntityLink.objects.filter(entity_1 = ent).count() +  EntityLink.objects.filter(entity_2 = ent).count() > 0:
            data['nodes'].append({'id':ent.entityID, 'name':ent.name})

    for link in links:
        if link.entity_1 in ents and link.entity_2 in ents:
            data['links'].append({'source':link.entity_1.entityID, 'target':link.entity_2.entityID})
        
    return data

def walk_tree(ent_id):
    nodes = [Entity.objects.get(entityID = ent_id)]
    discovered_nodes = {Entity.objects.get(entityID = ent_id).entityID}

    while len(nodes) > 0:
        node = nodes.pop()
        for ent in EntityLink.objects.filter(entity_1 = node.entityID).union(EntityLink.objects.filter(entity_2 = node.entityID)):
            if ent.entity_1.entityID not in discovered_nodes:
                discovered_nodes.add(ent.entity_1.entityID)
                nodes.append(ent.entity_1)
            elif ent.entity_2.entityID not in discovered_nodes:
                discovered_nodes.add(ent.entity_2.entityID)
                nodes.append(ent.entity_2)

    return discovered_nodes
            

def entity_details(request, ent_id):
    entity = Entity.objects.get(entityID = ent_id)
    reports=[]
    for entity_intelligence_report in EntityIntelligenceReport.objects.filter(entity = entity):
        reports.append(entity_intelligence_report.report)

    links = []

    for link in EntityLink.objects.filter(entity_1 = entity):
        links.append({'other_ent':link.entity_2.entityID, 'report':link.intelligence_report})

    for link in EntityLink.objects.filter(entity_2 = entity):
        links.append({'other_ent':link.entity_1, 'report':link.intelligence_report})

    print(entity, reports, links)
    context = {'entity':entity, 'reports':reports, 'links':links}
    return render(request, 'data_visualisation/entity_details.html', context=context)