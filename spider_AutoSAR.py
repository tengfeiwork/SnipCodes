import string
import re
import urllib2

old_start_url = r"https://www.autosar.org/nc/document-search/?tx_sysgsearch_pi1[category][{topclass}]={topclass}&tx_sysgsearch_pi1[category][{subclass}]={subclass}&tx_sysgsearch_pi1[query]="
new_start_url = r"https://www.autosar.org/nc/document-search/?tx_sysgsearch_pi1[category][26]=26&tx_sysgsearch_pi1[category][59]=59&tx_sysgsearch_pi1[query]="
test_url = r"http://www.baidu.com"

print "AutoSAR spider is ready, preparing for data..."
new_url = old_start_url.format(topclass=26,subclass = 59)
print "url:",new_url
try:
    mypage = urllib2.urlopen(test_url)
except urllib2.URLError as idx:
    print "url error:",idx
finally:
    print "open url ok!"

'''
html = mypage.read()

with open("out.html","a+") as f:
    f.write(html)
'''
