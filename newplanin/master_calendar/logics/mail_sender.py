
from django.http import HttpResponse, HttpResponseBadRequest,HttpResponseRedirect
from unicodedata import name
from django.core.mail import send_mail,BadHeaderError
from master_calendar.models import *
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse
from master_calendar.models import *

def send(project, user, slots) :

    title = f'[플래닌] {user.name}님, {project.name}의 면접 가능한 일정을 전달드립니다.'

    content = ''
    i = 0

    for s in slots:
        i += 1
        content += f"{i}: {s.start_timedate} ~ {s.end_timedate}\n"

    message = render_to_string('master_calendar/email.html', {
        'user': user.name,
        'project_title' : project.name,
        'content' : content,
        
        # 'link' : 'http://127.0.0.1:8000/calendar/'+ project.pid +'/'+ user.pass_key
        })
    
    if title and message :
        try :
            to_email = user.email
            send_email = EmailMessage(title, message, to=[to_email])
            send_email.send()

        except BadHeaderError :
            return HttpResponse('오류발생 : Invalid header found.')
        return HttpResponseRedirect(reverse('home:home'))    
    else :
        return HttpResponse('Make sure all fields are entered and valid.')

def sendErrorEmail(project, user) :

    title = f'[플래닌] {user.name}님, {project.name}의 면접 가능한 일정이 없습니다.'

    message = render_to_string('master_calendar/email_slot_unavailable.html', {
        'user': user.name,
        'project_title' : project.name,
        # 'link' : 'http://127.0.0.1:8000/calendar/'+ project.pid +'/'+ user.pass_key
        })
    
    if title and message :
        try :
            to_email = user.email
            send_email = EmailMessage(title, message, to=[to_email])
            send_email.send()

        except BadHeaderError :
            return HttpResponse('오류발생 : Invalid header found.')
        return HttpResponseRedirect(reverse('home:home'))    
    else :
        return HttpResponse('Make sure all fields are entered and valid.')
