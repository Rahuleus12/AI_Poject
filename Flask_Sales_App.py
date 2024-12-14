from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

def load_and_merge_data(customers_file, products_file, sales_file):
    # Load CSV files
    customers_df = pd.read_csv(customers_file)
    products_df = pd.read_csv(products_file)
    sales_df = pd.read_csv(sales_file)

    # Merge datasets
    customer_sales_df = pd.merge(sales_df, customers_df, on="CustomerID", how="left")
    full_data_df = pd.merge(customer_sales_df, products_df, on="ProductID", how="left")

    # Add a computed column
    full_data_df['TotalPrice'] = full_data_df['Quantity'] * full_data_df['PricePerUnit']
    return full_data_df

def analyze_regional_sales(data):
    # Perform regional sales analysis
    regional_sales = data.groupby('Region')["TotalPrice"].sum().sort_values(ascending=False)
    return regional_sales.to_dict()

@app.route('/')
def index():
    # Predefined file paths
    customers_file = "data/Customers_Data.csv"
    products_file = "data/Products_Data.csv"
    sales_file = "data/Sales_Data.csv"

    try:
        # Load and analyze data
        data = load_and_merge_data(customers_file, products_file, sales_file)
        regional_sales = analyze_regional_sales(data)
        return jsonify({"regional_sales": regional_sales})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
