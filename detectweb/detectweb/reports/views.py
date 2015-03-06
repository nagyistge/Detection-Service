from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_POST, require_GET

import datetime

@require_GET
def image_drop_box(request):
    html = "<html><body>dropbox</body></html>"
    return HttpResponse(html)

@require_POST
def upload_images(request):
    html = "<html><body>upload</body></html>"
    return HttpResponse(html)

@require_GET
def index_reports(request):
    html = "<html><body>index</body></html>"
    return HttpResponse(html)

@require_GET
def show_reports(request, **params):
    html = "<html><body>show %s </body></html>" % params['report_id']
    return HttpResponse(html)
