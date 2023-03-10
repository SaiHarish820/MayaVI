from django.shortcuts import render
from django.contrib.auth.models import User,auth
from datetime import datetime
from .models import Joinus
from django.core.mail import send_mail
# Create your views here.


def index(request):
     return render(request, 'index.html')

def base(request):
     return render(request, "base.html")

def gallery(request):
     return render(request, "gallery.html")

from django.core.mail import send_mail
from .models import Joinus
from datetime import datetime

def joinus(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        id_number = request.POST.get('id_number')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        joinus = Joinus(first_name=first_name, last_name=last_name, id_number=id_number, email=email, comment=comment, date=datetime.today())
        joinus.save()
        
        subject = 'Congratulations on Joining the Mayavi Club!'
        message = f"Dear {id_number},\n\nWe are excited to welcome you to the Mayavi Club!\n\nAs a member of the club, you'll have the opportunity to learn about Virtual Reality, Augmented Reality, and Game Development. We can't wait to see what you'll create!\n\nBest regards,\nTeam Mayavi Club"
        send_mail(subject, message, 'mayaviclubklu@gmail.com', [email], fail_silently=False)

        return render(request, "success.html")
    else:
        return render(request, "joinus.html")



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
