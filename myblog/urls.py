from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from myblog.views import home, allpost

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^allpost/$', allpost),
)
