from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(IntelligenceReport)
admin.site.register(Entity)
admin.site.register(EntityLink)
admin.site.register(EntityIntelligenceReport)