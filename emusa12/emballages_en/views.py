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
from .forms import enadd_form1, enadd_form2, enadd_form3, enadd_form4, enadd_form5, enadd_form6
from emballages_en import models
# Create your views here.
def enclientes (request):
	if request.method == 'GET':
		index = models.enindex.objects.last()
		clients = models.enclient.objects.last()
		footer = models.enfooter.objects.last()
		context_data = {'index': index, 'clients': clients,'footer': footer}
		return render(request, 'clientes_en.html', context_data)

def encontactanos (request):
	if request.method == 'GET':
		index = models.enindex.objects.last()
		contacts = models.encontact.objects.last()
		footer = models.enfooter.objects.last()
		context_data = {'index': index, 'contacts': contacts,'footer': footer}
		return render(request, 'contactanos_en.html', context_data)

def enindex (request):
	if request.method == 'GET':
		index = models.enindex.objects.last()
		footer = models.enfooter.objects.last()
		context_data = {'index': index, 'footer': footer}
		return render(request, 'index_en.html',context_data)


def enempacate (request):
	if request.method == 'GET':
		index = models.enindex.objects.last()
		empacar = models.enemballage.objects.last()
		footer = models.enfooter.objects.last()
		context_data = {'index': index, 'empacar': empacar,'footer': footer}
		return render(request, 'empacate_en.html',context_data)


def entecnologia (request):
	if request.method == 'GET':
		index = models.enindex.objects.last()
		tecnologys = models.entecnology.objects.last()
		footer = models.enfooter.objects.last()
		context_data = {'index': index, 'tecnologys': tecnologys,'footer': footer}
		return render(request, 'tecnologia_en.html', context_data)

def enadd_new_form (request):
	if request.method == "POST":
		instance1 = models.enindex.objects.last()
		instance2 = models.enemballage.objects.last()
		instance3 = models.entecnology.objects.last()
		instance4 = models.enclient.objects.last()
		instance5 = models.encontact.objects.last()
		instance6 = models.enfooter.objects.last()
		modelform1 = enadd_form1(request.POST, request.FILES, instance= instance1)
		modelform2 = enadd_form2(request.POST, request.FILES, instance= instance2)
		modelform3 = enadd_form3(request.POST, request.FILES, instance= instance3)
		modelform4 = enadd_form4(request.POST, request.FILES, instance= instance4)
		modelform5 = enadd_form5(request.POST, request.FILES, instance= instance5)
		modelform6 = enadd_form6(request.POST, request.FILES, instance= instance6)
		if modelform1.is_valid() and modelform2.is_valid() and modelform3.is_valid() and modelform4.is_valid() and modelform5.is_valid() and modelform6.is_valid():	
			modelform1.save()
			modelform2.save()
			modelform3.save()
			modelform4.save()
			modelform5.save()
			modelform6.save()
			return redirect("/form_en/")
	else:
		modelform1 = enadd_form1()
		modelform2 = enadd_form2()
		modelform3 = enadd_form3()
		modelform4 = enadd_form4()
		modelform5 = enadd_form5()
		modelform6 = enadd_form6()
		
	# print models.endata_info.objects.last()
	return render(request, "form_en.html", {"form1": modelform1,"form2": modelform2,"form3": modelform3,"form4": modelform4,"form5": modelform5,"form6": modelform6})

# from emballages import models
# models.enindex.objects.last()


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