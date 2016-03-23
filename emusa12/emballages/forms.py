# -*- coding: utf-8 -*- 

from django import forms
from .models import index, emballage, tecnology, client, contact, footer
from django.contrib.auth.models import User


class add_form1(forms.ModelForm):

# class ModelFormOptions(object):
#    def __init__(self, options=None):
#        self.model = getattr(options, 'model', None)
#        self.fields = getattr(options, 'fields', None)
#        self.exclude = getattr(options, 'exclude', None)
#        self.widgets = getattr(options, 'widgets', None)
#        self.localized_fields = getattr(options, 'localized_fields', None)
#        self.labels = getattr(options, 'labels', None)
#        self.help_texts = getattr(options, 'help_texts', None)
#        self.error_messages = getattr(options, 'error_messages', None)
 	def __init__(self, *args, **kwargs):           
        	super(add_form1, self).__init__(*args, **kwargs)
	        if index.objects.last():
	        	self.fields['menu1'].widget.attrs['placeholder'] = index.objects.last().menu1
		        self.fields['menu2'].widget.attrs['placeholder'] = index.objects.last().menu2
		        self.fields['menu3'].widget.attrs['placeholder'] = index.objects.last().menu3
		        self.fields['menu4'].widget.attrs['placeholder'] = index.objects.last().menu4
		        self.fields['menu5'].widget.attrs['placeholder'] = index.objects.last().menu5
		        self.fields['menu6'].widget.attrs['placeholder'] = index.objects.last().menu6
	        	self.fields['titulo_111'].widget.attrs['placeholder'] = index.objects.last().titulo_111
				
	class Meta:
		model = index
		fields = '__all__'
		help_texts = {
            'menu6': '<h2>1.1 INICIO</h2>',
            'imagen116': '<h2>1.2 INICIO</h2>',
            'imagen122': '<h2>1.3 INICIO</h2>',
            'imagen136': '<h2>1.4 INICIO</h2>',
            'imagen141': '<h2>1.5 INICIO</h2>',
            'img_certificado': '<h2>2.0 EMPACATE</h2>',
        }
		labels = {
            'telf1': 'Teléfonos',
            'telf2': '',
            'telf3': '',
            'menu1': 'Menú',
            'menu2': '',
            'menu3': '',
            'menu4': '',
            'menu5': '',
            'menu6': '',

            'titulo_111': 'Texto Título',
            'text_secundario111': 'Texto Secundario',
            'imagen111': 'Empaque 1',
            'imagen112': 'Empaque 2',
            'imagen113': 'Empaque 3',
            'imagen114': 'Empaque 4',
            'imagen115': 'Empaque 5',
            'imagen116': 'Empaque 6',
            
            'titulo_121': 'Texto Título',
            'text_secundario121': 'Texto Secundario',
            'imagen121': 'Imagen 1',
            'imagen122': 'Imagen 2',

            'titulo_131': 'Texto Título',
            'subtitulo131': 'Sub Título 1',
            'text_secundario131': 'Texto Secundario 1',
            'subtitulo132': 'Sub Título 2',
            'text_secundario132': 'Texto Secundario 2',
            'imagen131': 'Imagen 1',
            'imagen132': '',
      		'imagen133': '',
            'imagen134': 'Imagen 2',
      		'imagen135': '',
            'imagen136': '',

            'titulo_141': 'Texto Título',
            'text_secundario141': 'Texto Secundario',
            'imagen141': 'INFOGRAFIA',

            'titulo_151': 'Texto Título 1',
            'text_secundario151': 'Texto Secundario 1',
            'titulo_152': 'Texto Título 2',
            'text_secundario152': 'Texto Secundario 2',
            'imagen151': 'Imagen 1',
            'imagen152': '',
            'imagen153': '',
            'imagen154': '',
            'imagen155': '',
            'imagen156': '',
            'img_certificado': 'Certificado',
        }
		widgets = {
			 'logo' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),

			 'imagen111' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),

			 'imagen112' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),

			 'imagen113' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),

			 'imagen114' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),

			 'imagen115' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),

			 'imagen116' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),
			 'imagen121' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),
			 'imagen122' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),
			 'imagen131' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),
			 'imagen132' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),
			 'imagen133' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),
			 'imagen134' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),
			 'imagen135' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),
			 'imagen136' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),
			 'imagen141' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),
			 'imagen151' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),
			 'imagen152' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),
			 'imagen153' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),
			 'imagen154' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),
			 'imagen155' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),
			 'imagen156' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),
			 'img_certificado' : forms.ClearableFileInput(attrs = 
				{
				'class' : 'form-control', 
				}),


			 'titulo_111' : forms.TextInput(attrs = 
				{
				'class' : 'form-control', 
				# 'placeholder' : 
				}),
			 'text_secundario111' : forms.Textarea(attrs = 
				{
				'cols' : 30,
				'rows' : 2,
				# 'size' : 100,
				'class' : 'form-control', 
				}),
			 'text_secundario121' : forms.Textarea(attrs = 
				{
				'cols' : 30,
				'rows' : 4,
				'class' : 'form-control', 
				}),
			 'text_secundario131' : forms.Textarea(attrs = 
				{
				'cols' : 45,
				'rows' : 1,
				'class' : 'form-control', 
				}),
			 'text_secundario132' : forms.Textarea(attrs = 
				{
				'cols' : 30,
				'rows' : 3,
				'class' : 'form-control', 
				}),
			 'text_secundario141' : forms.Textarea(attrs = 
				{
				'cols' : 50,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'text_secundario151' : forms.Textarea(attrs = 
				{
				'cols' : 50,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'text_secundario152' : forms.Textarea(attrs = 
				{
				'cols' : 50,
				'rows' : 10,
				'class' : 'form-control', 
				}),
		}

class add_form2(forms.ModelForm):
	def __init__(self, *args, **kwargs):           
        	super(add_form2, self).__init__(*args, **kwargs)
	        # self.fields['boton_201'].widget.attrs['placeholder'] = emballage.objects.last().boton_201
	
	class Meta:
		model = emballage
		fields = '__all__'

		help_texts = {
            'imagen201': '<h2>2.1 EMPÁCATE</h2>',
            'imagen216': '<h2>2.2 EMPÁCATE</h2>',
            'empaque_img229': '<h2>2.3 EMPÁCATE</h2>',
            'imagen236': '<h2>2.4 EMPÁCATE</h2>',
            'imagen243': '<h2>2.5 EMPÁCATE</h2>',
            'boton_253': '<h2>3.0 tecnología</h2>',
        }
		labels = {
            'titulo_201': 'Texto Título 1',
            'text_secundario201': 'Texto Secundario',
            'boton_201': 'Botón 1',
            'imagen201': 'Imagen 1',

			'titulo_211' : 'Texto Título 1',
			'text_secundario211': 'Texto Secundario',
			'titulo_212' : 'Texto Título 2',
			'text_secundario212' : 'Texto Secundario',
			'titulo_213' : 'Texto Título 3',
			'text_secundario213' : 'Texto Secundario',
			'imagen211' : 'Imagen 1',
			'imagen212' : '',
			'imagen213' : 'Imagen 2',
			'imagen214' : '',
			'imagen215' : 'Imagen 3',
			'imagen216' : '',

			'titulo_221' : 'Texto Título 1',
			'empaque_220' : 'Opciones',
			'empaque_221' : '',
			'empaque_222' : '',
			'empaque_223' : '',
			'empaque_224' : '',
			'empaque_225' : '',
			'empaque_226' : '',
			'empaque_227' : '',
			'empaque_228' : '',
			'empaque_229' : '',
			'empaque_img220' : 'Imágenes',
			'empaque_img221' : '',
			'empaque_img222' : '',
			'empaque_img223' : '',
			'empaque_img224' : '',
			'empaque_img225' : '',
			'empaque_img226' : '',
			'empaque_img227' : '',
			'empaque_img228' : '',
			'empaque_img229' : '',

			'titulo_231' : 'Texto Título 1',
			'imagen231' : 'Imagen 1',
			'imagen232' : '',
			'imagen233' : '',
			'titulo_232' : 'Texto Título 2',
			'imagen234' : 'Imagen 2',
			'imagen235' : '',
			'imagen236' : '',
			'titulo_241' : 'Texto Título 1',
			'imagen241' : 'Imagen 1',
			'titulo_242' : 'Texto Título 2',
			'imagen242' : 'Imagen 2',
			'titulo_243' : 'Texto Título 3',
			'imagen243' : 'Imagen 3',
				
			'titulo_251' : 'Texto Título 1',
			'subtitulo2501' : 'SubTítulo 1',
			'imagen2501' : 'Imagen 1',
			'imagen2502' : '',
			'imagen2503' : '',
			'text_secundario2501' : 'Texto Secundario',
			'subtitulo2502' : 'SubTítulo 2',
			'imagen2504' : 'Imagen 2',
			'imagen2505' : '',
			'imagen2506' : '',
			'text_secundario2502' : 'Texto Secundario',
			'subtitulo2503' : 'SubTítulo 3',
			'imagen2507' : 'Imagen 3',
			'imagen2508' : '',
			'imagen2509' : '',
			'text_secundario2503' : 'Texto Secundario',
			'subtitulo2504' : 'SubTítulo 4',
			'imagen2510' : 'Imagen 4',
			'imagen2511' : '',
			'imagen2512' : '',
			'text_secundario2504' : 'Texto Secundario',
			'subtitulo2505' : 'SubTítulo 5',
			'imagen2513' : 'Imagen 5',
			'imagen2514' : '',
			'imagen2515' : '',
			'text_secundario2505' : 'Texto Secundario',
			'subtitulo2506' : 'SubTítulo 6',
			'imagen2516' : 'Imagen 6',
			'imagen2517' : '',
			'imagen2518' : '',
			'text_secundario2506' : 'Texto Secundario',
			'subtitulo2507' : 'SubTítulo 7',
			'imagen2519' : 'Imagen 7',
			'imagen2520' : '',
			'imagen2521' : '',
			'text_secundario2507' : 'Texto Secundario',
			'subtitulo2508' : 'SubTítulo 8',
			'imagen2522' : 'Imagen 8',
			'imagen2523' : '',
			'imagen2524' : '',
			'text_secundario2508' : 'Texto Secundario',
			'subtitulo2509' : 'SubTítulo 9',
			'imagen2525' : 'Imagen 9',
			'imagen2526' : '',
			'imagen2527' : '',
			'text_secundario2509' : 'Texto Secundario',
			'subtitulo2510' : 'SubTítulo 10',
			'imagen2528' : 'Imagen 10',
			'imagen2529' : '',
			'imagen2530' : '',
			'text_secundario2510' : 'Texto Secundario',
			'subtitulo2511' : 'SubTítulo 11',
			'imagen2531' : 'Imagen 11',
			'imagen2532' : '',
			'imagen2533' : '',
			'text_secundario2511' : 'Texto Secundario',
			'subtitulo2512' : 'SubTítulo 12',
			'imagen2534' : 'Imagen 12',
			'imagen2535' : '',
			'imagen2536' : '',
			'text_secundario2512' : 'Texto Secundario',
			'subtitulo2513' : 'SubTítulo 13',
			'imagen2537' : 'Imagen 13',
			'imagen2538' : '',
			'imagen2539' : '',
			'text_secundario2513' : 'Texto Secundario',
			'subtitulo2514' : 'SubTítulo 14',
			'imagen2540' : 'Imagen 14',
			'imagen2541' : '',
			'imagen2542' : '',
			'text_secundario2514' : 'Texto Secundario',
			'subtitulo2515' : 'SubTítulo 15',
			'imagen2543' : 'Imagen 15',
			'imagen2544' : '',
			'imagen2545' : '',
			'text_secundario2515' : 'Texto Secundario',
				
			'boton_251' : 'Botón 1',
			'boton_252' : 'Botón 2',
			'cuestionario' : 'cuestionario',
			'pregunta21' : 'Pregunta 1',
			'pregunta22' : 'Pregunta 2',
			'pregunta23' : 'Pregunta 3',
			'pregunta24' : 'Pregunta 4',
			'boton_253' : 'Botón 3',

        }
		widgets = {
			 'text_secundario201' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
				# 'size' : 100,
				'class' : 'form-control', 
				}),
			 'text_secundario211' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 4,
				'class' : 'form-control', 
				}),
			 'text_secundario212' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'text_secundario213' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'subtitulo2501' : forms.Textarea(attrs = 
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control', 
				}),
			 
			 'text_secundario2501' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'subtitulo2502' : forms.Textarea(attrs = 
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control', 
				}),
			 
			 'text_secundario2502' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'subtitulo2503' : forms.Textarea(attrs = 
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control', 
				}),
			 
			 'text_secundario2503' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'subtitulo2504' : forms.Textarea(attrs = 
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control', 
				}),
			 
			 'text_secundario2504' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'subtitulo2505' : forms.Textarea(attrs = 
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control', 
				}),
			 
			 'text_secundario2505' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'subtitulo2506' : forms.Textarea(attrs = 
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control', 
				}),
			 
			 'text_secundario2506' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'subtitulo2507' : forms.Textarea(attrs = 
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control', 
				}),
			 
			 'text_secundario2507' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'subtitulo2508' : forms.Textarea(attrs = 
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control', 
				}),
			 
			 'text_secundario2508' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'subtitulo2509' : forms.Textarea(attrs = 
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control', 
				}),
			 
			 'text_secundario2509' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'subtitulo2510' : forms.Textarea(attrs = 
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control', 
				}),
			 
			 'text_secundario2510' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'subtitulo2511' : forms.Textarea(attrs = 
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control', 
				}),
			 
			 'text_secundario2511' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'subtitulo2512' : forms.Textarea(attrs = 
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control', 
				}),
			 
			 'text_secundario2512' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'subtitulo2513' : forms.Textarea(attrs = 
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control', 
				}),
			 
			 'text_secundario2513' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'subtitulo2514' : forms.Textarea(attrs = 
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control', 
				}),
			 
			 'text_secundario2514' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'subtitulo2515' : forms.Textarea(attrs = 
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control', 
				}),
			 
			 'text_secundario2515' : forms.Textarea(attrs = 
				{
				'cols' : 40,
				'rows' : 2,
	 			'class' : 'form-control', 
				}),
			}			 
