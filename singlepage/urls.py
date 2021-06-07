from django.urls import path

from singlepage.views import PageDetail, snsCreate, ChangeProfile, ProfileUpdate, create_resume, \
    create_experience, create_edu, append, ProfileCreate, created_resume_db, check_Certificate, delete_resume, \
    created_career_db, delete_career, create_school_db, delete_edu, create_intro

app_name = 'singlepage'
urlpatterns = [
    path('<int:pk>/',PageDetail, name='page_detail'),
    path('<int:pk>/add_sns/',snsCreate.as_view(),name='addSNS'),
    path('<int:pk>/edit/',ChangeProfile, name='change_profile'),
    path('<int:pk>/resume_popup/',create_resume, name='addRESUME'),
    path('<int:pk>/experience_popup/',create_experience, name='addEXPER'),
    path('<int:pk>/edu_popup/',create_edu, name='addEDU'),
    path('<int:pk>/intro_popup/',create_intro, name='addIntro'),
    path('submit/',append,name='submit'),
    path('<int:pk>/profile_create/',ProfileCreate, name='profile'),
    path('created_resume_db/',created_resume_db, name='created_resume_db'),
    path('created_career_db/',created_career_db, name='created_career_db'),
    path('created_school_db/',create_school_db, name='created_school_db'),
    path('get_api/',check_Certificate,name='get_api'),
    path('<int:pk>/delete_resume/<int:resume_id>/',delete_resume,name='delete_resume'),
    path('<int:pk>/delete_career/<int:career_id>/',delete_career,name='delete_career'),
    path('<int:pk>/delete_edu/<int:edu_id>/',delete_edu,name='delete_edu'),
    # path('<int:pk>/edit/',ProfileUpdate.as_view(), name='updateprofile'),

]