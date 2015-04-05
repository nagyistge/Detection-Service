# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20150405_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='is_finished',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
