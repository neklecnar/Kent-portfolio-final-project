from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
     path("", views.base, name = "base"),
     path("portfolio/", views.portfolio, name = "portfolio"),
     path("about/", views.about, name = "about"),
     path("contact/", views.contact, name = "contact"),

]