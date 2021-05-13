from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from accounts.decorators import login_message_required
from resumes.models import SelfIntro, Experience, Education, Resume


def _page_id(request):
    single = request.session.session_key
    if not single:
        single = request.session.create()
    return single


@login_message_required
def PageDetail(request,pk):
    # print(request.user) : seop 출럭
    # print(request.user.profile.korName)
    user = User.objects.get(id=pk)
    print(request.user.id)
    intros = SelfIntro.objects.all()
    intro_list = intros.filter(user_id=pk)
    expers = Experience.objects.all()
    experience_list = expers.filter(user_id=pk)
    edus = Education.objects.all()
    education_list = edus.filter(user_id=pk)
    resumes = Resume.objects.all()
    resume_list = resumes.filter(user_id=pk)

    return render(request, 'singlepage/index.html',{'user': user, 'intro_list':intro_list,'experience_list':experience_list,'education_list':education_list,'resume_list':resume_list})

def ChangePicture(request,pk):
    user = User.objects.get(id=pk)
    return render(request, 'singlepage/picture_popup.html')