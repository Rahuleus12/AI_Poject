GEN AI PROJECT

Overview

This project demonstrates a Flask-based application that implements a simple ETL (Extract, Transform, Load) pipeline. The application reads data from three CSV files (Customers, Products, and Sales), processes the data, and displays the transformed results in a browser.

The project is containerized using Docker, allowing for easy setup and execution across different environments.

Features

Reads data from CSV files located in a data directory.

Performs data transformations including merging and calculations.

Displays the transformed data in a web interface.

Fully containerized with Docker.

Prerequisites

Install Docker.

Install Docker Compose.

Ensure the data folder exists with the following CSV files:

Customers_Data.csv

Products_Data.csv

Sales_Data.csv

File Structure

project-directory/
├── data/
│   ├── Customers_Data.csv
│   ├── Products_Data.csv
│   └── Sales_Data.csv
├── Flask_Sales_App.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

How to Run

1. Clone the Repository

Ensure you have the project files available locally.

# Clone the repository (if hosted in a VCS)
git clone <repository_url>
cd project-directory

2. Build and Run with Docker Compose

Build and start the application using Docker Compose:

# Build the Docker image
docker-compose build

# Start the container
docker-compose up

The application will be accessible at http://localhost:5000.

3. Access the Application

Navigate to /run-etl to execute the ETL process.

The transformed data will be displayed in your browser.

4. Stopping the Application

To stop the application, press CTRL+C in the terminal running Docker Compose or run:

docker-compose down

ETL Process Details

Extract: Reads data from the provided CSV files.

Transform:

Merges Sales data with Customers and Products based on their IDs.

Adds a TotalSale column calculated as Quantity * Price.

Load: Displays the processed data in an HTML table.

Environment Variables

FLASK_ENV=development: Enables development mode for the Flask application.

Troubleshooting

Common Issues

Port Already in Use:

Change the port mapping in docker-compose.yml:

ports:
  - "5001:5000"

Access the app at http://localhost:5001.

Missing Data Files:

Ensure the data directory contains the required CSV files.

App Not Loading:

Verify Flask is running with host='0.0.0.0' in the script.

Check logs with:

docker-compose logs

Additional Notes

Modify the Flask script (Flask_Sales_App.py) to adapt to your specific data requirements.

This project uses Python 3.12 and requires the dependencies listed in requirements.txt. Ensure compatibility if running locally outside Docker.
