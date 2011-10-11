from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
import settings
import view

urlpatterns = patterns('',
	(r'^blog/$',view.index),
	(r'^blog/onlyme/$',view.admin),
	(r'^blog/manager/$',view.manager),
	(r'^blog/manager/(?P<operation>\w+)/$',view.manager),
	(r'^blog/search/$',view.index),
	(r'^blog/(?P<name>\w+)/$',view.index),
	(r'^blog/(?P<name>\w+)/(?P<arid>\w+)/$',view.index,{'template_name':'details.html'}),
	('^static_url/(?P<path>.*)','django.views.static.serve',{'document_root': settings.STATIC_PATH}),







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
