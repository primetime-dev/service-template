FROM python:3.13-slim

WORKDIR /app
RUN pip install --no-cache-dir flask==3.1.1
COPY src ./src
ENV PYTHONPATH=/app/src

EXPOSE {{cookiecutter.container_port}}

CMD ["flask", "--app", "{{cookiecutter.python_package}}.main:app", "run", "--host=0.0.0.0", "--port={{cookiecutter.container_port}}"]
