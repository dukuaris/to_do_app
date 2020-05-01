from django.forms import ModelForm, TextInput

from .models import *


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {'title': TextInput(attrs={'class':'input', 'placeholder':'Add a new task'})}