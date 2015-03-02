from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^projeto_estagiario/', include('projeto_estagiario.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
