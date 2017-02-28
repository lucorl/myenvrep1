from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns	=	[
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls', include('mysite.apps.polls.urls')),
    url(r'^blog', include('mysite.apps.blog.urls')),
]
