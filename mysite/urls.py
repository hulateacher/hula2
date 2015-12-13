from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',

     url(r'^admin/', include('django.contrib.admin.urls')),
)


   

