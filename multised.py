#!/usr/bin/env python

import os
import sys

string0 = 'return False'
string1 = 'elif data.find(TFTPERR2) >= 0:'
string2 = 'return22 False'

str3 = '                elif data.find(TFTPERR3) >= 0:\n'
str4 = '                    return False\n'

def dofile(f):
    print f
    with open(f, 'r') as fh:
        content = fh.readlines()

    match = False
    for n in range(len(content)):
        if content[n].find(string0) >= 0:
            if content[n+1].find(string1) >= 0:
                if content[n+2].find(string2) >= 0:
                    match = True
                    break

    if match:
        # del content[n+2]
        content.insert(n+3, str4)
        content.insert(n+3, str3)

        with open(f, 'w') as fh:
            fh.writelines(content)
    else:
        print "        ----  Do not math the pattern  ----"

with open('filelist') as fd:
    flist = fd.readlines()    

for f in flist:
    dofile(f.strip('\n'))


