# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from sample_board.views import PostList, PostDetail, PostCreate


urlpatterns = [
    # Examples:
    # url(r'^$', 'tutoDjangoBoard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # 한글 주석이 문제가 되나요??

    url(r'^$', PostList.as_view(), name='home'),
    url(r'^(?P<pk>\d+)/$', PostDetail.as_view(), name='detail'),
    url(r'^create/$', PostCreate.as_view(), name='create'),
    url(r'^admin/', include(admin.site.urls)),
]