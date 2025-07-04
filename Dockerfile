# Use an official lightweight Python image
FROM python:3.12-slim

# Set workdir
WORKDIR /app

# Copy requirements first for better layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose Flask port
EXPOSE 5000

# Default command to run your app
CMD ["python", "app/main.py"]
