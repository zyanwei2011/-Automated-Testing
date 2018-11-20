a = 'Good morning,world!'
b = 'I love you'
# 读取
print(a[0])
print(a[0:7:2])
print(a[0:])
print(a[:-1])
# 拼接
c = a + b
print(c)
# 反转
print(a[-1::-1])
print(a[18::-1])
print(a[::-1])
# 大小写
print(a.lower())
print(a.upper())
# 查找---返回索引
print(a.find('mo'))
# 替换
print(a.replace('o', 'p'))
# 仅替换前n个
print(a.replace('o', 'p', 1))
