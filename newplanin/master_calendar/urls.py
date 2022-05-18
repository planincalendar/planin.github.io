from django.urls import path
from . import views 

app_name = "master_calendar"

urlpatterns = [
    path('<str:pid>/<str:pass_key>/',views.guest_calendar, name ="calendar"),
    path('<str:pid>/<str:pass_key>/save-events/', views.save_events, name="save"),
    path('thankyou/', views.thank_you, name="thankyou"),
]
