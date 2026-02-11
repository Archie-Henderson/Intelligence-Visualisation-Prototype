import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "intelligence.settings")

import django
django.setup()
from data_processing.models import *

def populate():
    reports = [{'fullReport':"""Intelligence provides that on 1 December 2023, a group of teenagers both boys and girls knocked over a large number of wheelie bins in Causeyside Street, Paisley causing a significant amount of rubbish including bottles to be scattered all over the road. 2AP """},
               {'fullReport':"""Intelligence provides that, every Friday at around 6pm a black coloured BMW, possibly a 3 series parks in the McDonalds car park, Linwood for about an hour. The driver doesn’t leave the vehicle but has been seen handing packages similar in size to a bag of sugar to different males who appear at the car during the time it is parked. There can be 4 or 5 different males appear during the hour 6-7pm. 

2AP """},
               {'fullReport':"""Intelligence provides that on Sunday 3 December 2023, The Canal bar, Stow Brae, Paisley was showing Sky Sports football matches and don’t have a contract with Sky. """},
               {'fullReport':"""Intelligence provides that on 4 March 2023 

 

Scott BAMBER 

Bn.12/03/2005 

80 Maryhill Road 

Glasgow 

G207QB 

  

Is responsible for assaulting to tourists in Queen Margaret Drive, Glasgow at the weekend. He was under the influence of alcohol at the time."""},
               {'fullReport':"""Intelligence provides that local residents near to  

 

Pollok Park 

Glasgow 

 

Are complaining that every Friday evening large groups of teenagers are gathering drinking alcohol and causing a disturbance near to the park entry on Haggs Road, Glasgow. """},
               {'fullReport':"""Intelligence provides that 

 

Every Friday evening the owner of  

Vauxhall Astra Reg No. SF13DDR 

 

Drives home from the  

Stumps bar 

7 Peel Street 

Glasgow 

G115LL 

 

Under the influence of alcohol. 

Note; 

The Registered keeper of SF13DDR is 

Robert UNDERWOOD 

12 Thornwood Terrace 

Glasgow  

G117QZ """},
               {'fullReport':"""Intelligence provides that  

 

An anonymous neighbour from Napiershall Street, Glasgow has reported that a couple only known to her as Richard and Michelle are regularly heard shouting abuse at each other causing a disturbance. The anonymous neighbour has noticed previously Michelle having marks of her face and arms as if she has been assaulted and on days when it is dull Michelle has been seen wearing oversized sun glasses. Other neighbours have allegedly also heard the disturbances.  """},
               {'fullReport':"""Intelligence provides that  

 

Kevin GRANDER 

Aka Tadpole 

Bn. 16/06/1987 

LKA 229 Liddesdale Road 

Glasgow 

G227QT 

 

Who operates as an enforcer for the POLLOCK crime family keeps weapons such as a baseball bat and hammers in the unit next to the front door in case of any uninvited guests appearing at his door.  """},
               {'fullReport':"""Intelligence provides that  

 

A male known only as Teabag is regularly reselling food products from his flat in Saracen Street, Glasgow. The items he is selling are all shoplifted from the local Lidl store. """},
               {'fullReport':"""Intelligence provides that the garage at situated in an industrial estate in 

 

McFarlane Street 

Paisley 

 

Is selling stolen alloy wheels. 

Note; 

There has been a 200 percent increase in reports of stolen alloy wheels in the last 2 months in the Paisley area. """},
               {'fullReport':"""Intelligence provides that 

 

Hugh GILLESPIE 

Bn.05/06/2005 

33 Cockmuir Street 

Glasgow 

G214XD 

 

Regularly carries a knife concealed in his socks when outwith his home address. """}]
    
    entities = [{'name': 'Causeyside, Paisley', 'type': 'street', 'reports':[1]},
                {'name': 'BMW Car', 'type': 'car', 'reports':[2]},
                {'name': 'McDonalds car park, Linwood', 'type': 'location', 'reports':[2]},
                {'name': 'Canal bar, Stow Brae, Paisley', 'type': 'location', 'reports':[3]},
                {'name': 'Scott BAMBER', 'type': 'person', 'reports':[4]},
                {'name': '80 Maryhill Road Glasgow, G207QB', 'type':'address', 'reports':[4]},
                {'name':'Queen Margaret Drive, Glasgow', 'type': 'street', 'reports':[4]},
                {'name':'Pollok Park, Glasgow residents', 'type':'group', 'reports':[5]},
                {'name':'Haggs Road, Glasgow', 'type': 'street', 'reports':[5]},
                {'name': 'Vauxhall Astra SF13DDR', 'type': 'car', 'reports':[6]},
                {'name': 'Stumps Bar', 'type':'location', 'reports':[6]},
                {'name':'7 Peel Street Glasgow, G115LL', 'type': 'address', 'reports':[6]},
                {'name':'Robert UNDERWOOD', 'type':'person', 'reports':[6]},
                {'name':'12 Thornwood Terrace Glasgow, G117QZ', 'type':'address', 'reports':[6]},
                {'name':'Napiershall Street', 'type':'street', 'reports':[7]},
                {'name':'Richard', 'type':'person', 'reports':[7]},
                {'name':'Michelle', 'type':'person', 'reports':[7]},
                {'name':'Kevin GRANDER', 'type':'person', 'reports':[8]},
                {'name':'Tadpole', 'type':'alias', 'reports':[8]},
                {'name':'LKA 229 Liddesdale Road Glasgow, G227QT', 'type':'address', 'reports':[8]},
                {'name':'POLLOCK', 'type':'group', 'reports':[8]},
                {'name':'Teabag', 'type':'alias', 'reports':[9]},
                {'name':'Saracen Street, Glasgow', 'type':'street', 'reports':[9]},
                {'name':'Lidl near Saracen Street', 'type':'location', 'reports':[9]},
                {'name':'McFarlane Street Paisley Garage', 'type':'location', 'reports':[10]},
                {'name':'Hugh GILLESPIE', 'type':'person', 'reports':[11]},
                {'name':'33 Cockmuir Street Glasgow, G214XD', 'type':'address', 'reports':[11]}
                ]
    
    links = [{'e1': 2,'e2': 3, 'report': 2},
             {'e1': 5,'e2': 6, 'report': 4},
             {'e1': 5,'e2': 7, 'report': 4},
             {'e1': 8,'e2': 9, 'report': 5},
             {'e1': 10,'e2': 11, 'report': 6},
             {'e1': 11,'e2': 12, 'report': 6},
             {'e1': 10,'e2': 13, 'report': 6},
             {'e1': 13,'e2': 14, 'report': 6},
             {'e1': 16,'e2': 17, 'report': 7},
             {'e1': 15,'e2': 16, 'report': 7},
             {'e1': 15,'e2': 17, 'report': 7},
             {'e1': 18,'e2': 19, 'report': 8},
             {'e1': 18,'e2': 20, 'report': 8},
             {'e1': 19,'e2': 20, 'report': 8},
             {'e1': 18,'e2': 21, 'report': 8},
             {'e1': 22,'e2': 23, 'report': 9},
             {'e1': 22,'e2': 24, 'report': 9},
             {'e1': 26,'e2': 27, 'report': 11},
             ]
    
    for report in reports:
        add_report(report['fullReport'])

    for ent in entities:
        add_entity(ent['name'], ent['type'], ent['reports'])

    for link in links:
        add_link(Entity.objects.get(entityID=link['e1']), Entity.objects.get(entityID=link['e2']), IntelligenceReport.objects.get(reportID=link['report']))


def add_report(text):
    report = IntelligenceReport.objects.create()
    report.fullReport = text
    report.save()
    return report

def add_entity(name, type, reportIDs):
    ent = Entity.objects.create()
    ent.name = name
    ent.type = type
    ent.save()
    for reportID in reportIDs:
        entity_intelligence_report = EntityIntelligenceReport.objects.create()
        entity_intelligence_report.entity = Entity.objects.get(name = name)
        entity_intelligence_report.report = IntelligenceReport.objects.get(reportID = reportID)
        entity_intelligence_report.save()
    return ent, entity_intelligence_report

def add_link(ent1, ent2, report):
    link = EntityLink.objects.get_or_create(entity_1 = ent1, entity_2 = ent2, intelligence_report = report)[0]
    link.save()
    return link

if __name__ == '__main__':
    populate()