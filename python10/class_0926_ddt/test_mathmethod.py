__author__ = 'zz'

import unittest
from ddt import ddt,data
from class_0926_ddt.do_excel import DoExcel
from class_0926_ddt.read_config import ReadConfig
from class_0926_ddt.math_method import MathMethod#导入被测试类

button=ReadConfig().read_config("case.config","FLAG","button")
case_id_list=eval(ReadConfig().read_config("case.config","FLAG","case_id_list"))
test_data=DoExcel().do_excel(button,case_id_list)

@ddt
class TestAdd(unittest.TestCase):#测试类
    def setUp(self):#测试环境的搭建
        print("我要开始测试！")
        self.t=MathMethod()
        self.wb=DoExcel()#操作Excel的实例

    @data(*test_data)
    def test_add_s(self,item):#测试加法 用例?
        print("正在执行的用例是:{0}".format(item['title']))
        print("a的值{0}".format(item['Param_a']))
        print("b的值{0}".format(item['Param_b']))
        print("expected的值{0}".format(item['ExpectedResult']))
        res=self.t.add(item['Param_a'],item['Param_b'])#实际运算值 要写入到每一行的第6列
        try:
            self.assertEqual(item['ExpectedResult'],res)#断言函数的调用
            test_result='PASS'#最终的测试结论  要写每一行的第7列
        except AssertionError as e:#捕捉的是断言异常?
            test_result='FAIL'#最终的测试结论 要写每一行的第7列
            print("测试出错了，错误是：{0}".format(e))
            raise e#抛出错误
        finally:
            self.wb.write_back(item['id']+1,res,test_result)

    def tearDown(self):#测试环境的销毁
        print("测试完成咯")
