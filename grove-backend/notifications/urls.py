from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("get", views.get_notifications),
    path("delete", views.delete_notifications),
]

urlpatterns = format_suffix_patterns(urlpatterns)
