from __future__ import absolute_import

from detectweb.celery import app

@app.task
def do_matlab(foo):
    return foo
