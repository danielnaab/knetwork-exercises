from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from exercises import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^menu/$', views.menu, name='exercises_menu'),
)
