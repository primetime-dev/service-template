"""Runnable template service backed by the Python standard library."""

from __future__ import annotations

import json
from collections.abc import Callable
from wsgiref.simple_server import make_server


def build_response(path: str) -> tuple[int, dict[str, object]]:
    """Return the response for a given request path."""
    if path == "/health":
        return 200, {"service": "{{cookiecutter.service_slug}}", "status": "ok"}

    if path == "/template":
        return 200, {"repo_type": "template", "workflow": "shared-golden-path"}

    return 404, {"error": "not-found", "path": path}


def application(
    environ: dict[str, object],
    start_response: Callable[[str, list[tuple[str, str]]], object],
) -> list[bytes]:
    """Serve JSON for the demo endpoints."""
    status_code, payload = build_response(str(environ.get("PATH_INFO", "/")))
    status_line = f"{status_code} {'OK' if status_code == 200 else 'Not Found'}"
    body = json.dumps(payload).encode("utf-8")
    headers = [
        ("Content-Type", "application/json"),
        ("Content-Length", str(len(body))),
    ]
    start_response(status_line, headers)
    return [body]


def run() -> None:
    """Run the development server."""
    with make_server("127.0.0.1", {{cookiecutter.container_port}}, application) as server:
        print(
            "{{cookiecutter.service_slug}} listening on "
            "http://127.0.0.1:{{cookiecutter.container_port}}"
        )
        server.serve_forever()


if __name__ == "__main__":
    run()
