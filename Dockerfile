# Use official Python 3.12 image from the Docker Hub
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app/

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies from requirements.txt if exists
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# If no requirements.txt, use this block to install Django
# RUN pip install django==4.x gunicorn

# Run database migrations (SQLite)
RUN python manage.py makemigrations
RUN python manage.py migrate

# Expose the port on which Django will run
EXPOSE 8000

# Run the Django development server on 0.0.0.0:8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
