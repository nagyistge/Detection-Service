from django.shortcuts import render
from django.template import RequestContext, loader

from django.views.decorators.http import require_http_methods, require_POST, require_GET

from detectweb.reports.models import Report
from detectweb.reports.forms import UploadImageForm

@require_GET
def image_drop_box(request):
    form = UploadImageForm()
    return render(request, 'reports/image_drop_box.html', {'form': form})

@require_POST
def upload_images(request):
    form = UploadImageForm(request.POST, request.FILES)

    if form.is_valid():
        report = Report(image_file=request.FILES['image'])
        report.save()
        # Start salary job!
        return render(request, 'reports/show_reports.html', {'report': report})
    else:
        return render(request, 'reports/image_drop_box.html', {'form': form})

@require_GET
def index_reports(request):
    reports = Report.objects.all()
    return render(request, 'reports/index_reports.html', {'reports': reports})

@require_GET
def show_reports(request, **params):
    report = Report.objects.get(id=params['report_id'])
    return render(request, 'reports/show_reports.html', {'report': report})
