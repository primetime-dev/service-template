"""Contract tests for the generated service."""

import unittest

from {{cookiecutter.python_package}}.main import build_response


class ServiceTemplateTests(unittest.TestCase):
    """Verify the generated service contract."""

    def test_health_returns_ok(self) -> None:
        """The generated service exposes a basic health endpoint."""
        status_code, payload = build_response("/health")

        self.assertEqual(status_code, 200)
        self.assertEqual(payload, {"service": "{{cookiecutter.service_slug}}", "status": "ok"})

    def test_template_endpoint_describes_golden_path(self) -> None:
        """The generated service advertises the expected starter behavior."""
        status_code, payload = build_response("/template")

        self.assertEqual(status_code, 200)
        self.assertEqual(
            payload,
            {
                "repo_type": "template",
                "workflow": "shared-golden-path",
            },
        )
