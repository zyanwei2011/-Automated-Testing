# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 21:06
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_0903_1.py
# def function(a,b=5):
#     print("a的值",a)
#     print("b的值",b)
#     return a+b

#参数 另外2种参数
#动态参数 *args  arguments 不定长参数
# def add(*args):
#     print(args)
#     print('args的类型',type(args))
#     for item in args:
#         print("获取到的值是：{0}".format(item))
#     # sum=0
    # for item in args:
    #     sum+=item
    # print("最后的求和是",sum)

# a=([1,2],[3,4])
# d={"dict_1":{"age":18},"dict_2":{"sex":"girl"}}
# add(*d)
#加一个*号 就等于脱一个外套
#常见的：列表里面嵌套字典 嵌套列表 嵌套元组

#关键字参数 **kwargs  key word arguments
#传递参数的时候 必须是 key=value  键值对
#返回的值是字典类型
def print_msg(**kwargs):
    print("kwargs的值是",kwargs)
    print("kwargs的类型是",type(kwargs))

# d={"class":"python10","grade":"100"}
# # print_msg(name='huahua',age='20')
#print_msg(**d)
#动态参数 关键字参数 不传值 也可以调用函数


#不同类型的参数混合使用 如何操作
#位置参数--默认参数--动态参数--关键字参数
def function_2(a,b,*args,c=4,**kwargs):
    print("a+b+c三个数之和：",a+b+c)
    print("args的参数：",args)
    print("kwargs的参数：",kwargs)

function_2(1,5,6,x=1)
#按顺序赋值