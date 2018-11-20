__author__ = 'zz'
#软件测试工程师类
class SoftWareTestEngineer:
    name="boy"
    age="24"

    def auto_testing(self,language="python"):
        print(self.name+"会做{0}自动化测试".format(language))

    def interface_testing(self):
        print(self.name+"会做接口测试")

    def write_working_doucumnets(self,*args):
        for item in args:
            print(self.name+"会写{0}".format(item))

t_1=SoftWareTestEngineer()
t_1.auto_testing()
t_1.interface_testing()
t_1.write_working_doucumnets("测试用例","测试计划","测试报告")
#类函数里面调用另外一个函数/变量值 self.函数名（参数） self.变量名