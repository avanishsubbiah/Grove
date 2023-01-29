from django.urls import path
from . import views

urlpatterns = [path("quests", views.index, name="quests")]