"""
Command File:
This task can be done with custom middleware to track
which user accessing which products with APIs with what filters and seaches
"""
import random
from django.core.management.base import BaseCommand
from apps.product.models import Recommendation, Product


class Command(BaseCommand):
    help = 'Creates recommendations for two user IDs with random products'

    def handle(self, *args, **kwargs):
        # User IDs for which recommendations will be created from fixtures
        user_ids = [
            "8f27dd01-d6b9-4302-b0a4-7e2c712933e3",
            "df9df0ef-79ac-474a-b5f5-5d06f69f0563"
        ]
        product_ids = list(Product.objects.values_list('id', flat=True))

        recommendations_to_create = []

        for user_id in user_ids:
            # Choose random number of products to recommend for each user (between 1 and 10)
            num_recommendations = random.randint(1, 100)

            # Choose random product IDs for recommendations
            random_product_ids = random.sample(product_ids, num_recommendations)

            for product_id in random_product_ids:
                recommendations_to_create.append(
                    Recommendation(
                        product_id=product_id,
                        user_id=user_id
                    )
                )

        Recommendation.objects.bulk_create(recommendations_to_create)

        self.stdout.write(self.style.SUCCESS('Recommendations created successfully!'))
