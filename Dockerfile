FROM python:3.12-slim

WORKDIR /app

COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY automation_toolkit automation_toolkit
COPY tests tests
COPY pyproject.toml .

CMD ["pytest"]
