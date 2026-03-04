from data_processing.models import EntityIntelligenceReport, EntityLink
from collections import defaultdict

#calculateing the relationLevel from 1 to 10 for the entities co-occurrence across inteligence reports
def relationLevelCalculator():

      #list the entity IDs
      entitiesReport = defaultdict(list)

      for row in EntityIntelligenceReport.objects.all():
            entitiesReport[row.report_id].append(row.entity_id)

      # counting the occurrences
      pairCount = defaultdict(int)

      for entityIDs in entitiesReport.values():
            unique_entities = sorted(set(entityIDs))

            for i in range(len(unique_entities)):
                  for j in range(1+i, len(unique_entities)):
                        pair = (unique_entities[i], unique_entities[j])
                        pairCount[pair] = pairCount[pair]+1

      #store and update entitylink
      for (entity1ID, entity2ID), count in pairCount.items():
            relationLevel = min(count,10)

            EntityLink.objects.update_or_create(entity1_id=entity1ID, entity2_id=entity2ID, reportLink=None, defaults = {"relationLevel": relationLevel})