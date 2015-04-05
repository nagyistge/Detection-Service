from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from django.views.decorators.http import require_http_methods, require_POST, require_GET


@require_GET
def image_drop_box(request):
    context = {'name': 'blah'}
    return render(request, 'reports/image_drop_box.html', context)

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
