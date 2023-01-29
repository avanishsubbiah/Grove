from django.urls import path
from . import views


urlpatterns = [path("groves", views.index, name="groves")]