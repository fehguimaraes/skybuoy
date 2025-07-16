FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Run the main script every hour. Adjust the sleep duration as needed
CMD ["sh", "-c", "while true; do python main.py; sleep 3600; done"]