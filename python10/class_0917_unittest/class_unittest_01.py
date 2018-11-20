__author__ = 'zz'
#单元测试---开发对自己写的代码去进行测试
#面向对象 封装 类  类属性值  类方法/类函数
#单元测试的本质--->类方法/类函数

#1)检测自己的脚本  2）unittest---利用这个框架 利用这个原理 去完成自动化测试
#功能测试：写用例--执行--比对结果（期望值/实际值）--报告
#啥时候做自动化测试？ok
#自动化框架搭建起来 需要多长的时间？-->自己去回答
#自动化用例编写 需要多长时间？ 跟功能测试的用例的区别？-->自己去回答
#自动化测试一般用在什么时候？ 功能测试/黑盒测试/数据驱动测试
#1）功能比较稳定 且不常改动。回归测试/迭代测试-->

#功能测试：写用例--执行--比对结果（期望值/实际值）--报告
#unittest：
# 1：写用例:TestCase 类
#:2：执行:TestSuite类 TestLoader类
#3：比对结果（期望值/实际值）:断言函数
#4：结果：TestTextRunner 类
#:5:报告: HtmlTestReport 类

import unittest
from class_0917_unittest.do_excel import DoExcel
from class_0917_unittest.math_method import MathMethod#导入被测试类

class TestAdd(unittest.TestCase):#测试类
    def setUp(self):#测试环境的搭建
        print("我要开始测试！")
        self.t=MathMethod()
        self.wb=DoExcel()#操作Excel的实例

    def __init__(self,a,b,expected,title,id,methodName):#初始化函数
        super(TestAdd,self).__init__(methodName)
        self.a=a
        self.b=b
        self.expected=expected
        self.title=title
        self.id=id#用例序号

    def test_add(self):#测试加法 用例?
        print("正在执行的用例是:{0}".format(self.title))
        print("a的值{0}".format(self.a))
        print("b的值{0}".format(self.b))
        print("expected的值{0}".format(self.expected))
        res=self.t.add(self.a,self.b)#实际运算值 要写入到每一行的第6列
        try:
            self.assertEqual(self.expected,res)#断言函数的调用
            test_result='PASS'#最终的测试结论  要写每一行的第7列
        except AssertionError as e:#捕捉的是断言异常?
            test_result='FAIL'#最终的测试结论 要写每一行的第7列
            print("测试出错了，错误是：{0}".format(e))
            raise e#抛出错误
        finally:
            self.wb.write_back(self.id+1,res,test_result)


    #写用例 每一条用例都是一个类函数
    #用例 def test_后缀（self）
    # def test_add_two_zero(self):#测试两个零相加
    #     res=self.t.add(0,0)
    #     try:
    #         self.assertEqual(-9,res)#断言函数的调用
    #     except AssertionError as e:
    #         print("测试出错了，错误是：{0}".format(e))
    #         raise e#抛出错误

    # def test_add_two_positive(self):#两个正数相加
    #     res=self.t.add(4,5)
    #     try:
    #         self.assertEqual(9,res)
    #     except AssertionError as e:
    #         print("测试出错了，错误是：{0}".format(e))
    #         raise e

    # def test_add_two_negative(self):#两个负数相加
    #     res=self.t.add(-4,-5)
    #     try:
    #         self.assertEqual(-9,res)
    #     except AssertionError as e:
    #         print("测试出错了，错误是：{0}".format(e))
    #         raise e

    def tearDown(self):#测试环境的销毁
        print("测试完成咯")

# class TestSub(unittest.TestCase):#测试类  专门测试减法
#     #写用例 每一条用例都是一个类函数
#     #用例 def test_后缀（self）
#     def test_sub_two_zero(self):#测试两个零相减
#         t=MathMethod()
#         res=t.sub(0,0)
#         print('测试结果是：{0}'.format(res))
#
#     def test_sub_two_positive(self):#两个正数相减
#         t=MathMethod()
#         res=t.sub(4,5)
#         print('测试结果是：{0}'.format(res))
#
#     def test_sub_two_negative(self):#两个负数相减
#         t=MathMethod()
#         res=t.sub(-4,-5)
#         print('测试结果是：{0}'.format(res))

if __name__ == '__main__':
    unittest.main()