class add_form3(forms.ModelForm):
	def __init__(self, *args, **kwargs):           
	    	super(add_form3, self).__init__(*args, **kwargs)
	        self.fields['imagen301'].widget.attrs['placeholder'] = 'Fondo 1'
	        self.fields['imagen311'].widget.attrs['placeholder'] = 'Fondo 2'
		self.fields['imagen312'].widget.attrs['placeholder'] = 'Fondo 3'
		self.fields['imagen321'].widget.attrs['placeholder'] = 'Fondo 4'

	class Meta:
		model = tecnology
		fields = '__all__'
		help_texts = {
            'imagen301': '<h2>3.1 Tecnología</h2>',
            'imagen311': '<h2>3.1 Tecnología</h2>',
            'imagen312': '<h2>3.2 Tecnología</h2>',
            'text_secundario321': '<h2>4.0 Nuestros Clientes</h2>',
        }

		labels = {
		'titulo_301' : 'Texto Título 1',
		'text_secundario301' : 'Texto Secundario',
		'boton_301' : 'Botón 1',
		'imagen301' : 'Imagen Fondo',

		'subtitulo311' : 'SubTítulo',
		'text_secundario311' : 'Cuadro Texto 1',
		'text_secundario312' : 'Cuadro Texto 2',
		'text_secundario313' : 'Cuadro Texto 3',
		'text_secundario314' : 'Cuadro Texto 4',
		'imagen311' : 'Imagen Fondo',
		'text_secundario315' : 'Cuadro Texto 5',
		'text_secundario316' : 'Cuadro Texto 6',
		'text_secundario317' : 'Cuadro Texto 7',
		'text_secundario318' : 'Cuadro Texto 8',
		'text_secundario319' : 'Cuadro Texto 9',
		'imagen312' : 'Imagen Fondo',
		'titulo_321' : 'Texto Título 1',
		'imagen321' : 'Imagen Fondo',
		'text_secundario321' : 'Texto Secundario',
		}
		widgets = {
		'text_secundario301': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'text_secundario311': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'text_secundario312': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'text_secundario313': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'text_secundario314': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'text_secundario315': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'text_secundario316': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'text_secundario317': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'text_secundario3018': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'text_secundario319': forms.Textarea(attrs={
			'cols' : 35,
			'rows' : 1,
			'class' : 'form-control',
			}),
		'text_secundario321': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 11,
			'class' : 'form-control',
			}),
		}
