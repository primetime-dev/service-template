"""Contract tests for the generated service."""

import unittest

from {{cookiecutter.python_package}}.main import create_app


class ServiceTemplateTests(unittest.TestCase):
    """Verify the generated service contract."""

    def test_root_returns_service_specific_hello_world(self) -> None:
        """The root endpoint returns a simple service-specific payload."""
        client = create_app().test_client()

        response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {"message": "hello world from {{cookiecutter.service_slug}}"},
        )

    def test_healthz_returns_ok(self) -> None:
        """The generated service exposes a basic liveness endpoint."""
        client = create_app().test_client()

        response = client.get("/healthz")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {"service": "{{cookiecutter.service_slug}}", "status": "ok"},
        )

    def test_readyz_returns_ok(self) -> None:
        """The generated service exposes a basic readiness endpoint."""
        client = create_app().test_client()

        response = client.get("/readyz")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {"service": "{{cookiecutter.service_slug}}", "status": "ok"},
        )
