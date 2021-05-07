from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from accounts.models import Blog, Profile


def home(request):
    blogs = Blog.objects
    return render(request, 'home2.html', {'blogs': blogs})
    # return render(request, 'zzsignup.html')


def detail(request, pk):
    # blog_detail = get_object_or_404(Blog, pk=pk)
    blog_detail = Blog.objects.get(pk=pk)
    return render(request, 'detail.html', {'blog': blog_detail})


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists():
            messages.info(request,'이미 가입한 아이디입니다')
            return redirect('signup')
        # redirect는 함수 명 적어.

        if request.POST['password1'] == request.POST['password2']:
            if len(request.POST['password1']) < 8:
                messages.info(request,'비밀 짧아')
                return redirect('signup')

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

        return render(request, 'signup_personal.html')
    return render(request, 'signup_personal.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


