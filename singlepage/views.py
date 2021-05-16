from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from accounts.decorators import login_message_required
from accounts.models import SNS, Profile
from resumes.models import SelfIntro, Experience, Education, Resume
from singlepage.forms import snsForm, ProfileForm, ResumeForm, ExperienceForm, EduForm


def _page_id(request):
    single = request.session.session_key
    if not single:
        single = request.session.create()
    return single


# person은 작성자로 념겨줌.
# user은 현재 세션상 로그인한 사용자 정보임.

# @login_required
@login_message_required
def PageDetail(request, pk):
    # print(request.user) : seop 출럭
    # print(request.user.profile.korName)
    person = get_object_or_404(User, pk=pk)
    # user = User.objects.get(id=pk)
    # print(user) : seop 출력
    # print(request.user.id) : 1출력 (첫번째 회원가입한곳)
    intros = SelfIntro.objects.all()
    intro_list = intros.filter(user_id=pk)
    expers = Experience.objects.all()
    experience_list = expers.filter(user_id=pk)
    edus = Education.objects.all()
    education_list = edus.filter(user_id=pk)
    resumes = Resume.objects.all()
    resume_list = resumes.filter(user_id=pk)

    return render(request, 'singlepage/index.html',
                  {'person': person, 'intro_list': intro_list, 'experience_list': experience_list,
                   'education_list': education_list, 'resume_list': resume_list})


@login_message_required
def ChangePicture(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'singlepage/picture_popup.html')


@method_decorator(login_message_required, name='dispatch')
class snsCreate(CreateView):
    model = SNS
    fields = ['name', 'url']
    template_name = 'singlepage/sns_create.html'

    def form_valid(self, form):
        # print(self.request.user.id) : 1이 출력
        # print(self.request.user) : seop이 출력
        # # 작성자는 현재 로그인 한 사용자로 설정함
        form.instance.user_id = self.request.user

        if form.is_valid():
            form.instance.save()
        else:
            pass

        return redirect('singlepage:page_detail', self.request.user.id)


@login_message_required
def create_sns(request, pk):
    form = snsForm(request.POST)
    if form.is_valid():
        sns = form.save(commit=False)
        # commit=False일 경우 실제 DB에는 적용X
        # 아직 작성자 정보가 없으니


def create_resume(request, pk):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('singlepage:page_detail', request.user.id)
        return render(request, 'singlepage/resume_create.html', {'form': form})
    else:
        form = ResumeForm()
        return render(request, 'singlepage/resume_create.html', {'form': form})


def create_experience(request, pk):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()
            return redirect('singlepage:page_detail', request.user.id)
        return render(request, 'singlepage/experience_create.html', {'form': form})
    else:
        form = ExperienceForm()
        print('hahaha')
        return render(request, 'singlepage/experience_create.html', {'form': form})


def create_edu(request, pk):
    if request.method == 'POST':
        form = EduForm(request.POST)
        if form.is_valid():
            edu = form.save(commit=False)
            edu.user = request.user
            edu.save()
            return redirect('singlepage:page_detail', request.user.id)
        return render(request, 'singlepage/edu_create.html', {'form': form})
    else:
        form = EduForm()
        print('hahaha')
        return render(request, 'singlepage/edu_create.html', {'form': form})


@login_message_required
def ChangeProfile(request, pk, created=None):
    profile = Profile.objects.get(user_id=pk)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        try: # SNS의 정보를 가져오는것을 먼저 시도해봄
            s = SNS.objects.get(user_id=pk)
            sns_form = snsForm(request.POST, instance=s)

            # sns_form = snsForm(request.POST, instance=sns)
            if profile_form.is_valid() and sns_form.is_valid():
                sns = sns_form.save(commit=False)
                prof = profile_form.save(commit=False)
                sns.save()
                prof.save()
                return redirect('singlepage:page_detail', pk)
            return redirect('singlepage:page_detail', pk)
        except: # 정보가 없으면 새로 추가해주면 됨
            sns = snsForm(request.POST)
            # sns.user_id = pk
            addsns = sns.save(commit=False)
            addsns.user = request.user
            addsns.save()
            return redirect('singlepage:page_detail', request.user.id)

    else:
        # s_form = snsForm(instance=snses[0])
        # sns_form = snsForm(instance=snses[1])
        snses = SNS.objects.all()
        snses = snses.filter(user_id=pk)

        profile_form = ProfileForm(instance=profile)

        if not snses:
            sns1 = snsForm()

            return render(request, 'singlepage/edit_page.html', {'profile_form': profile_form,
                                                                 'sns1_form': sns1,
                                                                 })
        else:
            s = SNS.objects.get(user_id=pk)
            sns_form = snsForm(instance=s)
            # for i in range(len(snses)):
            #     sns[i] = snsForm(instance=snses[i])
            # sns = snsForm(instance=snses)

            # print(profile)
            return render(request, 'singlepage/edit_page.html', {'profile_form': profile_form,
                                                                 'sns1_form': sns_form,
                                                                 })


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['korName', 'engName', 'address', 'email', 'phone', 'image', ]
    template_name = 'singlepage/edit_page.html'

    # def get_absolute_url(self):
    #     return reverse('singlepage:page_detail',args=[self.id])
