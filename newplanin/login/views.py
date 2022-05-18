from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import render, redirect

def login(request) :
    return render(request,'login/login.html') 

def logout(request) :
    #요청이 Post 인지 확인
    if request.method == "POST" :
        #로그아웃
        auth.logout(request)
    #리다이렉트 시켜주기 
    return redirect('login:login')

# Create your views here.
