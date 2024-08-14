from rest_framework import serializers
from ..models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    class Meta:
        model = Purchase
        fields = ['id', 'user', 'app', 'unique_key', 'link', 'created']
        read_only_fields = ('id', 'unique_key', 'link', 'created', 'price')

    def get_link(self, obj):
        return obj.app.link
