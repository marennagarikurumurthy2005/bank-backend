from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer,TransactionSerializer
from . models import User,Transactions

# Create your views here.

def get_token_for_user(user):
    refresh=RefreshToken.for_user(user)
    return{'refresh':str(refresh),
           'access':str(refresh.access_token)}

# Registerview
class Registration(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        if User.objects.filter(username=username).exists():
            return Response({"error":"User already exist"},status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        token =get_token_for_user(user)
        return Response({"user": UserSerializer(user).data, "token": token})



