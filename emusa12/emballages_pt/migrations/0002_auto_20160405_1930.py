# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emballages_pt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ptindex',
            name='pttelf1',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ptindex',
            name='pttelf2',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ptindex',
            name='pttelf3',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
