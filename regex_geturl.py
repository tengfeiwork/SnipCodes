# -*- coding:utf-8 -*-

import os
import re
import requests as rq


def findurls(src, pattern):
    rexp = re.compile(pattern)

    with open(src,"r") as srcp:
        for line in srcp:
            tmp = rexp.search(line)
            if tmp:
                yield tmp


src = "./AUTOSAR.html"
dest = "./outfile.txt"
pattern = r"https://.+((\.zip)|(\.pdf))"

with open(dest,"w+") as destp:
    for url in findurls(src, pattern):
        destp.write(url.group()+"\n")
        

'''
with open(dest,"r") as urlp:
    for url in urlp:
        print url
        #rq.get(url).content()
'''
