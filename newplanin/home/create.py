

from master_calendar.models import Project, UserTrackInfo, User
from django.shortcuts import get_object_or_404
import string
import random

def create_new_project(name, creator_id, start_date, end_date) :
    new_project = Project()
    new_project.name = name # 프로젝트 제목 생성
    new_project.pid = generate_pass_key()
    new_project.creator = get_object_or_404(User,id = creator_id)
    new_project.start_date = start_date
    new_project.end_date = end_date
    new_project.save()
    return new_project

def add_users_to_project (shared_user_id,project_id) : 
    target_project = get_object_or_404(Project,id=project_id)
    target_project.users.add(get_object_or_404(UserTrackInfo,id=shared_user_id))
    target_project.save()

def track_user_info(name,email) :
    target_user = UserTrackInfo()
    target_user.name = name
    target_user.email = email
    target_user.pass_key = generate_pass_key()
    target_user.save()
    return target_user

def generate_pass_key():
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(characters)
    new_pass_key = []
    for i in range(6) : 
	    new_pass_key.append(random.choice(characters))
    random.shuffle(new_pass_key)
    return ''.join(new_pass_key)