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
product_containers = soup.find_all('div', class_='product-item-info')

# Initialize list to store parsed products
parsed_products = []

# Function to clean the text by removing unwanted characters
def clean_text(text):
    return text.replace('\u200f', '').strip()

# Function to remove non-numeric characters from a string
def clean_price(price_str):
    return re.sub(r'[^0-9.]', '', price_str)

# Extract product details from each container
for container in product_containers:
    # Extract product name
    product_name = container.find('a', class_='product-item-link').text.strip()
    
    # Extract price
    price = container.find('span', class_='price').text.strip()
    # Clean the price string
    price = clean_price(price)
    
    # Extract additional description
    additional_description = clean_text(container.find('div', class_='product-additional-description').text)

    # Extract quantity and brand if available
    amount_span = container.find('span', class_='amount')
    quantity = clean_text(amount_span.text) if amount_span else ''
    brand_span = container.find('span', class_='brand')
    brand = clean_text(brand_span.text) if brand_span else ''
    
    # Extract discount description if available
    discount_descr = container.find('span', class_='discount_descr')
    discount = clean_text(discount_descr.text) if discount_descr else ''
    
    # Extract image URL if available
    image_tag = container.find('img', class_='product-image-photo')
    image_url = image_tag['src'] if image_tag and 'src' in image_tag.attrs else ''

    parsed_products.append({
        'product_name': product_name,
        'price_per_kg': price,
        'discount': discount,
        'additional_description': additional_description,
        'quantity': quantity,
        'brand': brand,
        'image_url': image_url
    })

# Write the parsed products to a JSON file
output_file = "C:/Users/zivit/Desktop/rami/src/output/fruits and vegetables.json"
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(parsed_products, json_file, ensure_ascii=False, indent=4)

print("Parsing and writing to JSON completed successfully.")
