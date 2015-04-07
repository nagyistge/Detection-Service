from __future__ import absolute_import

from detectweb.celery import app
from celery.utils.log import get_task_logger

from image_analysis import analyze

@app.task
def generate_report(report):
    logger = get_task_logger('Report Generator')
    logger.info('Running analysis for report {0}'.format(report.id))
    analyze(report)
