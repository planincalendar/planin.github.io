
from django.forms import NullBooleanField
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse, HttpResponseRedirect
from master_calendar.models import *
from master_calendar.create_models import *
import json
from django.urls import reverse


# Create your views here.


def calendar(request):
    if request.method == 'GET':
        return render(request,'master_calendar/calendar.html')
    elif request.method == 'POST':
        return redirect("/create-project/")

def load_events(request) :
    # print(request.user)로도 됨?
    response_body = json.loads(request.body)
    owner_id = response_body.get("owner_id")
    event_owner = Event.objects.filter(owner_id = owner_id)
    event_list = list(event_owner.values('title','start_date','end_date','owner_id'))
    return JsonResponse({
        "events" : event_list
    })

def save_events(request):
    response_body = json.loads(request.body)
    events = response_body.get("events")

    for event in events: 
        title = event.get("title") 
        start_date = event.get("start")
        end_date = event.get("end") 
        owner_id = event.get("owner_id")
        
        create_event(title,start_date,end_date,owner_id)
    
    return JsonResponse({})

def create_project(request) :
    if request.method == 'GET' : 
        return render (request,'master_calendar/create-project.html' )
    if request.method == 'POST' :
        return HttpResponseRedirect(reverse("home:home"))



def guest_calendar(request) :
    return render (request, 'master_calendar/guest-calendar.html')
