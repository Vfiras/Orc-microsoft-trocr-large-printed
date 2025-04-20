# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . /app/

# Expose port
EXPOSE 5002

# Set environment variables from .env file (for local dev, not for prod)
# For production, use docker secrets or pass env vars at runtime

# Start the app
CMD ["python", "gemihtt.py"]
