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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Name it something good', max_length=200)),
                ('description', models.TextField()),
                ('instructor', models.CharField(default='Django Guru', max_length=200)),
                ('duration', models.IntegerField(default=2, choices=[(2, '2 Weeks'), (8, '8 Weeks')], max_length=2)),
                ('course_art', models.FileField(upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
