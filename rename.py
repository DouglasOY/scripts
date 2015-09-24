#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

directory = "D:\\aa\\bb"
pattern = "ppppp"
replacement = "rrrrr"

os.chdir(directory)
for i,j,k in os.walk('.'):
    if i == '.':
        files = k

print os.getcwd()
for f in files:
    pos = f.find(pattern)
    if pos == -1:
        continue
    
    prefix = f[:pos]
    suffix = f[(pos + len(pattern)):]
    newf = prefix + replacement + suffix
        
    os.rename(f, newf)
    print f + " ==> " + newf


