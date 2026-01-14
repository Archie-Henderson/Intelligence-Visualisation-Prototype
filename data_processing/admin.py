from django.contrib import admin
from .models import IntelligenceReport, Entity, Users, EntityIntelligenceReport

# Register your models here.
admin.site.register(IntelligenceReport)
admin.site.register(Entity)
admin.site.register(Users)
admin.site.register(EntityIntelligenceReport)

