# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 21:10
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_double_for.py
#嵌套循环 for  for if
a=[[1,2,3,4,5,6],[5,6,7,8,9,10]]
#有几个元素？ 2个
#子元素是什么类型？ 列表 子列表有4个元素
#请你把a里面的子列表全部打印输出到控制台？
#请把a里面的字列表的元素一个一个的输出来到控制台？
#第一种方式：
# print(a[0][0])
# print(a[0][1])
# print(a[0][2])
# print(a[0][3])
# print(a[0][4])
# print(a[1][0])
# print(a[1][1])
# print(a[1][2])
# print(a[1][3])
# print(a[1][4])

#第二个方式：for循环
# for item in a:
#     print(item)#item是不是一个列表？
#     #对item再去进行一次遍历
#     for data in item:
#         print(data)
#要求是：一共有两行数据，请根据\n换行符来确定
#每一行数据 请保存到一个字典里面  param  url 是key  后面的值是value
#最后处理完毕的数据 请保存到一个列表里面
#最后的效果是
# res=[{'param':{"phone":"18688773467","pwd":"123456"},'url':'http://119.23.241.154:8080/futureloan/mvc/api/member/register'},
# {'param':{"phone":"18688773467","pwd":"123456"},'url':'http://119.23.241.154:8080/futureloan/mvc/api/member/login'},
#   ]
str_1='param:{"phone":"18688773467","pwd":"123456"}@url:"http://119.23.241.154:8080/futureloan/mvc/api/member/register"\nparam:{"phone":"18688773467","pwd":"123456"}@url:"http://119.23.241.154:8080/futureloan/mvc/api/member/login"'
#直接写：
split_data_list=str_1.split('\n')
# print(split_data_list)
list_data=[]
for item_1 in split_data_list:
    res=item_1.split('@')
    dict_data={}
    for item_2 in res:
        res_2=item_2.split(':',1)
        key=res_2[0]
        value=res_2[1]
        dict_data[key]=value
        # print('key',key)
        # print('value',value)
    list_data.append(dict_data)


# list_1= str_1.split("\n")#返回的是列表类型的数据？
# print("第一次切割的数据：",list_1)
# print("先处理第一个数据list_1[0]：",list_1[0])
# #先处理list_1里面的数据

#对list_1里面的第一个元素去进行处理 再次切割？
# list_2=list_1[0].split('@')
# print("第二次切割之后的数据：",list_2)
# #对list_2里面的数据再去进行处理？再次切割
#再去处理list_2里面的第一个数据 list_2[0]
# print("先处理第一个数据list_2[0]：",list_2[0])
# final_data=[]
# for data in list_1:#list_1[0] list_1[1]
#     res=data.split('@')
#     dict_1={}#空字典
#     for item in res:
#         list_3=item.split(':',1)
#         #print("第三次切割的数据：",list_3)
#         dict_1[list_3[0]]=list_3[1]
#     final_data.append(dict_1)
# print("返回的最终数据是",final_data)


# for item in list_1:
#     list_2 =item.split("@")
#     for a in list_2:
#         list_3 = a.split(":",1)
#         print("{%r}:{%r}" %(list_3[0],list_3[1]))
