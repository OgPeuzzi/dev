from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from AidAuto.forms import ContactForm, DemandeForm, RegistrationForm, loginForm, bookingForm
from .models import *
from django.core.mail import send_mail
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
import bcrypt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.

def demandeForm(request):
    if request.method == "POST":
        demande = DemandeForm(request.POST)
        if demande.is_valid():
            demande.save()
            try:
                return redirect('accueil')
            except:
                pass
    else:
        demande = DemandeForm()
    return render(request, "demande.html"
                  ,{'form': demande})


def accueil(request):
    Mecanicien_list = Utilisateur.objects.all()
    context = {'mecanicien_list': Mecanicien_list}
    return render(request, 'accueil.html', context)

def mecanicien(request):
    Mecanicien_list = Utilisateur.objects.all()
    context = {'mecanicien_list': Mecanicien_list}
    return render(request, 'mecanicien.html', context)

def about(request):
    Mecanicien_list = Utilisateur.objects.all()
    context = {'mecanicien_list': Mecanicien_list}
    return render(request, 'about.html', context)

def service(request):
    loader
    template = loader.get_template('service.html')

    return HttpResponse(template.render())

def booking(request):
    if request.method == 'POST':
        form = bookingForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                return redirect('accueil')
            except:
                pass
    else:
        form = bookingForm()
    return render(request, 'booking.html'
                  ,{'form': form})

def inscription(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                return redirect('accueil')
            except:
                pass
    else:
        form = RegistrationForm()
    return render(request, 'page-register.html'
                  ,{'form': form})

def connexion(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                return redirect('accueil')
            except:
                pass
    else:
        form = loginForm()
    return render(request, 'page-login.html'
                  ,{'form': form})

def forgot(request):
   loader
   template = loader.get_template('page-forgot-password.html')  

   return HttpResponse(template.render())

def found(request):
   loader
   template = loader.get_template('404.html')  

   return HttpResponse(template.render())

def contact(request):
    if request.method == "POST":
        contact = ContactForm(request.POST)
        if contact.is_valid():
            name = contact.cleaned_data['First_name']
            surname = contact.cleaned_data['Last_name']
            Subject = contact.cleaned_data['Subject']
            object = Subject
            msg = contact.cleaned_data['Message']
            Envoyé_à = contact.cleaned_data['Email']
            res = send_mail(object,msg,settings.EMAIL_HOST_USER,[Envoyé_à])
            if (res == 1):
                contact.save()
                try:
                    msg = "Mail sent successfuly"
                    return redirect('/accueil')
                except:
                    pass
            else:
                msg = "Mail could not sent"
            return redirect('/found')

    else:
        contact = ContactForm()
    return render(request, "contact.html"
                ,{'form': contact})