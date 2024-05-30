from bs4 import BeautifulSoup
import json


def clean_text(text):
    return text.replace('\u200f', '').strip()


html_file = "C:/Users/zivit/Desktop/rami/src/pages/meat.html"
with open(html_file, "r", encoding="utf-8") as file:
    html_content = file.read()


soup = BeautifulSoup(html_content, 'html.parser')


parsed_products = []


product_infos = soup.find_all('div', class_='product-item-info')


for info in product_infos:
    
    image_tag = info.find('img', class_='product-image-photo')
    image_url = image_tag['src'] if image_tag else ''

    
    detail = info.find('div', class_='product details product-item-details')

    
    discount_descr = detail.find('span', class_='discount_descr')
    discount = clean_text(discount_descr.text) if discount_descr else ''

    
    price_span = detail.find('span', class_='price').text.strip()
    price = ''.join(filter(lambda x: x.isdigit() or x == '.', price_span))

    
    baseprice_div = detail.find('div', class_='baseprice')
    unit_price = ''
    if baseprice_div:
        baseprice_span = baseprice_div.find('span', class_='price')
        if baseprice_span:
            unit_price = clean_text(baseprice_span.text)

    
    product_name_tag = detail.find('strong', class_='product-item-name')
    product_name = clean_text(product_name_tag.text)
    product_link = product_name_tag.find('a')['href']

    
    additional_description = clean_text(detail.find('div', class_='product-additional-description').text)

    
    amount_span = detail.find('span', class_='amount')
    quantity = clean_text(amount_span.text) if amount_span else ''
    brand_span = detail.find('span', class_='brand')
    brand = clean_text(brand_span.text) if brand_span else ''

    
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

    
    parsed_products.append(product)


output_file = "C:/Users/zivit/Desktop/rami/src/output/meat.json"
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(parsed_products, json_file, ensure_ascii=False, indent=4)

print("Filtered meat data saved to", output_file)
