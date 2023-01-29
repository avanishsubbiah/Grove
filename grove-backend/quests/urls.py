from django.urls import path, include
from .models import Quest
from rest_framework import routers, serializers, viewsets


class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ["description", "user_from", "user_to", "exp", "status"]


class QuestViewSet(viewsets.ModelViewSet):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer


router = routers.DefaultRouter()
router.register(r"quests", QuestViewSet)


urlpatterns = [path("", include(router.urls))]
