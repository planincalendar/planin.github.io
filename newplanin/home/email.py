from unicodedata import name
from django.core.mail import send_mail
from master_calendar.models import *
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def sendEmailToUsers(shared_user_id,project_pk) :
    shared_user = UserTrackInfo.objects.get(id=shared_user_id)
    project = Project.objects.get(id=project_pk)
    creator = User.objects.get(id = project.creator_id)

    mail_subject = print('[플래닌]'+ creator.get(first_name)+'님 께서 초대한'+{}+'일정 조정 캘린더에 참여하세요')
    message = render_to_string('email.html', {
        'name': name

        })
    to_email = ''
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.send()


# 'planiwithu@gmail.com',
# ['rig8696@likelion.org'],