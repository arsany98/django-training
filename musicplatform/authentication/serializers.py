from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})

    def validate_password(self, value):
        validate_password(value)
        return super().validate(value)

    def validate_confirm_password(self, value):
        if self.initial_data['password'] != value:
            raise serializers.ValidationError(
                'Passwords doesn\'t match')
        return super().validate(value)

    def save(self):
        get_user_model().objects.create_user(
            self.validated_data['username'], self.validated_data['email'], self.validated_data['password'])

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'confirm_password')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'})

    def validate(self, attrs):
        user = authenticate(
            username=attrs['username'], password=attrs['password'])
        if user == None:
            raise serializers.ValidationError('invalid username or password')
        return super().validate(attrs)
