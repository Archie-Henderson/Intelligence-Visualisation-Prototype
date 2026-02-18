from django.db import models

class Document(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "data_processing"

class Event(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="events")
    event_type = models.CharField(max_length=50, default="unknown")
    title = models.CharField(max_length=200, blank=True)
    datetime_start = models.DateTimeField(null=True, blank=True)
    datetime_end = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    people = models.JSONField(default=list, blank=True)   # list of strings
    organizations = models.JSONField(default=list, blank=True)
    vehicles = models.JSONField(default=list, blank=True)
    telecom = models.JSONField(default=list, blank=True)
    objects = models.JSONField(default=list, blank=True)
    description = models.TextField(blank=True)
    source_text_span = models.TextField(blank=True)

    class Meta:
        app_label = "data_processing"