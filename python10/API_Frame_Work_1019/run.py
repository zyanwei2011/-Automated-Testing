# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 21:35
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : run.py
import unittest
import HTMLTestRunnerNew
from API_Frame_Work_1019.common.send_email import sendEmail
from API_Frame_Work_1019.common import project_path
from API_Frame_Work_1019.common.test_api import TestApi

suite=unittest.TestSuite()
loader=unittest.TestLoader()

#加载用例
suite.addTest(loader.loadTestsFromTestCase(TestApi))

#执行用例
# runner=unittest.TextTestRunner()
with open(project_path.report_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='小试牛刀',description='test1017',tester='summer')
    runner.run(suite)

#执行完毕之后，发送测试报告
sendEmail().send_email("204893985@qq.com",project_path.report_path)
