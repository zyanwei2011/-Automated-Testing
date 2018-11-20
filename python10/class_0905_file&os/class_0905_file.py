# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 21:31
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_0905_file.py

#针对txt
#r 只读 文件必须要存在 r+ 支持读写
#w 只写 如果存在就直接写  不存在 就新建一个文件再去写内容
#清空了文件再去写  重写
# w+  读写  如果存在就直接写  不存在 就新建一个文件再去写内容 可以支持读
#a 追加 append 如果存在就直接写  不存在 就新建一个文件再去写内容
#a+ 追加 append 如果存在就直接写  不存在 就新建一个文件再去写内容
# file=open('test.txt','a+',encoding='utf-8')
#
# #写入内容到文件中
# file.write("齐达齐达齐达齐达齐达齐达")
# #挪动光标的位置
# file.seek(0,0)#第一个值表示偏移多少
# # 第二 相对哪里开始挪动 0头部 1当前位置 2尾巴 只支持0
# #二进制文件 可以支持0 1 2
# #针对文件内容的读取
# # res=file.read()#默认读取所有的内容
# #可不可以读取指定长度的内容
# res=file.read()
# print("读取到的结果是：{0}".format(res))

file=open('test.txt','w+',encoding='utf-8')
#res=file.read()#默认读取所有的内容 或者是按照指定的长度去读取内容
#res=file.readline()#读取单行 返回的数据类型是字符串
#res=file.readlines()#按行读取所有的数据 返回的数据类型是列表 列表里面的子元素是字符串
# print("读取到的结果是：{0}".format(res))

#一次性写入多行的话  就传入列表类型的数据
data=['A组666', 'B组大佬6666', 'C组大佬666']
file.writelines(data)