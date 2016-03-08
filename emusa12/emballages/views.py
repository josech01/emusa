#!/usr/bin/python
# -*- coding: utf-8 -*- 

from django.shortcuts import render , redirect, render_to_response

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

