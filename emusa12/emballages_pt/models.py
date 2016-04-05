#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
LANGUAGES_CHOICES = (
    ('es', 'Español'),
    ('en', 'English'),
    ('pt', 'Portuguese'),
)


class ptindex(models.Model):
	ptidioma = models.CharField(blank=True, max_length=2, choices=LANGUAGES_CHOICES, default='es')
	ptcorreo = models.EmailField(blank=True)
	pttelf1 = models.CharField(blank=True, max_length=50)
	pttelf2 = models.CharField(blank=True, max_length=50)
	pttelf3 = models.CharField(blank=True, max_length=50)
	ptlogo = models.ImageField(blank=True, upload_to = 'imgs')
	ptmenu1 = models.CharField(blank=True, max_length=40)
	ptmenu2 = models.CharField(blank=True, max_length=40)
	ptmenu3 = models.CharField(blank=True, max_length=40)
	ptmenu4 = models.CharField(blank=True, max_length=40)
	ptmenu5 = models.CharField(blank=True, max_length=40)
	ptmenu6 = models.CharField(blank=True, max_length=40)

	pttitulo_111 = models.CharField(blank=True, max_length=50)
	pttext_secundario111 = models.TextField(blank=True, max_length=1000)
	ptimagen111 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen112 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen113 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen114 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen115 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen116 = models.ImageField(blank=True, upload_to = 'imgs')

	pttitulo_121 = models.CharField(blank=True, max_length=50)
	pttext_secundario121 = models.TextField(blank=True, max_length=1000)
	ptimagen121 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen122 = models.ImageField(blank=True, upload_to = 'imgs')

	pttitulo_131 = models.CharField(blank=True, max_length=50)
        ptsubtitulo131 = models.CharField(blank=True, max_length=80)
	pttext_secundario131 = models.TextField(blank=True, max_length=1000)
	ptsubtitulo132 = models.CharField(blank=True, max_length=80)
	pttext_secundario132 = models.TextField(blank=True, max_length=1000)
        ptimagen131 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen132 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen133 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen134 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen135 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen136 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen137  = models.ImageField(blank=True, upload_to = 'imgs')

	pttitulo_141 = models.CharField(blank=True, max_length=50)
	pttext_secundario141 = models.TextField(blank=True, max_length=1000)
	ptimagen141 = models.ImageField(blank=True, upload_to = 'imgs')
        ptimagen142 = models.ImageField(blank=True, upload_to = 'imgs')

	pttitulo_151 = models.CharField(blank=True, max_length=50)
        ptimagen151 = models.ImageField(blank=True, upload_to = 'imgs')
	pttext_secundario151 = models.TextField(blank=True, max_length=1000)
	pttitulo_152 = models.CharField(blank=True, max_length=50)
        ptimagen152 = models.ImageField(blank=True, upload_to = 'imgs')
	pttext_secundario152 = models.TextField(blank=True, max_length=1000)
	ptimg_certificado= models.ImageField(blank=True, upload_to = 'imgs')


	def __unicode__(self):
		return u'%d - %s'%(self.id, self.titulo_111)

