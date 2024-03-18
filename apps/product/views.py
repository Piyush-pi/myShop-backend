"""Product Views File"""
from rest_framework import viewsets
from apps.product.models import Product
from apps.product.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
