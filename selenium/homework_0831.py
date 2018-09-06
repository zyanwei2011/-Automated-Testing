'''
1：编写一个名为 make_shirt()的函数，它接受一个尺码以及要印到 T 恤上的字样。这个函数应打印一个句子，概要地说明 T 恤的尺码和字样。
'''


def make_shirt(size, words):
    print('T恤的尺码:%s,字样是：%s' %(size, words))


make_shirt(30, 'Hello World!')

'''
2：编写一个名为 describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。
这个函数应打印一个简单的句子，如 Reykjavik is in Iceland。
给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
'''


def describe_city(city_name,country='China'):
    print(city_name,'is in',country)


describe_city('beijing')
describe_city('wuhan','China')
describe_city('NewYork','AMERICAN')

'''
3：编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。
这个函数应返回一个格式类似于这样的字符串："长沙, 中国"
至少使用三个城市-国家对调用这个函数，并打印它返回的值。
'''


def city_country(city_name,country='China'):
    print('"'+ city_name+','+country+ '"')


city_country('beijing')
city_country('wuhan','China')
city_country('NewYork','AMERICAN')


'''
4：编写一个名为 make_album()的函数，它创建一个描述音乐专辑的字典。
   这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
   使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
'''


def make_album(name,album):
    dict = {}
    dict['name'] = name
    dict['album'] = album

    print(dict)

make_album('刘德华','冰雨')
make_album('周杰伦','不知道')

'''
5：编写一个函数，它接受顾客要在三明治中添加的一系列食材。
这个函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点的三明治进行概述。
调用这个函数三次，每次都提供不同数量的实参。
'''


def make_sandwich(*args):
    print('三明治里添加',args)


make_sandwich('sugar')

make_sandwich('sugar','onion')

l = ['sugar','onion','egg']
make_sandwich(*l)



'''1：定义一个函数，成绩作为参数传入。
    如果成绩小于60，则输出不及格。
    如果成绩在60到80之间，则输出良好；
    如果成绩高于80分，则输出优秀，
    如果成绩不在0-100之间，则输出 成绩输入错误。
'''
def give_mark(score):
    if 0 <= score <= 100:
        if 0 <= score < 60:
            print('不及格')
        elif 60 <= score <= 80:
            print('良好')
        else:
            print('优秀')
    else:
        print('成绩输入错误')


give_mark(89)


'''
2：用函数实现：
企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
'''
def make_bonus(I):
    if I <= 10:
        b = I*0.1
    elif 10 < I <= 20:
        b = 10*0.1+(I-10)*0.075
    elif 20 < I <= 40:
        b = 10*0.1+(20 - 10)*0.075+(I-20)*0.05
    elif 40 < I <= 60:
        b = 10*0.1+(20 - 10)*0.075 +(40 - 20)*0.05+(I-40)*0.03
    elif 60 < I <= 100:
        b = 10*0.1+(20 - 10)*0.075 +(40 - 20)*0.05+(60 - 40)*0.03+ (I-60)*0.015
    elif I > 100:
        b = 10*0.1+(20 - 10)*0.075 +(40 - 20)*0.05 +(60 - 40)*0.03 + (100 - 60)*0.015+ (I-100)*0.01
    print(b)

make_bonus(1000)


'''
3：用python函数实现如下:
随机产生一个数，让用户来猜，猜中结束，若猜错，则提示用户猜大或猜小。
'''

import random

def guess_num(n):
    r = random.randint(1,9)
    if n != r:
        if n > r:
            print('猜大了')
        else:
            print('猜小了')
    else:
        print('猜对了')


guess_num(6)



'''
4：写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
'''


def get_len(s):
    n = len(s)
    if n > 5:
        print('长度大于5')
    else:
        print('长度不大于5')


l = [123123, 1231, 'asda', 12312, 1213213, sadasd]
get_len(l)

'''
5. 写函数，将姓名、性别，城市作为参数，并且性别默认为f(女)。
如果城市是在长沙并且性别为女，则输出姓名、性别、城市，并返回True,否则返回False。
'''

def func(name,city,sex = 'f'):
    if city == '长沙' and sex == 'f':
        return True
    else:
        return False

print(func('cc','长沙',))

'''
6：写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
'''

def func(l):
    if len(l)>2:
        l = l[0:2]
    else:
        l = l
    return l


l = [1, 2, 3, 4]
print(func(l))

'''
7：定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典。
'''

def func(str,dict):
    if str not in dict.values():
        dict['str'] = str
    else:
        print('字典中已存在')
    return dict



str = 'asdec'
dict = {'first': 'af', 'second': 'ce', 'third': 'ef'}

print(func(str,dict))

'''
1：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
'''
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if (x != y) and (y != z) and (x != z):
                print('%d%d%d' % (x, y, x), end=' ')



'''
2：一个足球队在寻找年龄在m岁到n岁的男生or女生（包括m岁和n岁，到底是找男生还是女生，可指定性别）加入。
编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。
'''

num = 0
for i in range(10):
    age,sex = input('请输入你的年龄和性别，以逗号分格：').split(',')
    if 10 <= eval(age) <= 12 and sex == 'f':
        print('可以加入球队')
        num += 1
    else:
        print('抱歉，你不符合条件')
print('共',num,'人满足条件')
