from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'csrf.views.home', name='home'),
    # url(r'^csrf/', include('csrf.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(
    "views",
    url(r"^$", 'root', name='index'),
    url(r"^register/$", 'register', name='register'),
    url(r"^search/$", 'search', name='search'),
    url(r"^register_result/$", 'register_result', name='register_result'),
    url(r"^get_json_js/$", 'get_json_js', name='get_json_js'),
    # not using now
    #url(r"^get_json/$", 'get_json', name='get_json'),
)
