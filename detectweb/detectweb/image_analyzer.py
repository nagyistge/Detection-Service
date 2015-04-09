from __future__ import absolute_import

import numpy as np

import matlab.engine

from imforensics.util import numpy2matlb
from imforensics import ela
from imforensics import copymove

class ImageAnalyzer(object):

    def __init__(self):
        self.eng = matlab.engine.start_matlab()

    def analyze(self, report):
        self.report = report
        img_file = report.file_path

        cm_result = self._do_copy_move(img_file)
        ela_result = self._do_ela(img_file)
        ho_result = self._do_higher_order(img_file)
        feature = self._do_aggregator(cm_result, ela_result, ho_result)
        classifier_result = self._do_classifier(feature)

        self.report.score = classifier_result
        self.report.is_finished = True
        self.report.save()
        self.eng.quit()

    def _do_copy_move(self, img_file):
        c = copymove.CopyMoveDetector(self.eng)
        ransac_img, ransac_matches = c.detect(img_file)
        self.report.cm_matches = ransac_matches
        return ransac_img

    def _do_ela(self, img_file):
        e = ela.ELA(img_file)
        return numpy2matlb(e.ela_image_scaled.astype(np.double))

    def _do_higher_order(self, img_file):
        return None

    def _do_aggregator(self, cm_result, ela_result, ho_result):
        return None

    def _do_classifier(self, feature):
        return 100
