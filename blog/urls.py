#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path('archives/<int:year>/<int:month>/', views.ArchivesViews.as_view(), name='archive'),
    path('categories/<int:pk>', views.CategoryView.as_view(), name='categories'),
    path('tags/<int:pk>', views.TagViews.as_view(), name='tag'),
]
