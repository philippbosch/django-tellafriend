from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'tellafriend.views.tellafriend', name="tellafriend"),
    url(r'^success/$', 'django.views.generic.simple.direct_to_template', { 'template': 'tellafriend/success.html'}, name="tellafriend_success"),
)