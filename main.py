import requests
from bs4 import BeautifulSoup
import lxml

url = "https://kups.club/"
agent = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
response = requests.get(url, headers=agent)
soup = BeautifulSoup(response.text, "lxml")

all_product = soup.find('div', class_='row mt-4')
list_product = all_product.find_all('div', class_='card h-100')

for elem in list_product:
    title = elem.find('h3', class_="card-title")
    price = elem.find('p', class_="card-text")
    # print(title.text)
    with open("product.txt", "a", encoding='UTF8') as f:
        f.write(f'{title.text}, "\n"')
        f.write(f'{price.text}, "\n"')



