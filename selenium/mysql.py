from PyMySQL import pymysql

db = pymysql.connect(host='localhost',user='pythontab',passwd='pythontab',db='pythontab',port=3306,charset='utf8')