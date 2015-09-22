#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
print os.getcwd()
os.chdir("D:\\aa\\bb")

pattern = "ppppp"
replacement = "rrrrr"

for i,j,k in os.walk('.'):
    if i == '.':
        files = k

for f in files:
    pos = f.find(pattern)
    if pos == -1:
        continue
    
    prefix = f[:pos]
    print prefix
    
    suffix = f[(pos + len(pattern)):]
    print suffix
    
    if not replacement:
        newf = prefix + replacement + suffix
    else:
        newf = prefix + suffix
        
    os.rename(f, newf)
    print f + " ==> " + newf
    

