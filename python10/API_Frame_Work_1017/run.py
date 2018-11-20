# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 21:35
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : run.py
import unittest
import HTMLTestRunnerNew

from API_Frame_Work_1017.common.test_api import TestApi

suite=unittest.TestSuite()
loader=unittest.TestLoader()

#加载用例
suite.addTest(loader.loadTestsFromTestCase(TestApi))

#执行用例
# runner=unittest.TextTestRunner()
with open("test_api.html",'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='小试牛刀',description='test1017',tester='summer')
    runner.run(suite)



# from API_Frame_Work.do_excel import DoExcel
# from API_Frame_Work.http_request import HttpRequest

# #获取测试数据数据用例：
# url='http://119.23.241.154:8080/futureloan/mvc/api/member/register'
# test_data=DoExcel().get_data("api.xlsx","testcase")
# for item in test_data:
#     res=HttpRequest().http_request(url,eval(item['param']),item['HttpMethod'])
#     if str(res['code'])==str(item['ExpectedResult']):#实际结果的code 与期望的code对比
#         TestResult='PASS'#测试结论
#     else:
#         TestResult='Failed'#测试结论
#
#     #写回结果  调用DoExcel里面的write_back函数
#     DoExcel().write_back("api.xlsx","testcase",item['id']+1,res['code'],TestResult)
