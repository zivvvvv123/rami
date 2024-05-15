from bs4 import BeautifulSoup
import json
import re

# Read the HTML file
html_file = "C:/Users/zivit/Desktop/rami/src/pages/fruits and vegetables.html"
with open(html_file, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all product details containers
product_containers = soup.find_all('div', class_='product details product-item-details')

# Initialize list to store parsed products
parsed_products = []

# Function to remove non-numeric characters from a string
def clean_price(price_str):
    return re.sub(r'[^0-9.]', '', price_str)

# Extract product details from each container
for container in product_containers:
    # Extract product name
    product_name = container.find('strong', class_='product-item-name').text.strip()
    
    # Extract price
    price = container.find('span', class_='price').text.strip()
    # Clean the price string
    price = clean_price(price)
    
    # Extract additional description
    additional_description = container.find('div', class_='product-additional-description').text.strip()

    parsed_products.append({
        'product_name': product_name,
        'price': price,
        'additional_description': additional_description
    })

# Write the parsed products to a JSON file
output_file = "C:/Users/zivit/Desktop/rami/src/output/fruits and vegetables.json"
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(parsed_products, json_file, ensure_ascii=False, indent=4)

print("Parsing and writing to JSON completed successfully.")