class ptemballage (models.Model):
	pttitulo_201 = models.CharField(blank=True, max_length=50)
        ptimagen201 = models.ImageField(blank=True, upload_to = 'imgs')
        pttext_secundario201 = models.TextField(blank=True, max_length=1000)
	ptboton_201 = models.CharField(blank=True, max_length=30)
	ptimagen202 = models.ImageField(blank=True, upload_to = 'imgs')
        ptimagen203 = models.ImageField(blank=True, upload_to = 'imgs')

	pttitulo_211 = models.CharField(blank=True, max_length=50)
	pttext_secundario211 = models.TextField(blank=True, max_length=1000)
	pttitulo_212 = models.CharField(blank=True, max_length=50)
	pttext_secundario212 = models.TextField(blank=True, max_length=1000)
	pttitulo_213 = models.CharField(blank=True, max_length=50)
	pttext_secundario213 = models.TextField(blank=True, max_length=1000)
	ptimagen211 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen212 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen213 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen214 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen215 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen216 = models.ImageField(blank=True, upload_to = 'imgs')

	pttitulo_221 = models.CharField(blank=True, max_length=50)
        ptempaque_220 = models.CharField(blank=True, max_length=50)
        ptimagen221 = models.ImageField(blank=True, upload_to = 'imgs')
	ptempaque_221 = models.CharField(blank=True, max_length=50)
	ptempaque_222 = models.CharField(blank=True, max_length=50)
	ptempaque_223 = models.CharField(blank=True, max_length=50)
	ptempaque_224 = models.CharField(blank=True, max_length=50)
	ptempaque_225 = models.CharField(blank=True, max_length=50)
	ptempaque_226 = models.CharField(blank=True, max_length=50)
	ptempaque_227 = models.CharField(blank=True, max_length=50)
	ptempaque_228 = models.CharField(blank=True, max_length=50)
	ptempaque_229 = models.CharField(blank=True, max_length=50)
	ptempaque_img220 = models.ImageField(blank=True, upload_to = 'imgs')
	ptempaque_img221 = models.ImageField(blank=True, upload_to = 'imgs')
	ptempaque_img222 = models.ImageField(blank=True, upload_to = 'imgs')
	ptempaque_img223 = models.ImageField(blank=True, upload_to = 'imgs')
	ptempaque_img224 = models.ImageField(blank=True, upload_to = 'imgs')
	ptempaque_img225 = models.ImageField(blank=True, upload_to = 'imgs')
	ptempaque_img226 = models.ImageField(blank=True, upload_to = 'imgs')
	ptempaque_img227 = models.ImageField(blank=True, upload_to = 'imgs')
	ptempaque_img228 = models.ImageField(blank=True, upload_to = 'imgs')
	ptempaque_img229 = models.ImageField(blank=True, upload_to = 'imgs')

        ptflecha = models.ImageField(blank=True, upload_to = 'imgs')
        ptimagen231 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen232 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen233 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen234 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen235 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen236 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen237 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen238 = models.ImageField(blank=True, upload_to = 'imgs')
	pttitulo_241 = models.CharField(blank=True, max_length=50)
        ptimagen241 = models.ImageField(blank=True, upload_to = 'imgs')
        ptimagen242 = models.ImageField(blank=True, upload_to = 'imgs')
	pttitulo_242 = models.CharField(blank=True, max_length=50)
        ptimagen243 = models.ImageField(blank=True, upload_to = 'imgs')
        ptimagen244 = models.ImageField(blank=True, upload_to = 'imgs')
        pttitulo_243 = models.CharField(blank=True, max_length=50)
        ptimagen245 = models.ImageField(blank=True, upload_to = 'imgs')
        ptimagen246 = models.ImageField(blank=True, upload_to = 'imgs')


	pttitulo_251 = models.CharField(blank=True, max_length=50)
	ptsubtitulo2501 = models.CharField(blank=True, max_length=80)
	ptimagen2501 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2502 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2503 = models.ImageField(blank=True, upload_to = 'imgs')
	pttext_secundario2501 = models.TextField(blank=True, max_length=1000)
	ptsubtitulo2502 = models.CharField(blank=True, max_length=80)
	ptimagen2504 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2505 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2506 = models.ImageField(blank=True, upload_to = 'imgs')
	pttext_secundario2502 = models.TextField(blank=True, max_length=1000)
	ptsubtitulo2503 = models.CharField(blank=True, max_length=80)
	ptimagen2507 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2508 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2509 = models.ImageField(blank=True, upload_to = 'imgs')
	pttext_secundario2503 = models.TextField(blank=True, max_length=1000)
	ptsubtitulo2504 = models.CharField(blank=True, max_length=80)
	ptimagen2510 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2511 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2512 = models.ImageField(blank=True, upload_to = 'imgs')
	pttext_secundario2504 = models.TextField(blank=True, max_length=1000)
	ptsubtitulo2505 = models.CharField(blank=True, max_length=80)
	ptimagen2513 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2514 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2515 = models.ImageField(blank=True, upload_to = 'imgs')
	pttext_secundario2505 = models.TextField(blank=True, max_length=1000)
	ptsubtitulo2506 = models.CharField(blank=True, max_length=80)
	ptimagen2516 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2517 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2518 = models.ImageField(blank=True, upload_to = 'imgs')
	pttext_secundario2506 = models.TextField(blank=True, max_length=1000)
	ptsubtitulo2507 = models.CharField(blank=True, max_length=80)
	ptimagen2519 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2520 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2521 = models.ImageField(blank=True, upload_to = 'imgs')
	pttext_secundario2507 = models.TextField(blank=True, max_length=1000)
	ptsubtitulo2508 = models.CharField(blank=True, max_length=80)
	ptimagen2522 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2523 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2524 = models.ImageField(blank=True, upload_to = 'imgs')
	pttext_secundario2508 = models.TextField(blank=True, max_length=1000)
	ptsubtitulo2509 = models.CharField(blank=True, max_length=80)
	ptimagen2525 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2526 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2527 = models.ImageField(blank=True, upload_to = 'imgs')
	pttext_secundario2509 = models.TextField(blank=True, max_length=1000)
	ptsubtitulo2510 = models.CharField(blank=True, max_length=80)
	ptimagen2528 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2529 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2530 = models.ImageField(blank=True, upload_to = 'imgs')
	pttext_secundario2510 = models.TextField(blank=True, max_length=1000)
	ptsubtitulo2511 = models.CharField(blank=True, max_length=80)
	ptimagen2531 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2532 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2533 = models.ImageField(blank=True, upload_to = 'imgs')
	pttext_secundario2511 = models.TextField(blank=True, max_length=1000)
	ptsubtitulo2512 = models.CharField(blank=True, max_length=80)
	ptimagen2534 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2535 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2536 = models.ImageField(blank=True, upload_to = 'imgs')
	pttext_secundario2512 = models.TextField(blank=True, max_length=1000)
	ptsubtitulo2513 = models.CharField(blank=True, max_length=80)
	ptimagen2537 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2538 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2539 = models.ImageField(blank=True, upload_to = 'imgs')
	pttext_secundario2513 = models.TextField(blank=True, max_length=1000)
	ptsubtitulo2514 = models.CharField(blank=True, max_length=80)
	ptimagen2540 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2541 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2542 = models.ImageField(blank=True, upload_to = 'imgs')
	pttext_secundario2514 = models.TextField(blank=True, max_length=1000)
	ptsubtitulo2515 = models.CharField(blank=True, max_length=80)
	ptimagen2543 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2544 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen2545 = models.ImageField(blank=True, upload_to = 'imgs')
	pttext_secundario2515 = models.TextField(blank=True, max_length=1000)

	ptboton_251 = models.CharField(blank=True, max_length=20)
	ptboton_252 = models.CharField(blank=True, max_length=30)
        ptimagen251 = models.ImageField(blank=True, upload_to = 'imgs')
        ptcuestionario = models.CharField(blank=True, max_length=50)
    	ptpregunta21 = models.CharField(blank=True, max_length=50)
    	ptpregunta22 = models.EmailField(blank=True, max_length=50)
    	ptpregunta23 = models.CharField(blank=True, max_length=50)
    	ptpregunta24 = models.CharField(blank=True, max_length=50)
    	ptboton_253 = models.CharField(blank=True, max_length=50)

	def __unicode__(self):
		return u'%d - %s'%(self.id, self.titulo_201)

