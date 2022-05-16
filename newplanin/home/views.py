from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect

from django.urls import reverse



# Create your views here.
def load_project_lists(request) :

    if request.method == 'GET' :
        return render(request, 'home/home.html')
    elif request.method == 'POST' :
        return HttpResponseRedirect(reverse("master_calendar:calendar"))
