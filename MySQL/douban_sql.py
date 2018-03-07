# -*- coding:utf8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import warnings
warnings.filterwarnings("ignore")
import MySQLdb
import MySQLdb.cursors


#链接数据库
db = MySQLdb.connect(host='localhost',user='root',passwd='****',db='moves',port=3306,charset='utf8')
db.autocommit(True)
cursor = db.cursor()

#打开豆瓣爬取的电影数据
count=0
fr = open('douban_movies.txt','r')
for lines in fr:
    count += 1
    print count
    if count == 1:
        continue

    line = lines.strip().split('^')
    print line[0]
    cursor.execute("insert into movies_runtime(title,urls,runtime) values(%s, %s, %s)", [line[0], line[2], line[-1] ])

fr.close()
# 关闭数据库
db.close()
cursor.close()