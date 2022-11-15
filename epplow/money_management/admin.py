from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category, Item, Account, AccountCode

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Account)
admin.site.register(AccountCode)