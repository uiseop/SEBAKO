from django.urls import path

from managepage.views import  certifications, certificationDatabase

app_name = 'managepage'
urlpatterns = [
    path('<int:pk>/', certificationDatabase, name='waitig_list'),
]