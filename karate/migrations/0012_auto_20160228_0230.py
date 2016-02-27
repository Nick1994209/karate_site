# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karate', '0011_auto_20160210_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='href',
            field=models.CharField(max_length=255, verbose_name='\u0423\u0440\u043b'),
        ),
    ]
