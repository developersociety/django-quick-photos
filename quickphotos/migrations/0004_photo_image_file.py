# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickphotos', '0003_counts'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image_file',
            field=models.FileField(upload_to='quickphotos/photo', blank=True),
        ),
    ]
