from django.utils.timezone import make_aware
from rest_framework import serializers, status
from rest_framework.response import Response

from core.models import Product
from datetime import datetime


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for product objects, display for non-admin users"""
    class Meta:
        model = Product
        fields = ('sku', 'name', 'price', 'brand', 'visits','is_active')
        read_only_fields = ('id','visits')


class ProductSerializerAdmin(serializers.ModelSerializer):
    """Serializer for product objects, display for admin users"""
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id','visits')

    def create(self, validated_data):
        """Create and return a new `Product` instance, given the validated data.
        :param validated_data: dict
        :rtype: object Product
        """
        try:
            product = Product.objects.create(created_at=make_aware(datetime.now()), **validated_data)
            return product
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, instance, validated_data):
        """Update and return an existing `Product` instance, given the validated data.
        :param instance: object Product
        :param validated_data: dict
        :rtype: object Product
        """
        try:
            instance.updated_at = make_aware(datetime.now())
            product = super().update(instance, validated_data)
            # Send an email to admins if product is updated
            #product_update_email(product)
            return product
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
