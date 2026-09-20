# ML Model API — Dockerfile
# =========================
#
# Build:  docker build -t ml-api .
# Run:    docker run -p 8000:8000 ml-api
# Test:   curl http://localhost:8000/health

# --- Base image ---
FROM python:3.11-slim

# --- Set working directory ---
WORKDIR /app

# --- Install dependencies ---
# Copy requirements first for Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Copy application code ---
COPY app.py .
COPY models/ models/

# --- Expose port ---
EXPOSE 8000

# --- Health check ---
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# --- Run the API ---
# --host 0.0.0.0 makes it accessible from outside the container
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
