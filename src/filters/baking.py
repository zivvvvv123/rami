from bs4 import BeautifulSoup
import json

# Function to clean the text by removing unwanted characters
def clean_text(text):
    return text.replace('\u200f', '').strip()

# Read HTML file
html_file = "C:/Users/zivit/Desktop/rami/src/pages/baking.html"
with open(html_file, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize list to store parsed products
parsed_products = []

# Find all product details
product_containers = soup.find_all('div', class_='product-item-info')

# Iterate through each product detail
for detail in product_containers:
    # Extract the discount description if available
    discount_descr = detail.find('span', class_='discount_descr')
    discount = clean_text(discount_descr.text) if discount_descr else ''

    # Extract price
    price = detail.find('span', class_='price-wrapper').text
    price = clean_text(price)

    # Extract unit price (base price) if available
    baseprice_div = detail.find('div', class_='baseprice')
    unit_price = ''
    if baseprice_div:
        baseprice_span = baseprice_div.find('span', class_='price')
        if baseprice_span:
            unit_price = clean_text(baseprice_span.text)

    # Extract product name and link
    product_name_tag = detail.find('strong', class_='product-item-name')
    product_name = clean_text(product_name_tag.text)
    product_link = product_name_tag.find('a')['href']

    # Extract additional description
    additional_description = clean_text(detail.find('div', class_='product-additional-description').text)

    # Extract quantity and brand if available
    amount_span = detail.find('span', class_='amount')
    quantity = clean_text(amount_span.text) if amount_span else ''
    brand_span = detail.find('span', class_='brand')
    brand = clean_text(brand_span.text) if brand_span else ''

    # Extract image URL
    image_tag = detail.find('img', class_='product-image-photo')
    image_url = image_tag['src'] if image_tag else ''

    # Create product dictionary
    product = {
        'product_name': product_name,
        'price': price,
        'unit_price': unit_price,
        'discount': discount,
        'product_link': product_link,
        'additional_description': additional_description,
        'quantity': quantity,
        'brand': brand,
        'image_url': image_url
    }

    # Append product to list of parsed products
    parsed_products.append(product)

# Save parsed products to JSON file
output_file = "C:/Users/zivit/Desktop/rami/src/output/baking.json"
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(parsed_products, json_file, ensure_ascii=False, indent=4)

print("Filtered baking data saved to", output_file)
