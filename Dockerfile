# Use a newer base image (Bullseye or Bookworm) to fix apt-get errors
FROM python:3.9-slim-bullseye

# Install FFmpeg and git
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Run the bot
CMD ["python3", "-m", "PornHub"]
