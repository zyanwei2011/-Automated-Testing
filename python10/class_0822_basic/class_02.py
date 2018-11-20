

# p_1='hello'#字符串
# #反序  请你把p_1这个字符串 倒序输出
# # print(p_1[6::-1])#这个也可以掌握
# # print(p_1[:-1])  这个方法不行
# print(p_1[::-1])#这个看个人掌握
# print(p_1[-1:-6:-1])#-1 -2 -3 -4 -5  这个可以掌握
# print(p_1[4::-1])#取左不取右

#字符串的进阶操作：python内置函数的调用
#切换大小写
# a='get'
# #a_1=a.upper()#把英文字母全部变成大写字母
# #字符串拼接：+
# c=a[0]+a[1].upper()+a[2]
# print(c)

# b='BiG'
# b_1=b.lower()#把英文字母全部变成小写字母
# print(b_1)

#查找字符串 字符串变量名.find(字符串)
# lemon_1='lemon is best'
# print(lemon_1.find('!'))
# #返回-1 说明查找的字符不存在
# print(lemon_1.find('b'))
# #返回9？  如果找到了单个字符 返回找到的第一个字符所在的索引
# print(lemon_1.find('lemon'))
# #返回0？ 如果是字符串 返回的是子字符串的第一个元素的索引
# print(lemon_1.find('is'))

#字符串的替换 字符串变量名.replace(替换目标，替换的值，替换次数）
s_4='hello python'
s_5=s_4.replace('o','@',1)#替换之后要保存起来
s_6=s_5.replace('o','66',1)
s_7=s_6.replace('@','o')
#不指定次数 就全部替换
print(s_7)
#能不能只替换第二个？

