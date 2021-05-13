from django.contrib import messages
from django.shortcuts import redirect


# 로그인 확인
def login_message_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, "로그인한 사용자만 이용할 수  있습니다")
            return redirect("accounts:login")
        return function(request, *args, **kwargs)
    return wrap

# 관리자 권한 확인
def company_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.company.is_company:
            return function(request, *args, **kwargs)
        messages.info(request, "접근 권한이 없습니다")
        return redirect("home")
    return wrap

# 비로그인 확인
def logout_message_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "접속중인 사용자입니다.")
            return redirect('home')
        return function(request, *args, **kwargs)

    return wrap