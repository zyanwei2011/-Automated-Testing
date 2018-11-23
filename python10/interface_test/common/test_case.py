import unittest
from interface_test.common.do_excel import DoExcel
from ddt import ddt,data  # 导入单元测试框架
from interface_test.common.read_config import ReadConfig
from interface_test.common.api_request import HttpRequest
from interface_test.common import project_path
from interface_test.common.test_log import MyLog

# 加载测试数据
button = ReadConfig().read_config(project_path.config_path, 'CASE_LIST', 'button')
case_id_list = ReadConfig().read_config(project_path.config_path, 'CASE_LIST', 'case_id_list')
test_data = DoExcel(project_path.test_data_path,'register').read_data(button, case_id_list)

login_cookies = None


@ddt
class TestApi(unittest.TestCase):
    def setUp(self):
        self.wb = DoExcel(project_path.test_data_path,'register')
        self.logger = MyLog()
        self.logger.info('Start')

    def tearDown(self):
        self.logger.info('End')
        pass

    @data(*test_data)
    def test_api(self, item):
        global login_cookies
        self.logger.info('正在执行第{0}条测试用例：{1}，参数：{2}'.format(item['id'], item['title'], item['param']))
        res = HttpRequest().http_request(item['method'], item['url'], eval(item['param']), cookies=login_cookies)
        if res.cookies:
            login_cookies = res.cookies
        self.logger.info('测试结果是:{0}'.format(res))
        try:
            self.assertEqual(int(res.json()['code']),item['ExpectedResult(code)'])
            test_result = 'PASS'
            self.logger.info('测试通过')
        except AssertionError as e:
            test_result = 'FAIL'
            self.logger.error('测试出错了：{0}'.format(e))
            raise e
        finally:
            self.wb.write_back(item['id'] + 1, res.json()['code'], test_result)

