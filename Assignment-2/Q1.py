# Sample sales data
sales_data = [
    {"product_name": "Laptop", "category": "Electronics", "units_sold": 10, "unit_price": 800.0},
    {"product_name": "Smartphone", "category": "Electronics", "units_sold": 25, "unit_price": 500.0},
    {"product_name": "Tablet", "category": "Electronics", "units_sold": 15, "unit_price": 300.0},
    {"product_name": "Headphones", "category": "Accessories", "units_sold": 30, "unit_price": 50.0},
    {"product_name": "Keyboard", "category": "Accessories", "units_sold": 20, "unit_price": 30.0},
    {"product_name": "Monitor", "category": "Electronics", "units_sold": 5, "unit_price": 200.0},
]

# Initialize variables to store insights
total_sales = 0.0
product_sales = {}
sales_by_category = {}
units_sold_by_category = {}

# Process the sales data
for record in sales_data:
    # Calculate the total sales for the record
    sales = record["units_sold"] * record["unit_price"]
    
    # Add to the total sales
    total_sales += sales
    
    # Update product sales
    product_sales[record["product_name"]] = sales
    
    # Update sales by category
    if record["category"] in sales_by_category:
        sales_by_category[record["category"]] += sales
        units_sold_by_category[record["category"]] += record["units_sold"]
    else:
        sales_by_category[record["category"]] = sales
        units_sold_by_category[record["category"]] = record["units_sold"]

# Calculate average sales per product
average_sales_per_product = total_sales / len(sales_data)

# Calculate average sales per category
average_sales_per_category = {}
for category in sales_by_category:
    average_sales_per_category[category] = sales_by_category[category] / units_sold_by_category[category]

# Determine the top-selling product
top_selling_product = max(product_sales, key=product_sales.get)

# Display the insights
print(f"Total Sales: ${total_sales:.2f}")

print(f"Average Sales per Product: ${average_sales_per_product:.2f}")

print(f"Top-Selling Product: {top_selling_product} with sales of ${product_sales[top_selling_product]:.2f}")

print("Sales by Category:")
for category, sales in sales_by_category.items():
    print(f"  {category}: ${sales:.2f}")
    
print("Average Sales per Unit by Category:")
for category, avg_sales in average_sales_per_category.items():
    print(f"  {category}: ${avg_sales:.2f}")