import pdfplumber
import re
import sys
import pandas as pd

def write2file(filex, start, end):
    with pdfplumber.open(filex) as pdf:
        for pageno in range(start,end):
            page=pdf.pages[pageno] #提取pdf第17页中的表格
            for row in page.extract_tables():
                yield row
                #print(row)

def extracttable(filex, start, end, p):
    start = start-1

    with open(filex + r".txt",'w+') as txt:
        for line in write2file(filex + ".pdf",start, end):
            #print (type(line)+'\n')
            for e in line:
                # txt.write(''.join(str(e)).strip('[]')+ '\n')
                txt.write(''.join(p.sub('',str(e)))+ '\n')

            # txt.write(''.join([str(x) for x in line]))
            '''
            for e in line:
                txt.write(''.join([str(x) for x in e]))
                txt.write('\n')
            '''

def extract2excel(filex,start,end,p):
    start = start-1

    x = pd.DataFrame()

    for line in write2file(filex + ".pdf",start, end):
        x = x.append(pd.DataFrame(line))
    x.to_excel(filex+".xlsx")

# rep = re.compile(r"['\[\]]|\\n")
rep = re.compile(r"\\n")

# 这里输入   “文件名, 开始页码，结束页码”
# extracttable("26262-6-2018", 39, 43, rep)
# extract2excel("ak-egas-v6-0-en-150922_1_marked_by_tf", 24, 28, rep)
extract2excel(r"GB8001", 78, 84, rep)
