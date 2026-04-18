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
- Apply manifests: `kubectl apply -f k8s/`

## Endpoints

- `GET /health`
- `GET /template`

## Pipeline

This repo consumes the reusable workflows from the org `.github` repository for:

- pull request CI
- post-merge Docker build and push to `ghcr.io/{{cookiecutter.ghcr_owner}}`
- Kubernetes deploy to the shared cluster
