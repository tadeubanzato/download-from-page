#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# download-from-page.py

import os
import requests
import html5lib
from bs4 import BeautifulSoup
import inquirer


options = ['Images only', 'CSS only', 'All (Images and CSS)']
questions = [
    inquirer.List('selected',
                message="What you want to download?",
                choices=options,
                ),
]
answers = inquirer.prompt(questions)

print(answers['selected'])
# print(answers['objects'])
if 'images' in answer.lower():
    objects = ['.svg','.jpg','.png','.gif']
elif 'all' in answer.lower():
    objects = ['.svg','.jpg','.png','.gif','css']
elif 'css' in answer.lower():
    objects = ['css']
    