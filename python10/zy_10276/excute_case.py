import unittest
from zy_10276.test_case import TestApi
import HTMLTestRunnerNew


suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestApi))

with open('test_result.html','wb+') as f:
    runner =HTMLTestRunnerNew.HTMLTestRunner(stream=f, title= '接口测试',description= '前程贷的注册接口测试',tester='张奕')
    runner.run(suite)


