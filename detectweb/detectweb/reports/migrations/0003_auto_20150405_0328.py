# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import detectweb.reports.models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20150405_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='image_file',
            field=models.FileField(upload_to=detectweb.reports.models.uploaded_file_name),
            preserve_default=True,
        ),
    ]
