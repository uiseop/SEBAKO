from django.shortcuts import render

# Create your views here.
from resumes.models import SelfIntro, Experience, Education, Resume


def _page_id(request):
    single = request.session.session_key
    if not single:
        single = request.session.create()
    return single

def PageDetail(request,pk):
    # print(request.user) : seop 출럭
    # print(request.user.profile.korName)
    intros = SelfIntro.objects.all()
    intro_list = intros.filter(user=request.user)
    expers = Experience.objects.all()
    experience_list = expers.filter(user=request.user)
    edus = Education.objects.all()
    education_list = edus.filter(user=request.user)
    resumes = Resume.objects.all()
    resume_list = resumes.filter(user=request.user)

    return render(request, 'singlepage/index.html',{'intro_list':intro_list,'experience_list':experience_list,'education_list':education_list,'resume_list':resume_list})
