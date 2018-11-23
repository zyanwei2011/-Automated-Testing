# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 20:47
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_1026.py
# d={"name":"ky","age":"25"}
# for item in d:
#     print(item)
#
# class PrintMsg:
#     a=10
#     b=20
#     c=None
#
# setattr(PrintMsg,'b',666)#设置
# print(PrintMsg.b)#获取
# #属性名存在  那就是赋值  如果不存在  就新建一个变量然后赋值
#变量的引用  如果变量值是一样 变量名不一样  他们共用一个内存空间
#
a=10
b=10
c=10
print(id(a))
print(id(b))
print(id(c))