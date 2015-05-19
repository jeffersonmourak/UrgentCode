from django.conf.urls import patterns, include, url
from django.contrib import admin
from webapp import views, forums

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'urgentcode.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.index, name="Index Page"),
    url(r'^forum/$',forums.index, name="Index Page"),
    url(r'^forum/login/$',forums.login, name="Index Page"),
    url(r'^admin/', include(admin.site.urls)),
)
