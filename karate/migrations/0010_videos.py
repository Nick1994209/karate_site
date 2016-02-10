# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karate', '0009_auto_20151202_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True)),
                ('href', models.URLField(verbose_name='\u0423\u0440\u043b')),
                ('dc', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0410\u043b\u044c\u0431\u043e\u043c\u0430',
                'verbose_name_plural': '\u0410\u043b\u044c\u0431\u043e\u043c\u044b',
            },
        ),
    ]
