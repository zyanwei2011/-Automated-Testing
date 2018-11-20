#encoding=utf-8
import unittest
import HTMLTestRunnerNew
from class_0926_ddt import test_mathmethod
from class_0926_ddt.test_mathmethod import TestAdd

#加载测试用例:
suite=unittest.TestSuite()#测试套件/测试用例的容器

suite.addTest(TestAdd("test_add_s"))
#怎么把用例放到测试套件suite里面去
#方法二：
loader=unittest.TestLoader()
#直接加载某个测试类里面的所有用例  直接加载某个测试模块里面的用例
#suite.addTest(loader.loadTestsFromTestCase(TestSub))
#suite.addTest(loader.loadTestsFromTestCase(TestAdd))
suite.addTest(loader.loadTestsFromModule(test_mathmethod))

file=open("test_1.html","wb+")
runner=HTMLTestRunnerNew.HTMLTestRunner(file)
runner.run(suite)
# runner=unittest.TextTestRunner()
# runner.run(suite)
