"""
1、一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
  编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，然后显示一条消息指出这个人是否可以加入球队，
  询问10次后，输出满足条件的总人数。
"""
n = 0
for i in range(10):
    age, sex = input('情输入年龄和性别，并以逗号分格：').split(',')
    if 10 <= eval(age) <= 12 and sex == 'm':
        print('你可以加入足球队')
        n += 1
print(n)
"""
#作业2：输入num为四位数，对其按照如下的规则进行加密：
# 1）每一位分别加5，然后分别将其替换为该数除以10取余后的结果
# 2）将该数的第1位和第4为互换，第二位和第三位互换
# 3）最后合起来作为加密后的整数输出
"""
n = input('请输入四位正整数：')
l = []
if len(n) ==4 and n.isdigit() == True:
    # 每一位分别加5，然后分别将其替换为该数除以10取余后的结果，再将次结果转化未字符串
    l = [str((int(i)+5)%10) for i in n]
    # for i in a: num.append(str((int(i)+5)%10))
    l.reverse()
    # join的值必为字符串数组，引号内为生成字符串的连接符
    r = ''.join(l)
    print(r)
else:
    n = input('请重新输入四位正整数：')
"""
#作业3：一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果购买金额大于100元会给20%折扣。
# 编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格
"""
pri = int(input('请输入商品价格：'))
if pri < 50:
    s_pri = pri
    discount = 0
    print('商品原价是{:.2f}，折扣是{:.2f}，售价是{:.2f}'.format(pri,discount,s_pri))
if 50 <= pri <= 100:
    s_pri = pri*(1-0.1)
    discount = pri*0.1
    print('商品原价是{:.2f}，折扣是{:.2f}，售价是{:.2f}'.format(pri,discount,s_pri))
if pri > 100:
    s_pri = pri * (1 - 0.2)
    discount = pri * 0.2
    print('商品原价是{:.2f}，折扣是{:.2f}，售价是{:.2f}'.format(pri,discount,s_pri))
"""
#作业4：生成随机整数，从1-9取出来。然后输入一个数字，来猜，如果大于，则打印bigger。 小了，则打印less。如果相等，则打印equal
"""
import random
m = random.randint(1,9)
n = input('请输入1个1-10的随机树：')
if n.isdigit() and 1:
    num = int(n)
    if num < m:
        print('less')
    if num > m:
        print('bigger')
    else:
        print('equal')
else:
    n = input('请正确输入1个1-10的随机树：')






