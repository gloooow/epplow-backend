from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Category, Item, Account, AccountCode
from .serializers import ItemSerializer, AccountSerializer
from rest_framework import viewsets



class ItemView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class AccountView(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

class AccountCodeView(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = AccountCode.objects.all()

class CategoryView(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Category.objects.all()