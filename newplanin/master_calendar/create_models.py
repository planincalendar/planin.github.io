from django.shortcuts import get_object_or_404
from master_calendar.models import *
import json

def create_user(name, gmail) :
    new_user = User()
    new_user.name = name
    new_user.gmail = gmail
    new_user.save()
    #중복처리?
    return new_user 

#owner_id 잠깐 없엠

def create_event(title,start_date,end_date) :
    new_event = Event()
    new_event.title = title
    new_event.start_date = start_date
    new_event.end_date = end_date
    #new_event.owner = get_object_or_404(User, id= owner_id)
    new_event.save()
    # print(new_event.owner.id, new_event.owner.name)
    return new_event

 
def add_shared_user_to_event(event_id, user_id):
    print(event_id, user_id)
    target_event = get_object_or_404(Event, id=event_id)
    target_event.shared_users.add(get_object_or_404(User, id=user_id))
    target_event.save()
 


