from django.conf.urls import url, include
from django.contrib import admin

from.views import  {
	blog_list,
	blog_create,
	blog_detail,
	blog_update,
	blog_delete,

}

urlpatterns = [
  
    url(r'^$', post_list),
    url(r'create/^$', post_create),
    url(r'detail/(?P<id>\d+)^$', post_detail, name='detail'),
    url(r'detail/(?P<id>\d+)/edit^$', post_update, name='detail'),
  
]
