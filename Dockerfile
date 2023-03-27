# Use the official Python image as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port the app will run on
EXPOSE 5000
ENV DATABASE_URI='mysql://user:password@host/database'
# Start the application
CMD ["python", "./app/app.py"]
