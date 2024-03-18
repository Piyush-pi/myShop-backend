from django.contrib import admin
from apps.product.models import Product, Recommendation

# Register your models here.
admin.site.register(Product)
admin.site.register(Recommendation)
