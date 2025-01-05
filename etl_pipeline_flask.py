from flask import Flask, jsonify
import os
import pandas as pd

app = Flask(__name__)

# Directory and file paths
DATA_DIR = 'Data'
CUSTOMERS_FILE = os.path.join(DATA_DIR, 'Customers_Data.csv')
PRODUCTS_FILE = os.path.join(DATA_DIR, 'Products_Data.csv')
SALES_FILE = os.path.join(DATA_DIR, 'Sales_Data.csv')

# Example ETL pipeline function
def etl_pipeline():
    try:
        # Ensure data directory exists
        if not os.path.exists(DATA_DIR):
            return {"status": "error", "message": f"Data directory '{DATA_DIR}' not found."}

        # Check for required files
        missing_files = [
            file for file in [CUSTOMERS_FILE, PRODUCTS_FILE, SALES_FILE] if not os.path.exists(file)
        ]
        if missing_files:
            return {"status": "error", "message": f"Missing files: {', '.join(missing_files)}"}

        # Load CSV files
        customers_df = pd.read_csv(CUSTOMERS_FILE)
        products_df = pd.read_csv(PRODUCTS_FILE)
        sales_df = pd.read_csv(SALES_FILE)

        # Example transformations (adjust as needed)
        # Merge sales with customers and products
        merged_df = sales_df.merge(customers_df, on='CustomerID', how='left')
        merged_df = merged_df.merge(products_df, on='ProductID', how='left')

        # Add a calculated column (e.g., TotalSale)
        merged_df['TotalSale'] = merged_df['Quantity'] * merged_df['Price']

        # Save the transformed data to a new file
        output_file = os.path.join(DATA_DIR, 'Transformed_Sales_Data.csv')
        merged_df.to_csv(output_file, index=False)

        return {"status": "success", "message": f"Data processed and saved to {output_file}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Define route
@app.route('/run-etl', methods=['GET'])
def run_etl():
    result = etl_pipeline()
    return jsonify(result)

# Run the Flask app
if __name__ == '__main__':
    # Ensure the data directory exists for testing
    os.makedirs(DATA_DIR, exist_ok=True)
    app.run(debug=True)
