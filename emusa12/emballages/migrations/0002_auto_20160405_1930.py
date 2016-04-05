# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emballages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='idioma',
            field=models.CharField(default=b'es', max_length=2, blank=True, choices=[(b'es', b'Espa\xc3\xb1ol'), (b'en', b'English'), (b'pt', b'Portugues')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='index',
            name='telf1',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='index',
            name='telf2',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='index',
            name='telf3',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
