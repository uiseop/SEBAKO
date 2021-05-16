from django import forms

from accounts.models import SNS, Profile


class snsForm(forms.ModelForm):
    class Meta:
        model = SNS
        fields = ['name','url']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['korName','engName','address','email','phone','image',]

