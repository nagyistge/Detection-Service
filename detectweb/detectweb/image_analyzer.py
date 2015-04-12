# -*- coding: utf-8 -*-
from __future__ import absolute_import

import numpy as np

import matlab.engine

from imforensics import *
from imforensics.util import numpy2matlab, is_jpeg

class ImageAnalyzer(object):

    def __init__(self, logger=None):
        self.eng = matlab.engine.start_matlab()
        self.logger = logger

    def analyze(self, report):
        self.report = report
        img_file = report.file_path

        self._do_metadata(img_file)
        cm_result = self._do_copy_move(img_file)
        ela_result = self._do_ela(img_file)
        ho_result = self._do_higher_order(img_file)
        self._do_double_jpeg(img_file)
        feature = self._do_aggregator(cm_result, ela_result, ho_result)
        self._do_classifier(feature)

        self.report.is_finished = True
        self.report.save()
        self.eng.quit()

    def _do_copy_move(self, img_file):
        self._log('------Doing copy move------')
        c = copymove.CopyMoveDetector(self.eng)
        ransac_img, ransac_matches = c.detect(img_file)
        self.report.cm_matches = ransac_matches
        return ransac_img

    def _do_ela(self, img_file):
        self._log('------Doing ela------')
        e = ela.ELA(img_file)
        ec = ela.ELAClassifier()
        result = ec.predict_message(e)
        if result == ela.ELAClassifier.SURE_AUTH_MSG:
            self.report.ela_result = \
                "We are sure the image has been manipulated based on error level analysis."
        elif result == ela.ELAClassifier.NOT_SURE_AUTH_MSG:
            self.report.ela_result = \
                "We think the image might be manipulated based on error level analysis."
        elif result == ela.ELAClassifier.NOT_SURE_FAKE_MSG:
            self.report.ela_result = \
                "We think the image might be authentic based on error level analysis."
        elif result == ela.ELAClassifier.SURE_FAKE_MSG:
            self.report.ela_result = \
                "We are sure the image is authentic based on error level analysis."
        self._log('ELA Result: {0}'.format(result))
        e.save_ela_image()
        return numpy2matlab(e.ela_image_scaled.astype(np.double))

    def _do_higher_order(self, img_file):
        self._log('------Doing higher order stats------')
        h = higherorderstats.HigherOrderStatsDetector(self.eng)
        return h.detect(img_file)

    def _do_metadata(self, img_file):
        if is_jpeg(img_file):
            self._log('------Doing metadata------')
            er = metadata.ExifReport(img_file).process()
            self.report.exif = er['exif']
            self.report.has_camera_attrs = er['results']['has_camera_attrs']
            self.report.has_crop_resize = er['results']['has_crop_resize']
            self.report.has_size_mismatch = er['results']['has_size_mismatch']
            self.report.has_software_manipulation = er['results']['has_software_manipulation']
            self.report.height = er['im']['height']
            self.report.width = er['im']['width']

    def _do_double_jpeg(self, img_file):
        if is_jpeg(img_file):
            self._log('------Doing double jpeg------')
            d = doublejpeg.DoubleJPEGCompressionDetector(self.eng)
            d.detect(img_file)

    def _do_aggregator(self, cm_result, ela_result, ho_result):
        self._log('------Doing aggregating------')
        a = aggregator.Aggregator(self.eng)
        return a.aggregate(cm_result, ela_result, ho_result)

    def _do_classifier(self, feature):
        self.report.score = 100

    def _log(self, msg):
        if self.logger:
            self.logger.info(msg)
        else:
            print msg
