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
from singlepage.forms import snsForm, ProfileForm


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


def ChangeProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            # profile.korName = profile_form.cleaned_data['korName']
            # profile.engName = profile_form.cleaned_data['engName']
            # profile.address = profile_form.cleaned_data['address']
            # profile.email = profile_form.cleaned_data['email']
            # profile.phone = profile_form.cleaned_data['phone']
            # profile.image = profile_form.cleaned_data['image']


            # prof.user_id = request.user.id
            # profile_form.save()
            prof = profile_form.save(commit=False)
            print(profile_form.cleaned_data['image'])
            print(profile_form.cleaned_data['image'])
            print(profile_form.cleaned_data['image'])
            prof.image = profile_form.cleaned_data['image']
            prof.save()
            return redirect('singlepage:page_detail', pk)
        return redirect('singlepage:page_detail', pk)
    else:
        profile_form = ProfileForm(instance=profile)
        # print(profile)
        return render(request, 'singlepage/edit_page.html',{'profile_form':profile_form})

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['korName','engName','address','email','phone','image',]
    template_name = 'singlepage/edit_page.html'

    def get_absolute_url(self):
        return reverse('singlepage:page_detail',args=[self.id])
