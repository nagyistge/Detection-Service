# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_report_is_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='score',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
    ]
