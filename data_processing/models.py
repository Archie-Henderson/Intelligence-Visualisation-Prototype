from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

# intelligence report contents are defined below
class IntelligenceReport(models.Model):
    reportID = models.AutoField(primary_key=True)
    fullReport = models.TextField()
    intelligenceSource = models.TextField(null=True, blank=True)

    # soft delete and audit timestamps
    isDeleted = models.BooleanField(default=False)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    # who uploaded and created this report
    createdBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_reports",
    )
    @property
    def creationTime(self):
        return self.createdAt

    # AI label and approval gate
    isAiGenerated = models.BooleanField(default=True)
    isApproved = models.BooleanField(default=False)
    approvedAt = models.DateTimeField(null=True, blank=True)
    approvedBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="approved_reports",
    )

    def __str__(self):
        return f"Report {self.pk}"

# entities are defined below
class Entity(models.Model):
    entityID = models.AutoField(primary_key = True)

    PEOPLE = "people"
    VEHICLE = "vehicle"
    TELECOM = "telecom"
    LOCATION = "location"

    ENTITY_TYPES = [
        (PEOPLE, "People"), (VEHICLE, "Vehicle"), (TELECOM, "Telecom"), (LOCATION, "Location"),
    ]

    name = models.CharField(max_length = 255)
    type = models.CharField(max_length = 20, choices= ENTITY_TYPES)

    #delete wrong ones
    isDeleted = models.BooleanField(default=False)     
    # AI or user, who added the entity
    source = models.CharField(max_length=20, default="SPACY")  
    updatedAt = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name} ({self.type})"

# user details are defined below
class User(AbstractUser):
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
     
    # ordering of the ranks
    RANKS = [(name, display) for (name, display, level) in RANK_DATA]
    RANK_ORDER = {name: level for (name, display, level) in RANK_DATA}

    isManager = models.BooleanField(default= False)
    policeID = models.CharField(max_length= 50, primary_key= True)
    rank = models.CharField(max_length=50, choices=RANKS, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        if self.rank:
            return f"{self.name} ({self.rank})"
        return self.name

    @property
    def rank_level(self):
        return self.RANK_ORDER.get(self.rank)

# entity's intelligence report creation is below
class EntityIntelligenceReport(models.Model):
    entity = models.ForeignKey(Entity, on_delete = models.CASCADE)
    report = models.ForeignKey(IntelligenceReport, on_delete = models.CASCADE)

    isDeleted = models.BooleanField(default=False)
    source = models.CharField(max_length=20, default="SPACY")  
    updatedAt = models.DateTimeField(auto_now=True) 

    class Meta:
        unique_together = ("entity", "report")

    def __str__(self):
        return f"{self.entity} in {self.report}"

# entity links between two entities are defined below
class EntityLink(models.Model):
    linkID = models.AutoField(primary_key=True)

    entity1 = models.ForeignKey(
        Entity, on_delete= models.CASCADE, related_name= "links_from"
    )

    entity2 = models.ForeignKey(
        Entity, on_delete= models.CASCADE, related_name= "links_to"
    )

    reportLink = models.ForeignKey(
        IntelligenceReport, on_delete= models.SET_NULL, null = True, blank= True
    )

    relationLevel = models.PositiveSmallIntegerField(
        null= True, blank = True, help_text= "Closeness score between the entities, from 1 to 10 (10 is strong relation)"
    )

    class Meta:
        unique_together = ("entity1", "entity2", "reportLink")
        
    def __str__(self):
         return f"{self.entity1} - {self.entity2} (Relation Level: {self.relationLevel}/10)"
    
#log of the access are going to be recorded for data safety reasons
class AccessLog(models.Model):
    
    logID = models.AutoField(primary_key= True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    report = models.ForeignKey(IntelligenceReport, on_delete= models.SET_NULL, null =  True, blank = True)

    # identify what was the action (edited, added, viewed...)
    ACTION_TYPES = [
        ('view', "View"), ("add", "Add"), ("edit", "Edit"), ("delete", "Delete")
    ]

    actionType = models.CharField(max_length=20, choices=ACTION_TYPES)
    actionTime = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.actionTime} {self.actionType} {self.user} {self.report}"
    
class EntityProfile(models.Model):
    profileID = models.AutoField(primary_key=True)
    entity = models.OneToOneField(Entity, on_delete=models.CASCADE, related_name="profile")

    age = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    role = models.CharField(max_length=80, null=True, blank=True)

    notes = models.TextField(null=True, blank=True)

    source = models.CharField(max_length=10, default="AI")  # AI / USER
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile for {self.entity}"
