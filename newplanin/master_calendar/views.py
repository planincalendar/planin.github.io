from django.forms import NullBooleanField
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from master_calendar.models import *
from master_calendar.create_models import *
import json

# Create your views here.

def calendar(request):
    return render(request,'master_calendar/calendar.html')


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


def load_events(request) :
    # user_id ? 
    event_owner = Event.objects.filter(owner_id = 16)
    event_list = list(event_owner.values('title','start_date','end_date'))
    return JsonResponse({
        "events" : event_list
    })

# def load_events_of_hannah(request) :
#     hannah_events = Event.objects.filter(owner_id = 17)
#     event_list = list(hannah_events.values('title','start_date','end_date'))
#     return JsonResponse({
#         "events" : event_list
#     })