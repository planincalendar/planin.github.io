from django.urls import path
from . import views 

app_name = "master_calendar"

urlpatterns = [
    path('',views.calendar),
    path("save-events/", views.save_events),
    path('load-events/', views.load_events),
    #path("test/<int:user_id>", views.test_show_user_name,name = "test_page"),
]
