# -*- coding: utf-8 -*-
# @Time    : 2018/9/7 21:24
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_file_homework.py
def read_data():
    try:
        file=open("test_data.txt")
    except Exception as e:
        print("打开文件的时候报错了：{0}".format(e))

    res=file.readlines()#返回列表类型的数据 每一行为列表的一个元素
    new_list=[]
    for data in res:
        res_strip=data.strip('\n').split('@')#返回一个列表
        #print("res的值",res_strip)
        #准备第二次切割
        new_dict={}#字典的位置？
        for item in res_strip:
            item_split=item.split(":",1)#返回列表
            try:
                key=item_split[0]
                value=item_split[1]
                new_dict[key]=value
            except Exception as e:
                print("切割的时候出错啦！{}".format(e))
        new_list.append(new_dict)
    print(new_list)

read_data()