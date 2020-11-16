#!python2
# -*- coding:utf-8 -*-

import string
import os
import time
import re
import urllib2
import urllib
import json
from bs4 import BeautifulSoup as mybs


cat_start_url = r"https://www.autosar.org/nc/document-search/?tx_sysgsearch_pi1[category][{topclass}]={topclass}&tx_sysgsearch_pi1[category][{subclass}]={subclass}&tx_sysgsearch_pi1[query]="

top = 26
sub = [ 68,69,70,71,72,\
        59,60,61,62,63,64,65,66,67,\
        55,56,57,58,113,\
        106,107,108,109,110,\
        111]

file_counter = 0

print "AutoSAR spider is ready, preparing for data..."
#print "scrapy url: ",new_start_url

'''
def openjson(src,mode):
    with open(src,mode) as load_f:
        load_dict = json.load(load_f, "utf-8")
        return load_dict
'''

def get_mainpageurl(url, top, sub):
    return url.format(topclass = str(top), subclass = str(sub))

def get_nextpage(html):
    base = get_baseurl(html)
    soup = mybs(html, 'lxml')
    next_url_obj = soup.find("a", id = "btn-load-more-1")
    if next_url_obj:
        next_url = next_url_obj.get('href')
        print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
        print "btn %s has been found ..................."%(next_url[-1])
        nextpage_url = base + next_url
        print nextpage_url
        return get_html(nextpage_url)
    else:
        print "no more next page ......"

def find_allpages(html):
    while html:
        print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
        print "getting next page ......"
        html = get_nextpage(html)
        yield html


#def get_fileurl(pageurl):
def get_fileurl(html):
    pattern = r'''("[a-zA-Z]*/.+(?:\.zip|\.pdf)")+'''
    return re.finditer(pattern, html)

def write2disk(url):
    f = urllib2.urlopen(url) 
    data = f.read() 
    fname = url.split('/')[-1]
    dirx = r"./AutoSAR/"

    if not os.path.exists(dirx):
        os.makedirs(dirx)

    pathx = dirx + fname
    print pathx
    with open(pathx, "wb") as filex:     
        filex.write(data)

def get_allfileurl(html):
    base_url = get_baseurl(html)
    '''
    print "###########################################################################"
    print page_url
    print "###########################################################################"
    '''
    file_urls = get_fileurl(html)
    for urlx in file_urls:
        global file_counter
        file_counter = file_counter + 1
        print "--- file No.", file_counter
        combine_url = base_url + eval(urlx.group())
        print combine_url
        #urllib.urlretrieve(combine_url, combine_url.split('/')[-1])
        write2disk(combine_url)
    time.sleep(2)


def get_baseurl(html):
    soup = mybs(html, 'lxml')
    return soup.find("base").get('href')

def get_html(page_url):
    response = urllib2.urlopen(page_url, timeout=30)
    html = response.read()
    return html

def create_dirs(folder):
    pass

def mainfunc(url, top, sub):
    '''
    src = r"./index.json"
    mode = "r"
    index = openjson(src, mode)
    for num, name in index['class'].items():
        folder = num+'_'+name
        create_dirs(folder)
    for classx, subclass in index['26'].items():
        page_url = get_pageurl(para[])
    '''
    for subx in sub:
        print "###########################################################################"
        print "\n"
        print "sub-class:",subx
        mainpage_url = get_mainpageurl(url, top,subx)
        print "###########################################################################"
        print mainpage_url
        print "###########################################################################"

        html = get_html(mainpage_url)
        get_allfileurl(html)
        for subpage in find_allpages(html):
            if subpage:
                get_allfileurl(subpage)
        
mainfunc(cat_start_url, top, sub)




'''
try:
    print "----------------------------------------------------------------------"
    print "opening ....... "

    response = urllib2.urlopen(new_start_url, timeout=30)
    print "----------------------------------------------------------------------"
    print "reading page ......"
    html = response.read()
    print "----------------------------------------------------------------------"
    print "read over ..... "
  
except urllib2.URLError as e:
    print e

print "----------------------------------------------------------------------"
print "parsering ..... "
soup = mybs(html, 'lxml')
base = soup.find("base").get('href')
target = soup.find("a", id = "btn-load-more-1").get('href')
combine = base + target
print "----------------------------------------------------------------------"
print combine
'''
