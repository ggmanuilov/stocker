#!/usr/bin/env python3
# zipman
# -*- coding: utf-8 -*-

import os
import sys
import zipfile
import image_thumb
import vektor_stock
from tkinter import filedialog
import pprint

scan_dir = filedialog.askdirectory()
# scan_dir = '/home/gregman/PycharmProjects/stock/files'

thumb = image_thumb.Thumb()

files = list(filter(lambda d: not os.path.isdir(os.path.join(scan_dir, d)) or not str(d).endswith('.zip'), os.listdir(scan_dir)))
files.sort()

for f in list(files):
    postfix = thumb.get_postfix(os.path.join(scan_dir, f), vektor_stock.VektorStock())
    if str(f).endswith(postfix):
        files.remove(f)

patterns = list(map(lambda f: ".".join(f.split('.')[:-1]), files))

for f in list(patterns):
    postfix = thumb.get_postfix(os.path.join(scan_dir, f), vektor_stock.VektorStock())
    if str(f).endswith('.zip'):
        patterns.remove(f)

for p in patterns:
    files_archive = list(filter(lambda f: str(f).startswith(p + '.'), files))

    # create preview image
    for n in files_archive:
        if os.path.join(scan_dir, n).endswith(('.jpeg', '.jpg')):
            thumb.create(os.path.join(scan_dir, n), scan_dir, vektor_stock.VektorStock())

    pprint.pprint(files_archive)

    # zip files
    zipf = zipfile.ZipFile(os.path.join(scan_dir, p + '.zip'), 'w', zipfile.ZIP_DEFLATED)
    for n in files_archive:
        zipf.write(os.path.join(scan_dir, n), n)
    # zipf.close()

sys.exit(0)
