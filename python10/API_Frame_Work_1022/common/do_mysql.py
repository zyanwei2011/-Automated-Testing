# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 21:56
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : do_mysql.py
#mysql_connector-python
import  mysql.connector
from API_Frame_Work_1019.common import project_path
from API_Frame_Work_1019.common.read_config import ReadConfig

class DoMysql:
    def do_mysql(self,sql):
        config=eval(ReadConfig().read_config(project_path.db_config_path,"DB","config"))
        #从配置文件里面读取出来--字符串--eval转成字典
        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()
        cursor.execute(sql)
        res=cursor.fetchall()#返回的是一个嵌套元组的列表
        cursor.close()
        conn.close()
        return res#返回数据库的查询结果

if __name__ == '__main__':
    sql='select max(id) from loan where memberid=23513'#不写死
    res=DoMysql().do_mysql(sql)
    print("测试结果：{0}".format(res))


