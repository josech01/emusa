# -*- coding: utf-8 -*-

from django import forms
from .models import ptindex, ptemballage, pttecnology, ptclient, ptcontact, ptfooter
from django.contrib.auth.models import User


class ptadd_form1(forms.ModelForm):

 	def __init__(self, *args, **kwargs):
        	super(ptadd_form1, self).__init__(*args, **kwargs)
	        if ptindex.objects.last():
	        	self.fields['ptcorreo'].widget.attrs['value'] = ptindex.objects.last().ptcorreo
	        	self.fields['pttelf1'].widget.attrs['value'] = ptindex.objects.last().pttelf1
	        	self.fields['pttelf2'].widget.attrs['value'] = ptindex.objects.last().pttelf2
	        	self.fields['pttelf3'].widget.attrs['value'] = ptindex.objects.last().pttelf3
	        	self.fields['ptmenu1'].widget.attrs['value'] = ptindex.objects.last().ptmenu1
		        self.fields['ptmenu2'].widget.attrs['value'] = ptindex.objects.last().ptmenu2
		        self.fields['ptmenu3'].widget.attrs['value'] = ptindex.objects.last().ptmenu3
		        self.fields['ptmenu4'].widget.attrs['value'] = ptindex.objects.last().ptmenu4
		        self.fields['ptmenu5'].widget.attrs['value'] = ptindex.objects.last().ptmenu5
		        self.fields['ptmenu6'].widget.attrs['value'] = ptindex.objects.last().ptmenu6
	        	self.fields['pttitulo_111'].widget.attrs['value'] = ptindex.objects.last().pttitulo_111
	        	self.fields['pttext_secundario111'].initial = ptindex.objects.last().pttext_secundario111
	        	self.fields['pttitulo_121'].widget.attrs['value'] = ptindex.objects.last().pttitulo_121
	        	self.fields['pttext_secundario121'].initial = ptindex.objects.last().pttext_secundario121
	        	#self.fields['pttitulo_131'].widget.attrs['value'] = ptindex.objects.last().pttitulo_131
	        	self.fields['ptsubtitulo131'].widget.attrs['value'] = ptindex.objects.last().ptsubtitulo131
	        	self.fields['pttext_secundario131'].initial = ptindex.objects.last().pttext_secundario131
	        	self.fields['ptsubtitulo132'].widget.attrs['value'] = ptindex.objects.last().ptsubtitulo132
	        	self.fields['pttext_secundario132'].initial = ptindex.objects.last().pttext_secundario132
	        	self.fields['pttitulo_151'].widget.attrs['value'] = ptindex.objects.last().pttitulo_151
	        	self.fields['pttext_secundario151'].initial = ptindex.objects.last().pttext_secundario151
	        	self.fields['pttext_secundario152'].initial = ptindex.objects.last().pttext_secundario152


	class Meta:
		model = ptindex
		fields = '__all__'
		
		help_texts = {
        }
		widgets = {
			 'ptlogo' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen111' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen112' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen113' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen114' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen115' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen116' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen121' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen122' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen131' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen132' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen133' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen134' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen135' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen136' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen137' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen141' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen142' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen151' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen152' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimagen153' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			 'ptimg_certificado' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),

			 'pttitulo_111' : forms.TextInput(attrs =
				{
				'value' : 'john',
				'class' : 'form-control',
				# 'placeholder' :
				}),
			 'pttext_secundario111' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 4,
				# 'size' : 100,
				'class' : 'form-control',
				}),
			 'pttext_secundario121' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 5,
				'class' : 'form-control',
				}),
			 'pttext_secundario131' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 3,
				'class' : 'form-control',
				}),
			 'pttext_secundario132' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 5,
				'class' : 'form-control',
				}),
			 'pttext_secundario141' : forms.Textarea(attrs =
				{
				'cols' : 30,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'pttext_secundario151' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 11,
				'class' : 'form-control',
				}),
			 'pttext_secundario152' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 3,
				'class' : 'form-control',
				}),
		}

