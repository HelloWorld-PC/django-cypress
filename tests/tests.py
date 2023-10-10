import json
from http import HTTPStatus
from typing import Dict

from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse


class CSRFTokenViewTestCase(TestCase):
    """Test case for testing the CSRF token view."""

    def setUp(self) -> None:
        """Set up the test case."""
        self.client = Client()

    def test_get_csrf_token(self) -> None:
        """Do an HTTP GET request to the CSRFTokenView.

        Make sure that the HTTP Status Code of the response
        is 200 and that the response body is in this format.
        {"token": "<csrftoken>"}.
        """
        path = reverse("csrftoken-view")
        response = self.client.get(path)

        expected_status_code = HTTPStatus.OK
        actual_status_code = response.status_code
        self.assertEqual(expected_status_code, actual_status_code)

        json_response_body: Dict[str, str] = json.loads(response.content)
        csrf_token = json_response_body.get("token")
        self.assertIsNotNone(csrf_token)


class ManageViewTestCase(TestCase):
    """Test case for the Manage view."""

    def setUp(self) -> None:
        """Set up the test case."""
        self.client = Client()

    def test_run_manage_command(self) -> None:
        """Do an HTTP POST request to the ManageView.

        First of all, create a dummy user. Then run the
        manage.py flush command through the ManageView.
        Finally, make sure that the HTTP Status Code of
        the response is 200 and the database is empty.
        """
        path = reverse("manage-view")

        User.objects.create(username="Testuser")

        request_data = {"command": "flush", "parameters": ["--no-input"]}
        content_type = "application/json"
        response = self.client.post(path, request_data, content_type)

        expected_count = 0
        actual_count = User.objects.all().count()
        self.assertEqual(expected_count, actual_count)

        expected_status_code = HTTPStatus.OK
        actual_status_code = response.status_code
        self.assertEqual(expected_status_code, actual_status_code)


class MigrateViewTestCase(TestCase):
    """Test case for the Migrate view."""

    def setUp(self) -> None:
        """Set up the test case."""
        self.client = Client()

    def test_run_migrate_command(self) -> None:
        """Do an HTTP POST request to the MigrateView.

        Run the manage.py migrate command through the MigrateView.
        Finally, make sure that the HTTP Status Code of
        the response is 200.
        """
        path = reverse("migrate-view")
        response = self.client.post(path)

        expected_status_code = HTTPStatus.OK
        actual_status_code = response.status_code
        self.assertEqual(expected_status_code, actual_status_code)


class RefreshDatabaseViewTestCase(TestCase):
    """Test case for the Migrate view."""

    def test_run_migrate_command(self) -> None:
        """Do an HTTP POST request to the RefreshDatabaseView.

        First of all, create a new user. Then,
        run the manage.py flush command through
        the RefreshDatabaseView. Finally, make sure
        that the HTTP Status Code of the response
        is 200 and the database is empty.
        """
        User.objects.create(username="Testuser")

        path = reverse("refresh-database-view")
        response = self.client.post(path)

        expected_status_code = HTTPStatus.OK
        actual_status_code = response.status_code
        self.assertEqual(expected_status_code, actual_status_code)

        expected_users_count = 0
        actual_users_count = User.objects.all().count()
        self.assertEqual(expected_users_count, actual_users_count)
