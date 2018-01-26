#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding( "utf8" )
from flask import *
import warnings
warnings.filterwarnings("ignore")
import MySQLdb
import MySQLdb.cursors
from config import *
import time

app = Flask(__name__)
app.config.from_object(__name__)

# 连接数据库
def connectdb():
	db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWORD, db=DATABASE, port=PORT, charset=CHARSET)
	db.autocommit(True)
	cursor = db.cursor()
	return (db,cursor)

# 关闭数据库
def closedb(db,cursor):
	db.close()
	cursor.close()

# 首页
@app.route('/')
def index():
	return render_template('index.html')

# 处理表单提交
@app.route('/handle', methods=['POST'])
def handle():

	# 获取post数据
	data = request.form
	print data
	username = request.form['name']
	password = request.form['password']
#	return redirect(url_for('list'))

	# 连接数据库
	(db,cursor) = connectdb()
	# 数据库中添加注册信息
	cursor.execute("insert into zhuce(name, mima, youxiang,timess) values(%s, %s, %s, %s)", [data['name'], data['mima'], data['youxiang'],str(int(time.time()))])
	# 最后添加行的id
	# post_id = cursor.lastrowid

	# 关闭数据库
	closedb(db,cursor)

	return redirect(url_for('list'))

@app.route('/list')
def list():
	# 连接数据库
	(db,cursor) = connectdb()

	# 获取数据
	cursor.execute("select * from zhuce")
	postss = cursor.fetchall()
	print postss
	# 格式化时间戳
	for xx in xrange(0, len(postss)):
	 	print xx
	# 	postss[x]['timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(postss[x]['timestamp'])))


	# 关闭数据库
	closedb(db,cursor)

	# 后端向前端传递数据
	return render_template('list.html', ppp=postss, qqq=xx)


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)