class pttecnology(models.Model):
	pttitulo_301 = models.CharField(blank=True, max_length=50)
	pttext_secundario301 = models.TextField(blank=True, max_length=1000)
	ptboton_301 = models.CharField(blank=True, max_length=30)
        ptfondo1 = models.ImageField(blank=True, upload_to = 'imgs')
        ptimagen301 = models.ImageField(blank=True, upload_to = 'imgs')
    	ptimagen302 = models.ImageField(blank=True, upload_to = 'imgs')

	ptsubtitulo311 = models.CharField(blank=True, max_length=80)
	pttext_secundario311 = models.TextField(blank=True, max_length=1000)
	pttext_secundario312 = models.TextField(blank=True, max_length=1000)
	pttext_secundario313 = models.TextField(blank=True, max_length=1000)
	pttext_secundario314 = models.TextField(blank=True, max_length=1000)
	ptimagen311 = models.ImageField(blank=True, upload_to = 'imgs')
	ptimagen312 = models.ImageField(blank=True, upload_to = 'imgs')
        ptfondo2 = models.ImageField(blank=True, upload_to = 'imgs')
        pttext_secundario315 = models.TextField(blank=True, max_length=1000)
    	pttext_secundario316 = models.TextField(blank=True, max_length=1000)
    	pttext_secundario317 = models.TextField(blank=True, max_length=1000)
    	pttext_secundario318 = models.TextField(blank=True, max_length=1000)
    	pttext_secundario319 = models.TextField(blank=True, max_length=1000)
    	ptimagen313 = models.ImageField(blank=True, upload_to = 'imgs')
        ptfondo3 = models.ImageField(blank=True, upload_to = 'imgs')
        pttr_top = models.ImageField(blank=True, upload_to = 'imgs')
    	pttitulo_321 = models.CharField(blank=True, max_length=50)
        pttext_secundario321 = models.TextField(blank=True, max_length=1000)
    	pttr_bottom = models.ImageField(blank=True, upload_to = 'imgs')

	def __unicode__(self):
		return u'%d - %s'%(self.id, self.titulo_301)

class ptclient(models.Model):
	pttitulo_401 = models.CharField(blank=True, max_length=50)
	ptimagen401 = models.ImageField(blank=True, upload_to = 'imgs')

	def __unicode__(self):
		return u'%d - %s'%(self.id, self.titulo_401)

class ptcontact(models.Model):
	pttitulo_501 = models.CharField(blank=True, max_length=50)
	ptpregunta51 = models.CharField(blank=True, max_length=50)
	ptpregunta52 = models.EmailField(blank=True, max_length=50)
	ptpregunta53 = models.CharField(blank=True, max_length=50)
	ptpregunta54 = models.CharField(blank=True, max_length=50)
	ptboton_501 = models.CharField(blank=True, max_length=50)

	def __unicode__(self):
		return u'%d - %s'%(self.id, self.titulo_501)

class ptfooter(models.Model):
	pttitulo_601 = models.CharField(blank=True,  max_length=50)

	def __unicode__(self):
		return u'%d - %s'%(self.id, self.titulo_601)
