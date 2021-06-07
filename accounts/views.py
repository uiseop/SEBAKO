from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from accounts.forms import personForm
from accounts.models import Profile, Person, SNS, Company


def home(request):
    return render(request, 'accounts/home2.html')
    # return render(request, 'zzsignup.html')


def detail(request, pk):
    # blog_detail = get_object_or_404(Blog, pk=pk)
    return render(request, 'accounts/detail.html')


def index(request):
    return render(request, 'accounts/index.html')


def signup(request):
    return render(request, 'accounts/signup.html')


def signup_company(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists():
            messages.info(request, '이미 가입한 아이디입니다')
            return redirect('accounts:signup_personal')
        # redirect는 함수 명 적어.

        if request.POST['password1'] == request.POST['password2']:
            if len(request.POST['password1']) < 8:
                messages.info(request, '비밀 짧아')
                return redirect('accounts:signup_personal')

            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
            )
            # korName = '한국'
            # engName = 'Engl'
            # address = 'bababobo'
            # email = 'babo@babo.com'
            # phone = '010-5123-4567'
            korName = request.POST['korName']
            engName = request.POST['engName']
            address = request.POST['Address']
            email = request.POST['EmailId'] + '@' + request.POST['EmailDomain']
            phone = request.POST['Phone1'] + '-' + request.POST['Phone2'] + '-' + request.POST['Phone3']
            # sns = request.POST['GitSns']

            profile = Profile(user=user, korName=korName, engName=engName, address=address, email=email, phone=phone)
            profile.save()
            auth.login(request, user)
            return redirect('home')

        return render(request, 'accounts/signup_personal.html')
    return render(request, 'accounts/signup_company.html')


def signup_personal(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists():
            messages.info(request, '이미 가입한 아이디입니다')
            return redirect('accounts:signup_personal')
        # redirect는 함수 명 적어.

        if request.POST['password1'] == request.POST['password2']:
            if len(request.POST['password1']) < 8:
                messages.info(request, '비밀 짧아')
                return redirect('accounts:signup_personal')

            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
            )
            # korName = '한국'
            # engName = 'Engl'
            # address = 'bababobo'
            # email = 'babo@babo.com'
            # phone = '010-5123-4567'
            korName = request.POST['korName']
            engName = request.POST['engName']
            address = request.POST['Address']
            email = request.POST['EmailId'] + '@' + request.POST['EmailDomain']
            phone = request.POST['Phone1'] + '-' + request.POST['Phone2'] + '-' + request.POST['Phone3']
            # sns = request.POST['GitSns']

            profile = Profile(user=user, korName=korName, engName=engName, address=address, email=email, phone=phone)
            profile.save()
            auth.login(request, user)
            return redirect('home')

        return render(request, 'accounts/signup_personal.html')
    return render(request, 'accounts/signup_personal.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('singlepage:page_detail', user.person.pk)
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect'})

    else:
        return render(request, 'accounts/login.html')


def login_personal(request):
    return render(request, 'accounts/login_personal.html')


def login_company(request):
    return render(request, 'accounts/login_company.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def personal_signUp(request):
    if request.method == 'POST':
        print(request.POST['walletAddress'])
        print(request.POST['walletAddress'])
        user = User.objects.create_user(
            username=request.POST['walletAddress']
        )
        person = Person(user=user)
        person.save()

        profile = Profile(user_id=person)
        sns = SNS(user_id=person)
        sns.save()
        profile.save()
        auth.login(request, user)
        return redirect('home')
    else:
        print('why no')
        print('why no')
        print('why no')
        render(request, 'accounts/signup.html')

def company_signUp(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['walletAddress']
        )
        company = Company(user=user)
        company.save()
        return redirect('home')
    else:
        render(request, 'accounts/signup_company.html')

def login_wallet(request):
    if request.method == 'POST':
        username = request.POST['walletAddress']
        print(username)
        print(username)
        print(username)
        try:
            if User.objects.get(username=username):
                user = User.objects.get(username=username)
                if Person.objects.get(user=user):
                    auth.login(request,user)
                    # 유저모델과 1:1 연결한 PERSON모델의 pk로 연결함으로써 오류를 방지함
                    return redirect('singlepage:page_detail', user.person.pk)
                else:
                    auth.login(request,user)
                    return redirect('home')

        except:
            messages.info(request,'회원가입을 먼저 진행해주세요')
            return render(request,'accounts/login.html',{'error': 'WalletAccount is incorrect'})

    else:
        return render(request, 'accounts/login.html')
