#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# download-from-page.py

import os
import requests
import html5lib
from bs4 import BeautifulSoup

def check_folder(folder):
    folder = ('downloads')
    check_folder = os.path.isdir(folder)
    return check_folder 

def main(objects,folder):
    for object in objects:
        
        print(object)
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
                    print('skip')
                
if __name__ == '__main__':
    folder = ('downloads')
    checked = check_folder(folder)
    
    if checked:
        print(folder, "folder already exists.")
    else:
        os.makedirs(folder)
        print("created folder : ", folder)
    
    url = 'https://www.uol.com.br'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    img_tags = soup.find_all('img')
    objects = [img['src'] for img in img_tags]
    
    main(objects,folder)