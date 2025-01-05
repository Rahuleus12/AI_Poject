# Use a lightweight base Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code to the container
COPY . .

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask application port
EXPOSE 5000

# Specify the command to run the Flask application
CMD ["python", "etl_pipeline_flask.py"]
