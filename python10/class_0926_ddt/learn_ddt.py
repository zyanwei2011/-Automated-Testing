# -*- coding: utf-8 -*-
# @Time    : 2018/9/26 21:47
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : learn_ddt.py
#ddt 结合单元测试 来做的
#帮我们拆分数据 传递参数给测试用例

# def print_msg(*args):
#     print("获取到的参数是:",args)
#     print("获取到的参数类型是:",type(args))
#     print("获取到的参数长度是:",len(args))

#print_msg(1,2,3,4,5,6,7,8)
# a=(1,2,3,4)
# a=[{"age":18,"name":"二两"},
#    {"age":20,"name":"boy"},
#    {"age":23,"name":"流沙"}]
# print_msg(*a)
#ddt 单元测试
import unittest
from ddt import ddt,data,unpack
from class_0926_ddt.do_excel import DoExcel
from class_0926_ddt.read_config import ReadConfig

# test_data=[[1,2,3],
#            [3,4,5]]

test_data=[{"x":1,"y":2},
           {"x":2,"y":3}]
# button=ReadConfig().read_config("case.config","FLAG","button")
# case_id_list=eval(ReadConfig().read_config("case.config","FLAG","case_id_list"))
# test_data=DoExcel().do_excel(button,case_id_list)

@ddt  #@装饰器  ddt 专门装饰测试类
class TestMath(unittest.TestCase):

    @data(*test_data)         #专门装饰测试用例的
    # @unpack
    def test_add_1(self,item):
        print("******")
        print(item)
        a=item["x"]
        b=item["y"]
        print("a+b的和是:{0}".format(a+b))


if __name__ == '__main__':
    unittest.main()
