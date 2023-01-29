from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from groves.models import Grove
from .serializers import UserSerializer


@api_view(["GET"])
def list_users(request):
    print(request)
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def list_users_groves(request):
    return Response(
        UserSerializer(
            Grove.get_friends(User.get_by_username(request.user)),
            many=True
        ).data
    )
