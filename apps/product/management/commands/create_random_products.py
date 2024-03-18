import random
from django.core.management.base import BaseCommand
from apps.product.models import Product


class Command(BaseCommand):
    help = 'Adds random values to the Product table'

    def handle(self, *args, **kwargs):
        """Handle function"""
        shapes = ['circle', 'square', 'triangle']
        sizes = ['small', 'medium', 'large']
        locations = ['New York', 'London', 'Paris', 'Tokyo']
        min_price = 1  # minimum price
        max_price = 1000  # maximum price
        product_count = 10000

        products_to_create = []

        for _ in range(product_count):
            name = f"Product {_ + 1}"
            shape = random.choice(shapes)
            size = random.choice(sizes)
            location = random.choice(locations)
            price = round(random.uniform(min_price, max_price), 2)

            products_to_create.append(
                Product(
                    name=name,
                    shape=shape,
                    size=size,
                    location=location,
                    price=price
                )
            )

        # Bulk Create records
        Product.objects.bulk_create(products_to_create)

        self.stdout.write(self.style.SUCCESS('Random values added to Product table successfully!'))
