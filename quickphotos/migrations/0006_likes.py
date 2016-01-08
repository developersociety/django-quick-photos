# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickphotos', '0005_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('user', models.CharField(max_length=30, db_index=True)),
                ('photo', models.ForeignKey(to='quickphotos.Photo')),
            ],
            options={
                'ordering': ('-photo',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('user', 'photo')]),
        ),
    ]
