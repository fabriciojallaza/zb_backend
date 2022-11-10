from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Product
from products.serializers import ProductSerializer, ProductSerializerAdmin


class ProductList(viewsets.ModelViewSet):
    """
    list:
        Return a list of all the existing products. No authentication required.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductView(generics.RetrieveAPIView):
    """
    get:
        Return a product by its id. If user is not authenticated, visits are incremented.
    """
    queryset = ''
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)

    def get_object(self) -> object:
        """
        :rtype: object Product
        """
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        # If user is not authenticated, visits field is incremented
        if not self.request.user.is_authenticated:
            product.visits += 1
            product.save()
        return product


class ProductCreate(generics.CreateAPIView):
    """
    post:
        Create a new product. Only authenticated users can create products.
    """
    serializer_class = ProductSerializerAdmin
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ProductControl(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
        Return a product by its id. Authentication required in order to not increment visits field.

    patch:
        Update the entire product. Only authenticated users can update products.

    put:
        Partially update of product. Only authenticated users can update products.

    delete:
        Delete a product. Only authenticated users can delete products.
    """
    queryset = ''
    serializer_class = ProductSerializerAdmin
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self) -> object:
        """ Return a product by its id
        :rtype: object Product
        """
        product = get_object_or_404(Product, id=self.kwargs['pk'])
        return product

    def delete(self, request, *args, **kwargs):
        """ Delete a product
        :param request: HttpRequest
        :param args: object
        :param kwargs: object
        :rtype: object
        """
        product = get_object_or_404(Product, id=self.kwargs['pk'])
        product.delete()
        return HttpResponse(status=200)
