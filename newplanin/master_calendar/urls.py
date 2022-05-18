from django.urls import path
from . import views 

app_name = "master_calendar"

urlpatterns = [
    path('<str:pid>/<str:pass_key>/',views.guest_calendar, name ="calendar"),
    path('<str:pid>/<str:pass_key>/save-events/', views.save_events, name="save"),
    # path('<str:pid>/<str:pass_key>/load-events/', views.load_events, name="load"),

    #path("test/<int:user_id>", views.test_show_user_name,name = "test_page"),
]
