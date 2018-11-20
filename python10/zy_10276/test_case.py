import unittest
from zy_10276.do_excel import DoExcel
from ddt import ddt,data  # 导入单元测试框架
from zy_10276.read_config import ReadConfig
from zy_10276.zy_re import HttpRequest

# 加载测试数据
button = ReadConfig().read_config('case.config', 'CASE_LIST', 'button')
case_id_list = ReadConfig().read_config('case.config', 'CASE_LIST', 'case_id_list')
test_data = DoExcel('test_data.xlsx').read_data(button, case_id_list)

@ddt
class TestApi(unittest.TestCase):
    def setUp(self):
        self.wb = DoExcel('test_data.xlsx')

    def tearDown(self):
        pass

    @data(*test_data)
    def test_api(self, item):
        print('正在执行测试用例{0}：{1}'.format(item['id'],item['title']))
        url_register = 'http://47.107.168.87:8080/futureloan/mvc/api/member/register'
        res = HttpRequest().http_request(item['method'], url_register, eval(item['param']))
        try:
            self.assertEqual(int(res),item['ExpectedResult(code)'])
            test_result = 'PASS'
        except AssertionError as e:
            test_result = 'FAIL'
            raise e
        finally:
            self.wb.write_back(item['id'] + 1, res, test_result)

