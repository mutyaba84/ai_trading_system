# Use Python 3.12
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src
COPY configs/ ./configs
COPY data/ ./data

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Entry point
CMD ["python", "src/main.py"]
