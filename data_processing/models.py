from django.db import models

class IntelligenceReport(models.Model):
     reportID = models.AutoField(primary_key = True)
     fullReport = models.TextField()
     intelligenceSource = models.TextField(null = True, blank = True)

     def __str__(self):
        return f"Report {self.pk}"

class Entity(models.Model):
     entityID = models.AutoField(primary_key = True)
     name = models.CharField(max_length = 255)
     type = models.CharField(max_length = 255)

     def __str__(self):
        return f"{self.name} ({self.type})"

class Users(models.Model):
     # ranks by the 'Metropolitan Police' website
     RANK_DATA = [
        ("Constable", "Constable", 1),
        ("Sergeant", "Sergeant", 2),
        ("Inspector", "Inspector", 3),
        ("Chief Inspector", "Chief Inspector", 4),
        ("Superintendent", "Superintendent", 5),
        ("Chief Superintendent", "Chief Superintendent", 6),
        ("Commander", "Commander", 7),
        ("Deputy Assistant Commissioner", "Deputy Assistant Commissioner", 8),
        ("Assistant Commissioner", "Assistant Commissioner", 9),
        ("Deputy Commissioner", "Deputy Commissioner", 10),
        ("Commissioner", "Commissioner", 11),
    ]
     
     # order the ranks
     RANKS = [(name, display) for (name, display, level) in RANK_DATA]
     RANK_ORDER = {name: level for (name, display, level) in RANK_DATA}

     userID = models.AutoField(primary_key=True)
     name = models.CharField(max_length=255)
     rank = models.CharField(max_length=50, choices=RANKS)

     def __str__(self):
          return f"{self.name} ({self.rank})"

     @property
     def rank_level(self):
          return self.RANK_ORDER.get(self.rank)

class EntityIntelligenceReport(models.Model):
     entity = models.ForeignKey(Entity, on_delete = models.CASCADE, null = True)
     report = models.ForeignKey(IntelligenceReport, on_delete = models.CASCADE, null = True)

     class Meta:
        unique_together = ("entity", "report")

     def __str__(self):
        return f"{self.entity} in {self.report}"
