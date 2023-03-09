from django.shortcuts import render
from django.contrib.auth.models import User,auth
# Create your views here.


def index(request):
     return render(request, 'index.html')

def base(request):
     return render(request, "base.html")

def gallery(request):
     return render(request, "gallery.html")

def joinus(request):
     return render(request,"joinus.html")

def projects(request):
     return render(request,"projects.html")

def team(request):
     return render(request,"team.html")

def success(request):
     return render(request,"success.html")

def landingpage(request):
     return render(request,"landingpage.html")

def events(request):
     return render(request,"events.html")

def aboutus(request):
     return render(request,"aboutus.html")
