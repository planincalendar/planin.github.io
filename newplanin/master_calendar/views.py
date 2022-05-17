
from django.forms import NullBooleanField
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse, HttpResponseRedirect
from master_calendar.models import *
from master_calendar.create_models import *
import json
from django.urls import reverse


# Create your views here.

def guest_calendar(request,pid):
    #프로젝트의 내용을 담고 있는 링크?
    project = Project.objects.get(pid=pid)
    context ={
        "pid":project.id,
        "name" : project.name, 
        "creator" : project.creator,
        "users" : project.users,
        "start_date" : project.start_date,
        "end_date" : project.end_date
    }
    if request.method == "GET" :
        return render(request,'master_calendar/guest_calendar.html',context)
   
    if request.method == "POST" :
        response_body = json.loads(request.body)
        slots = response_body.get("slots")

        for slot in slots: 
            name = slot.get("name") 
            start_timedate = slot.get("start_timedate")
            end_timedate = slot.get("end_timedate") 
            creator_id= slot.get("creator_id")
            create_slot(name,start_timedate,end_timedate,pid,creator_id)
        
        return JsonResponse({})
# def calendar(request):
#     if request.method == 'GET':
#         return render(request,'master_calendar/calendar.html')
#     elif request.method == 'POST':
#         return redirect("/create-project/")

# def load_slots(request,pid) :
#     # print(request.user)로도 됨?
#     response_body = json.loads(request.body)
#     owner_id = response_body.get("owner_id")
#     event_owner = Event.objects.filter(owner_id = owner_id)
#     event_list = list(event_owner.values('title','start_date','end_date','owner_id'))
#     return JsonResponse({
#         "events" : event_list
#     })


