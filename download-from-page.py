#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# download-from-page.py

import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.uol.com.br'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')

img_tags = soup.find_all('img')
urls = [img['src'] for img in img_tags]

for url in urls:
    
    
    
    
    filename = re.search(r'/(jpg|gif|png|svg|webp)$', url)
    print(filename)
    if not filename:
         print("Regex didn't match with the url: {}".format(url))
         continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            url = '{}{}'.format(site, url)
            print(url)
        response = requests.get(url)
        f.write(response.content)


open('facebook.ico', 'wb').write(r.content)