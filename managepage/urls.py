from django.urls import path

from managepage.views import waitingList, certifications

app_name = 'managepage'
urlpatterns = [
    path('', certifications, name='waitig_list'),
]