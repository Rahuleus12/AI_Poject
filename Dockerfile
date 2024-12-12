#Using base Python
FROM python:3.12-slim

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy the current directory contents to the container
COPY . .

# Step 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Expose Flask port
EXPOSE 5000

# Step 5: Specify the command to run the Python script
CMD ["python3", "analysis.py"]
