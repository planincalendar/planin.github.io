from django.urls import path 
from . import views


app_name = "home"

urlpatterns = [
    path('', views.load_project_lists, name = "home"),
]