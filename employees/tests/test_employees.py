from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from employees.models import Employee

class EmployeeAPITests(APITestCase):
    def setUp(self):
        # create a user
        self.user = User.objects.create_user(username="testuser", password="Test@12345")

        # get token
        token_response = self.client.post(
            "/api/token/",
            {"username": "testuser", "password": "Test@12345"},
            format="json",
        )
        self.access_token = token_response.data["access"]

        # authenticate client
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

    def test_auth_required(self):
        # Remove auth header
        self.client.credentials()
        response = self.client.get("/api/employees/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_employee(self):
        payload = {
            "name": "John Doe",
            "email": "john@example.com",
            "department": "Engineering",
            "role": "Developer"
        }
        response = self.client.post("/api/employees/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["email"], "john@example.com")

    def test_duplicate_email_should_fail(self):
        Employee.objects.create(name="A", email="dup@example.com")
        payload = {"name": "B", "email": "dup@example.com"}
        response = self.client.post("/api/employees/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)

    def test_get_employee_list_paginated(self):
        # create 15 employees
        for i in range(15):
            Employee.objects.create(name=f"Emp {i}", email=f"emp{i}@example.com")

        response = self.client.get("/api/employees/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # DRF paginated response format
        self.assertIn("results", response.data)
        self.assertEqual(len(response.data["results"]), 10)

    def test_filter_by_department(self):
        Employee.objects.create(name="HR Guy", email="hr@example.com", department="HR", role="Manager")
        Employee.objects.create(name="Eng Guy", email="eng@example.com", department="Engineering", role="Developer")

        response = self.client.get("/api/employees/?department=HR")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["department"], "HR")

    def test_filter_by_role(self):
        Employee.objects.create(name="Dev1", email="dev1@example.com", department="Engineering", role="Developer")
        Employee.objects.create(name="Manager1", email="mgr1@example.com", department="HR", role="Manager")

        response = self.client.get("/api/employees/?role=Developer")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["role"], "Developer")

    def test_retrieve_update_delete_employee(self):
        emp = Employee.objects.create(name="Temp", email="temp@example.com")

        # retrieve
        get_response = self.client.get(f"/api/employees/{emp.id}/")
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_response.data["email"], "temp@example.com")

        # update
        put_payload = {
            "name": "Temp Updated",
            "email": "temp@example.com",
            "department": "Sales",
            "role": "Lead"
        }
        put_response = self.client.put(f"/api/employees/{emp.id}/", put_payload, format="json")
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.data["department"], "Sales")

        # delete
        del_response = self.client.delete(f"/api/employees/{emp.id}/")
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)

        # ensure gone
        get_again = self.client.get(f"/api/employees/{emp.id}/")
        self.assertEqual(get_again.status_code, status.HTTP_404_NOT_FOUND)
