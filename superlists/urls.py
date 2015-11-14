from django.conf.urls import include, url
from django.contrib import admin
from lists import views 

urlpatterns = [
    url(r'^$', 'lists.views.home_page', name='home'),
    # Examples:
    # url(r'^$', 'superlists.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
]
