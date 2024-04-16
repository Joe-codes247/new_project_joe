from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader #for routing your templates
from django.views.decorators.csrf import csrf_exempt
from .models import student
def registration(request):
    return HttpResponse("Welcome to registration!")

def mypage(request):
    template = loader.get_template("register.html")
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template("About us.html")
    return HttpResponse(template.render())

def contacts(request):
    template = loader.get_template("contacts.html")
    return HttpResponse(template.render())

@csrf_exempt
def addstudent(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        mydata = {'email': email, 'password': password}
        print(mydata)

        query = student(email=email, password=password)
        query.save()
#fetch the student data to be displayed





