FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Fix the time synchronization issue
RUN apt-get update -o Acquire::Check-Valid-Until=false \
  && apt-get install -y \
  build-essential \
  && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port Gradio will run on
EXPOSE 7860

# Command to run the application
CMD ["python", "main.py"]