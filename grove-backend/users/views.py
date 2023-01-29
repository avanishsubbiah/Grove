from django.http import HttpRequest, Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User
from groves.models import Grove
from .serializers import UserSerializer
from django.db.models import Q


@api_view(["GET"])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def list_users_groves(request):
    username = request.query_params["username"]
    if username is None:
        raise Http404
    uid = User.objects.filter(username=username)
    if len(uid) != 1:
        raise Http404

    uid = uid[0].id
    groves = Grove.objects.filter(Q(user_a=uid) | Q(user_b=uid))
    friends = []
    for pair in groves:
        if pair.user_a.id == uid:
            friends.append(pair.user_b)
        else:
            friends.append(pair.user_a)
    
    return Response(UserSerializer(friends, many=True).data)
