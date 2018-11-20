'''
1：写一个软件测试工程师类，具有的属性和技能，你们自己去定
'''
class TestEnginner:

    def auto_test(self,language):
        print('会做{}自动化'.format(language))

    def communicate(self):
        print('善于交流')

    def test_skill(self, *args):
        for item in args:
            print('会{}技能'.format(item))

    def personal_information(self, name, **kwargs):
        print('name:', name, 'other:', kwargs)


t = TestEnginner()
t.auto_test('python')
t.communicate()
t.test_skill('数据库', 'linux', '接口', '自动化', '性能')
t.personal_information('dana', age=23, sex='男')


'''
2：创建一个名为 User 的类：
1）其中包含属性 first_name 和 last_name，还有用户简介通常会存储的其他几个属性，均是自定义， 请放在初始化函数里面。
2）在类 User 中定义一个名为 describe_user()的方法，它打印用户信息摘要；
3）再定义一个名为 greet_user()的方法，它向用户发出个性化的问候。:
请创建多个表示不同用户的实例，并对每个实例都调用上述两个方法
'''

class User:
    def __init__(self,first_name,last_name,height,weight):
        self.name = first_name + last_name
        self.height = height
        self.weight = weight

    def describe_user(self):
        print('{0}的身高是{1}，体重{2}KG'.format(self.name, self.height, self.weight))

    def greet_user(self):
        print('{},欢迎加入我们'.format(self.name))


a = User('张','三','178','65')
a.describe_user()
a.greet_user()

b = User('张','六','123','55')
b.describe_user()
b.greet_user()


'''
4：定义一个学生类。
1）有下面的类属性： 1 姓名 2 年龄 3 成绩（语文，数学，英语)[每课成绩的类型为整数] ,均放在初始化函数里面。
2）类方法：
a)获取学生的姓名：get_name() 返回类型:str b)获取学生的年龄：get_age() 返回类型:int
c) 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下: zm = Student('zhangming',20,[69,88,100]) 返回结果： zhangming 20 100
'''

class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.max_score = max(score)

    def get_name(self):
        return self.name

    def get_age(self):
        return int(self.age)

    def get_course(self):
        return self.max_score


zm = Student('zhangming',20,[69,88,100])
print(zm.get_name())
print(zm.get_age())
print(zm.get_course())

'''
5。人和机器猜拳游戏写成一个类，有如下几个函数：
1）函数1：选择角色1 曹操 2张飞 3 刘备
2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
'''
import  random

class PersonVsMachine:

    def select_role(self):
        d = {'1': '曹操', '2': '张飞', '3': '刘备'}
        n = input('请选择角色(1 曹操 2张飞 3 刘备):')
        while int(n) not in (1,2,3):
            n = input('您的输入有误，请重新输入数字1-3选择角色(1 曹操 2张飞 3 刘备):')
        else:
            role = d[n]
        return role

    def person_fist(self):
        r = input('角色猜拳(1剪刀 2石头 3布),请输入数字1-3:')
        return int(r)

    def machine_fist(self):
        r = random.randint(1,3)
        return r

    def personVsMachine(self):
        role_name = self.select_role()
        d = {1: '剪刀', 2: '石头', 3: '布'}
        person_win = 0
        machine_win = 0
        ping = 0

        while True:
            person_num = self.person_fist()
            machine_num = self.machine_fist()
            res = person_num - machine_num
            print(role_name+'出拳{}'.format(d[person_num]))
            print('电脑出拳{}'.format(d[machine_num]))

            if res in (-2,1):
                person_win += 1
                print('角色赢电脑输')
            elif res in (-1,2):
                machine_win += 1
                print('电脑赢角色输')
            else:
                ping += 1
                print('电脑和角色平局')

            choice = input('是否继续？按y继续，按n退出:')
            try:
                if choice == 'y':
                    continue
                elif choice == 'n':
                    print('{}赢{}局，电脑赢{}局，平局{}'.format(role_name,person_win,machine_win,ping))
                    print('游戏结束')
                    break
            except:
                print('游戏结束')