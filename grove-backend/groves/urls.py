from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [path("shake/", views.shake_friend), path("plant/", views.establish), path("pair/", views.get_grove)]

urlpatterns = format_suffix_patterns(urlpatterns)
