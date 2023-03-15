#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# download-from-page.py

import os
import requests
import html5lib
from bs4 import BeautifulSoup

def download(objects,folder):
    cheked = os.path.isdir(folder)
    if cheked:
        print(folder, 'Folder already exists.')
    else:
        os.makedirs(folder)
        print(f'Created folder : {folder}')
    
    for object in objects:
        ext_check = ['.svg','.jpg','.png','.gif']
        for ext in ext_check:
            if ext in object:
                file_url = object.split(ext)[0] + ext
                file_name = object.split(ext)[0].split('/')[-1] + ext
                print(f'Downloading: {file_name}')
                
                try:
                    r = requests.get(file_url, allow_redirects=True)
                    open(f'{folder}/{file_name}', 'wb').write(r.content)
                except:
                    print('Skip')
 
                
if __name__ == '__main__':
    folder = 'downloads'
    
    ### External file
    # with open('html_file.html', 'r') as f:
    #     r = f.read()
            
    url = 'https://www.uol.com.br'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    img_tags = soup.find_all('img')
    objects = [img['src'] for img in img_tags]
    
    download(objects,folder)