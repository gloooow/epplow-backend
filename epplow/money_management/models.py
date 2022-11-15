from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class Item(models.Model):
    class Type(models.TextChoices):
        INCOME = 'INCOME'
        EXPENSE = 'EXPENSE'
        TRANSFER = 'TRANSFER'

    name = models.CharField(max_length=100)
    price = models.FloatField()
    spare = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    type = models.CharField(max_length=10, choices=Type.choices, default=Type.EXPENSE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name