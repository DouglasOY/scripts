#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import chardet

directory = "D:\\computer\\vim33"
pattern = "使用脚本编写 Vim 编辑器，"
replacement = ""

os.chdir(directory)
for i,j,k in os.walk('.'):
    if i == '.':
        files = k

print os.getcwd()

for f in files:
    encodingdict = chardet.detect(f)
    if encodingdict['confidence'] < 0.9:
        continue

    fcoding = encodingdict['encoding']
    utf8f = f.decode(fcoding).encode('UTF-8')
    
    pos = utf8f.find(pattern)
    if pos == -1:
        continue

    prefix = utf8f[:pos]
    suffix = utf8f[(pos + len(pattern)):]
    utf8newf = prefix + replacement + suffix
    newf = utf8newf.decode('UTF-8').encode(fcoding)

    os.rename(f, newf)
    print f + "    ====>    " + newf



