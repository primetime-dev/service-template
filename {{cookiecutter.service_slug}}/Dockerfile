FROM python:3.13-slim

WORKDIR /app
RUN groupadd --gid 10001 app \
    && useradd --uid 10001 --gid app --home-dir /app --no-create-home \
        --shell /usr/sbin/nologin app \
    && pip install --no-cache-dir flask==3.1.1
COPY --chown=10001:10001 src ./src
ENV PYTHONPATH=/app/src

EXPOSE {{cookiecutter.container_port}}

USER 10001

CMD ["flask", "--app", "{{cookiecutter.python_package}}.main:app", "run", "--host=0.0.0.0", "--port={{cookiecutter.container_port}}"]
