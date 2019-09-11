from django.contrib.auth import authenticate
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.status import(
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from bookapp.models import User
from bookapp.serializers import RegistrationSerializer


@permission_classes((AllowAny,))
@api_view(['GET', 'POST'])
def registration_view(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = RegistrationSerializer(user, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            password2 = serializer.validated_data['password2']
            if password == password2:
                user = User(
                    user_type=serializer.validated_data['user_type'],
                    username=serializer.validated_data['username'],
                    email=serializer.validated_data['email'],
                )
                user.set_password(password)
                user.save()
            else:
                return Response("Please confirm your password")
        else:
            return Response(serializer.errors)
        return Response(serializer.data)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({"error":"Please provide both username and password!!"}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    # return Response(str(user))
    if not user:
        return Response({"error":"Invalid Credentials"}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key}, status=HTTP_200_OK)
