from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'tutoDjangoBoard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'sample_board.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
]