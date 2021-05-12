from django.urls import path

from resumes.views import ResumeCreate, ResumeDelete, ResumeUpdate, ResumeDetail, ResumeList

app_name = 'resumes'
urlpatterns = [
    path('create/', ResumeCreate.as_view(), name='resume_create'),
    path('delete/<int:pk>/', ResumeDelete.as_view(), name='resume_delete'),
    path('update/<int:pk>/',ResumeUpdate.as_view(), name='resume_update'),
    path('detail/<int:pk>',ResumeDetail.as_view(), name='resume_detail'),
    path('', ResumeList, name='resume_list'),
]