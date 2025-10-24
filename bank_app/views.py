from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer,TransactionSerializer
from . models import User,Transactions
from decimal import Decimal

# Create your views here.

def get_token_for_user(user):
    refresh=RefreshToken.for_user(user)
    return{'refresh':str(refresh),
           'access':str(refresh.access_token)}

# Registerview
class Registrationview(APIView):
    def post(self,request):
        username=request.data.get('username')
        email=request.data.get('email')
        account_number=request.data.get('account_number')
        balance=request.data.get('balance',0)
        balance = Decimal(str(balance))
        password=request.data.get('password')
        
        if User.objects.filter(username=username , account_number=account_number).exists():
            return Response({"error":"User already exist"},status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username,email=email,account_number=account_number,balance=balance ,password=password)
        token =get_token_for_user(user)
        return Response({"user": UserSerializer(user).data, "token": token})

# Loginview
class Loginview(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')

        user=authenticate(username=username,password=password)
        if not user:
            return Response({"error":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)
        token=get_token_for_user(user)
        return Response({"user": UserSerializer(user).data, "token": token})
    
# Dashboard 
class Dashboardview(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=request.user
        return Response(UserSerializer(user).data)
    
class Transactionview(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        user=request.user
        tr_type=request.data.get('type')
        amount = Decimal(str(request.data.get('amount')))
        if tr_type=='debit' and user.balance<amount:
            return Response({"error":"Insufficient balance"},status=status.HTTP_400_BAD_REQUEST)
        elif tr_type=='credit':
            user.balance+=amount
        elif tr_type=='debit' and user.balance>amount:
            user.balance-=amount
        else:
            return Response({'error':'Invalid transaction'})
        user.save()
        trans_det = Transactions.objects.create(user=user, type=tr_type, amount=amount)
        return Response(TransactionSerializer(trans_det).data)









