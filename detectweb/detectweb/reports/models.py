from __future__ import absolute_import

from django.db import models
from jsonfield import JSONField
import collections
import uuid
import json

def uploaded_file_name(instance, filename):
    return '/'.join(['uploaded_images', str(uuid.uuid4()), filename]);

# Create your models here.
class Report(models.Model):
    # Length 36 uuid.
    image_file = models.FileField(upload_to=uploaded_file_name)

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

    @property
    def file_path(self):
        return self.image_file.url

    @property
    def cm_matches_as_json(self):
        return json.dumps(self.cm_matches)
