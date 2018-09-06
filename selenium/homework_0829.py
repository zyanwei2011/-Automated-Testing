"""
1.利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序（冒泡排序：小的排前面，大的排后面。）
"""
a=[1,7,4,89,34,2]
for i in range(len(a)-1):  # 冒泡排序进行的次数
    for j in range(len(a)-1-i):  ## 下标
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)

"""
2.输出99乘法表
"""
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d '%(j,i,i*j),end=' ')
    print('')

"""
3.请利用while循环来完成：一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
"""
sum = 0
n = 1
while n <= 10:
    n += 1
    age, sex = input('请输入年龄和性别，并以逗号分格：').split(',')
    if 10 <= eval(age) <= 12 and sex == 'm':
        print('你可以加入足球队')
        sum += 1
print(sum)

"""
4：万科笔试题：

有一组用户的登录信息存储在字典 login_ifno 里面，字典格式如下：login_info={"username":"admin","passwd":"123456"}

username表示用户名，passwd表示密码，请编写函数满足如下条件：

1）设计1个登陆的程序， 不同的用户名和对成密码存在个字典里面， 输入正确的用户名和密码去登陆，

2）首先输入用户名，如果用户名不存在或者为空，则一直提示输入正 确的用户名

3)当用户名正确的时候，提示去输入密码，如果密码跟用户名不对应， 则提示密码错误请重新输入。

4)如果密码输入错误超过三次，中断程序运行。

5)当输入密码错误时，提示还有几次机会

6)用户名和密码都输入正确的时候，提示登陆成功!'''

目前不考虑多个用户的情况，只考虑一个admin账户的情况，请不要多想~~。
"""

login_info={"username":"admin","passwd":"123456"}

user_name = input('请输入用户名：')
if user_name == login_info["username"]:
    for i in range(3):
        user_passwd = input('请输入密码：')
        if user_name == login_info["passwd"]:
            print('登录成功')
        else:
            if i != 2:
                print('密码错误请重新输入')
                print('你还有%d次机会'%(2-i))
            else:
                print('您已输入错误3次，请稍后重试！')

else:
    print('请输入正确的用户名')