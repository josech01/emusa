# -*- coding: utf-8 -*-

from django import forms
from .models import enindex, enemballage, entecnology, enclient, encontact, enfooter
from django.contrib.auth.models import User


class enadd_form1(forms.ModelForm):

# class ModelFormOptions(object):
#    def __init__(self, options=None):
#        self.model = engetattr(options, 'model', None)
#        self.fields = getattr(options, 'fields', None)
#        self.exclude = getattr(options, 'exclude', None)
#        self.widgets = getattr(options, 'widgets', None)
#        self.localized_fields = getattr(options, 'localized_fields', None)
#        self.labels = getattr(options, 'labels', None)
#        self.help_texts = getattr(options, 'help_texts', None)
#        self.error_messages = getattr(options, 'error_messages', None)
 	def __init__(self, *args, **kwargs):
        	super(enadd_form1, self).__init__(*args, **kwargs)
	        if enindex.objects.last():
	        	self.fields['encorreo'].widget.attrs['value'] = index.objects.last().encorreo
	        	self.fields['entelf1'].widget.attrs['value'] = index.objects.last().entelf1
	        	self.fields['entelf2'].widget.attrs['value'] = index.objects.last().entelf2
	        	self.fields['entelf3'].widget.attrs['value'] = index.objects.last().entelf3
	        	self.fields['enmenu1'].widget.attrs['value'] = index.objects.last().enmenu1
		        self.fields['enmenu2'].widget.attrs['value'] = index.objects.last().enmenu2
		        self.fields['enmenu3'].widget.attrs['value'] = index.objects.last().enmenu3
		        self.fields['enmenu4'].widget.attrs['value'] = index.objects.last().enmenu4
		        self.fields['enmenu5'].widget.attrs['value'] = index.objects.last().enmenu5
		        self.fields['enmenu6'].widget.attrs['value'] = index.objects.last().enmenu6
	        	self.fields['entitulo_111'].widget.attrs['value'] = index.objects.last().entitulo_111
	        	self.fields['entext_secundario111'].initial = index.objects.last().entext_secundario111
	        	self.fields['entitulo_121'].widget.attrs['value'] = index.objects.last().entitulo_121
	        	self.fields['entext_secundario121'].initial = index.objects.last().entext_secundario121
	        	#self.fields['entitulo_131'].widget.attrs['value'] = index.objects.last().entitulo_131
	        	self.fields['ensubtitulo131'].widget.attrs['value'] = index.objects.last().ensubtitulo131
	        	self.fields['entext_secundario131'].initial = index.objects.last().entext_secundario131
	        	self.fields['ensubtitulo132'].widget.attrs['value'] = index.objects.last().ensubtitulo132
	        	self.fields['entext_secundario132'].initial = index.objects.last().entext_secundario132
	        	self.fields['entitulo_151'].widget.attrs['value'] = index.objects.last().entitulo_151
	        	self.fields['entext_secundario151'].initial = index.objects.last().entext_secundario151
	        	self.fields['entext_secundario152'].initial = index.objects.last().entext_secundario152


	class Meta:
		model = enindex
		fields = '__all__'
		exclude = ('entitulo_131', 'enimagen132', 'enimagen133', 'enimagen135','entitulo_141', 'entext_secundario141', 'entitulo_152', 'enimagen152', 'enimagen153', 'enimagen154', 'enimagen156')
		help_texts = {
        }
		
		widgets = {
			 'enlogo' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen111' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen112' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen113' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen114' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen115' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen116' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen121' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen122' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen131' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen132' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen133' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen134' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen135' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen136' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen137' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen141' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen142' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen151' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen152' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimagen153' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'enimg_certificado' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),

			 'entitulo_111' : forms.TextInput(attrs =
				{
				'value' : 'john',
				'class' : 'form-control',
				# 'placeholder' :
				}),
			 'entext_secundario111' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 4,
				# 'size' : 100,
				'class' : 'form-control',
				}),
			 'entext_secundario121' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 5,
				'class' : 'form-control',
				}),
			 'entext_secundario131' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 3,
				'class' : 'form-control',
				}),
			 'entext_secundario132' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 5,
				'class' : 'form-control',
				}),
			 'entext_secundario141' : forms.Textarea(attrs =
				{
				'cols' : 30,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'entext_secundario151' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 11,
				'class' : 'form-control',
				}),
			 'entext_secundario152' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 3,
				'class' : 'form-control',
				}),
		}

