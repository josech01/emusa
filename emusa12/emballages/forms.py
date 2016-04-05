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
	        	self.fields['correo'].widget.attrs['value'] = index.objects.last().correo
	        	self.fields['telf1'].widget.attrs['value'] = index.objects.last().telf1
	        	self.fields['telf2'].widget.attrs['value'] = index.objects.last().telf2
	        	self.fields['telf3'].widget.attrs['value'] = index.objects.last().telf3
	        	self.fields['menu1'].widget.attrs['value'] = index.objects.last().menu1
		        self.fields['menu2'].widget.attrs['value'] = index.objects.last().menu2
		        self.fields['menu3'].widget.attrs['value'] = index.objects.last().menu3
		        self.fields['menu4'].widget.attrs['value'] = index.objects.last().menu4
		        self.fields['menu5'].widget.attrs['value'] = index.objects.last().menu5
		        self.fields['menu6'].widget.attrs['value'] = index.objects.last().menu6
	        	self.fields['titulo_111'].widget.attrs['value'] = index.objects.last().titulo_111
	        	self.fields['text_secundario111'].initial = index.objects.last().text_secundario111
	        	self.fields['titulo_121'].widget.attrs['value'] = index.objects.last().titulo_121
	        	self.fields['text_secundario121'].initial = index.objects.last().text_secundario121
	        	#self.fields['titulo_131'].widget.attrs['value'] = index.objects.last().titulo_131
	        	self.fields['subtitulo131'].widget.attrs['value'] = index.objects.last().subtitulo131
	        	self.fields['text_secundario131'].initial = index.objects.last().text_secundario131
	        	self.fields['subtitulo132'].widget.attrs['value'] = index.objects.last().subtitulo132
	        	self.fields['text_secundario132'].initial = index.objects.last().text_secundario132
	        	self.fields['titulo_151'].widget.attrs['value'] = index.objects.last().titulo_151
	        	self.fields['text_secundario151'].initial = index.objects.last().text_secundario151
	        	self.fields['text_secundario152'].initial = index.objects.last().text_secundario152


	class Meta:
		model = index
		fields = '__all__'
		
		help_texts = {
        }
		# labels = {
  #           'telf1': 'Teléfonos',
  #           'telf2': '',
  #           'telf3': '',
  #           'menu1': 'Menú',
  #           'menu2': '',
  #           'menu3': '',
  #           'menu4': '',
  #           'menu5': '',
  #           'menu6': '',

  #           'titulo_111': 'Texto Título',
  #           'text_secundario111': 'Texto Secundario',
  #           'imagen111': 'Empaque 1',
  #           'imagen112': 'Empaque 2',
  #           'imagen113': 'Empaque 3',
  #           'imagen114': 'Empaque 4',
  #           'imagen115': 'Empaque 5',
  #           'imagen116': 'Empaque 6',

  #           'titulo_121': 'Texto Título',
  #           'text_secundario121': 'Texto Secundario',
  #           'imagen121': 'Imagen 1',
  #           'imagen122': 'Imagen 2',

  #           'titulo_131': 'Texto Título',
  #           'subtitulo131': 'Sub Título 1',
  #           'text_secundario131': 'Texto Secundario 1',
  #           'subtitulo132': 'Sub Título 2',
  #           'text_secundario132': 'Texto Secundario 2',
  #           'imagen131': 'Imagen 1',
  #           'imagen132': '',
  #     		'imagen133': '',
  #           'imagen134': 'Imagen 2',
  #     		'imagen135': '',
  #           'imagen136': '',

  #           'titulo_141': 'Texto Título',
  #           'text_secundario141': 'Texto Secundario',
  #           'imagen141': 'INFOGRAFIA',

  #           'titulo_151': 'Texto Título 1',
  #           'text_secundario151': 'Texto Secundario 1',
  #           'titulo_152': 'Texto Título 2',
  #           'text_secundario152': 'Texto Secundario 2',
  #           'imagen151': 'Imagen 1',
  #           'imagen152': '',
  #           'imagen153': '',
  #           'imagen154': '',
  #           'imagen155': '',
  #           'imagen156': '',
  #           'img_certificado': 'Certificado',
        #}
		widgets = {
			 'logo' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen111' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen112' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen113' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen114' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen115' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen116' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen121' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen122' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen131' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen132' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen133' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen134' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen135' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen136' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen137' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen141' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen142' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen151' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen152' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'imagen153' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'img_certificado' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),

			 'titulo_111' : forms.TextInput(attrs =
				{
				'value' : 'john',
				'class' : 'form-control',
				# 'placeholder' :
				}),
			 'text_secundario111' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 4,
				# 'size' : 100,
				'class' : 'form-control',
				}),
			 'text_secundario121' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 5,
				'class' : 'form-control',
				}),
			 'text_secundario131' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 3,
				'class' : 'form-control',
				}),
			 'text_secundario132' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 5,
				'class' : 'form-control',
				}),
			 'text_secundario141' : forms.Textarea(attrs =
				{
				'cols' : 30,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'text_secundario151' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 11,
				'class' : 'form-control',
				}),
			 'text_secundario152' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 3,
				'class' : 'form-control',
				}),
		}

