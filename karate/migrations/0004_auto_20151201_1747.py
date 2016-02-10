# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karate', '0003_photo_planofevents'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoAlbum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0430\u043b\u044c\u0431\u043e\u043c\u0430')),
                ('image', models.ImageField(upload_to='photo_albom', verbose_name='\u0424\u043e\u043d \u0430\u043b\u044c\u0431\u043e\u043c\u0430')),
                ('dc', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e \u0430\u043b\u044c\u0431\u043e\u043c',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e \u0430\u043b\u044c\u0431\u043e\u043c\u044b',
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=255, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='dc',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='photos', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430'),
        ),
    ]
