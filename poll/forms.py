from django import forms
from django.forms import ModelForm
from .models import PollModel

class PollForm(forms.ModelForm):
    class Meta:
        model = PollModel
        fields = ['title', 'c1', 'c2', 'c3']