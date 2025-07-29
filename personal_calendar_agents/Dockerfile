# Start with an official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy requirements first (leverages docker cache)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your code (assumes core/ and server/ at project root)
COPY ./core ./core
COPY ./server ./server
COPY . /app

# Set environment variable for unbuffered output (good for logs)
ENV PYTHONUNBUFFERED=1

# Default command: run FastAPI app on port 8000 (or change as needed)
CMD ["uvicorn", "server.server:app", "--host", "0.0.0.0", "--port", "8000"]
