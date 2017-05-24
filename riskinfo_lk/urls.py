from django.conf.urls import patterns, url

from geonode.urls import *

urlpatterns = patterns('',
   (r'^i18n/', include('django.conf.urls.i18n')),
   url(r'^/?$',
       TemplateView.as_view(template_name='site_index.html'),
       name='home'),
 ) + urlpatterns
