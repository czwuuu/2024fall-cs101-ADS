import requests
from bs4 import BeautifulSoup

url = 'https://oi-wiki.org'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href:
            print(href)
else:
    print(f"请求失败，状态码：{response.status_code}")