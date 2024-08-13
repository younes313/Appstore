from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AppCreatorViewSet, AppListViewSet

app_name = "app"

router = DefaultRouter()
router.register(r'my-app', AppCreatorViewSet, basename='my-app')
router.register(r'apps', AppListViewSet, basename='apps')

urlpatterns = [
    path('', include(router.urls)),
]
