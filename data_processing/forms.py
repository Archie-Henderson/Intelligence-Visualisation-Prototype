from django import forms
from .models import IntelligenceReport, Entity, User, EntityIntelligenceReport
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'policeID', 'rank', "password1", "password2")
