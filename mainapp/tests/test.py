from django.test import TestCase, SimpleTestCase
from rest_framework.test import APITestCase
from django.urls import reverse, resolve

# Create your tests here.

class TestPersonAPI(APITestCase):
    test_url = reverse("personlist")
    def test_get_personlist(self):
        response = self.client.get(self.test_url)
        self.assertEqual(200, response.status_code)