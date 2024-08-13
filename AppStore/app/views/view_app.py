from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser

from ..models import App
from ..permissions import IsCreatorOrReadOnly
from ..serializers import AppCreatorSerializer


class AppCreatorViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppCreatorSerializer
    permission_classes = [IsCreatorOrReadOnly]
    parser_classes = (MultiPartParser,)

    def get_queryset(self):
        return App.objects.filter(creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('icon', openapi.IN_FORM, description="Upload icon file", type=openapi.TYPE_FILE)
        ]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
