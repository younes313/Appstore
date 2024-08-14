from rest_framework import status, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Purchase
from ..serializers import PurchaseSerializer
from ..services import create_purchase


class PurchaseViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user = request.user
        app_id = request.data.get('app_id')

        try:
            purchase = create_purchase(user, app_id)
            serializer = PurchaseSerializer(purchase)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
