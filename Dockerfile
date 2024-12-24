FROM --platform=linux/arm64 python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    bluetooth \
    bluez \
    libglib2.0-dev \
    && rm -rf /var/lib/apt/lists/*

# Set up the application directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY scanner.py .

# Command to run the application
CMD ["python", "bluetooth_scanner.py"]