
import re
from django.contrib import admin
from django.urls import path , include
from django.shortcuts import redirect
from django.urls import reverse
from datetime import datetime
from django.http import JsonResponse
from login import views
# def google_login(request) :
#     return redirect(reverse(login:))
def social_login_cancel(request) :
    return redirect(reverse("boot:login") + "?error=cancelled")

def social_login_error(request) :
    return redirect(reverse("boot:login") + "?error=error")

# def google_login(reqeust) :
#     return redirect(reverse('https://accounts.google.com/o/oauth2/auth/oauthchooseaccount')+"?client_id=")


def test_timezone(request):
    print(request.GET.get("time"))
    print(datetime.now())
    return JsonResponse({
        "now": str(datetime.now())
    })


urlpatterns = [
    path("test-time/", test_timezone),
    # path("accounts/google/login/",google_login),
    path("accounts/social/login/cancelled",social_login_cancel),
    path("accounts/social/login/error", social_login_error),
    path('accounts/',include('allauth.urls')),

    path('admin/', admin.site.urls),
    path('login/',include('login.urls')),
    path('',views.login),
    path('home/', include('home.urls')),
    path('calendar/',include('master_calendar.urls')),
    

]
