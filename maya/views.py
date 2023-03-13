from django.shortcuts import render
from django.contrib.auth.models import User,auth
from datetime import datetime
from .models import Joinus
from django.core.mail import send_mail
# Create your views here.


def index(request):
     if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        id_num = request.POST.get('id')
        message = request.POST.get('message')
        joinus = Joinus(name=name, id_num=id_num, email=email, message=message, date=datetime.today())
        joinus.save()
        
        subject = 'Congratulations on Joining the Mayavi Club!'
        message = f"Dear {id_num},\n\nWe are excited to welcome you to the Mayavi Club!\n\nAs a member of the club, you'll have the opportunity to learn about Virtual Reality, Augmented Reality, and Game Development. We can't wait to see what you'll create!\n\nBest regards,\nTeam Mayavi Club"
        send_mail(subject, message, 'mayaviclubklu@gmail.com', [email], fail_silently=False)
        return render(request, "index.html")
     else:
          return render(request, 'index.html')
