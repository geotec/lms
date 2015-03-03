# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='Provide some information about what students will learn.')),
                ('instructor', models.CharField(max_length=200)),
                ('duration', models.IntegerField(max_length=2, default=2, choices=[(2, '2 Weeks'), (8, '8 Weeks')])),
                ('course_art', models.FileField(upload_to='img')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
