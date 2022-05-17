from django.shortcuts import get_object_or_404
from master_calendar.logics.tools import *
from master_calendar.models import *

def on_save_events(events):
    
    user = get_object_or_404(User, id= events[0].get("owner_id"))

    return