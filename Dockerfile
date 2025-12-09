FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Docker CLI inside container (so Flask can call docker run)
RUN apt-get update && \
    apt-get install -y docker.io && \
    rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Start Flask API
CMD ["python", "server.py"]
