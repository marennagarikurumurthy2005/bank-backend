from rest_framework import serializers
from . models import User, Transactions

class UserSerializer(serializers.ModelSerializers):
    class Meta:
        model=User
        fields=['id','username','account_number','balance']

class TransactionSerializer(serializers.ModelSerializers):
    class Meta:
        model=Transactions
        fields=all
        