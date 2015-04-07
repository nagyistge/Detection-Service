from __future__ import absolute_import

import numpy as np

def analyze(report):
    img_file = r.file_path

    feature_vec = []
    feature_vec.extend(do_copy_move(img_file))
    feature_vec.extend(do_ela(img_file))
    feature_vec.extend(do_metadata(img_file))
    feature_vec.extend(do_splicing(img_file))
    feature_vec = np.array(feature_vec)
    classifier_result = do_classifier(feature_vec)

    report.score = classifier_result
    report.is_finished = True
    report.save()

def do_copy_move(img_file):
    pass

def do_ela(img_file):
    pass

def do_metadata(img_file):
    pass

def do_splicing(img_file):
    pass

def do_classifier(feature_vec):
    pass
