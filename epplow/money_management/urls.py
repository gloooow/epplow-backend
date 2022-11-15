from django.conf import settings
from django.urls import path, include

from .views import ItemView, AccountView

from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('items', ItemView, basename='items')
router.register('accounts', AccountView, basename='accounts')

urlpatterns = router.urls