from bs4 import BeautifulSoup
import json
import re


html_file = "C:/Users/zivit/Desktop/rami/src/pages/one time use.html"
with open(html_file, "r", encoding="utf-8") as file:
    html_content = file.read()


soup = BeautifulSoup(html_content, 'html.parser')


product_containers = soup.find_all('div', class_='product-item-info')


parsed_products = []


def clean_price(price_str):
    return re.sub(r'[^0-9.]', '', price_str)


def clean_text(text):
    return text.strip()


for container in product_containers:
    
    product_name = container.find('a', class_='product-item-link').text.strip()
    
    
    price = container.find('span', class_='price').text.strip()
    
    price = clean_price(price)
    
    
    additional_description = container.find('div', class_='product-additional-description').text.strip()
    
    additional_description = clean_text(additional_description)
    
    
    brand_span = container.find('span', class_='brand')
    brand = brand_span.text.strip() if brand_span else ''
    
    brand = clean_text(brand)
    
    
    discount_descr = container.find('span', class_='discount_descr')
    discount = discount_descr.text.strip() if discount_descr else ''
    
    discount = clean_text(discount)
    
    
    image_tag = container.find('img', class_='product-image-photo')
    image_url = image_tag['src'] if image_tag and 'src' in image_tag.attrs else ''

    parsed_products.append({
        'product_name': clean_text(product_name),
        'price': price,
        'additional_description': additional_description,
        'brand': brand,
        'discount': discount,
        'image_url': image_url
    })


output_file = "C:/Users/zivit/Desktop/rami/src/output/one_time_use.json"
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(parsed_products, json_file, ensure_ascii=False, indent=4)

print("Parsing and writing to JSON completed successfully.")
