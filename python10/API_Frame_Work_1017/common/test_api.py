# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 21:10
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : test_api.py
#引入ddt
import unittest

from ddt import ddt,data

from API_Frame_Work_1017.common.http_request import HttpRequest
from API_Frame_Work_1017.common.do_excel import DoExcel
from API_Frame_Work_1017.common.read_config import ReadConfig


#从配置文件里面获取button和case_id_list的值
button=ReadConfig().read_config('case.config','CASECONFIG','button')
case_id_list=ReadConfig().read_config('case.config','CASECONFIG','case_id_list')
#获取测试数据
test_data=DoExcel("api.xlsx").get_data(button,case_id_list)

@ddt
class TestApi(unittest.TestCase):
    def setUp(self):
        self.t=DoExcel("api.xlsx")#创建一个Excel操作实例
        print("开始测试了")

    @data(*test_data)
    def test_api(self,data_item):
        print("正在运行第{0}条用例：{1}".format(data_item['id'],data_item['description']))
        print("测试数据是:{0}".format(data_item['param']))
        url='http://119.23.241.154:8080/futureloan/mvc/api/member/register'
        #进行HTTP请求
        res=HttpRequest().http_request(url,eval(data_item['param']),data_item['HttpMethod'])
        print("测试结果是：",res)
        #加断言
        try:
            self.assertEqual(str(data_item['ExpectedResult']),str(res['code']))
            TestResult='PASS'
        except AssertionError as e:#断言异常
            TestResult='Failed'
            raise e#对异常处理完毕之后 要记得抛出
        finally:#最终都要写回到Excel
            self.t.write_back(data_item['id']+1,res['code'],TestResult)

    def tearDown(self):
        print("结束这个用例的测试")