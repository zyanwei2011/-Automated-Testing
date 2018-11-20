import os

data = open('test_data.txt','r')
res = data.read()
dict = {}
list =[]
l = res.split('\n')
for item_01 in l:
    res_01 = item_01.split('@')
    for item_02 in res_01:
        res_02 = item_02.split(':',1)
        dict[res_02[0]] = res_02[1]
    list.append(dict)
print(list)
