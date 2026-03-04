from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import (
    IntelligenceReport, Entity, EntityIntelligenceReport,
    EntityLink, AccessLog, EntityProfile
)

User = get_user_model()

admin.site.register(User)
admin.site.register(IntelligenceReport)
admin.site.register(Entity)
admin.site.register(EntityIntelligenceReport)
admin.site.register(EntityLink)
admin.site.register(AccessLog)
admin.site.register(EntityProfile)