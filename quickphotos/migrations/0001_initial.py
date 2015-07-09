# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('photo_id', models.CharField(unique=True, max_length=100)),
                ('user', models.CharField(db_index=True, max_length=30)),
                ('thumb', models.URLField()),
                ('thumb_width', models.PositiveIntegerField()),
                ('thumb_height', models.PositiveIntegerField()),
                ('created', models.DateTimeField(db_index=True)),
                ('caption', models.TextField()),
                ('link', models.URLField()),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
