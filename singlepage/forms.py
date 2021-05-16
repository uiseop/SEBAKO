from django import forms

from accounts.models import SNS, Profile
from resumes.models import Resume, Experience, Education


class snsForm(forms.ModelForm):
    class Meta:
        model = SNS
        fields = ['name','url']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['korName','engName','address','email','phone','image',]

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title','regiNum','issure','dateAcq','file_upload',]

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title','company','text','dateFrom','dateEnd',]

class EduForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school','major','dateFrom','dateEnd',]