from django.conf.urls import patterns
from django.conf.urls import  url
from myflatpages import views
#urlpatterns = patterns('django.contrib.flatpages.views',
#    (r'^(?P<url>.*)$', 'flatpage'),
#)
urlpatterns = patterns('myflatpages.views',
    (r'^(?P<url>.*)$', 'flatpage'),
    )
