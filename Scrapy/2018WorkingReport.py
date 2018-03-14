#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import jieba
import jieba.analyse

from urllib2 import urlopen
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")
import json

file = open("WorkingReport.txt",'w')
news_url = "http://news.ifeng.com/a/20180305/56472392_0.shtml"
html = urlopen(news_url)
bsObj = BeautifulSoup(html)
pages = bsObj.findAll("div", {"id":"artical_real"})[0].findAll("p")
print pages
for nnn in pages:
    for mmm in nnn:
        print mmm
        str1 = type(mmm)
        try:
            file.write(mmm)
        except:
            pass
file.close()
file2 = open("WorkingReport.txt",'r')
content = file2.read()
print content
#content='中国特色社会主义是我们党领导的伟大事业，全面推进党的建设新的伟大工程，是这一伟大事业取得胜利的关键所在。党坚强有力，事业才能兴旺发达，国家才能繁荣稳定，人民才能幸福安康。党的十八大以来，我们党坚持党要管党、从严治党，凝心聚力、直击积弊、扶正祛邪，党的建设开创新局面，党风政风呈现新气象。习近平总书记围绕从严管党治党提出一系列新的重要思想，为全面推进党的建设新的伟大工程进一步指明了方向。'
keyss = jieba.analyse.extract_tags(content, topK=50, withWeight=True, allowPOS=())
exclude_words = [
        "中国", "推进", "全面", "提高", "工作", "坚持", "推动",
        "支持", "促进", "实施", "加快", "增加", "实现", "基本",
        "重大", "我国", "我们", "扩大", "继续", "优化", "加大",
        "今年", "地方", "取得", "以上", "供给", "坚决", "力度",
        "着力", "深入", "积极", "解决", "降低", "维护", "问题",
        "保持", "万亿元", "改善", "做好", "代表", "合理"
    ]
for word in keyss:
    print word[0],word[1]

# for word in keyss:
#     if word in exclude_words:
#         print word[0] ,word[1]
