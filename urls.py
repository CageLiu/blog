from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

import view

urlpatterns = patterns('',
	(r'^$',view.index),
	(r'^onlyme/$',view.admin),
	(r'^manager/$',view.manager),
	(r'^search/$',view.index),
	(r'^(?P<name>\w*)/$',view.index),
	(r'^(?P<name>\w*)/(?P<title>\w*)/$',view.index,{'template_name':'details.html'}),







	#------------------------------------admin view--------------------------------------
	#(r'^admin/',include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
