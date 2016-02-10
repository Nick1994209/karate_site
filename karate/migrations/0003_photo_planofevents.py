# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karate', '0002_auto_20151130_0258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('dc', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='PlanOfEvents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f')),
                ('name', models.CharField(max_length=155, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f')),
                ('sity', models.CharField(max_length=100, verbose_name='\u0413\u043e\u0440\u043e\u0434')),
                ('time', models.TimeField(verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430', blank=True)),
            ],
            options={
                'verbose_name': '\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f',
                'verbose_name_plural': '\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f',
            },
        ),
    ]
