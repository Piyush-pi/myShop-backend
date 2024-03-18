"""Product API Test-cases"""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.product.models import Product


class ProductAPITestCases(TestCase):
    """Product API Testcases"""

    def setUp(self):
        self.client = APIClient()
        self.product1 = Product.objects.create(
            name="Product 1", shape="circle", size="small",
            location="Location 1", price=10.99
        )
        self.product2 = Product.objects.create(
            name="Product 2", shape="square", size="medium",
            location="Location 2", price=20.99
        )

    def test_list_products(self):
        """List all products test-case"""
        response = self.client.get(reverse("product-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_product(self):
        """Create Product test-case"""
        data = {
            'name': 'New Product',
            'shape': 'triangle',
            'size': 'large',
            'location': 'New Location',
            'price': 30.99
        }
        response = self.client.post(reverse('product-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 3)

    def test_retrieve_product(self):
        """Retrieve particular Product data"""
        response = self.client.get(
            reverse('product-detail', kwargs={'pk': self.product1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Product 1")
        self.assertEqual(response.data['shape'], "circle")

    def test_update_product(self):
        """Update product test-case"""
        data = {
            'name': 'Updated Product',
            'shape': 'square',
            'size': 'large',
            'location': 'Updated Location',
            'price': 40.99
        }
        response = self.client.put(
            reverse('product-detail', kwargs={'pk': self.product1.pk}), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get(pk=self.product1.pk).name, 'Updated Product')

    def test_delete_product(self):
        """Delete product test case"""
        response = self.client.delete(
            reverse('product-detail', kwargs={'pk': self.product1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 1)
