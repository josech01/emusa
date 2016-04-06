# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emballages_en', '0002_auto_20160405_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='enindex',
            name='enimagen153',
            field=models.ImageField(upload_to=b'imgs', blank=True),
            preserve_default=True,
        ),
    ]