class enadd_form2(forms.ModelForm):
	def __init__(self, *args, **kwargs):
        	super(enadd_form2, self).__init__(*args, **kwargs)
	        if enemballage.objects.last():
	        	self.fields['entitulo_201'].widget.attrs['value'] = emballage.objects.last().entitulo_201
	        	self.fields['entext_secundario201'].initial = emballage.objects.last().entext_secundario201
	        	self.fields['enboton_201'].widget.attrs['value'] = emballage.objects.last().enboton_201
    			self.fields['enboton_251'].widget.attrs['value'] = emballage.objects.last().enboton_251
		    	self.fields['enboton_252'].widget.attrs['value'] = emballage.objects.last().enboton_252
	    		self.fields['enboton_253'].widget.attrs['value'] = emballage.objects.last().enboton_253
			self.fields['entitulo_211'].widget.attrs['value'] = emballage.objects.last().entitulo_211
			self.fields['entitulo_212'].widget.attrs['value'] = emballage.objects.last().entitulo_212
			self.fields['entitulo_213'].widget.attrs['value'] = emballage.objects.last().entitulo_213
			self.fields['enempaque_220'].widget.attrs['value'] = emballage.objects.last().enempaque_220
			self.fields['enempaque_221'].widget.attrs['value'] = emballage.objects.last().enempaque_221
			self.fields['enempaque_222'].widget.attrs['value'] = emballage.objects.last().enempaque_222
			self.fields['enempaque_223'].widget.attrs['value'] = emballage.objects.last().enempaque_223
			self.fields['enempaque_224'].widget.attrs['value'] = emballage.objects.last().enempaque_224
			self.fields['enempaque_225'].widget.attrs['value'] = emballage.objects.last().enempaque_225
			self.fields['enempaque_226'].widget.attrs['value'] = emballage.objects.last().enempaque_226
			self.fields['enempaque_227'].widget.attrs['value'] = emballage.objects.last().enempaque_227
			self.fields['enempaque_228'].widget.attrs['value'] = emballage.objects.last().enempaque_228
			self.fields['enempaque_229'].widget.attrs['value'] = emballage.objects.last().enempaque_229
			self.fields['entitulo_251'].widget.attrs['value'] = emballage.objects.last().entitulo_251
			self.fields['encuestionario'].widget.attrs['value'] = emballage.objects.last().encuestionario
			self.fields['ensubtitulo2501'].initial = emballage.objects.last().ensubtitulo2501
			self.fields['ensubtitulo2502'].initial = emballage.objects.last().ensubtitulo2502
			self.fields['ensubtitulo2503'].initial = emballage.objects.last().ensubtitulo2503
			self.fields['ensubtitulo2504'].initial = emballage.objects.last().ensubtitulo2504
			self.fields['ensubtitulo2505'].initial = emballage.objects.last().ensubtitulo2505
			self.fields['ensubtitulo2506'].initial = emballage.objects.last().ensubtitulo2506
			self.fields['ensubtitulo2507'].initial = emballage.objects.last().ensubtitulo2507
			self.fields['ensubtitulo2508'].initial = emballage.objects.last().ensubtitulo2508
			self.fields['ensubtitulo2509'].initial = emballage.objects.last().ensubtitulo2509
			self.fields['ensubtitulo2510'].initial = emballage.objects.last().ensubtitulo2510
			self.fields['ensubtitulo2511'].initial = emballage.objects.last().ensubtitulo2511
			self.fields['ensubtitulo2512'].initial = emballage.objects.last().ensubtitulo2512
			self.fields['ensubtitulo2513'].initial = emballage.objects.last().ensubtitulo2513
			self.fields['ensubtitulo2514'].initial = emballage.objects.last().ensubtitulo2514
			self.fields['ensubtitulo2515'].initial = emballage.objects.last().ensubtitulo2515
			self.fields['entext_secundario201'].initial = emballage.objects.last().entext_secundario201
			self.fields['entext_secundario211'].initial = emballage.objects.last().entext_secundario211
			self.fields['entext_secundario212'].initial = emballage.objects.last().entext_secundario212
			self.fields['entext_secundario2501'].initial = emballage.objects.last().entext_secundario2501
			self.fields['entext_secundario2502'].initial = emballage.objects.last().entext_secundario2502
			self.fields['entext_secundario2503'].initial = emballage.objects.last().entext_secundario2503
			self.fields['entext_secundario2504'].initial = emballage.objects.last().entext_secundario2504
			self.fields['entext_secundario2505'].initial = emballage.objects.last().entext_secundario2505
			self.fields['entext_secundario2506'].initial = emballage.objects.last().entext_secundario2506
			self.fields['entext_secundario2507'].initial = emballage.objects.last().entext_secundario2507
			self.fields['entext_secundario2508'].initial = emballage.objects.last().entext_secundario2508
			self.fields['entext_secundario2509'].initial = emballage.objects.last().entext_secundario2509
			self.fields['entext_secundario2510'].initial = emballage.objects.last().entext_secundario2510
			self.fields['entext_secundario2511'].initial = emballage.objects.last().entext_secundario2511
			self.fields['entext_secundario2512'].initial = emballage.objects.last().entext_secundario2512
			self.fields['entext_secundario2513'].initial = emballage.objects.last().entext_secundario2513
			self.fields['entext_secundario2514'].initial = emballage.objects.last().entext_secundario2514
			self.fields['entext_secundario2515'].initial = emballage.objects.last().entext_secundario2515

	class Meta:
		model = enemballage
		fields = '__all__'

		
		widgets = {
			'entext_secundario201' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 5,
				'class' : 'form-control',
				}),
			'enimagen201' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'enimagen202' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'enimagen203' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'enimagen211' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'enimagen213' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'enimagen215' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'enimagen221' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),

            'enflecha' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'enimagen231' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'enimagen232' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'enimagen233' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'enimagen234' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'enimagen235' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'enimagen236' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'enimagen237' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'enimagen238' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'enimagen241' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'enimagen242' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'enimagen243' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'enimagen244' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'enimagen245' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'enimagen246' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),

            'enempaque_img220' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'enempaque_img221' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'enempaque_img222' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'enempaque_img223' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'enempaque_img224' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'enempaque_img225' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'enempaque_img226' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'enempaque_img227' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'enempaque_img228' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'enempaque_img229' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),

			'enimagen2501' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2502' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2503' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2504' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2505' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2506' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2507' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2508' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2509' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2510' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2511' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2512' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2513' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2514' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2515' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2516' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2517' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2518' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2519' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2520' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2521' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2522' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2523' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2524' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2525' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2526' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2527' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2528' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2529' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2530' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2531' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2532' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2534' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2535' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2536' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2537' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2538' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2539' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2540' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2541' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2542' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2543' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2544' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen2545' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'enimagen251' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),

			 'entext_secundario211' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 5,
				'class' : 'form-control',
				}),
			 'entext_secundario212' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'entext_secundario213' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ensubtitulo2501' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'entext_secundario2501' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ensubtitulo2502' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'entext_secundario2502' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ensubtitulo2503' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'entext_secundario2503' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ensubtitulo2504' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'entext_secundario2504' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ensubtitulo2505' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'entext_secundario2505' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ensubtitulo2506' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'entext_secundario2506' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ensubtitulo2507' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'entext_secundario2507' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ensubtitulo2508' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'entext_secundario2508' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ensubtitulo2509' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'entext_secundario2509' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ensubtitulo2510' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'entext_secundario2510' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ensubtitulo2511' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'entext_secundario2511' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ensubtitulo2512' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'entext_secundario2512' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ensubtitulo2513' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'entext_secundario2513' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ensubtitulo2514' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'entext_secundario2514' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ensubtitulo2515' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'entext_secundario2515' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
	 			'class' : 'form-control',
				}),
			}

