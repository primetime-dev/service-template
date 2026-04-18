"""Validate Cookiecutter inputs before rendering the service template."""

from __future__ import annotations

import re
import sys


def _fail(message: str) -> None:
    """Exit with a clear validation error."""
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def _validate_slug(value: str) -> None:
    """Ensure the service slug is safe for repos and Kubernetes names."""
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value):
        _fail("service_slug must be lowercase kebab-case, for example 'billing-api'")


def _validate_package(value: str) -> None:
    """Ensure the Python package is import-safe."""
    if not re.fullmatch(r"[a-z_][a-z0-9_]*", value):
        _fail("python_package must be a valid snake_case Python package name")


def _validate_port(value: str) -> None:
    """Ensure the container port is an integer in the valid TCP range."""
    try:
        port = int(value)
    except ValueError:
        _fail("container_port must be an integer")

    if port < 1 or port > 65535:
        _fail("container_port must be between 1 and 65535")


def main() -> None:
    """Validate the supported Cookiecutter inputs."""
    _validate_slug("{{ cookiecutter.service_slug }}")
    _validate_package("{{ cookiecutter.python_package }}")
    _validate_port("{{ cookiecutter.container_port }}")


if __name__ == "__main__":
    main()
