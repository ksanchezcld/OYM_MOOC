from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'registro_estudiantes_oym.views.home', name='home'),
    # url(r'^registro_estudiantes_oym/', include('registro_estudiantes_oym.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
      url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),  
      url(r'^',include('registro_estudiantes_oym.apps.home.urls')),
      #url(r'^',include('registro_estudiantes_oym.apps.registro.urls')),
)