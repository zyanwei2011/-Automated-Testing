__author__ = 'zz'
#for while
#for 遍历元素==通过元素的个数 来控制循环次数
#语法：for item in datas:# datas 是数据范围 列表 元组 字典 字符串
          #重复执行的代码块
# a='666@#'#5 #字符串
# b=[1,2,3]#
# c=(1,2,[5,6],(7,8))#0 1 2 3  索引 range(4)
# for i in range(len(c)):#
#     print(c[i])
# d={'age':1,'name':'kk'}
# for item in d.items():#item是一个变量 item依次访问a里面的元素，然后取到对应的值
#     print(item)
#for循环的次数的是由数据的元素个数

#数据集合呢？ range(m,n,k) 生成一个整数序列  数据集合
#1.range(m,n,k)
#m 开始  n-1 结束  k步长
# r=list(range(0,6,4))#0 4

#2:range(m,n) 默认k=1 步长默认为1
# r=list(range(2,3))

#3.range(n) 默认m=0 k=1
# r=list(range(8))
# print(r)

# for i in range(4):
#     print(i)


#课堂小练习
L=[1,2,3,4,5,6,7]
#7654321 # -1 -2 -3 -4 -5 -6 -7  range(-1,-8,-1)
#请利用for循环 倒序输出这个列表的每一个元素
# L.reverse()
# for item in L:
#     print(item)
# print(list(range(-1,-8,-1)))#取左不取右？
L=[1,2,3,4,5,6,7]
#-7 -6 -5 -4 -3 -2 -1
#-1 -2 -3 -4 -5 -6 -7
#根据索引来倒序输出？  这不是切片！！！
for i in range(-1,-8,-1):
    print(L[i])

