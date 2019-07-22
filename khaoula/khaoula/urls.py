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
    url(r'^$', LoginView.as_view(template_name="front/login.html")),
    url(r'^login','khaoulaApp.views.login'),
    url(r'^home/','khaoulaApp.views.home'),
    #url(r'^reserver','khaoulaApp.views.reserver_par_Etage'),
    url(r'^money','khaoulaApp.views.money'),
)