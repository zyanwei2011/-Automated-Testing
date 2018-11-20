import unittest
from zy_sub import test_case
import HTMLTestRunnerNew


suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_case))

with open('TestResult.html', 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(file, title='减法测试', description='第二轮整体回归测试减法方法的正确性', tester='华杰-zy_sub')
    runner.run(suite)
