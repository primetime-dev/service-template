"""Tests for the Cookiecutter service template structure."""

from __future__ import annotations

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = ROOT / "{{cookiecutter.service_slug}}"


class CookiecutterTemplateTests(unittest.TestCase):
    """Verify the repo is wired as a Cookiecutter template."""

    def test_cookiecutter_config_declares_expected_inputs(self) -> None:
        """The template exposes the supported prompt surface."""
        config_path = ROOT / "cookiecutter.json"

        self.assertTrue(config_path.exists(), "cookiecutter.json should exist")

        config = json.loads(config_path.read_text(encoding="utf-8"))

        self.assertEqual(config["service_name"], "Example Service API")
        self.assertEqual(config["description"], "Standardized Python API service.")
        self.assertEqual(config["container_port"], "8000")
        self.assertEqual(config["ghcr_owner"], "primetime-dev")
        self.assertIn("cookiecutter.service_name", config["service_slug"])
        self.assertIn("cookiecutter.service_slug", config["python_package"])

    def test_template_tree_contains_templated_project_files(self) -> None:
        """The project output lives under a rendered service slug directory."""
        expected_paths = [
            TEMPLATE_ROOT / "README.md",
            TEMPLATE_ROOT / "Dockerfile",
            TEMPLATE_ROOT / "Makefile",
            TEMPLATE_ROOT / "pyproject.toml",
            TEMPLATE_ROOT / ".gitignore",
            TEMPLATE_ROOT / ".github" / "workflows" / "ci.yml",
            TEMPLATE_ROOT / ".github" / "workflows" / "deploy-image.yml",
            TEMPLATE_ROOT / "k8s" / "deployment.yaml",
            TEMPLATE_ROOT / "k8s" / "service.yaml",
            TEMPLATE_ROOT / "src" / "{{cookiecutter.python_package}}" / "__init__.py",
            TEMPLATE_ROOT / "src" / "{{cookiecutter.python_package}}" / "main.py",
            TEMPLATE_ROOT / "tests" / "test_app.py",
        ]

        for expected_path in expected_paths:
            self.assertTrue(expected_path.exists(), f"Missing template file: {expected_path}")

    def test_kubernetes_manifest_uses_template_variables(self) -> None:
        """The deployment should render the service slug, registry owner, and port."""
        deployment = (
            TEMPLATE_ROOT / "k8s" / "deployment.yaml"
        ).read_text(encoding="utf-8")
        service = (TEMPLATE_ROOT / "k8s" / "service.yaml").read_text(encoding="utf-8")

        self.assertIn("{{cookiecutter.service_slug}}", deployment)
        self.assertIn("ghcr.io/{{cookiecutter.ghcr_owner}}/{{cookiecutter.service_slug}}", deployment)
        self.assertIn("{{cookiecutter.container_port}}", deployment)
        self.assertIn("{{cookiecutter.service_slug}}", service)
        self.assertIn("targetPort: {{cookiecutter.container_port}}", service)


if __name__ == "__main__":
    unittest.main()
