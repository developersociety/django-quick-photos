# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickphotos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='thumb',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='thumb_height',
            new_name='image_height',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='thumb_width',
            new_name='image_width',
        ),
    ]
