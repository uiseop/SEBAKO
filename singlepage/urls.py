from django.urls import path

from singlepage.views import PageDetail, ChangePicture

app_name = 'singlepage'
urlpatterns = [
    path('<int:pk>/',PageDetail, name='page_detail'),
    path('<int:pk>/picture_popup/',ChangePicture, name='picture'),

]