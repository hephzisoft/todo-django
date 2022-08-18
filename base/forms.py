
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Todo


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'username', 'password1', 'password2']


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['tag', 'description']
