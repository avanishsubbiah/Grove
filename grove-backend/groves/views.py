from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, Http404
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import User
from groves.models import Grove
from groves.serializers import GroveSerializer
from notifications.models import Notification
from django.utils import timezone


@api_view(["POST"])
def shake_friend(request):
    src = User.get_by_username(request.name)
    if (dst_name := request.data["dst"]) is None:
        return Http404
    dst = User.objects.filter(username=dst_name).first()
    if (friendship := Grove.get_grove(src, dst)) is None:
        return Http404
    friendship.xp += 50
    friendship.save()
    n = Notification(user_to=dst, content="What's shaking?", src=str(src))
    n.save()
    return HttpResponse(f"Created shake to {dst}")

@api_view(["GET"])
def establish(request):
    src = User.get_by_username(request.name)
    if (dst_name := request.data["dst"]) is None:
        return Http404
    if (dst := User.get_by_username(dst_name)) is None:
        return HttpResponseBadRequest
    if Grove.get_grove(src, dst) is not None:
        return HttpResponseBadRequest("Already friends")

    if len(User.objects.filter(id=src.id).all()) > 12:
        return HttpResponseBadRequest("Friends list full....")
    g = Grove(user_a=src, user_b=src, xp=0, start_data=timezone.now)
    g.save()
    return Response(GroveSerializer(Grove).data)    
