from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("create/", views.create_challenge),
    path("get-active/", views.get_active_challenges)
    
]

urlpatterns = format_suffix_patterns(urlpatterns)