class add_form4(forms.ModelForm):
	class Meta:
		model = client
		fields = '__all__'
		help_texts = {
	        'imagen401': '<h2>5.0 Contáctanos</h2>',
	    }
		labels = {
		'titulo_401' : 'Texto Título',
		'imagen401' : 'Imagen Fondo',
		}
class add_form5(forms.ModelForm):
	class Meta:
		model = contact
		fields = '__all__'
		help_texts = {
	        'boton_501': '<h2>Footer</h2>',
	    }
		labels = {
		'titulo_501' : 'Texto Título 1',
		'pregunta51' : 'Pregunta 1',
		'pregunta52' : 'Pregunta 2',
		'pregunta53' : 'Pregunta 3',
		'pregunta54' : 'Pregunta 4',
		'boton_501' : 'Botón Enviar',
		}
class add_form6(forms.ModelForm):
	class Meta:
		model = footer
		fields = '__all__'
		labels = {
		'titulo_601' : 'Footer Texto',
		}
class UserRegisterForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		widgets = {
			'username' : forms.TextInput(attrs = 
				{
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un nombre de usuario',
				'readonly':'readonly'
				}),
			'email' : forms.TextInput(attrs = 
				{
				'type' : 'email',
				'class' : 'form-control',
				'placeholder' : 'Ingresa un email',
				'readonly':'readonly'
				}),
			'password' : forms.TextInput(attrs = 
				{
				'type' : 'password',
				'class' : 'form-control',
				'placeholder' : 'Ingresa un password',
				'readonly':'readonly'
				})
		}

class LoginForm(forms.Form):

	username = forms.CharField(max_length=30, 
				widget = forms.TextInput(attrs = {
					'class' : 'form-control',
					'placeholder' : 'Ingresa un nombre de usuario',
					}))
	password = forms.CharField(max_length=30,
	 			widget = forms.TextInput(attrs = {
	 				'type' : 'password',
	 				'class' : 'form-control',
	 				'placeholder' : 'Ingresa un password',
	 				}))	 	 