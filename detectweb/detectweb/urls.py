from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from detectweb.reports import views as reports_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'detectweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', reports_views.image_drop_box, name='image_drop_box'),
    url(r'^upload/$', reports_views.upload_images, name='upload_images'),
    url(r'^reports/$', reports_views.index_reports, name='index_reports'),
    url(r'^reports/(?P<report_id>\d+)/$', reports_views.show_reports, name='show_reports'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
