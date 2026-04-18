# service-template

Minimal Cookiecutter template for Primetime Python API services.

It generates a starter repo that already matches the shared conventions for:

- Python package layout
- local `Makefile` commands
- Docker image build
- reusable GitHub Actions workflows
- Kubernetes deployment and service manifests

## Usage

Install Cookiecutter:

```bash
pipx install cookiecutter
```

Generate a new service:

```bash
cookiecutter https://github.com/primetime-dev/service-template.git
```

Cookiecutter prompts for:

- `service_name`
- `description`
- `container_port`
- `service_slug` with a default derived from `service_name`
- `python_package` with a default derived from `service_slug`
- `ghcr_owner` defaulting to `primetime-dev`

## Output

The generated repo includes:

- a simple Flask API service
- `make bootstrap`, `make lint`, `make test`, and `make build`
- K8s manifests wired to the service slug, GHCR owner, and container port
- reusable CI and deploy workflow references

The generated service README also includes a quick-start flow for:

- local startup with the project toolchain
- building and running the Docker image
- verifying the service with `curl`
