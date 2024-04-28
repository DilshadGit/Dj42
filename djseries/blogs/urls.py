from django.urls import re_path

from .views import home, post_edit_view

app_name = 'blogs'

urlpatterns = [
    re_path(r'^', home, name='blog_home'),
    re_path(r'^detail/$', post_edit_view, name='detail'),
]
