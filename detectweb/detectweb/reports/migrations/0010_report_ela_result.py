# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_report_uploaded_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='ela_result',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
