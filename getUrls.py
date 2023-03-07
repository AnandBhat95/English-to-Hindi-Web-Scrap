import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.classcentral.com/',
}

cookies = {
    'session_id': 'a39c87561d182f837bcc2327ad',
}

url = 'https://www.classcentral.com'

response = requests.get(url,headers=headers,cookies=cookies)

soup = BeautifulSoup(response.content,'html.parser')

with open('index.html','w') as f:
    f.write(soup.prettify())

all_links = soup.find_all('a')
hrefs = list(map(lambda x:x.get('href'),all_links))
full_url = [i for i in hrefs if i.startswith('http')]
relative_path = [i for i in hrefs if i.startswith('/')]
relative_path = list(set(relative_path))
rels = [i.split('/')[1].strip() for i in relative_path]
rels = list(set(rels))
for i in relative_path:
    res = requests.get(url+i,headers=headers,cookies=cookies)
    soup = BeautifulSoup(res.content,'html.parser')
    fname = i.split('/')[1].strip()
    if not fname:
        continue
    
    with open(f'{fname}.html','w',encoding="utf-8") as f:
        f.write(soup.prettify())
    