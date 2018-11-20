#字符串的进阶操作
# str_1='hello,python,kk'
#split() 根据你传入指定的字符去进行切割
#res=str_1.split(',')#返回的是列表类型的数据  默认全部切割
#res=str_1.split('k',1)#指定字符  指定切割次数  与replace类似
#列表里面的元素 都是字符串
#res=str_1.split()#默认切割空格
#print(res)

#去除指定元素 strip() 去除头和尾指定的字符
str_1='hello,python,kk'
res=str_1.strip('h')#不传任何字符的时候 默认去除空格
#如果传了字符 就去除指定的字符
print(res)