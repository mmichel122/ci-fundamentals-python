# Stage 1: Build
FROM python:3.11-slim AS builder
WORKDIR /app

COPY app/requirements.txt .
RUN pip install --user -r requirements.txt

COPY app/ .

# Stage 2: Runtime
FROM python:3.11-alpine
WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY app/ .

ENV PATH=/root/.local/bin:$PATH
CMD ["python", "app.py"]