class ptadd_form2(forms.ModelForm):
	def __init__(self, *args, **kwargs):
        	super(ptadd_form2, self).__init__(*args, **kwargs)
	        if ptemballage.objects.last():
	        	self.fields['pttitulo_201'].widget.attrs['value'] = ptemballage.objects.last().pttitulo_201
	        	self.fields['pttext_secundario201'].initial = ptemballage.objects.last().pttext_secundario201
	        	self.fields['ptboton_201'].widget.attrs['value'] = ptemballage.objects.last().ptboton_201
    			self.fields['ptboton_251'].widget.attrs['value'] = ptemballage.objects.last().ptboton_251
		    	self.fields['ptboton_252'].widget.attrs['value'] = ptemballage.objects.last().ptboton_252
	    		self.fields['ptboton_253'].widget.attrs['value'] = ptemballage.objects.last().ptboton_253
			self.fields['pttitulo_211'].widget.attrs['value'] = ptemballage.objects.last().pttitulo_211
			self.fields['pttitulo_212'].widget.attrs['value'] = ptemballage.objects.last().pttitulo_212
			self.fields['pttitulo_213'].widget.attrs['value'] = ptemballage.objects.last().pttitulo_213
			self.fields['ptempaque_220'].widget.attrs['value'] = ptemballage.objects.last().ptempaque_220
			self.fields['ptempaque_221'].widget.attrs['value'] = ptemballage.objects.last().ptempaque_221
			self.fields['ptempaque_222'].widget.attrs['value'] = ptemballage.objects.last().ptempaque_222
			self.fields['ptempaque_223'].widget.attrs['value'] = ptemballage.objects.last().ptempaque_223
			self.fields['ptempaque_224'].widget.attrs['value'] = ptemballage.objects.last().ptempaque_224
			self.fields['ptempaque_225'].widget.attrs['value'] = ptemballage.objects.last().ptempaque_225
			self.fields['ptempaque_226'].widget.attrs['value'] = ptemballage.objects.last().ptempaque_226
			self.fields['ptempaque_227'].widget.attrs['value'] = ptemballage.objects.last().ptempaque_227
			self.fields['ptempaque_228'].widget.attrs['value'] = ptemballage.objects.last().ptempaque_228
			self.fields['ptempaque_229'].widget.attrs['value'] = ptemballage.objects.last().ptempaque_229
			self.fields['pttitulo_251'].widget.attrs['value'] = ptemballage.objects.last().pttitulo_251
			self.fields['ptcuestionario'].widget.attrs['value'] = ptemballage.objects.last().ptcuestionario
			self.fields['ptsubtitulo2501'].initial = ptemballage.objects.last().ptsubtitulo2501
			self.fields['ptsubtitulo2502'].initial = ptemballage.objects.last().ptsubtitulo2502
			self.fields['ptsubtitulo2503'].initial = ptemballage.objects.last().ptsubtitulo2503
			self.fields['ptsubtitulo2504'].initial = ptemballage.objects.last().ptsubtitulo2504
			self.fields['ptsubtitulo2505'].initial = ptemballage.objects.last().ptsubtitulo2505
			self.fields['ptsubtitulo2506'].initial = ptemballage.objects.last().ptsubtitulo2506
			self.fields['ptsubtitulo2507'].initial = ptemballage.objects.last().ptsubtitulo2507
			self.fields['ptsubtitulo2508'].initial = ptemballage.objects.last().ptsubtitulo2508
			self.fields['ptsubtitulo2509'].initial = ptemballage.objects.last().ptsubtitulo2509
			self.fields['ptsubtitulo2510'].initial = ptemballage.objects.last().ptsubtitulo2510
			self.fields['ptsubtitulo2511'].initial = ptemballage.objects.last().ptsubtitulo2511
			self.fields['ptsubtitulo2512'].initial = ptemballage.objects.last().ptsubtitulo2512
			self.fields['ptsubtitulo2513'].initial = ptemballage.objects.last().ptsubtitulo2513
			self.fields['ptsubtitulo2514'].initial = ptemballage.objects.last().ptsubtitulo2514
			self.fields['ptsubtitulo2515'].initial = ptemballage.objects.last().ptsubtitulo2515
			self.fields['pttext_secundario201'].initial = ptemballage.objects.last().pttext_secundario201
			self.fields['pttext_secundario211'].initial = ptemballage.objects.last().pttext_secundario211
			self.fields['pttext_secundario212'].initial = ptemballage.objects.last().pttext_secundario212
			self.fields['pttext_secundario2501'].initial = ptemballage.objects.last().pttext_secundario2501
			self.fields['pttext_secundario2502'].initial = ptemballage.objects.last().pttext_secundario2502
			self.fields['pttext_secundario2503'].initial = ptemballage.objects.last().pttext_secundario2503
			self.fields['pttext_secundario2504'].initial = ptemballage.objects.last().pttext_secundario2504
			self.fields['pttext_secundario2505'].initial = ptemballage.objects.last().pttext_secundario2505
			self.fields['pttext_secundario2506'].initial = ptemballage.objects.last().pttext_secundario2506
			self.fields['pttext_secundario2507'].initial = ptemballage.objects.last().pttext_secundario2507
			self.fields['pttext_secundario2508'].initial = ptemballage.objects.last().pttext_secundario2508
			self.fields['pttext_secundario2509'].initial = ptemballage.objects.last().pttext_secundario2509
			self.fields['pttext_secundario2510'].initial = ptemballage.objects.last().pttext_secundario2510
			self.fields['pttext_secundario2511'].initial = ptemballage.objects.last().pttext_secundario2511
			self.fields['pttext_secundario2512'].initial = ptemballage.objects.last().pttext_secundario2512
			self.fields['pttext_secundario2513'].initial = ptemballage.objects.last().pttext_secundario2513
			self.fields['pttext_secundario2514'].initial = ptemballage.objects.last().pttext_secundario2514
			self.fields['pttext_secundario2515'].initial = ptemballage.objects.last().pttext_secundario2515

	class Meta:
		model = ptemballage
		fields = '__all__'

		widgets = {
			'pttext_secundario201' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 5,
				'class' : 'form-control',
				}),
			'ptimagen201' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'ptimagen202' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'ptimagen203' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'ptimagen211' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'ptimagen213' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'ptimagen215' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'ptimagen221' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),

            'ptflecha' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'ptimagen231' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'ptimagen232' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'ptimagen233' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'ptimagen234' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'ptimagen235' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'ptimagen236' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'ptimagen237' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'ptimagen238' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'ptimagen241' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'ptimagen242' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'ptimagen243' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'ptimagen244' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'ptimagen245' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
            'ptimagen246' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),

            'ptempaque_img220' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'ptempaque_img221' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'ptempaque_img222' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'ptempaque_img223' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'ptempaque_img224' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'ptempaque_img225' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'ptempaque_img226' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'ptempaque_img227' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'ptempaque_img228' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),
			'ptempaque_img229' : forms.ClearableFileInput(attrs = {'class' : 'form-control', }),

			'ptimagen2501' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2502' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2503' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2504' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2505' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2506' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2507' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2508' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2509' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2510' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2511' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2512' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2513' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2514' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2515' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2516' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2517' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2518' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2519' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2520' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2521' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2522' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2523' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2524' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2525' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2526' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2527' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2528' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2529' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2530' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2531' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2532' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2534' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2535' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2536' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2537' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2538' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2539' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2540' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2541' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2542' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2543' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2544' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen2545' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
			'ptimagen251' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),

			 'pttext_secundario211' : forms.Textarea(attrs =
				{
				'cols' : 50,
				'rows' : 5,
				'class' : 'form-control',
				}),
			 'pttext_secundario212' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'pttext_secundario213' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ptsubtitulo2501' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'pttext_secundario2501' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ptsubtitulo2502' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'pttext_secundario2502' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ptsubtitulo2503' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'pttext_secundario2503' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ptsubtitulo2504' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'pttext_secundario2504' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ptsubtitulo2505' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'pttext_secundario2505' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ptsubtitulo2506' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'pttext_secundario2506' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ptsubtitulo2507' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'pttext_secundario2507' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ptsubtitulo2508' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'pttext_secundario2508' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ptsubtitulo2509' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'pttext_secundario2509' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ptsubtitulo2510' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'pttext_secundario2510' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ptsubtitulo2511' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'pttext_secundario2511' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ptsubtitulo2512' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'pttext_secundario2512' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ptsubtitulo2513' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'pttext_secundario2513' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ptsubtitulo2514' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'pttext_secundario2514' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
				'class' : 'form-control',
				}),
			 'ptsubtitulo2515' : forms.Textarea(attrs =
				{
				'cols' : 20,
				'rows' : 1,
				'class' : 'form-control',
				}),

			 'pttext_secundario2515' : forms.Textarea(attrs =
				{
				'cols' : 40,
				'rows' : 2,
	 			'class' : 'form-control',
				}),
			}

