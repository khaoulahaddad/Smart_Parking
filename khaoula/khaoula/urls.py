from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from khaoulaApp.views import *
from django.contrib import admin
from django.contrib.auth.decorators import login_required
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'khaoula.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LoginView.as_view()),
    url(r'^khaoulaApp/$', login_required(TemplateView.as_view(template_name='khaoulaApp/login.html'))),
    url(r'^home','khaoulaApp.views.home'),
    url(r'^reserver/(?P<identif>\d+)/$','khaoulaApp.views.reserver'),
    #url(r'^updateDate/(?P<identif>\d+)/$','khaoulaApp.views.updateDate'),
    url(r'^money/(?P<identif>\d+)/$','khaoulaApp.views.money'),
    url(r'^idplace/','khaoulaApp.views.idplace'),
)
