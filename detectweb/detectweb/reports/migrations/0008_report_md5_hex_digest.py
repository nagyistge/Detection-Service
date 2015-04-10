# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20150410_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='md5_hex_digest',
            field=models.CharField(default=None, unique=True, max_length=32),
            preserve_default=True,
        ),
    ]
