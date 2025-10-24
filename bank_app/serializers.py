from rest_framework import serializers
from . models import User, Transactions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','account_number','balance']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transactions
        fields="__all__"
        