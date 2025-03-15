FROM python:3.10-slim

#System dependencies
RUN apt-get update && apt-get install -y \
    libportaudio2 \
    alsa-utils \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -e .

CMD ["assistant"]