class ptadd_form3(forms.ModelForm):
	def __init__(self, *args, **kwargs):
	    	super(ptadd_form3, self).__init__(*args, **kwargs)
	        if pttecnology.objects.last():
		        self.fields['pttitulo_301'].widget.attrs['value'] = pttecnology.objects.last().pttitulo_301
	        	self.fields['pttext_secundario301'].initial = pttecnology.objects.last().pttext_secundario301
	        	self.fields['ptboton_301'].widget.attrs['value'] = pttecnology.objects.last().ptboton_301
	        	self.fields['ptsubtitulo311'].initial = pttecnology.objects.last().ptsubtitulo311
	        	self.fields['pttext_secundario311'].initial = pttecnology.objects.last().pttext_secundario311
	        	self.fields['pttext_secundario312'].initial = pttecnology.objects.last().pttext_secundario312
	        	self.fields['pttext_secundario313'].initial = pttecnology.objects.last().pttext_secundario313
	        	self.fields['pttext_secundario314'].initial = pttecnology.objects.last().pttext_secundario314
	        	self.fields['pttext_secundario315'].initial = pttecnology.objects.last().pttext_secundario315
	        	self.fields['pttext_secundario316'].initial = pttecnology.objects.last().pttext_secundario316
	        	self.fields['pttext_secundario317'].initial = pttecnology.objects.last().pttext_secundario317
	        	self.fields['pttext_secundario318'].initial = pttecnology.objects.last().pttext_secundario318
	        	self.fields['pttext_secundario319'].initial = pttecnology.objects.last().pttext_secundario319
	        	self.fields['pttitulo_321'].widget.attrs['value'] = pttecnology.objects.last().pttitulo_321
	        	self.fields['pttext_secundario321'].initial = pttecnology.objects.last().pttext_secundario321

	class Meta:
		model = pttecnology
		fields = '__all__'

		widgets = {
		'ptfondo1' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'ptimagen301' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'ptimagen302' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'ptimagen311' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'ptimagen312' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'ptfondo2' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'ptimagen313' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'ptfondo3' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'pttr_top' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		'pttr_bottom' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),

		'pttext_secundario301': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'pttext_secundario311': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'pttext_secundario312': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'pttext_secundario313': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'pttext_secundario314': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'pttext_secundario315': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'pttext_secundario316': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'pttext_secundario317': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'pttext_secundario3018': forms.Textarea(attrs={
			'cols' : 40,
			'rows' : 2,
			'class' : 'form-control',
			}),
		'pttext_secundario319': forms.Textarea(attrs={
			'cols' : 35,
			'rows' : 1,
			'class' : 'form-control',
			}),
		'pttext_secundario321': forms.Textarea(attrs={
			'cols' : 50,
			'rows' : 11,
			'class' : 'form-control',
			}),
		}
