import unittest
from ddt import ddt, data, unpack

test_data = [[1, 2],
             [3, 4],
             [5, 6],
             [7, 8]]

@ddt  # ddt：装饰测试类
class Testmul(unittest.TestCase):
    def setUp(self):
        print('开始测试了')


    def tearDown(self):
        print('测试结束了')

    @data(*test_data)                 # 装饰测试用例
    @unpack
    def test_mul(self, a, b):
        print('两个数的乘积是{0}'.format(a * b))



if __name__ == '__main__':
    unittest.main()
