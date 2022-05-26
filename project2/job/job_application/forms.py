from .models import jobApplication
from django import forms

class jobAppliedForm(forms.ModelForm):
    class Meta:
        model = jobApplication
        fields = "__all__"