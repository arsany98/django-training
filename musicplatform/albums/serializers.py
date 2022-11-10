from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'artist', 'name', 'release_datetime', 'cost')
        depth = 1

    def validate_cost(self, value):
        if value < 0:
            raise ValidationError('Cost mustn\'t be negative')
        return super().validate(value)

    def validate(self, attrs):
        if not self.context.get('artist'):
            raise ValidationError('Artist must be provided')
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data['artist'] = self.context['artist']
        return super().create(validated_data)
