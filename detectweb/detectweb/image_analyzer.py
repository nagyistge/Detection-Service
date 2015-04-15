# -*- coding: utf-8 -*-
from __future__ import absolute_import

import matlab.engine

from imforensics import *
from imforensics.util import is_jpeg, load_matlab_util

class ImageAnalyzer(object):

    def __init__(self, logger=None):
        self.eng = matlab.engine.start_matlab()
        load_matlab_util(self.eng)
        self.logger = logger

    def analyze(self, report):
        self.report = report
        img_file = report.file_path

        self._do_metadata(img_file)
        self._do_copy_move(img_file)
        self._do_ela(img_file)
        self._do_higher_order(img_file)
        self._do_double_jpeg(img_file)

        self.report.is_finished = True
        self.report.save()
        self.eng.quit()

    def _do_copy_move(self, img_file):
        try:
            self._log('------Doing copy move------')
            c = copymove.CopyMoveDetector(self.eng)
            ransac_img, ransac_matches = c.detect(img_file)
            self.report.cm_matches = ransac_matches
        except Exception as e:
            self._log(e.message)

    def _do_ela(self, img_file):
        try:
            self._log('------Doing ela------')
            e = ela.ELA(img_file)
            ec = ela.ELAClassifier()
            msg_result = ec.predict_message(e)
            flag_result = ec.predict_flag(e)
            self.report.ela_result = flag_result
            self._log('ELA Result: {0}'.format(msg_result))
            e.save_ela_image()
            e.save_suspect_region(True,
                                  low_risk_color=(255, 196, 0),
                                  high_risk_color=(255, 23, 68))
        except Exception as e:
            self._log(e.message)

    def _do_higher_order(self, img_file):
        try:
            self._log('------Doing higher order stats------')
            higherorderstats.HigherOrderStatsDetector(self.eng)
        except Exception as e:
            self._log(e.message)

    def _do_metadata(self, img_file):
        try:
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
        except Exception as e:
            self._log(e.message)

    def _do_double_jpeg(self, img_file):
        try:
            if is_jpeg(img_file):
                self._log('------Doing double jpeg------')
                d = doublejpeg.DoubleJPEGCompressionDetector(self.eng)
                d.detect(img_file)
        except Exception as e:
            self._log(e.message)

    def _log(self, msg):
        if self.logger:
            self.logger.info(msg)
        else:
            print msg
