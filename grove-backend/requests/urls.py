from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("create/", views.create_request),
    path("get-active/", views.get_request),
    path("cancel/", views.cancel_request),
    path("accept/", views.accept_request),
]

urlpatterns = format_suffix_patterns(urlpatterns)