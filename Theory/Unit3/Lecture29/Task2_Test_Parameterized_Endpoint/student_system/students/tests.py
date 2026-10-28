from django.test import TestCase
from django.urls import reverse


class StudentDetailEndpointTest(TestCase):
    def test_student_detail_returns_student_id(self):
        response = self.client.get(
            reverse("student-detail", kwargs={"student_id": 42})
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["student_id"], 42)