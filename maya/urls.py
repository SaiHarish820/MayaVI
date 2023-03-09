from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
     path("", views.landingpage, name='home'),
     path("base", views.base),
     path("gallery", views.gallery),
     path("joinus",views.joinus),
    path("projects",views.projects),
    path("success",views.success),
    path("index",views.index),
    path("events",views.events),
    path("aboutus",views.aboutus),

]