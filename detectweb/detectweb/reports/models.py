# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os

from django.conf import settings
from django.db import models

from jsonfield import JSONField
import collections
import json

from imforensics.ela import ELAClassifier
from imforensics.util import is_jpeg

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

    djca_score = models.FloatField(null=True)
    djcu_score = models.FloatField(null=True)

    ELA_IMG_SUFFIX = '.ela_suspect.jpeg'
    DJCA_IMG_SUFFIX = '.djca.png'
    DJCU_IMG_SUFFIX = '.djcu.png'
    HOS_IMG_SUFFIX = '.hos.png'
    DJCA_HOVER_IMG_SUFFIX = '.hover' + DJCA_IMG_SUFFIX
    DJCU_HOVER_IMG_SUFFIX = '.hover' + DJCU_IMG_SUFFIX
    HOS_HOVER_IMG_SUFFIX = '.hover' + HOS_IMG_SUFFIX

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
    def is_jpeg(self):
        return is_jpeg(self.file_path)

    @property
    def manipulation_classification(self):
        return 100

    """ *** ELA Properties *** """
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

    """ *** Copy Move Properties *** """
    @property
    def cm_matches_as_json(self):
        return json.dumps(self.cm_matches)

    @property
    def cm_num_matches(self):
        """Return the number of copymove matches."""
        return len(self.cm_matches['source'])

    """ *** Metadata Properties *** """
    @property
    def exif_as_json(self):
        return json.dumps(self.exif)

    """ *** DJC Properties *** """
    @property
    def is_djc_suspicious(self):
        return self.is_djca_suspicious or self.is_djcu_suspicious
    @property
    def is_djca_suspicious(self):
        return self.djca_score > 0.0125

    @property
    def is_djcu_suspicious(self):
        return self.djcu_score > 0.0125

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
    def djca_image_hover_url(self):
        return self.original_image_url + Report.DJCA_HOVER_IMG_SUFFIX

    @property
    def djcu_image_url(self):
        return self.original_image_url + Report.DJCU_IMG_SUFFIX

    @property
    def djcu_image_hover_url(self):
        return self.original_image_url + Report.DJCU_HOVER_IMG_SUFFIX

    @property
    def hos_image_url(self):
        return self.original_image_url + Report.HOS_IMG_SUFFIX

    @property
    def hos_image_hover_url(self):
        return self.original_image_url + Report.HOS_HOVER_IMG_SUFFIX

    @property
    def to_url(self):
        """Return the full URL of the report."""
        return u'/reports/{id}'.format(id=self.id)
