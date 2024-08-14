from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PurchaseViewSet

app_name = "purchase"

router = DefaultRouter()
router.register(r'', PurchaseViewSet, basename='purchase')

urlpatterns = [
    path('', include(router.urls)),
]
