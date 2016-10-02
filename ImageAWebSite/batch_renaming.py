# -*- coding: utf-8 -*-

import os

path = '/Users/voidhug/Desktop/overbuild'

for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)) and '.' not in file:
        new_file_name = file + '.html'
        os.rename(os.path.join(path, file), os.path.join(path, new_file_name))

