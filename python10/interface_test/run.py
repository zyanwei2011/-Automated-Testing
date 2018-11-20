import unittest
from interface_test.common.test_case import TestApi
import HTMLTestRunnerNew
from interface_test.common import project_path
from interface_test.common.send_email import sendEmail


suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestApi))


with open(project_path.test_result_path, 'wb+') as f:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f, title='接口测试', description='前程贷的注册接口测试', tester='张奕')
    runner.run(suite)


# 测试完成后自动发送测试报告
sendEmail().send_email("784366503@qq.com", project_path.test_result_path)



