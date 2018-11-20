# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 21:05
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_01.py
#什么是函数呢？
#insert append print input range type len upper lower

#特点？直接调用  随意调用  多次使用  复用性强
#函数是一段可以重复完成某个功能的代码块

#语法:define  定义
#def 函数名(参数1，参数2，参数3):
   #函数代码块

#调用： 函数名()

#1:写一个简单问候函数
#2:如果要提高函数的复用性，我们可以想想 哪里可以参数化
#定义函数 参数：形参/位置参数  调用函数：实参
def greet_user(content,name):
    #content='小蚂蚁'
    #name='你好聪明'
     # str=name+'同学，'+content
     # print(str)
     #str=print('{0}同学，{1}'.format(name,content))
     #print(str)#字符串拼接 输出到控制台
     print('{0}同学,{1}！'.format(name,content))#格式化输出
     return ('{0}同学,{1}！'.format(name,content))



#调用函数
res=greet_user(name='小蚂蚁',content='你好聪明')
print("获取到的数据是：",res)
#函数参数：
#1：位置参数/形参，函数可以有多个参数 也可以没有参数
#2：定义函数的时候 有几个传参数  那么调用就要传递几个参数！不要多不要少
#3:默认参数 必须放在位置参数的后面，如果有默认参数，这个参数可以不用传递
#4:默认参数可以有多个吗？可以啊，你开心就好！
#5:调用函数的时候，默认情况下都是按顺序赋值
#6：调用函数的时候，你可以强制指定参数的赋值
#7：return关键字 返回一个值？返回给谁？ 必须要拿一个变量去进行接收？
#return可以说是函数结束的标志
# def greet_user_2():
#      print('charming同学,晚上好！')
#
# def greet_user(name='北辰'):#默认值
#      print(name+'同学,你好勤奋呀！')
# greet_user()

#写一个函数  计算1-100的总和
#三步走
#1：先用零散的代码写出这个功能  1-5 ：1 2 3 4 5==15
#选取一组数据来完成功能
#2：把代码变成一个函数 def 函数名():
#3：想办法提高他的复用性
def add_number(m,n):
    sum=0#存储总和的一个变量
    for i in range(m,n+1):#range k默认值就是1
        sum=sum+i
    print('总和是：{0}'.format(sum))

# add_number(1,100)
