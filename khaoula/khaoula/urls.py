from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'khaoula.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','khaoulaApp.views.home',name='home'),
    url(r'^reserver/(?P<identif>\d+)/$','khaoulaApp.views.reserver'),
)
