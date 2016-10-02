# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import os

path = '/Users/voidhug/Desktop/overbuild'

for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)) and '.html' in file:
        file = os.path.join(path, file)
        with open(file) as out:
            content = out.read()
            soup = BeautifulSoup(content, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                if 'href' in link.attrs:
                    if '.' not in link['href'] and '#' not in link['href'] and link['href'] != 'javascript:void(0)':
                        link['href'] += '.html'
        fout = open(file, 'w')
        fout.write(str(soup))
        fout.close()

