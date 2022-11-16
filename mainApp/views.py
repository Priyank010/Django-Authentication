from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            django_login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            context = {"email": request.data['email'],
                       "user_id": User.objects.get(email=request.data['email']).id,
                       'token': token.key}
        else:
            context = {"error_msg": serializer.errors['non_field_errors'][0]}
        return Response(context, status=200)

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)