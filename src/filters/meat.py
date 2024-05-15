from bs4 import BeautifulSoup
import json

# Read HTML file
html_file = "C:/Users/zivit/Desktop/rami/src/pages/meat.html"
with open(html_file, "r", encoding="utf-8") as file:
    html_content = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize list to store parsed products
parsed_products = []

# Find all product details
product_details = soup.find_all('div', class_='product details product-item-details')

# Iterate through each product detail
for detail in product_details:
    # Extract price
    price_span = detail.find('span', class_='price').text.strip()
    price = ''.join(filter(lambda x: x.isdigit() or x == '.', price_span))

    # Extract product name
    product_name = detail.find('strong', class_='product-item-name').text.strip()

    # Extract additional description
    additional_description = detail.find('div', class_='product-additional-description').text.strip()

    # Create product dictionary
    product = {
        'product_name': product_name,
        'price': price,
        'additional_description': additional_description
    }

    # Append product to list of parsed products
    parsed_products.append(product)

# Save parsed products to JSON file
output_file = "C:/Users/zivit/Desktop/rami/src/output/meat.json"
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(parsed_products, json_file, ensure_ascii=False, indent=4)

print("Filtered meat data saved to", output_file)
