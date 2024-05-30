from bs4 import BeautifulSoup
import json

# Read HTML file
html_file = "C:/Users/zivit/Desktop/rami/src/pages/freezables.html"
with open(html_file, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all product details containers
product_containers = soup.find_all('div', class_='product-item-info')

# Initialize list to store parsed products
parsed_products = []

# Extract product details from each container
for container in product_containers:
    # Extract product name
    product_name = container.find('strong', class_='product-item-name').text.strip()
    
    # Extract price
    price = container.find('span', class_='price').text.strip()
    
    # Extract additional description
    additional_description = container.find('div', class_='product-additional-description').text.strip()
    
    # Extract brand
    brand = container.find('span', class_='brand').text.strip() if container.find('span', class_='brand') else ''
    
    # Extract discount
    discount = container.find('span', class_='discount_descr').text.strip() if container.find('span', class_='discount_descr') else ''

    # Extract image URL
    image_url = container.find('img', class_='product-image-photo')['src'] if container.find('img', class_='product-image-photo') else ''

    parsed_products.append({
        'product_name': product_name,
        'price': price,
        'additional_description': additional_description,
        'brand': brand,
        'discount': discount,
        'image_url': image_url
    })

# Write the parsed products to a JSON file
output_file = "C:/Users/zivit/Desktop/rami/src/output/freezeables.json"
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(parsed_products, json_file, ensure_ascii=False, indent=4)

print("Parsing and writing to JSON completed successfully.")
