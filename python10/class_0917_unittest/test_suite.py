__author__ = 'zz'
import unittest
import HTMLTestRunnerNew
from class_0917_unittest.do_excel import DoExcel
from class_0917_unittest.class_unittest_01 import TestAdd#测试类
#from class_0917_unittest.class_unittest_01 import TestSub#测试类
from class_0917_unittest import class_unittest_01#模块名
#功能测试：写用例--执行--比对结果（期望值/实际值）--报告
#unittest：
# 1：写用例:TestCase 类
#:2：加载用例:TestSuite类 TestLoader类
#3：比对结果（期望值/实际值）:断言函数
#4：执行并出结果：TextTestRunner 类
#:5:报告: HtmlTestReport 类

#加载测试用例:
suite=unittest.TestSuite()#测试套件/测试用例的容器

#获取测试数据
test_data=DoExcel().do_excel()
#怎么把用例放到测试套件suite里面去
#方法一
for item in test_data:
    suite.addTest(TestAdd(item['Param_a'],item['Param_b'],item['ExpectedResult'],item['title'],item['id'],"test_add"))#测试用例实例？实例的方式的去添加
#suite.addTest(TestAdd(0,0,0))

#方法二：
#loader=unittest.TestLoader()
#直接加载某个测试类里面的所有用例  直接加载某个测试模块里面的用例
#suite.addTest(loader.loadTestsFromTestCase(TestSub))
#suite.addTest(loader.loadTestsFromTestCase(TestAdd))
#suite.addTest(loader.loadTestsFromModule(class_unittest_01))

#执行用例TextTestRunner 类 专门来执行suite测试套件里面的利用
with open("test_result.html",'wb+') as file:
    #runner=unittest.TextTestRunner(file,verbosity=2)
    runner=HTMLTestRunnerNew.HTMLTestRunner(file,title='python10-0919',description="数学类的测试",tester="华华")
    runner.run(suite)

