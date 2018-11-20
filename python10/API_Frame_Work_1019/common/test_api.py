# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 21:10
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : test_api.py
#引入ddt
import unittest

from ddt import ddt,data
from API_Frame_Work_1019.common import project_path
from API_Frame_Work_1019.common.http_request import HttpRequest
from API_Frame_Work_1019.common.do_excel import DoExcel
from API_Frame_Work_1019.common.read_config import ReadConfig
from API_Frame_Work_1019.common.my_log import  MyLog

logger=MyLog()#实例

#从配置文件里面获取button和case_id_list的值
button=ReadConfig().read_config(project_path.case_config_path,'CASECONFIG','button')
case_id_list=ReadConfig().read_config(project_path.case_config_path,'CASECONFIG','case_id_list')
#获取测试数据
test_data=DoExcel(project_path.test_cases_path).get_data(button,case_id_list)

#全局变量
COOKIES=None

@ddt
class TestApi(unittest.TestCase):
    def setUp(self):
        self.t=DoExcel(project_path.test_cases_path)#创建一个Excel操作实例
        logger.info("开始测试了")

    @data(*test_data)
    def test_api(self,data_item):
        global COOKIES#声明是全局变量
        logger.info("正在运行第{0}条用例：{1}".format(data_item['id'],data_item['description']))
        logger.info("测试数据是:{0}".format(data_item['param']))
        #进行HTTP请求
        res=HttpRequest().http_request(data_item['url'],eval(data_item['param']),data_item['HttpMethod'],COOKIES)#全局变量
        #可以获取到cookie吗？
        if res.cookies:#任何非空数据的布尔值都为True  cookies是一个类字典的格式
            COOKIES=res.cookies#如果cookies不为空 就替换全局变量的COOKIES 修改全局变量

        logger.info("测试结果是：{0}".format(res.json()))
        #加断言
        try:
            self.assertEqual(str(data_item['ExpectedResult']),str(res.json()['code']))#res.json()['code']
            TestResult='PASS'
        except AssertionError as e:#断言异常
            TestResult='Failed'
            logger.error("请求出错了，错误是{0}".format(e))
            raise e#对异常处理完毕之后 要记得抛出
        finally:#最终都要写回到Excel
            self.t.write_back(data_item['id']+1,res.json()['code'],TestResult)

    def tearDown(self):
        logger.info("结束这个用例的测试")