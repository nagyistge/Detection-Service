from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'detectweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.image_drop_box),
    url(r'^upload/$', views.upload_images),
    url(r'^reports/$', views.index_reports),
    url(r'^reports/(?P<report_id>\d+)/$', views.show_reports),
)
