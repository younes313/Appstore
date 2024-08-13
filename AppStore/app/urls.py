from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AppCreatorViewSet

app_name = "app"

router = DefaultRouter()
router.register(r'my-app', AppCreatorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
