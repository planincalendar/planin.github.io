from django.urls import path
from . import views 

app_name = "master_calendar"

urlpatterns = [
    path('<str:pid>/<str:pass_key>',views.guest_calendar, name ="calendar"),
    #path("save-events/<int:pid>", views.save_events),
    # path('load-events/<int:pid>', views.load_events),

    #path("test/<int:user_id>", views.test_show_user_name,name = "test_page"),
]
