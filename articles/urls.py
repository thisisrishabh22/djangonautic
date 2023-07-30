from django.urls import path
from . import views

urlpatterns = [
  path('', views.article_index),
  path('/<slug>', views.article_show)
]
