from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "policeID", "rank", "password1", "password2")