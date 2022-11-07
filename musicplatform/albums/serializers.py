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
