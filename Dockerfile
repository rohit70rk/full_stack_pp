# Dockerfile - app image (Python 3.11 slim)
FROM python:3.11-slim

# system deps (no ffmpeg here; ffmpeg will be a separate container)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy project code into the image
COPY . /app

ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production

# ensure data dir exists for sqlite persistence (volume will mount here)
RUN mkdir -p /app/data

EXPOSE 5000

# Allow tuning workers via env vars; fspp_run.py exposes `app`
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:5000 fspp_run:app --workers ${GUNICORN_WORKERS:-3} --threads ${GUNICORN_THREADS:-2} --timeout 30"]
