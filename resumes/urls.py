from django.urls import path

from resumes.views import ResumeCreate, ResumeDelete, ResumeUpdate, ResumeDetail, ResumeList

urlpatterns = [
    path('create/', ResumeCreate.as_view(), name='create'),
    path('delete/<int:pk>/', ResumeDelete.as_view(), name='delete'),
    path('update/<int:pk>/',ResumeUpdate.as_view(), name='update'),
    path('detail/<int:pk>',ResumeDetail.as_view(), name='detail'),
    path('', ResumeList.as_view(), name='index'),
]