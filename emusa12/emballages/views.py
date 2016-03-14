#!/usr/bin/python
# -*- coding: utf-8 -*- 

from django.shortcuts import render , redirect, render_to_response
import json

from django.http import HttpResponseServerError, HttpResponse,  HttpResponseBadRequest,  HttpResponseNotAllowed
from django.db.models import Model

from models import *

from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import add_form,UserRegisterForm, LoginForm
from .functions import LogIn
# Create your views here.
def clientes (request):
	if request.method == 'GET':
		return render(request, 'clientes.html')

def contactanos (request):
	if request.method == 'GET':
		return render(request, 'contactanos.html')

def index (request):
	if request.method == 'GET':
		return render(request, 'index.html')


def empacate (request):
	if request.method == 'GET':
		return render(request, 'empacate.html')


def tecnologia (request):
	if request.method == 'GET':
		return render(request, 'tecnologia.html')

def add_new_form (request):
	if request.method == "POST":
		modelform = add_form(request.POST)
		if modelform.is_valid():
			modelform.save()
			return redirect("/form/")
	else:
		modelform = add_form()

	return render(request, "form.html", {"form": modelform})


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
				return redirect('form/')
	else:
		user_register = UserRegisterForm()
		login_form = LoginForm()
	return render(request, 'login.html', 
				{'user_register' : user_register, 'login_form' : login_form})


def LogOut(request):
	logout(request)
	return redirect('/')
