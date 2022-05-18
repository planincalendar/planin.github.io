from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from home.create import *
from django.urls import reverse
from master_calendar.models import *
from home.email import sendEmailToUser


# Create your views here.
def load_project_lists(request) :
    if request.user.is_authenticated:
        if request.method == 'GET' :
            user = User.objects.get(id=request.user.id)
            user_projects = Project.objects.filter(creator=user)
            context = {
                "user_projects" : user_projects
            }
            return render(request, 'home/home.html',context)
        if request.method == 'POST' :
            return HttpResponseRedirect(reverse("home:create"))
    else :
        return HttpResponseRedirect(reverse("login:login"))

def create_project(request) :
    if request.method == 'GET' : 
        return render (request,'home/create-project.html' )
    
    if request.method == 'POST' :
        name = request.POST["project-name"]
        creator_id = request.user.id
        start_date = request.POST["project-start-date"]
        end_date = request.POST["project-end-date"]
        new_project = create_new_project(name, creator_id, start_date, end_date)
       
        shared_users_name_email_str= str(request.POST.get("project-shared-user-name-email",False))
        shared_users = parseSharedUserStr(shared_users_name_email_str)
        print(shared_users)

        for shared_user in shared_users :
            name = shared_user.get("name")
            email = shared_user.get("email")
            shared_user_info = track_user_info(name,email)
            add_users_to_project(shared_user_info.id,new_project.id)
            pass_key = shared_user_info.pass_key
            pid = new_project.pid
            sendEmailToUser(pass_key,pid)

        return HttpResponseRedirect(reverse("home:home"))

def parseSharedUserStr(shared_users_name_email_str) :
    users_name_email = shared_users_name_email_str.splitlines()
    shared_user_info = []
    for a_user_name_email in users_name_email:
        if a_user_name_email is None:
            continue
        name_email = a_user_name_email.split("/")
        # name_email ['이진현','rig8696@naver.com']
        dictkey= ["name","email"] 
        user_info = dict(zip(dictkey, name_email)) 
        shared_user_info.append(user_info)
    return shared_user_info

def edit_project(request,pid) :
    a_project = Project.objects.get(pid=pid)
    shared_users = a_project.users.all()
    context = {
        "name" : a_project.name,
        "end_date" : a_project.end_date,
        "start_date" : a_project.start_date,
        "pid" : pid,
        "shared_users" : shared_users
    }
    if request.method == 'GET' :
        return render(request,'home/edit-project.html',context)

    if request.method == 'POST' :
        a_project.name = request.POST["project-name"]
        a_project.end_date = request.POST["project-end-date"]
        a_project.start_date = request.POST["project-start-date"]
        a_project.save()

        shared_users_name_email_str= str(request.POST.get("project-shared-user-name-email",False))
        shared_users = parseSharedUserStr(shared_users_name_email_str)

        for shared_user in shared_users :
            name = shared_user.get("name")
            email = shared_user.get("email")
            pass_key = shared_user.get("pass_key")
            pid = a_project.pid
            new_shared_user = track_user_info(name,email)
            print(new_shared_user)
            pass_key = new_shared_user.pass_key
            pid = a_project.pid
            print(pass_key)
            print(pid)
            sendEmailToUser(pass_key,pid)
            
        return HttpResponseRedirect(reverse("home:home"))


def delete_project(request,pid) :
     if request.method == "POST" :
        a_project = Project.objects.get(pid = pid)
        a_project.delete()
        return HttpResponseRedirect(reverse("home:home"))

# def invite_users(request,pid,user_email) :
#     request.method == 'POST' 

