__author__ = 'zz'
class MathMethod:
    def __init__(self,a,b):#初始化函数  通过他可以传递属性值进来
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def chengfa(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b

t_1=MathMethod(6,3)#如果有初始化函数  创建实例的时候传递对应初始化函数的参数个数
res=t_1.sub()
print("运行结果是:{}".format(res))
#类没有定义属性
#初始化函数 创建实例的时候去传递
#def __int__() 没有return