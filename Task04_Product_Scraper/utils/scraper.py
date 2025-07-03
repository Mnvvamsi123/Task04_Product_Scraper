import requests
from bs4 import BeautifulSoup

def get_product_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.select('.product_pod'):
        name = item.h3.a['title']
        price = item.select_one('.price_color').text
        rating = item.select_one('p.star-rating')['class'][1]

        products.append({
            'Name': name,
            'Price': price,
            'Rating': rating
        })

    return products
