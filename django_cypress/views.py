import json

from django.core import management
from django.http import HttpRequest, JsonResponse
from django.middleware.csrf import get_token
from django.views import View


class RefreshDatabaseView(View):
    """A view for running Django's flush command via HTTP POST requests."""

    def post(
        self,
        _: HttpRequest,
    ) -> JsonResponse:
        """Handle HTTP POST requests to execute Django's flush command.

        Args:
        ----
        request (HttpRequest): The HTTP request object.

        Returns:
        -------
        JsonResponse: A JSON response indicating the success of the command execution.
        """
        management.call_command("flush", "--no-input")

        return JsonResponse({"success": True})


class MigrateView(View):
    """A view for running Django's migrate command via HTTP POST requests."""

    def post(
        self,
        _: HttpRequest,
    ) -> JsonResponse:
        """Handle HTTP POST requests to execute Django's migrate command.

        Args:
        ----
        request (HttpRequest): The HTTP request object.

        Returns:
        -------
        JsonResponse: A JSON response indicating the success of the command execution.
        """
        management.call_command("migrate")

        return JsonResponse({"success": True})


class ManageView(View):
    """A view for running Django management commands via HTTP POST requests."""

    def post(
        self,
        request: HttpRequest,
    ) -> JsonResponse:
        """Handle HTTP POST requests to execute Django management commands.

        Args:
        ----
        request (HttpRequest): The HTTP request object containing the command to execute.

        Returns:
        -------
        JsonResponse: A JSON response indicating the success of the command execution.
        """
        body = json.loads(request.body.decode("utf-8"))
        command = body.get("command")
        parameters = body.get("parameters")
        management.call_command(
            command,
            *parameters,
        )

        return JsonResponse({"success": True})


class CSRFTokenView(View):
    """A view for retrieving the CSRF token via HTTP GET requests."""

    def get(
        self,
        request: HttpRequest,
    ) -> JsonResponse:
        """Handle HTTP GET requests to retrieve the CSRF token.

        Args:
        ----
        request (HttpRequest): The HTTP request object.

        Returns:
        -------
        JsonResponse: A JSON response containing the CSRF token.
        """
        token = get_token(request)

        return JsonResponse({"token": token})
