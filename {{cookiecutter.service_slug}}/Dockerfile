FROM python:3.13-slim

WORKDIR /app
COPY src ./src
ENV PYTHONPATH=/app/src

EXPOSE {{cookiecutter.container_port}}

CMD ["python", "-m", "{{cookiecutter.python_package}}.main"]
