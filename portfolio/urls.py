from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('journey/', views.journey, name='journey'),
    path('toolbox/', views.toolbox, name='toolbox'),
    path('projects/', views.projects, name='projects'),
    path('experience/', views.experience, name='experience'),
]