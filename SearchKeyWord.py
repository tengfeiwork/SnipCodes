#!python3
# -*- code=utf-8 -*-

import sys
import fnmatch
import os
import re
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter

def parserpdf2txt(bread, outfile):
    '''
    convert pdf to txt
    '''
    # print(bread, outfile)
    outfp = open(outfile, 'wb+')
    # input option
    pagenos = set()

    # output option
    laparams = LAParams()

    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, outfp, codec='utf-8' ,laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    with open(bread, 'rb') as fp:
        for page in PDFPage.get_pages(fp, pagenos):
            interpreter.process_page(page)

    device.close()
    outfp.close()
    return


def GetTxtFiles(path, files):
    '''
    get file names list from txt folder
    '''
    # txtfiles = [fnmatch.fnmatch(filex, '*.txt').split('.')[0] for filex in files]
    txtfiles = [filex.split('.')[0] for filex in fnmatch.filter(files, '*.txt')]
    return txtfiles

def GetPdfFiles(path, files):
    '''
    get file name list from pdf folder
    '''
    # pdffiles = [fnmatch.fnmatch(filex, '*.pdf').split('.')[0] for filex in files]
    pdffiles = [filex.split('.')[0] for filex in fnmatch.filter(files, '*.pdf')]
    return pdffiles

def Convert2txt(srcpath, destpath, fix):
    '''
    convert pdf to txt, if txt not exist in destpath
    '''
    srcfiles = [filex.split('/')[-1] for filex in os.listdir(srcpath)]
    destfiles = [filex.split('/')[-1] for filex in os.listdir(destpath)]
    pdffiles = GetPdfFiles(srcpath, srcfiles)
    txtfiles = GetTxtFiles(destpath, destfiles)
    for pdfx in pdffiles:
        if pdfx not in txtfiles:
            print("converting %s.pdf ......"%pdfx)
            parserpdf2txt(srcpath + pdfx + '.pdf', destpath + pdfx +'.txt')

def SearchKey(path, filex, keyw):
    '''
    search key words from filex, return "found" if hit
    '''
    found = False
    p = re.compile(keyw + r'\b')
    with open(path+filex, 'r',encoding='utf-8') as fp:
        found = (p.search(fp.read()) != None)
    return found

def SearchFiles(path, keyw):
    '''
    iterate search “path” search str from all txt files, return txt file name if hit
    '''
    for filex in os.listdir(path):
        print ("searching file %s..."%filex)
        if SearchKey(path, filex, keyw):
            yield filex

def SearchStr(keyw, srcpath, destpath, nameonly = True, fix='pdf'):
    '''
    search str from txt files, if not exist, convert correponding pdf to txt
    '''
    print("searching str ...")
    Convert2txt(srcpath, destpath, fix)
    resultfile = keyw + '.txt'
    with open(resultfile, "w") as fp:
        for resultx in SearchFiles(destpath, keyw):
            if nameonly == False:
                fp.write(os.getcwd() + '\\files\\' + resultx.split('.')[0] + '.pdf' + '\n')
            else:
                fp.write(resultx.split('.')[0] + '.pdf' + '\n')


keyw = "Overview of Functional Safety Measures in AUTOSAR"
srcpath = './files/'
destpath = './text/'

SearchStr(keyw, srcpath, destpath, nameonly=False)
