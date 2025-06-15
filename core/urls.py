from django.urls import path
from . import views

urlpatterns = [
    path('projects/create/', views.create_project, name='create_project'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
]