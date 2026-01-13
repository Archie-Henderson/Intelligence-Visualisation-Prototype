from django.db import models

class IntelligenceReport(models.Model):
     reportID = models.AutoField(primary_key = True)
     fullReport = models.TextField()

     def __str__(self):
        return f"Report {self.pk}"

class Entity(models.Model):
     entityID = models.AutoField(primary_key = True)
     name = models.CharField(max_length = 255)
     type = models.CharField(max_length = 255)

     def __str__(self):
        return f"{self.name} ({self.type})"

class EntityIntelligenceReport(models.Model):
     entity = models.ForeignKey(Entity, on_delete = models.CASCADE, null = True)
     report = models.ForeignKey(IntelligenceReport, on_delete = models.CASCADE, null = True)

     class Meta:
        unique_together = ("entity", "report")

     def __str__(self):
        return f"{self.entity} in {self.report}"

class EntityLink(models.Model):
    linkID = models.AutoField(primary_key=True)
    entity_1 = models.ForeignKey(Entity, on_delete = models.CASCADE, null = True)
    entity_2 = models.ForeignKey(Entity, on_delete = models.CASCADE, null = True, related_name='entity_1')
    intelligence_report = models.ForeignKey(IntelligenceReport, on_delete = models.CASCADE, null = True)