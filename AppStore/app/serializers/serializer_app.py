from rest_framework import serializers

from ..models import App


class AppCreatorSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.id')

    class Meta:
        model = App
        fields = '__all__'
        read_only_fields = ['id', 'creator', 'is_verified']
