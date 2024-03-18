"""Product Views File"""
from rest_framework.response import Response
from rest_framework import viewsets, views, generics, status
from apps.product.models import Product, Recommendation
from apps.product.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRecommendationAPIView(generics.ListAPIView):
    """Product Recommend View"""
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        """
        More filtering other than basic filtering
        can be done wrt to user selections and searches
        """
        # Retrieve users search history/preferences
        # Assuming you have user authentication and user ID is available
        # user_id = request.user.id
        # For now using fixture ID
        user_id = '8f27dd01-d6b9-4302-b0a4-7e2c712933e3'

        # Retrieve recommendations for the user
        recommended_product_ids = Recommendation.objects.filter(
            user_id=user_id).values_list('product', flat=True)

        # Fetch recommended products from the Product model
        recommended_products = Product.objects.filter(
            id__in=recommended_product_ids)
        serializer_products = ProductSerializer(recommended_products, many=True)

        return Response(serializer_products.data, status=status.HTTP_200_OK)
