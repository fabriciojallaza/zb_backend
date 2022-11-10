from django.shortcuts import render
from products.models import Product
from rest_framework.response import Response
from rest_framework.views import APIView

from products.serializers import ProductSerializer


class ProductList(APIView):
    """
    List all products, create a new product.
    """
    def get(self, request, format=None):
        """
        Return a list of all products.
        @param request:
        @param format:
        @return:
        """
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
