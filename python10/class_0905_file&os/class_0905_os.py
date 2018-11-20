# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 20:32
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_0905_os.py
#import  from...import 引入模块 引入类
#如果文件是在lib下面 而且是Python模块
# print("我是一个语句")
# time.sleep(4)
# print("我是第二个语句")
#我如果要调用模块里面的函数 模块名.函数名()
# #从包名开始一层一层的剥开
# import class_0903_function.test_1.class_0903_3
# # #调用这个模块里面的函数
# class_0903_function.test_1.class_0903_3.print_name("amanda")

#from...import..  import 可以具体到模块名 也可以具体到函数名
# from class_0903_function.test_1.class_0903_3 import print_name
# print_name('水滴')

import os
#只针对文件夹（目录）的操作

#获取当前工作目录
# path=os.getcwd()
# path=os.path.realpath(__file__)#__file__ 当前文件

#创建目录 和删除目录
# os.mkdir('test_1')
# os.rmdir('test_1')
# print("获取到的额路径是：{0}".format(path))
#新建大于2级的目录的时候 要注意上级目录要存在
#必须是一级一级的创建
# os.mkdir("test/test")

#路径的拼接
# path=os.getcwd()
# # new_path=path+"\\test_1"
# new_path=os.path.join(path,'test_2','test_3')#专门拼接路径
# # os.mkdir(new_path)
# os.rmdir(new_path)
# print("获取到的额路径是：{0}".format(new_path))

#判断文件的类型 返回值是布尔值
# print(os.path.isfile(os.getcwd()))
# print(os.path.isdir(os.getcwd()))

#切割 split  返回的是元组类型数据
# res=os.path.split(os.getcwd())
res=os.path.split(os.path.realpath(__file__))
print("切割路径之后的值是：{0}".format(res))