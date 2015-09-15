#!/usr/bin/env python

import os
import sys

def isascii(s):
    en = 0
    for c in s:
        if ord(c) < 128:
            en += 1
    
    rate = float(en)/len(s)
    if (rate > 0.9):
        return True
    else:
        return False

def combinationfile(first, second, to):
    firstfd = file(first, 'r', 0)
    secondfd = file(second, 'r', 0)
    tofd = file(to, 'a', 0)
    
    for line in firstfd.readlines():
        tofd.write(line)    

    for i in range(10):
        tofd.write('\n')    
        
    for line in secondfd.readlines():
        tofd.write(line)    

    firstfd.close()
    secondfd.close()
    tofd.close()

def dofile(f):
    print f
    with open(f, 'r') as fh:
        content = fh.readlines()

    fen = 'en_' + f
    fcn = 'cn_' + f
    fenfd = file(fen, 'a', 0)
    fcnfd = file(fcn, 'a', 0)

    for line in content:
        if len(line) < 5:
            continue

        if isascii(line):
            fenfd.write(line + '\n')
        else:
            fcnfd.write(line + '\n')

    fenfd.close()
    fcnfd.close()

    fnew = 'new_' + f
    combinationfile(fcn, fen, fnew)
    os.remove(fen)
    os.remove(fcn)

with open('filelist') as fd:
    flist = fd.readlines()    

for f in flist:
    dofile(f.strip('\n'))


