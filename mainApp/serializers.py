from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import *

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
    
    def update(self,instance, validated_data):

        if validated_data.get('password') == instance.password or validated_data.get('password') == None:
            return super(UserSerializer, self).update(instance,validated_data)
        else:
            validated_data['password'] = make_password(validated_data.get('password', instance.password))
            return super(UserSerializer, self).update(instance,validated_data)
    
    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email', '')
        password = data.get('password', '')

        if email and password:
            user = authenticate(username=email, password=password)
            print(user)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    msg = "User is not active"
                    raise exceptions.ValidationError(msg)
            else:
                try:
                    check = User.objects.get(email=email)
                    # print(check.password)
                    msg = "Password is incorrect for {}".format(check.email)
                    raise exceptions.ValidationError(msg)
                except User.DoesNotExist:
                    msg = "this email not registered with us"
                    raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both"
            raise exceptions.ValidationError(msg)
        return data