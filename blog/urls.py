#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archives, name='archive'),
    path('categories/<int:pk>', views.category, name='categories'),
    path('tags/<int:pk>', views.tag, name='tag'),
]
