from __future__ import absolute_import

from detectweb.celery import app
from celery.utils.log import get_task_logger

from detectweb.image_analyzer import ImageAnalyzer
import time

@app.task
def generate_report(report):
    logger = get_task_logger('Report Generator')
    logger.info('Running analysis for report {0}'.format(report.id))
    start = time.time()
    analyzer = ImageAnalyzer(logger)
    analyzer.analyze(report)
    duration = int(time.time() - start)
    logger.info('Report {0} is analyzed; TIME: {1}'.format(report.id, duration))
