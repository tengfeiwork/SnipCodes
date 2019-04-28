#!python2
# -*- coding:utf-8 -*-

import string
import re
import urllib2

start_url = r"https://www.autosar.org/nc/document-search/?tx_sysgsearch_pi1[category][26]=26&tx_sysgsearch_pi1[category][59]=59&tx_sysgsearch_pi1[query]="

print "AutoSAR spider is ready, preparing for data..."

mypage = urllib2.urlopen(start_url)
html = mypage.read()

with open("out.html","a+") as f:
    f.write(html)
