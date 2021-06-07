from django.urls import path

from managepage.views import waitingList

app_name = 'managepage'
urlpatterns = [
    path('', waitingList, name='waitig_list'),
]