from django.shortcuts import get_object_or_404
from master_calendar.models import *
import json

# def create_user(name, gmail) :
#     new_user = User()
#     new_user.name = name
#     new_user.gmail = gmail
#     new_user.save()
#     #중복처리?
#     return new_user 

#owner_id 잠깐 없엠

def create_slot(name,start_timedate,end_timedate,project_id,slot_creator_id) :
    new_slot = Slot()
    new_slot.name = name
    new_slot.start_timedate = start_timedate
    new_slot.end_timedate = end_timedate
    new_slot.project = get_object_or_404(Project, id=project_id)
    new_slot.creator = get_object_or_404(UserTrackInfo, id=slot_creator_id )
    new_slot.save()
    # print(new_event.owner.id, new_event.owner.name)
    return new_slot

# def create_user(name,email) :
#     new_user = User()
#     new_user.password = "password12345"
#     new_user.is_superuser = False
#     new_user.username = name
#     new_user.email = email
#     new_user.save()
#     return new_user


# def add_shared_user_to_event(event_id, user_id):
#     print(event_id, user_id)
#     target_event = get_object_or_404(Event, id=event_id)
#     target_event.shared_users.add(get_object_or_404(User, id=user_id))
#     target_event.save()
 


