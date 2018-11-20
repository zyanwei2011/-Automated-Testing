__author__ = 'zz'
# 数据+函数
#类 数据 函数
#类的划分标准：我们自己

#数学类：加减乘除 数字  微积分 几何  函数

#一名合格的软件测试工程师类：会扯皮 怼开发 找bug 理解需求 会写用例 报告

#理想型对象：怎样的男生才能成为你的男朋友？===>男朋友类
#小太阳 上进心 有钱 美 180  责任心 男友力 能够保护你 会做家务
#会赚钱？ 会做饭？

#Python类的语法
#关键字 class
#class 类名:
   #属性：数据  类属性
   #函数：方法、动作行为  类方法/类函数
#类名规范：数字字母下划线组成  不能数字开头  见名知意 首字母大写 不需要隔开

class BoyFriend:#男朋友类
    #类属性 类里面变量
    # height=180
    # money='2000万'
    def __init__(self,name,height,money="100万"):
        self.name=name
        self.height=height
        self.money=money


    #类函数/类方法
    def cooking(self,dish_1,dish_2,dish_3,dish_4):#做饭
        print("会下厨做：{}".format(dish_1))
        print("会下厨做：{}".format(dish_2))
        print("会下厨做：{}".format(dish_3))
        print("会下厨做：{}".format(dish_4))

    def earn(self,work="IT行业",money="100万"):#会赚钱
        print(self.name+"从事{0}，会赚钱，年薪是：{1}".format(work,money))

    def sport(self,*args):#会运动
        for item in args:
            print("热爱{0}运动".format(item))

    def skill(self,**kwargs):#从业技能 key-value
        print(kwargs)

    def my_bf(self):
        self.earn()
        self.skill(code='java',job='develop')
        self.sport("跑步")

#创建对象  p_1=类名()  实例/对象
p_1=BoyFriend("水滴","180")
p_1.my_bf()
# p_2=BoyFriend()

#创建的实例 可以调用类里面的方法和属性
# print("存款是：{}".format(p_1.money))
# p_1.skill(code='python',job='测试')
# p_1.sport("羽毛球","篮球","游泳","足球")
# #p_1.earn()
# p_1.cooking("鸡蛋炒茄子","蒸鱼","辣椒炒肉","泡面")
# p_1.cooking()
# p_1.cooking(")


#类函数
#1：类函数可以传递位置参数吗？可以
#2：类函数可以传递多个位置参数吗？可以
#3：类函数可以传递默认参数吗？可以！
#4：类函数可以同时传递位置参数 默认参数吗？可以！ 按顺序赋值 位置参数在默认参数之前
#5：类函数可以有多个默认参数吗？可以！
#6：类函数可以有动态参数吗？可以！ * args
#7：类函数可以有关键字参数吗？可以！ **kwargs
#8：函数之间的相互调用？self.函数名（参数）

#课堂作业：
#写一个软件测试工程师类 属性  方法







