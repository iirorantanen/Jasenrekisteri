from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^members/', include('jasenrekisteri.rekisteri.urls')),
    #(r'^members/$', 'jasenrekisteri.rekisteri.views.index'),
    #(r'^members/(?P<member_id>\d+)/$', 'jasenrekisteri.rekisteri.views.detail'),
    # Example:
    # (r'^jasenrekisteri/', include('jasenrekisteri.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
