from django.conf.urls.defaults import *
from openid_consumer.views import complete, signout
from django.views.generic.simple import direct_to_template

#Login Views
urlpatterns = patterns('',
  url(r'^connect/$', 'clients.views.connect', name="connect"),
  url(r'^not_user/$', 'clients.views.not_user', name="not_user"),
  url(r'^claim_data/(?P<token>\w+)$', 'clients.views.claim_data', name="claim_data"),
  url(r'^consumer/$', 'clients.views.consumer', name="counsumer"),
  url(r'^logout/$', 'clients.views.logout', name="logout"),
  
)