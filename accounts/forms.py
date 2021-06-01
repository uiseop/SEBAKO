from django import forms

from accounts.models import Person, Company


class personForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['user']

class companyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['user']