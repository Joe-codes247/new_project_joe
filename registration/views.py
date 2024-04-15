from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #for routing your templates
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

def addstudent(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        query = Student(email=email, password=password)
        query.save()




