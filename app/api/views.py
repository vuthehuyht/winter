from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if not user:
        return Response(status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response(status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")

    new_user = User.objects.create(
        first_name=first_name,
        last_name=last_name,
        username=username,
        password=password,
        email=email,
    )
    Token.objects.create(user=new_user)
    return Response(status=HTTP_200_OK)
