# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karate', '0006_auto_20151201_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='pf/', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='photoalbum',
            name='image',
            field=models.ImageField(upload_to='photo_album/', verbose_name='\u0424\u043e\u043d \u0430\u043b\u044c\u0431\u043e\u043c\u0430', blank=True),
        ),
    ]
