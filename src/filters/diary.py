from bs4 import BeautifulSoup
import json
import re

def clean_price(price_str):
    return re.sub(r'[^0-9.]', '', price_str)

def clean_text(text):
    return text.strip()

html_file = "C:/Users/zivit/Desktop/rami/src/pages/diary.html"
with open(html_file, "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

product_containers = soup.find_all('div', class_='product-item-info')

parsed_products = []

for container in product_containers:
    product_name_tag = container.find('strong', class_='product-item-name')
    product_name = product_name_tag.text.strip() if product_name_tag else ''

    price_tag = container.find('span', class_='price')
    price = clean_price(price_tag.text.strip()) if price_tag else ''

    additional_description_tag = container.find('div', class_='product-additional-description')
    additional_description = clean_text(additional_description_tag.text.strip()) if additional_description_tag else ''

    brand_tag = container.find('span', class_='brand')
    brand = clean_text(brand_tag.text.strip()) if brand_tag else ''

    discount_tag = container.find('span', class_='discount_descr')
    discount = clean_text(discount_tag.text.strip()) if discount_tag else ''

    image_tag = container.find('img', class_='product-image-photo')
    image_url = image_tag['src'] if image_tag and 'src' in image_tag.attrs else ''

    parsed_products.append({
        'product_name': product_name,
        'price': price,
        'additional_description': additional_description,
        'brand': brand,
        'discount': discount,
        'image_url': image_url
    })

output_file = "C:/Users/zivit/Desktop/rami/src/output/diary.json"
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(parsed_products, json_file, ensure_ascii=False, indent=4)

print("Parsing and writing to JSON completed successfully.")
