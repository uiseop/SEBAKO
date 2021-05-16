from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from accounts.models import SNS
from resumes.models import Resume


def ResumeList(request): # 가장 메인에 보여줄 로직
    # model = Resume
    # template_name_suffix = '_list'
    resumes = Resume.objects.all()
    return render(request,'resumes/resume_list.html',{'objects':resumes})

class ResumeCreate(CreateView): # 자격증 생성할때 사용,채워야할 필드 확인, 이후에 연결될 탬플릿 이름은 resume_create일것
    model = Resume
    fields = ['title','regiNum','issure','dateAcq','file_upload']
    # template_name = 'resumes/resume_create.html'
    template_name_suffix = '_create'
    success_url = '/index'

    def form_valid(self, form):
        # 작성자는 현재 로그인 한 사용자로 설정함
        form.instance.user_id = self.request.user.id
        if form.is_valid():
            # 올바르다면 form : 모델폼
            form.instance.save()
            return redirect('/')
        else:
            # 올바르지 않다면
            return self.render_to_response({'form': form})

class ResumeUpdate(UpdateView):
    model = Resume
    # template_name = 'resumes/resume_update.html'
    fields = ['title','regiNum','issure','dateAcq', 'file_upload']
    template_name_suffix = '_update'
    success_url = '/resume/'

class ResumeDelete(DeleteView):
    model = Resume
    # template_name = 'resumes/resume_delete.html'
    template_name_suffix = '_delete'
    success_url = '/index'

class ResumeDetail(DetailView):
    model = Resume
    # template_name = 'resumes/resume_detail.html'
    template_name_suffix = '_detail'

