# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emballages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_info',
            name='idioma',
            field=models.CharField(default=b'espa\xc3\xb1ol', max_length=10, blank=True, choices=[(b'english', b'English'), (b'espa\xc3\xb1ol', b'Espa\xc3\xb1ol')]),
            preserve_default=True,
        ),
    ]
