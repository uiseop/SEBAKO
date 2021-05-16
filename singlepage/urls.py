from django.urls import path

from singlepage.views import PageDetail, ChangePicture, snsCreate, ChangeProfile, ProfileUpdate

app_name = 'singlepage'
urlpatterns = [
    path('<int:pk>/',PageDetail, name='page_detail'),
    path('<int:pk>/picture_popup/',ChangePicture, name='picture'),
    path('<int:pk>/add_sns/',snsCreate.as_view(),name='addSNS'),
    path('<int:pk>/edit/',ProfileUpdate.as_view(), name='updateprofile'),

]