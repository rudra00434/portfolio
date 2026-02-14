from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'polls/home.html')

def about(request):
    return render(request,'polls/about.html')

def contact(request):
    return render(request,'polls/contact.html')
def skills(request):
    return render(request,'polls/skills.html')
def projects(request):
    return render(request,'polls/projects.html')