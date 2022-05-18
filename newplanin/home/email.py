
from django.http import HttpResponse, HttpResponseBadRequest,HttpResponseRedirect
from unicodedata import name
from django.core.mail import send_mail,BadHeaderError
from master_calendar.models import *
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse


def sendEmailToUser(pass_key,pid) :
    shared_user = UserTrackInfo.objects.get(pass_key=pass_key)
    print(shared_user.email)
    project = Project.objects.get(pid=pid)
    creator = User.objects.get(id = project.creator_id)

    mail_subject ='[플래닌] '+ creator.first_name+'님 께서 초대한 '+project.name+' 일정 조정 캘린더에 참여하세요'
    message = render_to_string('home/email.html', {
        'shared_user': shared_user.name,
        'project_title' : project.name,
        'project_start_date' : project.start_date,
        'project_end_date' : project.end_date,
        'link' : 'https://www.hiplanin.shop/calendar/'+project.pid+'/'+shared_user.pass_key+'/'
        })
    
    if mail_subject and message :
        try :
            to_email = shared_user.email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

        except BadHeaderError :
            return HttpResponse('오류발생 : Invalid header found.')
        return HttpResponseRedirect(reverse('home:home'))    
    else :
        return HttpResponse('Make sure all fields are entered and valid.')        


# 'planiwithu@gmail.com',
# ['rig8696@likelion.org'],