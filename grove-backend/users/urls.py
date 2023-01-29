from rest_framework import routers
from django.urls import include, path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("list/", views.list_users),
    path("friends/", views.list_users_groves),
]

urlpatterns = format_suffix_patterns(urlpatterns)
