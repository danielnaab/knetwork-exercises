from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.contrib import admin

from exercises import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.menu, name='exercises_menu'),
    url(r'^css/(?P<id>.+)', redirect_to, {'url': '/static/khan-exercises/css/%(id)s'}),
    url(r'^js/(?P<id>.+)', redirect_to, {'url': '/static/khan-exercises/js/%(id)s'}),
    url(r'^utils/(?P<id>.+)', redirect_to, {'url': '/static/khan-exercises/utils/%(id)s'}),
    url(r'^khan-exercise.js(?P<id>.+)', redirect_to, {'url': '/static/khan-exercises/khan-exercise.js%(id)s'}),
    url(r'^jquery(?P<id>.+)', redirect_to, {'url': '/static/khan-exercises/jquery%(id)s'}),
    url(r'^exercises/(?P<id>.+)', redirect_to, {'url': '/static/khan-exercises/exercises/%(id)s'}),
    url(r'^build/(?P<id>.+)', redirect_to, {'url': '/static/khan-exercises/build/%(id)s'}),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
