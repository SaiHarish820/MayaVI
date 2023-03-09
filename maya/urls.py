from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
     path("", views.index, name='home'),
     path("base.html", views.base),
     path("gallery.html", views.gallery),
     path("joinus.html",views.joinus),
    path("projects.html",views.projects),
    path("success.html",views.success),
    path("events.html",views.events),
    path("aboutus.html",views.aboutus),
    path("team.html",views.team),
    path("landingpage.html",views.landingpage),

]