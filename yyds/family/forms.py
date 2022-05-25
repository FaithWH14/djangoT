from django import forms
from .models import familyINFO

class familyForm(forms.ModelForm):
    class Meta:
        model = familyINFO
        fields = [
            "name",
            "age",
            "salary",
            "relationship"
        ]
    def clean_data(self):
        name = self.cleaned_data.get("name")
        if name.lower() == "abc":
            raise forms.ValidationError("This is not a proper name")
        return name
