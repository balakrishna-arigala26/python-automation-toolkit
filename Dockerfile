# ----------------------- STAGE 1: build --------------------
FROM python:3.11-slim AS builder

WORKDIR /app  

# Install build tools (only here)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# ----------------------- STAGE 2: runtime ---------------------
FROM python:3.11-slim

WORKDIR /app

# create a non-root user (VERY IMPORTANT)
RUN groupadd -r appuser && useradd -r -g appuser appuser

# copy only installed packages + app code
COPY --from=builder /usr/local/lib/python3.11/site-packages \
                    /usr/local/lib/python3.11/site-packages
COPY automation_toolkit ./automation_toolkit
COPY setup.py .

USER appuser

ENTRYPOINT ["python", "-m", "automation_toolkit.cli"]
