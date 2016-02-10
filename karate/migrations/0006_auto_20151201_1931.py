# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karate', '0005_auto_20151201_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='planofevents',
            name='additionally',
            field=models.CharField(max_length=255, verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f', blank=True),
        ),
        migrations.AddField(
            model_name='planofevents',
            name='place',
            field=models.CharField(max_length=100, verbose_name='\u041c\u0435\u0441\u0442\u043e \u043f\u0440\u043e\u0432\u0438\u0434\u0435\u043d\u0438\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='photoalbum',
            name='dc',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
    ]
