"""emusa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin

from emballages import views as emba_views
from emballages_en import views as emba_views_en
from emballages_pt import views as emba_views_pt
from django.conf import settings
admin.autodiscover()


urlpatterns = [
    url(r'^form_en.html', emba_views_en.enadd_new_form),
    url(r'^form_pt.html', emba_views_pt.ptadd_new_form),
    url(r'^form.html', emba_views.add_new_form),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^clientes.html', emba_views.clientes),
    url(r'^contactanos.html', emba_views.contactanos),
    url(r'^empacate.html', emba_views.empacate),
    url(r'^galeria.html', emba_views.galeria),
    url(r'^galeria_en.html', emba_views_en.engaleria),
    url(r'^galeria_pt.html', emba_views_pt.ptgaleria),
    url(r'^tecnologia.html', emba_views.tecnologia),
    url(r'^index.html', emba_views.index),
    url(r'^clientes_en.html', emba_views_en.enclientes),
    url(r'^contactanos_en.html', emba_views_en.encontactanos),
    url(r'^empacate_en.html', emba_views_en.enempacate),
    url(r'^tecnologia_en.html', emba_views_en.entecnologia),
    url(r'^index_en.html', emba_views_en.enindex),
    url(r'^clientes_pt.html', emba_views_pt.ptclientes),
    url(r'^contactanos_pt.html', emba_views_pt.ptcontactanos),
    url(r'^empacate_pt.html', emba_views_pt.ptempacate),
    url(r'^tecnologia_pt.html', emba_views_pt.pttecnologia),
    url(r'^index_pt.html', emba_views_pt.ptindex),
    url(r'^$', emba_views.index),
    url(r'^login/$', emba_views.userlogin, name="login"),
    # url(r"^logout/$", "django.contrib.auth.views.logout_then_login",
    # name="logout"),
    url(r'^salir/$', emba_views.LogOut, name = 'logout'),
    
]
if settings.DEBUG:
    urlpatterns += patterns("",
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,}
        ),
    )