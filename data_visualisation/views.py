from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from data_processing.models import *

import os
import json

# Create your views here.
def graph_view(request):
    ents = Entity.objects.all()
    links = EntityLink.objects.all()
    context = {'unlinked':[]}
    
    json_path = os.path.abspath("./static/graph_data.json")

    data = {'nodes':[],
            'links':[]}
    
    for ent in ents:
        if EntityLink.objects.filter(entity_1 = ent).count() +  EntityLink.objects.filter(entity_2 = ent).count() == 0:
            context['unlinked'].append({'id':ent.entityID, 'name':ent.name})
            print("Unlinked: " + str(ent.entityID) + ", " + ent.name)
        else:
            data['nodes'].append({'id':ent.entityID, 'name':ent.name})
    
    for link in links:
        data['links'].append({'source':link.entity_1.entityID, 'target':link.entity_2.entityID})


    print(json_path)
    with open(json_path, "w") as f:
        json.dump(data, f)

    return render(request, 'data_visualisation/graph.html', context = context)