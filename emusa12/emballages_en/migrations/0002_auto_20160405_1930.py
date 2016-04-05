# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emballages_en', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enindex',
            name='enidioma',
            field=models.CharField(default=b'es', max_length=2, blank=True, choices=[(b'es', b'Espa\xc3\xb1ol'), (b'en', b'English'), (b'pt', b'Portuguese')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='enindex',
            name='entelf1',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='enindex',
            name='entelf2',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='enindex',
            name='entelf3',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
