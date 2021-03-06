from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    model = User
    fields = [
        'username',
        'password',
        'password2',
        'email'
    ]