from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import smtplib
import os
from os import environ
# Create your views here.
def index(request):
  return render(request, 'index.html')

def contact(request):
    
      
  if request.method== 'POST':
        email = request.POST['email']
        username = request.POST['username']
        msg = request.POST['message']
        
        #Email_Password = os.environ.get('Email_Password')

        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("thealphadebuggers@gmail.com", "olxewnhbbvmyzywd")
        SUBJECT = "Thank you!"
        TEXT = f"Hi {username}! Thank you for checking out my website!"
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        s.sendmail("thealphadebuggers@gmail.com", f"{email}", message)

        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("thealphadebuggers@gmail.com", "olxewnhbbvmyzywd")
        SUBJECT = "Contact"
        TEXT = f"Using the email address {email}, here is a message from {username}: {msg}"
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        s.sendmail("thealphadebuggers@gmail.com", "thealphadebuggers@gmail.com", message)

        s.quit()
        

      
        #return redirect('/')
        return redirect('https://rohaanjohn.glitch.me')
  else:
         return render(request, 'contact.html')
         return redirect('contact')
