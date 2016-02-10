# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karate', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u044e', 'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='short_text',
            field=models.CharField(max_length=255, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435'),
        ),
    ]
