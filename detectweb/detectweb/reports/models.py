from __future__ import absolute_import

import os

from django.db import models
from jsonfield import JSONField
import collections
import json

UPLOADED_IMAGE_DIR = 'uploaded_images'

def uploaded_file_name(instance, filename):
    return '/'.join([UPLOADED_IMAGE_DIR,
                     instance.md5_hex_digest,
                     filename]);

# Create your models here.
class Report(models.Model):
    image_file = models.FileField(upload_to=uploaded_file_name)
    md5_hex_digest = models.CharField(max_length=32, unique=True, default=None)

    is_finished = models.BooleanField(default=False)
    score = models.FloatField(null=True)

    cm_matches = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict},
                           null=True)

    exif = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict}, null=True)
    has_camera_attrs = models.NullBooleanField()
    has_crop_resize = models.NullBooleanField()
    has_size_mismatch = models.NullBooleanField()
    has_software_manipulation = models.NullBooleanField()
    height = models.PositiveIntegerField(null=True)
    width = models.PositiveIntegerField(null=True)

    @classmethod
    def find_by_md5(cls, digest):
        results = cls.objects.filter(md5_hex_digest=digest)
        return results[0] if results else None

    @property
    def directory(self):
        return os.path.dirname(self.file_path)

    @property
    def file_path(self):
        return self.image_file.url

    @property
    def cm_matches_as_json(self):
        return json.dumps(self.cm_matches)
