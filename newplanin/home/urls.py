from django.urls import path 
from . import views


app_name = "home"

urlpatterns = [
    path('', views.load_project_lists, name = "home"),
    path('create-project/', views.create_project, name="create"),
    path('edit-project/<str:pid>/',views.edit_project, name="edit"),
    path('delete-project/<str:pid>/',views.delete_project, name="delete")
    # path('invite/<int:pid>/<str:user_email>',views.invite_users, name="invite_users")
]