from django import forms
from . import models 
from .models import Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'date', 'content','street', 'city')