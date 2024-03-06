from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def login(request):
    return HttpResponse('<h1>страница авторизации</h1>')

def reg(request):
    return HttpResponse('<h1>страница регистрации</h1>')

def logout_user(request):
    return HttpResponse('<h1>страница выхода</h1>')
    #logout(request)