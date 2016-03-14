# -*- coding: utf-8 -*- 

from django import forms
from models import index, emballage, tecnology, clients, contact, footer
from django.contrib.auth.models import User

class add_form(forms.ModelForm):
	class Meta:
		model = index
		fields = ('idioma' , 'correo' , 'telf1' , 'telf2' , 'telf3' , 'logo' , 'menu1' , 'titulo_111' , 'text_secundario111' , 'imagen111' , 'imagen112' , 'imagen113' , 'imagen114' , 'imagen115' , 'imagen116' , 'titulo_121' , 'text_secundario121' , 'imagen121' , 'imagen122' , 'titulo_131' , 'subtitulo131' , 'text_secundario131' , 'subtitulo132' , 'text_secundario132' , 'imagen131' , 'imagen132' , 'imagen133' , 'imagen134' , 'imagen135' , 'imagen136' , 'titulo_141' , 'text_secundario141' , 'imagen141' , 'titulo_151' , 'text_secundario151' , 'titulo_152' , 'text_secundario152' , 'imagen152' , 'imagen153' , 'imagen151' , 'imagen154' , 'imagen155' , 'imagen156' , 'img_certificado')
		widgets = {
			'idioma' : forms.select(attrs = 
				{
				'title' : 'Idioma'
				# 'class' : 'form-control', 
				}),
			'email' : forms.TextInput(attrs = 
				{
				'type' : 'email',
				'class' : 'form-control',
				'placeholder' : 'Ingresa un correo'
				}),
			'telf1' : forms.TextInput(attrs = 
				{
				'type' : 'TextInput',
				'class' : 'form-control',
				'placeholder' : 'Teléfonos'
				}),
			'telf2' : forms.TextInput(attrs = 
				{
				'type' : 'TextInput',
				'class' : 'form-control',
				'placeholder' : ''
				}),
			'telf3' : forms.TextInput(attrs = 
				{
				'type' : 'TextInput',
				'class' : 'form-control',
				'placeholder' : ''
				}),
			'logo' : forms.TextInput(attrs = 
				{
				'class' : 'form-control',
				'placeholder' : 'Logo'
				}),
			 'menu1' : forms.TextInput(attrs = 
				{
				'class' : 'form-control', 
				'placeholder' : 'Menu'
				}),
			 'titulo_111' : forms.TextInput(attrs = 
				{
				'class' : 'form-control', 
				'placeholder' : 'Texto Título'
				}),
			 'text_secundario111' : forms.TextInput(attrs = 
				{
				'class' : 'form-control', 
				'placeholder' : 'Texto Secundario'
				}),
			 'imagen111' : forms.TextInput(attrs = 
				{
				'class' : 'form-control', 
				'placeholder' : 'Imagen 1'
				}),

		}

class UserRegisterForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		widgets = {
			'username' : forms.TextInput(attrs = 
				{
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un nombre de usuario'
				}),
			'email' : forms.TextInput(attrs = 
				{
				'type' : 'email',
				'class' : 'form-control',
				'placeholder' : 'Ingresa un email'
				}),
			'password' : forms.TextInput(attrs = 
				{
				'type' : 'password',
				'class' : 'form-control',
				'placeholder' : 'Ingresa un password'
				})
		}

class LoginForm(forms.Form):

	username = forms.CharField(max_length=30, 
				widget = forms.TextInput(attrs = {
					'class' : 'form-control',
					'placeholder' : 'Ingresa un nombre de usuario'
					}))
	password = forms.CharField(max_length=30,
	 			widget = forms.TextInput(attrs = {
	 				'type' : 'password',
	 				'class' : 'form-control',
	 				'placeholder' : 'Ingresa un password'
	 				}))	 	 