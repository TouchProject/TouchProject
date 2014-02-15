from django.conf.urls import patterns, include, url

from django.contrib import admin
from TouchNetApp import views
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.index, name='index'),
	url(r'^profile/(?P<utilisateur_id>\d+)/$', views.profile, name='profile'),
)