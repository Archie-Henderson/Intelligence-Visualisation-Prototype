from django.contrib import admin
from .models import IntelligenceReport, Entity, User, EntityIntelligenceReport

# Register your models here.
from .models import *
admin.site.register(IntelligenceReport)
admin.site.register(EntityLink)
admin.site.register(Entity)
admin.site.register(User)
admin.site.register(EntityIntelligenceReport)
