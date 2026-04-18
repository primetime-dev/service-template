"""Runnable template service backed by Flask."""

from flask import Flask, jsonify


def create_app() -> Flask:
    """Create the Flask application."""
    app = Flask(__name__)

    @app.get("/")
    def index() -> tuple[object, int]:
        return jsonify(
            {"message": "hello world from {{cookiecutter.service_slug}}"},
        ), 200

    @app.get("/healthz")
    def healthz() -> tuple[object, int]:
        return jsonify(
            {"service": "{{cookiecutter.service_slug}}", "status": "ok"},
        ), 200

    @app.get("/readyz")
    def readyz() -> tuple[object, int]:
        return jsonify(
            {"service": "{{cookiecutter.service_slug}}", "status": "ok"},
        ), 200

    return app


app = create_app()


def run() -> None:
    """Run the development server."""
    app.run(host="0.0.0.0", port={{cookiecutter.container_port}})


if __name__ == "__main__":
    run()
