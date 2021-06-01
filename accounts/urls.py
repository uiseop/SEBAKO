from django.urls import path

from accounts import views
from accounts.views import personal_signUp

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup_personal/', views.signup_personal, name='signup_personal'),
    path('signup_company/', views.signup_company, name='signup_company'),
    path('login/', views.login, name='login'),
    path('login_wallet/', views.login_wallet, name='login_wallet'),
    path('login_personal/', views.login_personal, name='login_personal'),
    path('login_company/', views.login_company, name='login_company'),
    path('print/',personal_signUp, name='printconsole'),
    
    path('logout/', views.logout, name='logout'),
]