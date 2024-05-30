from bs4 import BeautifulSoup
import json

# Read HTML file
html_file = "C:/Users/zivit/Desktop/rami/src/pages/meholet.html"
with open(html_file, "r", encoding="utf-8") as file:
    html_content = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize list to store parsed products
parsed_products = []

# Find all product item info
product_infos = soup.find_all('div', class_='product-item-info')

# Iterate through each product info
for info in product_infos:
    # Extract product image URL
    image_tag = info.find('img', class_='product-image-photo')
    image_url = image_tag['src'] if image_tag else ''

    # Extract product details
    detail = info.find('div', class_='product details product-item-details')

    # Extract discount description if available
    discount_descr = detail.find('span', class_='discount_descr')
    discount = discount_descr.text.strip() if discount_descr else ''

    # Extract price
    price_span = detail.find('span', class_='price').text.strip()
    price = ''.join(filter(lambda x: x.isdigit() or x == '.', price_span))

    # Extract unit price (base price) if available
    baseprice_div = detail.find('div', class_='baseprice')
    unit_price = ''
    if baseprice_div:
        baseprice_span = baseprice_div.find('span', class_='price')
        if baseprice_span:
            unit_price = baseprice_span.text.strip()

    # Extract product name and link
    product_name_tag = detail.find('strong', class_='product-item-name')
    product_name = product_name_tag.text.strip() if product_name_tag else ''
    product_link = product_name_tag.find('a')['href'] if product_name_tag and product_name_tag.find('a') else ''

    # Extract additional description
    additional_description = detail.find('div', class_='product-additional-description').text.strip() if detail.find('div', class_='product-additional-description') else ''

    # Extract quantity and brand if available
    amount_span = detail.find('span', class_='amount')
    quantity = amount_span.text.strip() if amount_span else ''
    brand_span = detail.find('span', class_='brand')
    brand = brand_span.text.strip() if brand_span else ''

    # Create product dictionary
    product = {
        'product_name': product_name,
        'image_url': image_url,
        'price_per_kg': price,
        'unit_price': unit_price,
        'discount': discount,
        'product_link': product_link,
        'additional_description': additional_description,
        'quantity': quantity,
        'brand': brand
    }

    # Append product to list of parsed products
    parsed_products.append(product)

# Save parsed products to JSON file
output_file = "C:/Users/zivit/Desktop/rami/src/output/meholet.json"
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(parsed_products, json_file, ensure_ascii=False, indent=4)

print("Filtered meholet data saved to", output_file)
