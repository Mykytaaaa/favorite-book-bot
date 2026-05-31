# Use a lightweight official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot script
COPY book_bot.py .

# Run the bot
CMD ["python", "book_bot.py"]