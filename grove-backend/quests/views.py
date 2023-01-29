from django.http import HttpRequest, Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User
from groves.models import Grove
from .serializers import UserSerializer
from django.db.models import Q
# Create your views here.
def index(req: HttpRequest) -> HttpResponse:
    return HttpResponse("Start your quest")