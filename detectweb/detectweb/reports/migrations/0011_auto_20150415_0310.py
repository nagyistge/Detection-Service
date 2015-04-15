# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0010_report_ela_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='djca_score',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='djcu_score',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
    ]
