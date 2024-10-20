'''
    Get latest subscription from mibei77
'''
import os
import requests
from bs4 import BeautifulSoup as BS


url = 'https://www.mibei77.com'

# get latest sub page url
wb_data = requests.get(url)
soup = BS(wb_data.text, 'html.parser')
latest_article = soup.body.find_all('article', class_='post-0')[0]
latest_sub_page = latest_article.find_all('a')[0].get('href')
print(f'last subscription page: {latest_sub_page}')

# get latest subscription url
wb_data = requests.get(latest_sub_page)
soup = BS(wb_data.text, 'html.parser')
post = soup.find('div', id='post-body')

latest_sub_url = ''
for p in post.find_all('p'):
    if 'mibei77.com/' in p.text and '.txt' in p.text:
        latest_sub_url = p.text

print(f'last subscription: {latest_sub_url}')

# download latest subscription to local
latest_sub = requests.get(latest_sub_url)
local_file = f"{os.path.abspath('.')}{os.path.sep}latest_sub_mibei.txt"
open(local_file, 'wb').write(latest_sub.content)
print(f'last subscription saved to {local_file}')