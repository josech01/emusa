# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emballages', '0003_auto_20160323_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='idioma',
            field=models.CharField(default=b'es', max_length=2, blank=True, choices=[(b'es', b'Espa\xc3\xb1ol'), (b'en', b'English')]),
            preserve_default=True,
        ),
    ]