class ptadd_form4(forms.ModelForm):
	class Meta:
		model = ptclient
		fields = '__all__'
		widgets = {
		'ptimagen401' : forms.ClearableFileInput(attrs = {'class' : 'form-control',}),
		}
class ptadd_form5(forms.ModelForm):
	def __init__(self, *args, **kwargs):
	    	super(ptadd_form5, self).__init__(*args, **kwargs)
	        if ptcontact.objects.last():
		        self.fields['pttitulo_501'].widget.attrs['value'] = ptcontact.objects.last().pttitulo_501
		        self.fields['ptpregunta51'].widget.attrs['placeholder'] = "Ingresa tu nombre"
		        self.fields['ptpregunta52'].widget.attrs['placeholder'] = "Ingresa tu correo"
		        self.fields['ptpregunta53'].widget.attrs['placeholder'] = "Ingresa tu número"
		        self.fields['ptpregunta54'].widget.attrs['placeholder'] = "Escribe el mensaje"
		        self.fields['ptboton_501'].widget.attrs['value'] = ptcontact.objects.last().ptboton_501


	class Meta:
		model = ptcontact
		fields = '__all__'

class ptadd_form6(forms.ModelForm):
	def __init__(self, *args, **kwargs):
	    	super(ptadd_form6, self).__init__(*args, **kwargs)
	        if ptfooter.objects.last():
	        	self.fields['pttitulo_601'].widget.attrs['value'] = ptfooter.objects.last().pttitulo_601
	class Meta:
		model = ptfooter
		fields = '__all__'

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
