# -*- coding:utf-8 -*-

import os
import re
import requests as rq

infile = "./AUTOSAR.html"
outfile = "./outfile.txt"
#infilep = open(infile,"r")
outfilep = open(outfile,"w+")

pattern = r"https://.+((\.zip)|(\.pdf))"
rexp = re.compile(pattern)

#try:
with open(infile,"r") as infilep:
    for line in infilep:
        tmp = rexp.search(line)
        if tmp:
            outfilep.write(tmp.group()+"\n")
'''
finally:
    infilep.close()
    '''

outfilep.close()


urlp = open(outfile,"r")

for url in urlp:
    print url
    #rq.get(url).content()

urlp.close()
