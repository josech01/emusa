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
from emballages_pt.forms import ptadd_form1, ptadd_form2, ptadd_form3, ptadd_form4, ptadd_form5, ptadd_form6
from emballages_pt import models
# Create your views here.
def ptclientes (request):
	if request.method == 'GET':
		index = models.ptindex.objects.last()
		clients = models.ptclient.objects.last()
		footer = models.ptfooter.objects.last()
		context_data = {'index': index, 'clients': clients,'footer': footer}
		return render(request, 'clientes_pt.html', context_data)

def ptcontactanos (request):
	if request.method == 'GET':
		index = models.ptindex.objects.last()
		contacts = models.ptcontact.objects.last()
		footer = models.ptfooter.objects.last()
		context_data = {'index': index, 'contacts': contacts,'footer': footer}
		return render(request, 'contactanos_pt.html', context_data)

def ptindex (request):
	if request.method == 'GET':
		index = models.ptindex.objects.last()
		footer = models.ptfooter.objects.last()
		context_data = {'index': index, 'footer': footer}
		return render(request, 'index_pt.html',context_data)


def ptempacate (request):
	if request.method == 'GET':
		index = models.ptindex.objects.last()
		empacar = models.ptemballage.objects.last()
		footer = models.ptfooter.objects.last()
		context_data = {'index': index, 'empacar': empacar,'footer': footer}
		return render(request, 'empacate_pt.html',context_data)


def pttecnologia (request):
	if request.method == 'GET':
		index = models.ptindex.objects.last()
		tecnologys = models.pttecnology.objects.last()
		footer = models.ptfooter.objects.last()
		context_data = {'index': index, 'tecnologys': tecnologys,'footer': footer}
		return render(request, 'tecnologia_pt.html', context_data)

def ptadd_new_form (request):
	if request.method == "POST":
		instance1 = models.ptindex.objects.last()
		instance2 = models.ptemballage.objects.last()
		instance3 = models.pttecnology.objects.last()
		instance4 = models.ptclient.objects.last()
		instance5 = models.ptcontact.objects.last()
		instance6 = models.ptfooter.objects.last()
		modelform1 = ptadd_form1(request.POST, request.FILES, instance= instance1)
		modelform2 = ptadd_form2(request.POST, request.FILES, instance= instance2)
		modelform3 = ptadd_form3(request.POST, request.FILES, instance= instance3)
		modelform4 = ptadd_form4(request.POST, request.FILES, instance= instance4)
		modelform5 = ptadd_form5(request.POST, request.FILES, instance= instance5)
		modelform6 = ptadd_form6(request.POST, request.FILES, instance= instance6)
		if modelform1.is_valid() and modelform2.is_valid() and modelform3.is_valid() and modelform4.is_valid() and modelform5.is_valid() and modelform6.is_valid():	
			modelform1.save()
			modelform2.save()
			modelform3.save()
			modelform4.save()
			modelform5.save()
			modelform6.save()
			return redirect("/form_pt.html")
	else:
		modelform1 = ptadd_form1()
		modelform2 = ptadd_form2()
		modelform3 = ptadd_form3()
		modelform4 = ptadd_form4()
		modelform5 = ptadd_form5()
		modelform6 = ptadd_form6()
		
	# print models.ptdata_info.objects.last()
	return render(request, "form_pt.html", {"form1": modelform1,"form2": modelform2,"form3": modelform3,"form4": modelform4,"form5": modelform5,"form6": modelform6})
