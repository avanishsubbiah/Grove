from django.http import HttpRequest, Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import User
from groves.models import Grove
from notifications.models import Notification
from .serializers import UserSerializer
from django.db.models import Q


@api_view(["GET"])
def list_users(request):
    print(request)
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def list_users_groves(request):
    return Grove.get_friends(User.get_by_username(request.user))
