FROM python:3.11-slim

# Run as non-root where possible
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install system dependencies needed to build some Python packages
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	   build-essential \
	   ca-certificates \
	   curl \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy top-level requirements if present (keeps layer caching efficient)
COPY ../../requirements.txt /app/requirements.txt

# Upgrade pip and install runtime deps. Keep image small by --no-cache-dir
RUN pip install --upgrade pip setuptools wheel \
	&& if [ -f /app/requirements.txt ]; then pip install --no-cache-dir -r /app/requirements.txt; fi \
	&& pip install --no-cache-dir fastapi[all] uvicorn[standard] joblib prometheus_client \
	   opentelemetry-api opentelemetry-sdk opentelemetry-exporter-jaeger opentelemetry-exporter-prometheus

# Copy only the ml package into the image (avoid copying CI/config/etc.)
# This expects the repo layout: <repo-root>/src/ml/...
COPY . /app

# If you prefer a smaller image, copy only the ml package and models like:
# COPY src/ml /app/ml
# COPY models/model_ml.joblib /app/models/

# Ensure python can import the package files under /app/src or /app
ENV PYTHONPATH=/app

# Expose the service port
EXPOSE 5000

# Default command: run uvicorn pointing to the FastAPI app object.
# The module path used here works if your FastAPI entrypoint is at `src/ml/app.py`
# and the package root is in PYTHONPATH. We use `ml.app:app` to match package layout in `src/ml`.
CMD ["uvicorn", "ml.app:app", "--host", "0.0.0.0", "--port", "5000"]