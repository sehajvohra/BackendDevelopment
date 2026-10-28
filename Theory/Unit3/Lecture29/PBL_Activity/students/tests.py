
from django.test import TestCase
from django.urls import reverse

from .models import Student
from unittest.mock import Mock, patch

import requests

from .utils import fetch_external_data


class HealthEndpointTest(TestCase):
    def test_health_endpoint_returns_ok(self):
        response = self.client.get(reverse("health-check"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")


class StudentEndpointTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="Sehaj Vohra",
            email="sehaj@example.com",
            age=21
        )

    def test_student_list_endpoint(self):
        response = self.client.get(reverse("student-list"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["students"]), 1)
        self.assertEqual(
            response.json()["students"][0]["name"],
            "Sehaj Vohra"
        )

    def test_student_detail_endpoint(self):
        response = self.client.get(
            reverse(
                "student-detail",
                kwargs={"student_id": self.student.id}
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Sehaj Vohra")

    def test_student_detail_returns_404_for_missing_student(self):
        response = self.client.get(
            reverse("student-detail", kwargs={"student_id": 9999})
        )

        self.assertEqual(response.status_code, 404)


class StudentModelTest(TestCase):
    def test_student_creation_and_string_representation(self):
        student = Student.objects.create(
            name="Sehaj Vohra",
            email="sehaj@example.com",
            age=21
        )

        self.assertEqual(str(student), "Sehaj Vohra")
        self.assertEqual(student.email, "sehaj@example.com")


class ExternalServiceTest(TestCase):
    @patch("students.utils.requests.get")
    def test_external_service_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            "message": "External service available"
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = fetch_external_data("https://example.com/api")

        self.assertEqual(
            result["data"],
            {"message": "External service available"}
        )
        self.assertIsNone(result["error"])
        mock_get.assert_called_once_with(
            "https://example.com/api",
            timeout=5
        )

    @patch("students.utils.requests.get")
    def test_external_service_timeout(self, mock_get):
        mock_get.side_effect = requests.Timeout

        result = fetch_external_data("https://example.com/api")

        self.assertIsNone(result["data"])
        self.assertEqual(
            result["error"],
            "External service timed out"
        )
        mock_get.assert_called_once_with(
            "https://example.com/api",
            timeout=5
        )
