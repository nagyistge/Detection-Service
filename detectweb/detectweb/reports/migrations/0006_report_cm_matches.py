# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_report_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='cm_matches',
            field=jsonfield.fields.JSONField(null=True),
            preserve_default=True,
        ),
    ]
