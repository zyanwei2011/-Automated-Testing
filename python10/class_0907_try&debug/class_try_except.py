# -*- coding: utf-8 -*-
# @Time    : 2018/9/7 20:35
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_try_except.py
#异常？
#处理异常 try...except...
#try:
    #放自己觉得可能有问题的代码
#except:
   # 处理错误的方式

#第一种
# try:
#     print(a)
# except Exception as e:#指定只处理哪种类型的错误
#     print("出错啦:{0}".format(e))

#第二种：try...except...finally
#在异常之前和异常代码之后 执行的结果不一样  注意以下
# try:
#     print(a)
#     print("柠檬班的各位同学真是萌萌滴！")
# except Exception as e:#指定只处理哪种类型的错误
#     print("出错啦:{0}".format(e))
# finally:
#     print("柠檬班的各位同学真是萌萌滴！")

#第三种： try...except..else
#当try下面的代码 不报错的时候  才会执行else下面的代码  否则不执行
# try:
#     print(a)
# except Exception as e:#指定只处理哪种类型的错误
#     print("出错啦:{0}".format(e))
# else:
#     print("柠檬班的各位同学真是萌萌滴！")

#资源的交互处理  上下文管理器
# file=open("test_data.txt",'a')
# print("1",file.closed)
# file.close()
# print("2",file.closed)
with open("test_data.txt",'a') as file:
    file.write("6666")
print("file的状态",file.closed)