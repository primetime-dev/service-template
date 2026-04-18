# {{cookiecutter.service_name}}

{{cookiecutter.description}}

This service follows the shared Primetime Python API, Docker, GitHub Actions,
and Kubernetes conventions.

## Local Commands

- Bootstrap dependencies: `make bootstrap`
- Lint: `make lint`
- Run tests: `make test`
- Build the package: `make build`
- Start the API: `PYTHONPATH=src uv run --frozen python -m {{cookiecutter.python_package}}.main`
- Build the image: `docker build -t {{cookiecutter.service_slug}}:dev .`
- Render shared chart: `helm template {{cookiecutter.service_slug}} oci://ghcr.io/{{cookiecutter.ghcr_owner}}/charts/flask-service --version 0.1.0 -f deploy/values.yaml --set image.repository=ghcr.io/{{cookiecutter.ghcr_owner}}/{{cookiecutter.service_slug}} --set image.tag=dev`

## Quick Start

Start the service directly:

```bash
make bootstrap
PYTHONPATH=src uv run --frozen python -m {{cookiecutter.python_package}}.main
```

In another terminal, verify it is serving traffic:

```bash
curl http://127.0.0.1:{{cookiecutter.container_port}}/
curl http://127.0.0.1:{{cookiecutter.container_port}}/healthz
curl http://127.0.0.1:{{cookiecutter.container_port}}/readyz
```

Build and run the container:

```bash
docker build -t {{cookiecutter.service_slug}}:dev .
docker run --rm -p {{cookiecutter.container_port}}:{{cookiecutter.container_port}} {{cookiecutter.service_slug}}:dev
```

Then verify the containerized service:

```bash
curl http://127.0.0.1:{{cookiecutter.container_port}}/
curl http://127.0.0.1:{{cookiecutter.container_port}}/healthz
curl http://127.0.0.1:{{cookiecutter.container_port}}/readyz
```

## Endpoints

- `GET /`
- `GET /healthz`
- `GET /readyz`

## Pipeline

This repo consumes the reusable workflows from the org `.github` repository for:

- pull request CI
- post-merge Docker build and push to `ghcr.io/{{cookiecutter.ghcr_owner}}`
- Helm-based deployment via the shared `flask-service` chart

The generated repo stores chart overrides in `deploy/values.yaml`.
