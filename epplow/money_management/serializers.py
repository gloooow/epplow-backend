from rest_framework import serializers
from .models import Category, Item, Account, AccountCode


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class AccountCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountCode
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'