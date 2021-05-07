from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from resumes.models import Resume


class ResumeList(ListView): # 가장 메인에 보여줄 로직
    model = Resume
    template_name_suffix = '_list'

class ResumeCreate(CreateView): # 자격증 생성할때 사용,채워야할 필드 확인, 이후에 연결될 탬플릿 이름은 resume_create일것
    model = Resume
    fields = ['title','regiNum','issure','dateAcq']
    template_name_suffix = '_create'
    success_url = '/index'

class ResumeUpdate(UpdateView):
    model = Resume
    fields = ['title','regiNum','issure','dateAcq']
    template_name_suffix = '_update'
    success_url = '/index'

class ResumeDelete(DeleteView):
    model = Resume
    template_name_suffix = '_delete'
    success_url = '/index'

class ResumeDetail(DetailView):
    model = Resume
    template_name_suffix = '_detail'

