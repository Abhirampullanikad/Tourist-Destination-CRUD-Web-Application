# Dockerfile
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /tourist_app

# Install dependencies
COPY requirements.txt /tourist_app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /tourist_app/

# Collect static files (optional for production)
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000",'*']
