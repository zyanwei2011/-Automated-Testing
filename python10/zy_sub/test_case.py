import unittest
from ddt import ddt,data,unpack
from zy_sub.code import Sub
from zy_sub.do_excel import DoExcel
from zy_sub.conf import ReadConfig


button = ReadConfig().read_config('case.conf', 'SECTION', 'button')
case_no = eval(ReadConfig().read_config('case.conf', 'SECTION', 'case_id'))  # 配置文件读取的数据默认为字符串
# ['case_id', 'title', 'param_a', 'param_b', 'ExpectedResult', 'ActualResult', 'TestResult']

test_data = DoExcel().read_data(button, case_no)


@ddt  # ddt：装饰测试类
class TestSub(unittest.TestCase):
    def setUp(self):
        self.t = Sub()
        self.wb = DoExcel()


    @data(*test_data)
    def test_sub(self, item):
        print('用例标题：{}'.format(item['title']))
        res = self.t.sub(item['param_a'], item['param_b'])
        try:
            self.assertEqual(res, item['ExpectedResult'])
            test_result = 'PASS'
        except AssertionError as e:
            test_result = 'FAIL'
            raise e
        finally:
            self.wb.write_back(item['case_id']+1, res, test_result)

    def tearDown(self):
        print('测试完成了')

