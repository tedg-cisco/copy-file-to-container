# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the application code
COPY app.py .

# Set the entry point
ENTRYPOINT ["python", "app.py"]
