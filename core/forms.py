from django import forms
from .models import Master

class MasterForm(forms.ModelForm):

    class Meta:
        model = Master
        fields = ()