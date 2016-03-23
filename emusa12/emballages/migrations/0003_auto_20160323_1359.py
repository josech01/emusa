# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emballages', '0002_auto_20160323_1332'),
    ]

    operations = [
        migrations.DeleteModel(
            name='data_info',
        ),
        migrations.AddField(
            model_name='index',
            name='correo',
            field=models.EmailField(max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='index',
            name='idioma',
            field=models.CharField(default=b'espa\xc3\xb1ol', max_length=10, blank=True, choices=[(b'english', b'English'), (b'espa\xc3\xb1ol', b'Espa\xc3\xb1ol')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='index',
            name='logo',
            field=models.ImageField(upload_to=b'imgs', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='index',
            name='menu1',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='index',
            name='menu2',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='index',
            name='menu3',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='index',
            name='menu4',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='index',
            name='menu5',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='index',
            name='menu6',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='index',
            name='telf1',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='index',
            name='telf2',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='index',
            name='telf3',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
    ]