class add_form2(forms.ModelForm):
	def __init__(self, *args, **kwargs):
        	super(add_form2, self).__init__(*args, **kwargs)
	        if emballage.objects.last():
	        	self.fields['titulo_201'].widget.attrs['value'] = emballage.objects.last().titulo_201
	        	self.fields['text_secundario201'].initial = emballage.objects.last().text_secundario201
	        	self.fields['boton_201'].widget.attrs['value'] = emballage.objects.last().boton_201
    			self.fields['boton_251'].widget.attrs['value'] = emballage.objects.last().boton_251
		    	self.fields['boton_252'].widget.attrs['value'] = emballage.objects.last().boton_252
	    		self.fields['boton_253'].widget.attrs['value'] = emballage.objects.last().boton_253
			self.fields['titulo_211'].widget.attrs['value'] = emballage.objects.last().titulo_211
			self.fields['titulo_212'].widget.attrs['value'] = emballage.objects.last().titulo_212
			self.fields['titulo_213'].widget.attrs['value'] = emballage.objects.last().titulo_213
			self.fields['empaque_220'].widget.attrs['value'] = emballage.objects.last().empaque_220
			self.fields['empaque_221'].widget.attrs['value'] = emballage.objects.last().empaque_221
			self.fields['empaque_222'].widget.attrs['value'] = emballage.objects.last().empaque_222
			self.fields['empaque_223'].widget.attrs['value'] = emballage.objects.last().empaque_223
			self.fields['empaque_224'].widget.attrs['value'] = emballage.objects.last().empaque_224
			self.fields['empaque_225'].widget.attrs['value'] = emballage.objects.last().empaque_225
			self.fields['empaque_226'].widget.attrs['value'] = emballage.objects.last().empaque_226
			self.fields['empaque_227'].widget.attrs['value'] = emballage.objects.last().empaque_227
			self.fields['empaque_228'].widget.attrs['value'] = emballage.objects.last().empaque_228
			self.fields['empaque_229'].widget.attrs['value'] = emballage.objects.last().empaque_229
			self.fields['titulo_251'].widget.attrs['value'] = emballage.objects.last().titulo_251
			self.fields['cuestionario'].widget.attrs['value'] = emballage.objects.last().cuestionario
			self.fields['subtitulo2501'].initial = emballage.objects.last().subtitulo2501
			self.fields['subtitulo2502'].initial = emballage.objects.last().subtitulo2502
			self.fields['subtitulo2503'].initial = emballage.objects.last().subtitulo2503
			self.fields['subtitulo2504'].initial = emballage.objects.last().subtitulo2504
			self.fields['subtitulo2505'].initial = emballage.objects.last().subtitulo2505
			self.fields['subtitulo2506'].initial = emballage.objects.last().subtitulo2506
			self.fields['subtitulo2507'].initial = emballage.objects.last().subtitulo2507
			self.fields['subtitulo2508'].initial = emballage.objects.last().subtitulo2508
			self.fields['subtitulo2509'].initial = emballage.objects.last().subtitulo2509
			self.fields['subtitulo2510'].initial = emballage.objects.last().subtitulo2510
			self.fields['subtitulo2511'].initial = emballage.objects.last().subtitulo2511
			self.fields['subtitulo2512'].initial = emballage.objects.last().subtitulo2512
			self.fields['subtitulo2513'].initial = emballage.objects.last().subtitulo2513
			self.fields['subtitulo2514'].initial = emballage.objects.last().subtitulo2514
			self.fields['subtitulo2515'].initial = emballage.objects.last().subtitulo2515
			self.fields['text_secundario201'].initial = emballage.objects.last().text_secundario201
			self.fields['text_secundario211'].initial = emballage.objects.last().text_secundario211
			self.fields['text_secundario212'].initial = emballage.objects.last().text_secundario212
			self.fields['text_secundario2501'].initial = emballage.objects.last().text_secundario2501
			self.fields['text_secundario2502'].initial = emballage.objects.last().text_secundario2502
			self.fields['text_secundario2503'].initial = emballage.objects.last().text_secundario2503
			self.fields['text_secundario2504'].initial = emballage.objects.last().text_secundario2504
			self.fields['text_secundario2505'].initial = emballage.objects.last().text_secundario2505
			self.fields['text_secundario2506'].initial = emballage.objects.last().text_secundario2506
			self.fields['text_secundario2507'].initial = emballage.objects.last().text_secundario2507
			self.fields['text_secundario2508'].initial = emballage.objects.last().text_secundario2508
			self.fields['text_secundario2509'].initial = emballage.objects.last().text_secundario2509
			self.fields['text_secundario2510'].initial = emballage.objects.last().text_secundario2510
			self.fields['text_secundario2511'].initial = emballage.objects.last().text_secundario2511
			self.fields['text_secundario2512'].initial = emballage.objects.last().text_secundario2512
			self.fields['text_secundario2513'].initial = emballage.objects.last().text_secundario2513
			self.fields['text_secundario2514'].initial = emballage.objects.last().text_secundario2514
			self.fields['text_secundario2515'].initial = emballage.objects.last().text_secundario2515

	class Meta:
		model = emballage
		fields = '__all__'

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
				'cols' : 50,
				'rows' : 5,
				'class' : 'form-control',
				}),
			'imagen201' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'imagen202' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'imagen203' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'imagen211' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'imagen213' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'imagen215' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'imagen221' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),

            'flecha' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'imagen231' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'imagen232' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'imagen233' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'imagen234' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'imagen235' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'imagen236' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'imagen237' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'imagen238' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'imagen241' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'imagen242' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'imagen243' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'imagen244' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'imagen245' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'imagen246' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),

            'empaque_img220' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'empaque_img221' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'empaque_img222' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'empaque_img223' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'empaque_img224' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'empaque_img225' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'empaque_img226' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'empaque_img227' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'empaque_img228' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'empaque_img229' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),

			'imagen2501' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2502' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2503' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2504' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2505' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2506' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2507' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2508' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2509' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2510' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2511' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2512' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2513' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2514' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2515' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2516' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2517' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2518' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2519' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2520' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2521' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2522' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2523' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2524' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2525' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2526' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2527' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2528' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2529' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2530' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2531' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2532' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2534' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2535' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2536' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2537' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2538' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2539' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2540' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2541' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2542' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2543' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2544' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen2545' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'imagen251' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),

			 'text_secundario211' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 5,
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
	        if tecnology.objects.last():
		        self.fields['titulo_301'].widget.attrs['value'] = tecnology.objects.last().titulo_301
	        	self.fields['text_secundario301'].initial = tecnology.objects.last().text_secundario301
	        	self.fields['boton_301'].widget.attrs['value'] = tecnology.objects.last().boton_301
	        	self.fields['subtitulo311'].initial = tecnology.objects.last().subtitulo311
	        	self.fields['text_secundario311'].initial = tecnology.objects.last().text_secundario311
	        	self.fields['text_secundario312'].initial = tecnology.objects.last().text_secundario312
	        	self.fields['text_secundario313'].initial = tecnology.objects.last().text_secundario313
	        	self.fields['text_secundario314'].initial = tecnology.objects.last().text_secundario314
	        	self.fields['text_secundario315'].initial = tecnology.objects.last().text_secundario315
	        	self.fields['text_secundario316'].initial = tecnology.objects.last().text_secundario316
	        	self.fields['text_secundario317'].initial = tecnology.objects.last().text_secundario317
	        	self.fields['text_secundario318'].initial = tecnology.objects.last().text_secundario318
	        	self.fields['text_secundario319'].initial = tecnology.objects.last().text_secundario319
	        	self.fields['titulo_321'].widget.attrs['value'] = tecnology.objects.last().titulo_321
	        	self.fields['text_secundario321'].initial = tecnology.objects.last().text_secundario321





	class Meta:
		model = tecnology
		fields = '__all__'

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
		'fondo1' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'imagen301' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'imagen302' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'imagen311' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'imagen312' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'fondo2' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'imagen13' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'fondo3' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'tr_top' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'tr_bottom' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),

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
			'cols' : 50,
			'rows' : 11,
			'class' : 'form-control',
			}),
		}