class enadd_form3(forms.ModelForm):
	def __init__(self, *args, **kwargs):
	    	super(enadd_form3, self).__init__(*args, **kwargs)
	        if entecnology.objects.last():
		        self.fields['entitulo_301'].widget.attrs['value'] = tecnology.objects.last().entitulo_301
	        	self.fields['entext_secundario301'].initial = tecnology.objects.last().entext_secundario301
	        	self.fields['enboton_301'].widget.attrs['value'] = tecnology.objects.last().enboton_301
	        	self.fields['ensubtitulo311'].initial = tecnology.objects.last().ensubtitulo311
	        	self.fields['entext_secundario311'].initial = tecnology.objects.last().entext_secundario311
	        	self.fields['entext_secundario312'].initial = tecnology.objects.last().entext_secundario312
	        	self.fields['entext_secundario313'].initial = tecnology.objects.last().entext_secundario313
	        	self.fields['entext_secundario314'].initial = tecnology.objects.last().entext_secundario314
	        	self.fields['entext_secundario315'].initial = tecnology.objects.last().entext_secundario315
	        	self.fields['entext_secundario316'].initial = tecnology.objects.last().entext_secundario316
	        	self.fields['entext_secundario317'].initial = tecnology.objects.last().entext_secundario317
	        	self.fields['entext_secundario318'].initial = tecnology.objects.last().entext_secundario318
	        	self.fields['entext_secundario319'].initial = tecnology.objects.last().entext_secundario319
	        	self.fields['entitulo_321'].widget.attrs['value'] = tecnology.objects.last().entitulo_321
	        	self.fields['entext_secundario321'].initial = tecnology.objects.last().entext_secundario321





	class Meta:
		model = entecnology
		fields = '__all__'

		widgets = {
		'enfondo1' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'enimagen301' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'enimagen302' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'enimagen311' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'enimagen312' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'enfondo2' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'enimagen13' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'enfondo3' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'entr_top' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'entr_bottom' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),

		'entext_secundario301': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'entext_secundario311': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'entext_secundario312': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'entext_secundario313': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'entext_secundario314': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'entext_secundario315': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'entext_secundario316': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'entext_secundario317': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'entext_secundario3018': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'entext_secundario319': forms.Textarea(attrs={
			'cols' : 35,
			'rows' : 1,
			'class' : 'form-control',
			}),
		'entext_secundario321': forms.Textarea(attrs={
			'cols' : 50,
			'rows' : 11,
			'class' : 'form-control',
			}),
		}
