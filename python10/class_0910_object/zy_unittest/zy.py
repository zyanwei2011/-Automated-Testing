# 引入单元测试框架
import unittest
# 引入测试类
from zy_unittest.math import Jisuanqi

class TestJisuanqi(unittest.TestCase):

    def test_add(self):
        t = Jisuanqi()
        r = t.add(4, 3)
        print('测试结果是{}'.format(r))

    def test_sub(self):
        t = Jisuanqi()
        r = t.sub(4, 3)
        print('测试结果是{}'.format(r))

    def test_mul(self):
        t = Jisuanqi()
        r = t.mul(4, 3)
        print('测试结果是{}'.format(r))

    def test_div(self):
        t = Jisuanqi()
        r = t.div(4, 3)
        print('测试结果是{}'.format(r))



