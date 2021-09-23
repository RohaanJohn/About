from django.urls import path
from . import views

urlpatterns = [path("", views.index, name="index"),
               path("aboutrohaan/contact", views.contact, name="contact")]    
