from django.urls import path
from . import views 

app_name = "master_calendar"

urlpatterns = [
    path('',views.calendar, name ="calendar"),
    path("save-events/", views.save_events),
    path('load-events/', views.load_events),
    path('create-project/', views.create_project, name = "create_project"),
    path('guest/',views.guest_calendar),
    #path("test/<int:user_id>", views.test_show_user_name,name = "test_page"),
]
