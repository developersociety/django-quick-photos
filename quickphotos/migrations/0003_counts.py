# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickphotos', '0002_thumb_to_standard_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='comment_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='photo',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
