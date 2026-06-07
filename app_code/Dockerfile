# Build stage
FROM python:3.13-slim AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --from=builder /install /usr/local

COPY . .

EXPOSE 8000

# Collect static files that will be later consumed by nginx proxy
RUN python manage.py collectstatic --noinput


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi:application"]