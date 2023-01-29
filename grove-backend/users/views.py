from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(req: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, new user")