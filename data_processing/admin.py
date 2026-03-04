from django.contrib import admin
from .models import IntelligenceReport, Entity, User, EntityIntelligenceReport

# Register your models here.
admin.site.register(IntelligenceReport)
admin.site.register(Entity)
admin.site.register(User)
admin.site.register(EntityIntelligenceReport)
