# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_report_cm_matches'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='exif',
            field=jsonfield.fields.JSONField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='has_camera_attrs',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='has_crop_resize',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='has_size_mismatch',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='has_software_manipulation',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='height',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='width',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
    ]
