
# Use Python base image
FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Prevent Python from generating bytecode
ENV PYTHONDONTWRITEBYTECODE=1

# Display Python output immediately
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements-docker.txt .
RUN pip install --no-cache-dir -r requirements-docker.txt

# Copy project files
COPY . .

# Create directory for SQLite database
RUN mkdir -p /app/data /app/staticfiles

# Expose Django application port
EXPOSE 8000

# Start Django using Gunicorn
CMD ["gunicorn", "sticky_notes.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "1"]
