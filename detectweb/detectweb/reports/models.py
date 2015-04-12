# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os

from django.conf import settings
from django.db import models

from jsonfield import JSONField
import collections
import json

from imforensics.ela import  ELAClassifier

def uploaded_file_name(instance, filename):
    return '/'.join([
         instance.md5_hex_digest,
         filename,
    ])

# Create your models here.
class Report(models.Model):
    image_file = models.FileField(upload_to=uploaded_file_name)
    md5_hex_digest = models.CharField(max_length=32, unique=True, default=None)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)

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

    ela_result = models.IntegerField(null=True)

    ELA_IMG_SUFFIX = '.ela.png'
    DJCA_IMG_SUFFIX = '.djca.png'
    DJCU_IMG_SUFFIX = '.djcu.png'

    @classmethod
    def find_by_md5(cls, digest):
        results = cls.objects.filter(md5_hex_digest=digest)
        return results[0] if results else None

    @property
    def image_name(self):
        """Return the image name."""
        return os.path.split(self.image_file.name)[-1]

    @property
    def directory(self):
        return os.path.dirname(self.file_path)

    @property
    def base_path(self):
        """Returns the base path of the images for this report."""
        return os.path.join(settings.MEDIA_URL, self.md5_hex_digest)

    @property
    def file_path(self):
        """Return the file path to the image on disk."""
        return self.image_file.path

    @property
    def is_ela_sure_auth(self):
        return self.ela_result == ELAClassifier.SURE_AUTH_FLAG

    @property
    def is_ela_maybe_auth(self):
        return self.ela_result == ELAClassifier.NOT_SURE_AUTH_FLAG

    @property
    def is_ela_maybe_fake(self):
        return self.ela_result == ELAClassifier.NOT_SURE_FAKE_FLAG

    @property
    def is_ela_sure_fake(self):
        return self.ela_result == ELAClassifier.SURE_FAKE_FLAG

    @property
    def cm_matches_as_json(self):
        return json.dumps(self.cm_matches)

    @property
    def cm_num_matches(self):
        """Return the number of copymove matches."""
        return len(self.cm_matches['source'])

    @property
    def exif_as_json(self):
        return json.dumps(self.exif)

    @property
    def original_image_url(self):
        """Return the full URL to the primary image of this report."""
        return self.image_file.url

    @property
    def ela_image_url(self):
        return self.original_image_url + Report.ELA_IMG_SUFFIX

    @property
    def djca_image_url(self):
        return self.original_image_url + Report.DJCA_IMG_SUFFIX

    @property
    def djcu_image_url(self):
        return self.original_image_url + Report.DJCU_IMG_SUFFIX

    @property
    def to_url(self):
        """Return the full URL of the report."""
        return u'/reports/{id}'.format(id=self.id)
