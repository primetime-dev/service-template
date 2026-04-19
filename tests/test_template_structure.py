"""Tests for the Cookiecutter service template structure."""

from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace
import unittest

from jinja2 import StrictUndefined
from jinja2 import Template


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
        self.assertEqual(config["container_port"], "8080")
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
            TEMPLATE_ROOT / "deploy" / "values.yaml",
            TEMPLATE_ROOT / ".github" / "workflows" / "ci.yml",
            TEMPLATE_ROOT / ".github" / "workflows" / "deploy-image.yml",
            TEMPLATE_ROOT / "src" / "{{cookiecutter.python_package}}" / "__init__.py",
            TEMPLATE_ROOT / "src" / "{{cookiecutter.python_package}}" / "main.py",
            TEMPLATE_ROOT / "tests" / "test_app.py",
        ]

        for expected_path in expected_paths:
            self.assertTrue(expected_path.exists(), f"Missing template file: {expected_path}")

    def test_deploy_files_use_template_variables(self) -> None:
        """The deploy workflow should render the service slug and values file path."""
        workflow = (
            TEMPLATE_ROOT / ".github" / "workflows" / "deploy-image.yml"
        ).read_text(encoding="utf-8")
        values_file = (TEMPLATE_ROOT / "deploy" / "values.yaml").read_text(encoding="utf-8")

        self.assertIn("{{cookiecutter.service_slug}}", workflow)
        self.assertIn("values-file: deploy/values.yaml", workflow)
        self.assertIn("{{cookiecutter.service_slug}}.demo.local", values_file)

    def test_deploy_workflow_renders_github_actions_secrets_literal(self) -> None:
        """GitHub Actions expressions should survive Cookiecutter rendering."""
        workflow = (
            TEMPLATE_ROOT / ".github" / "workflows" / "deploy-image.yml"
        ).read_text(encoding="utf-8")

        rendered = Template(workflow, undefined=StrictUndefined).render(
            cookiecutter=SimpleNamespace(service_slug="example-service-api")
        )

        self.assertIn("KUBE_CONFIG: ${{ secrets.KUBE_CONFIG }}", rendered)

    def test_template_image_declares_non_root_runtime_user(self) -> None:
        """Generated images must satisfy runAsNonRoot admission checks."""
        dockerfile = (TEMPLATE_ROOT / "Dockerfile").read_text(encoding="utf-8")

        self.assertIn("USER 10001", dockerfile)

    def test_template_image_installs_dependencies_with_uv(self) -> None:
        """Generated images should use project metadata instead of duplicate pip pins."""
        dockerfile = (TEMPLATE_ROOT / "Dockerfile").read_text(encoding="utf-8")

        self.assertIn("COPY pyproject.toml uv.lock ./", dockerfile)
        self.assertIn("uv sync --no-dev --no-install-project", dockerfile)
        self.assertNotIn("pip install --no-cache-dir flask", dockerfile)


if __name__ == "__main__":
    unittest.main()
