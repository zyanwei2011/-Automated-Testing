__author__ = 'zz'
#字典
#关键字 dict  {}
#值的特点是 键值对 key:value
# a={}#空字典
# a={'age':18,'name':'无闻'}
#元组  列表 都是有序的数据类型
#字典是无序的数据类
#字典里面key是唯一的  value是不唯一
#取值  就是按照key取值  字典名[key]
# print(a['age'])

#所有的值 字典名.values()
# print(a.values())

#所有的值 字典名.keys()
# print(a.keys())

# a={'age':18,'name':'无闻'}
#字典可以增删改吗？
# 新增值 a[新key]=value
# a['score']=99.87
#修改值 a[已存在的key]=新value
# a['age']=20
#删除值 字典名.pop(key)
# a.pop('name')
# print(a)

a={'age':18,'name':'无闻','score':{'ch':99,'en':98,'math':100},
   'name_2':'无闻'}
print(a)