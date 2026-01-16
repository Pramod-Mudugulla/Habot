from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class JWTAuthTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="Test@12345")

    def test_get_jwt_token(self):
        url = "/api/token/"
        data = {"username": "testuser", "password": "Test@12345"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
