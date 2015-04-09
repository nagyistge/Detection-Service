from __future__ import absolute_import

import numpy as np

from imforensics.util import numpy2matlb
from imforensics import ela

def analyze(report):
    img_file = r.file_path

    cm_result = do_copy_move(img_file)
    ela_result = do_ela(img_file)
    ho_result = do_higher_order(img_file)
    feature = do_aggregator(cm_result, ela_result, ho_result)
    classifier_result = do_classifier(feature)

    report.score = classifier_result
    report.is_finished = True
    report.save()

def do_copy_move(img_file):
    pass

def do_ela(img_file):
    e = ela.ELA(img_file)
    return numpy2matlb(e.ela_image_scaled.astype(np.double))

def do_higher_order(img_file):
    pass

def do_aggregator(cm_result, ela_result, ho_result):
    pass

def do_classifier(feature):
    pass
