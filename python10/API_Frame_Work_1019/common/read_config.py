# -*- coding: utf-8 -*-
# @Time    : 2018/9/26 20:41
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : read_config.py
#配置文件：.ini  .properties  .config .conf   [ .xml ]
#主要讲文本形式的 configparser模块 专门处理配置文件
#配置文件的数据读取都是字符串类型
import configparser

class ReadConfig:
    def read_config(self,file_path,section,option):
        cf=configparser.ConfigParser()#实例化
        cf.read(file_path,encoding="utf-8")#调用read函数打开文件

        #获取数据
        value=cf.get(section,option)
        # print("获取到的值是：{0}".format(value))
        return value
#eval()
if __name__ == '__main__':
    value=ReadConfig().read_config("case.config","FLAG","case_id_list")
    print("获取到的值是：{0}".format(value))
