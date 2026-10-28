from unittest.mock import patch
import requests
from django.test import SimpleTestCase

from .utils import fetch_external_data


class ExternalServiceTest(SimpleTestCase):
    @patch("students.utils.requests.get")
    def test_external_service_timeout(self, mock_get):
        mock_get.side_effect = requests.Timeout

        result = fetch_external_data("https://example.com/api")

        self.assertIsNone(result["data"])
        self.assertEqual(
            result["error"],
            "External service timed out"
        )