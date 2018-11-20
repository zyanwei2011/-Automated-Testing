# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 22:11
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_02.py
# str_1='hello@huahua'
# #split strip?
# #find replace
#
# str_1.find('@')

#strip处理字符串的头和尾
# str_1='ahello@huahua'
# res=str_1.strip('a')
# print(res)

#下节课局部 全局   动态参数 关键字参数  函数间的调用
# def add(a,b):
#     print("两数相加的和是",a+b)
#
# #调用函数
# res=add(1,3)
# print("我收到的返回值是：",res)

#定义一个函数
def add(a,b):
    return(a+b)

#调用函数
res=add(3,4)

#单纯的一个输出语句
print("我有一个加法函数add,他的结果加4，最后得出：",res+4)