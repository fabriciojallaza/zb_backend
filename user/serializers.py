from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model, authenticate


class UserSerializerToken(serializers.Serializer):
    """User authentication serializer"""
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        """Validate and authenticate the user
        :param attrs: request object
        :return: User object
        """
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(request=self.context.get('request'), username=username, password=password)
        if not user:
            msg = _('Invalid credentials, please try again')
            raise serializers.ValidationError(msg, code='authentication')

        # If authentication is successful, return the user
        attrs['user'] = user
        return attrs


class UserSerializerAdmin(serializers.ModelSerializer):
    """User creation and update serializer"""

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password', 'is_staff', 'is_active')
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """User object creation with encrypted password
        :param validated_data: object
        :return: object
        """
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """User object update with encrypted password"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