class add_form4(forms.ModelForm):
	class Meta:
		model = client
		fields = '__all__'
		labels = {
		'titulo_401' : 'Texto Título',
		'imagen401' : 'Imagen Fondo',
		}
		widgets = {
		'imagen401' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		}
class add_form5(forms.ModelForm):
	def __init__(self, *args, **kwargs):
	    	super(add_form5, self).__init__(*args, **kwargs)
	        if contact.objects.last():
		        self.fields['titulo_501'].widget.attrs['value'] = contact.objects.last().titulo_501
		        self.fields['pregunta51'].widget.attrs['placeholder'] = "Ingresa tu nombre"
		        self.fields['pregunta52'].widget.attrs['placeholder'] = "Ingresa tu correo"
		        self.fields['pregunta53'].widget.attrs['placeholder'] = "Ingresa tu número"
		        self.fields['pregunta54'].widget.attrs['placeholder'] = "Escribe el mensaje"
		        self.fields['boton_501'].widget.attrs['value'] = contact.objects.last().boton_501


	class Meta:
		model = contact
		fields = '__all__'
		labels = {
		'titulo_501' : 'Texto Título 1',
		'pregunta51' : 'Pregunta 1',
		'pregunta52' : 'Pregunta 2',
		'pregunta53' : 'Pregunta 3',
		'pregunta54' : 'Pregunta 4',
		'boton_501' : 'Botón Enviar',
		}
class add_form6(forms.ModelForm):
	def __init__(self, *args, **kwargs):
	    	super(add_form6, self).__init__(*args, **kwargs)
	        if footer.objects.last():
	        	self.fields['titulo_601'].widget.attrs['value'] = footer.objects.last().titulo_601
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
				'readonly':'readonly',
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
