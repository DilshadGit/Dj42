from django.urls import re_path

from .views import (
	home,
	post_list_view,
	post_detail_view,
	post_edit_view,
	post_create_view,
	post_delete_view
)

app_name = 'blogs'

urlpatterns = [
    re_path(r'^', home, name='blog_home'),
    re_path(r'^detail/$', post_edit_view, name='detail'),
]
