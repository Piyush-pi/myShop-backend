from django.db import models
from apps.user.models import User


class Product(models.Model):
    """Product Model"""
    name = models.CharField(max_length=255, verbose_name="Name")
    shape = models.CharField(max_length=100, verbose_name="Shape")
    size = models.CharField(max_length=100, verbose_name="Size")
    location = models.CharField(max_length=100, verbose_name="Location")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")

    class Meta:
        """Meta Class"""
        verbose_name_plural = "Products"
        verbose_name = "Product"
        ordering = ['id']

    def __str__(self):
        """String Representation"""
        return f"{self.shape} - {self.size}"


class Recommendation(models.Model):
    """Recommendation Model"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product ID")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User ID")

    class Meta:
        """Meta Class"""
        verbose_name_plural = "Recommendations"
        verbose_name = "Recommendation"
        ordering = ['id']

    def __str__(self):
        """String Representation"""
        return f"Recommendation for {self.product} by {self.user}"
