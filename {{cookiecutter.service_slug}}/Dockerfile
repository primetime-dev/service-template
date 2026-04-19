FROM python:3.13-slim

WORKDIR /app
RUN groupadd --gid 10001 app \
    && useradd --uid 10001 --gid app --home-dir /app --no-create-home \
        --shell /usr/sbin/nologin app
COPY --from=ghcr.io/astral-sh/uv:0.10.11 /uv /uvx /usr/local/bin/
COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev --no-install-project
COPY --chown=10001:10001 src ./src
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH=/app/src

EXPOSE {{cookiecutter.container_port}}

USER 10001

CMD ["flask", "--app", "{{cookiecutter.python_package}}.main:app", "run", "--host=0.0.0.0", "--port={{cookiecutter.container_port}}"]
