from django.urls import path
from . import views

app_name = 'captioner'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_image, name='upload'),
    path('download/', views.download_captions, name='download'),
]