# -*- coding: utf-8 -*-

# @File    : urls.py
# @Date    : 2020-04-10
# @Author  : rjh_fdz

from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),
]
