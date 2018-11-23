# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 21:56
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : do_mysql.py
#mysql_connector-python
import  mysql.connector



#你要提供数据库信息：地址 端口 用户名 密码
#写在字典  以字典的形式 传递我们的参数
config={'host':'119.23.241.154',
        'user':'python',
        'password':'python666',
        'port':3306 ,
        'database':'future',#指定你的数据库名
        }

#1：根据登录的信息 去登录数据库 产生一个数据库连接
conn=mysql.connector.connect(**config)

#2:产生一个游标 可以获取数据库的操作权限
cursor=conn.cursor()

#3:利用游标进行操作
sql='select * from member where id=23513'
cursor.execute(sql)

#4:获取结果：1）获取单条  2）获取多条
res=cursor.fetchone()#返回的是一个元祖#mysql.connector.errors.InternalError: Unread result found.
res=cursor.fetchall()#返回的是一个嵌套元组的列表

print("数据库的查询结果是{0}".format(res[0]))

#5关掉游标 关掉连接
cursor.close()
conn.close()


