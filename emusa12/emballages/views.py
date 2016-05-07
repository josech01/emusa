#!/usr/bin/python
# -*- coding: utf-8 -*- 

from django.shortcuts import render , redirect, render_to_response
import json

from django.http import HttpResponseServerError, HttpResponse,  HttpResponseBadRequest,  HttpResponseNotAllowed
from django.db.models import Model

# from models import *
# from .models import data_info, index, emballage, tecnology, client, contact, footer
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import add_form1, add_form2, add_form3, add_form4, add_form5, add_form6, UserRegisterForm, LoginForm
from .functions import LogIn
from emballages import models
from django.core.mail import EmailMessage
# Create your views here.
def clientes (request):
	if request.method == 'GET':
		index = models.index.objects.last()
		clients = models.client.objects.last()
		footer = models.footer.objects.last()
		context_data = {'index': index, 'clients': clients,'footer': footer}
		return render(request, 'clientes.html', context_data)

def contactanos (request):
	if request.method == 'POST':
		formulario = add_form5(request.POST)
		if formulario.is_valid():
			asunto = 'Mensaje de página Web Emusa'
			nombre = request.POST['name']
			# nombre = formulario.cleaned_data['pregunta51']
			email = request.POST['email']
			numero = request.POST['number']
			mensaje = request.POST['textarea1']
			body = "Nombre:  %s \nNumero:  %s \nEmail:   %s \nMensaje: %s" %(nombre, numero, email, mensaje)
			mail = EmailMessage(asunto, body, to=['customerservice@emusa.com.pe'])
			mail.send()
		return redirect("/contactanos.html")
	else:
		index = models.index.objects.last()
		empacar = models.emballage.objects.last()
		contacts = models.contact.objects.last()
		footer = models.footer.objects.last()
		context_data = {'index': index,'empacar': empacar, 'contacts': contacts,'footer': footer}
		return render(request, 'contactanos.html', context_data)

def index (request):
	if request.method == 'GET':
		index = models.index.objects.last()
		footer = models.footer.objects.last()
		context_data = {'index': index, 'footer': footer}
		return render(request, 'index.html',context_data)


def empacate (request):
	if request.method == 'POST':
		formulario = add_form5(request.POST)
		if formulario.is_valid():
			asunto = 'Este es un mensaje de un usuario en emusa.com.pe'
			nombre = request.POST['name']
			# nombre = formulario.cleaned_data['pregunta51']
			email = request.POST['email']
			numero = request.POST['number']
			mensaje = request.POST['textarea1']
			body = "Nombre:  %s \nNumero:  %s \nEmail:   %s \nMensaje: %s" %(nombre, numero, email, mensaje)
			mail = EmailMessage(asunto, body, to=['customerservice@emusa.com.pe'])
			mail.send()
		return redirect("/empacate.html")
	else:
		index = models.index.objects.last()
		empacar = models.emballage.objects.last()
		footer = models.footer.objects.last()
		context_data = {'index': index, 'empacar': empacar,'footer': footer}
		return render(request, 'empacate.html',context_data)


def tecnologia (request):
	if request.method == 'GET':
		index = models.index.objects.last()
		tecnologys = models.tecnology.objects.last()
		footer = models.footer.objects.last()
		context_data = {'index': index, 'tecnologys': tecnologys,'footer': footer}
		return render(request, 'tecnologia.html', context_data)

def galeria (request):
	if request.method == 'GET':
		index = models.index.objects.last()
		context_data = {'index': index}
		return render(request, 'galeria.html', context_data)

@login_required
def add_new_form (request):
	if request.method == "POST":
		instance1 = models.index.objects.last()
		instance2 = models.emballage.objects.last()
		instance3 = models.tecnology.objects.last()
		instance4 = models.client.objects.last()
		instance5 = models.contact.objects.last()
		instance6 = models.footer.objects.last()
		modelform1 = add_form1(request.POST, request.FILES, instance= instance1)
		modelform2 = add_form2(request.POST, request.FILES, instance= instance2)
		modelform3 = add_form3(request.POST, request.FILES, instance= instance3)
		modelform4 = add_form4(request.POST, request.FILES, instance= instance4)
		modelform5 = add_form5(request.POST, request.FILES, instance= instance5)
		modelform6 = add_form6(request.POST, request.FILES, instance= instance6)
		if modelform1.is_valid() and modelform2.is_valid() and modelform3.is_valid() and modelform4.is_valid() and modelform5.is_valid() and modelform6.is_valid():	
			modelform1.save()
			modelform2.save()
			modelform3.save()
			modelform4.save()
			modelform5.save()
			modelform6.save()
			return redirect("/form.html")
	else:
		modelform1 = add_form1()
		modelform2 = add_form2()
		modelform3 = add_form3()
		modelform4 = add_form4()
		modelform5 = add_form5()
		modelform6 = add_form6()
		
	# print models.data_info.objects.last()
	return render(request, "form.html", {"form1": modelform1,"form2": modelform2,"form3": modelform3,"form4": modelform4,"form5": modelform5,"form6": modelform6})

# from emballages import models
# models.index.objects.last()


# def userlogin(request):
# 	if request.method == "POST":
# 		if 'register_form' in request.POST:
# 			user_register = UserRegisterForm(request.POST)
# 			if user_register.is_valid():
# 				User.objects.create_user(username = user_register.cleaned_data['username'],
# 				 email = user_register.cleaned_data['email'], 
# 				 password = user_register.cleaned_data['password'])
# 				LogIn(request, user_register.cleaned_data['username'],
# 						user_register.cleaned_data['password'])
# 				# return redirect('/form/')
# 		if 'login_form' in request.POST:
# 			login_form = LoginForm(request.POST)
# 			if login_form.is_valid():
# 				LogIn(request, login_form.cleaned_data['username'],	login_form.cleaned_data['password'])
# 				return redirect('/form/')
# 		else:
# 			print "incorrecto usuario"
# 			user_register = UserRegisterForm()
# 			login_form = LoginForm()
# 			# return redirect('/login/')
# 	return render(request, 'login.html', 
# 				{'user_register' : user_register, 'login_form' : login_form})


# def LogOut(request):
# 	logout(request)
# 	return redirect('/')


def userlogin(request):
	if request.method == "POST":
		if 'register_form' in request.POST:
			user_register = UserRegisterForm(request.POST)
			if user_register.is_valid():
				User.objects.create_user(username = user_register.cleaned_data['username'],
				 email = user_register.cleaned_data['email'], 
				 password = user_register.cleaned_data['password'])
				LogIn(request, user_register.cleaned_data['username'],
						user_register.cleaned_data['password'])
				return redirect('/')
		if 'login_form' in request.POST:
			login_form = LoginForm(request.POST)
			if login_form.is_valid():
				LogIn(request, login_form.cleaned_data['username'],
						login_form.cleaned_data['password'])
				return redirect('/form.html')
	else:
		user_register = UserRegisterForm()
		login_form = LoginForm()
	return render(request, 'login.html', 
				{'user_register' : user_register, 'login_form' : login_form})


def LogOut(request):
	logout(request)
	return redirect('/login')