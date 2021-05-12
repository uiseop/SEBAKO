from django.urls import path

from singlepage.views import PageDetail

app_name = 'singlepage'
urlpatterns = [
    path('<int:pk>/',PageDetail, name='page_detail')
]