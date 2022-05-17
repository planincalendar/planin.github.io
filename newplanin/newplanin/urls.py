
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',include('login.urls')),
    path('accounts/',include('allauth.urls')),
    path('home/', include('home.urls')),
    path('calendar/',include('master_calendar.urls')),
    

]
