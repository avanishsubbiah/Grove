from django.shortcuts import render
from rest_framework.decorators import api_view
from users.models import User
from .models import Request
from notifications.models import Notification
from requests.serializers import RequestSerializer
from groves.serializers import GroveSerializer
from rest_framework.response import Response
from groves.models import Grove


# Create your views here.
@api_view(["POST"])
def create_request(request):
    username = request.user
    user = User.get_by_username(username=username)
    friend =  User.get_by_username(request.data["new_friend"])
    r = Request(src = user, dst = friend)
    prompt = "Be my friend?"
    n = Notification(
        user_to=user,
        content=f"{prompt}",
        src=f"{user.first_name} {user.last_name}",
    )
    n.save()
    r.save()
    return Response(RequestSerializer(r, many=False).data)

@api_view(["GET"])
def get_request(request):
    user = User.objects.filter(username=request.user).first()
    reqlist = Request.objects.filter(dst=user).all()
    return Response(RequestSerializer(reqlist, many=True).data)

@api_view(["DELETE"])
def cancel_request(request):
    user = User.objects.filter(username=request.user).first()
    id = request.data["id"]
    delfren = Request.objects.filter(id=id).first()
    nofren = Response(RequestSerializer(delfren, many=False).data)
    delfren.delete()
    return nofren

@api_view(["DELETE"])
def accept_request(request):
    user = User.objects.filter(username=request.user).first()
    id = request.data["id"]
    newfren = Request.objects.filter(id=id).first().src
    g = Grove(user_a = user, user_b = newfren)
    g.save()
    newestfren = Response(GroveSerializer(g, many=False).data)
    newfren.delete()
    return newestfren
    
    
    
    