class enadd_form4(forms.ModelForm):
	class Meta:
		model = enclient
		fields = '__all__'
		widgets = {
		'enimagen401' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		}
class enadd_form5(forms.ModelForm):
	def __init__(self, *args, **kwargs):
	    	super(enadd_form5, self).__init__(*args, **kwargs)
	        if encontact.objects.last():
		        self.fields['entitulo_501'].widget.attrs['value'] = contact.objects.last().entitulo_501
		        self.fields['enpregunta51'].widget.attrs['placeholder'] = "Ingresa tu nombre"
		        self.fields['enpregunta52'].widget.attrs['placeholder'] = "Ingresa tu correo"
		        self.fields['enpregunta53'].widget.attrs['placeholder'] = "Ingresa tu número"
		        self.fields['enpregunta54'].widget.attrs['placeholder'] = "Escribe el mensaje"
		        self.fields['enboton_501'].widget.attrs['value'] = contact.objects.last().enboton_501


	class Meta:
		model = encontact
		fields = '__all__'

class enadd_form6(forms.ModelForm):
	def __init__(self, *args, **kwargs):
	    	super(enadd_form6, self).__init__(*args, **kwargs)
	        if enfooter.objects.last():
	        	self.fields['entitulo_601'].widget.attrs['value'] = footer.objects.last().entitulo_601
	class Meta:
		model = enfooter
		fields = '__all__'


# class UserRegisterForm(forms.ModelForm):

# 	class Meta:
# 		model = enUser
# 		fields = ('username', 'email', 'password')
# 		widgets = {
# 			'username' : forms.TextInput(attrs =
# 				{
# 				'class' : 'form-control',
# 				'placeholder' : 'Ingresa un nombre de usuario',
# 				'readonly':'readonly'
# 				}),
# 			'email' : forms.TextInput(attrs =
# 				{
# 				'type' : 'email',
# 				'class' : 'form-control',
# 				'placeholder' : 'Ingresa un email',
# 				'readonly':'readonly'
# 				}),
# 			'password' : forms.TextInput(attrs =
# 				{
# 				'type' : 'password',
# 				'class' : 'form-control',
# 				'placeholder' : 'Ingresa un password',
# 				'readonly':'readonly',
# 				})
# 		}

# class LoginForm(forms.Form):

# 	username = forms.CharField(max_length=30,
# 				widget = forms.TextInput(attrs = {
# 					'class' : 'form-control',
# 					'placeholder' : 'Ingresa un nombre de usuario',
# 					}))
# 	password = forms.CharField(max_length=30,
# 	 			widget = forms.TextInput(attrs = {
# 	 				'type' : 'password',
# 	 				'class' : 'form-control',
# 	 				'placeholder' : 'Ingresa un password',
# 	 				}))
