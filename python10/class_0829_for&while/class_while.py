# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 22:06
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_while.py
#while循环
#语法：
#  while  条件表达式:
    #循环的代码块
#执行顺序：首先判断while后面的条件 如果 满足 就执行代码块 执行完毕之后
# 再去判断while后面的条件 再执行代码块 执行完了之后再判断 ... 如此反复
# a=-1
# while a<9:#-1 0 1 2 3 4 5 6 7 8
#     print("Python的while循环 正在进行中")
#     a=a+1#
#     # if a>10:
    #     break
    # break

#用while循环 很容易陷入死循环 所以请慎重使用，一定要设置好条件
#怎么防止while 语句进入死循环？？
#1：break  跳出循环 结束循环 终止循环
#2：利用一个变量来控制循环次数  指定循环次数

#请分别利用for 循环 while循环完成1-100整数相加，求出和
#并把总和输出到控制台
#第一点：要拿到1-100的整数？ range(1,101)
# sum=0#存储值
# for item in range(1,101):
#     sum=sum+item
# print("最后的总和是：",sum)

#while循环
sum=0
a=1
while True:
    sum=sum+a#控制加法#sum 0  a 1 -->sum=1  sum 1 a 2-->sum=3
    a=a+1#控制a参数a -->2  a--> 3
    if a==101:
        break
print(sum)