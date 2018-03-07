# -*- coding: utf-8 -*-
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
from urllib2 import urlopen
from bs4 import BeautifulSoup
#按照书的序号往后下载书籍
for i in range(1, 10):  #183--200 1069--1073   1646-1650 1690-1692

    try:
        iss = str(i)
        html00 = 'http://www.gutenberg.org/ebooks/' + iss
        # print html00
        html = urlopen(html00)
        bsObj = BeautifulSoup(html)
        namesss = bsObj.findAll("td", {"property": "dcterms:format"})[2].findAll("a")[0]
        sss = namesss['href']
        # print namesss
        print i
        sss1 = "http://" + sss[2:]
        # os.system("wget %s" % sss1)
        print sss1
        mkpath = "ebook/"
        if  os.path.exists(mkpath):
            filename ="ebook/book" + iss + ".epub"                      #存储路径
            urllib.urlretrieve(sss1,filename)
        else:
            os.makedirs(mkpath)
            filename = "ebook/book" + iss + ".epub"  # 存储路径
            urllib.urlretrieve(sss1, filename)
    except Exception, e:
        # 没有提取到简介，则简介为空
        i = i
        print "无此书本",i
    finally:
        pass


