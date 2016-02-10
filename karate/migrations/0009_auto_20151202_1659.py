# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karate', '0008_auto_20151202_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='album/photo/', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430'),
        ),
    ]
