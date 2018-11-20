import requests
from interface_test.common.test_log import MyLog

requests_logger = MyLog()  # 实例化


class HttpRequest:
    def http_request(self, method, url, params, cookies=None):
        try:
            res = requests.request(method, url, params=params, cookies=cookies)
            requests_logger.info('正在进行{0}请求'.format(method))
        except Exception as e:
            requests_logger.error('请求出错了：{0}'.format(e))
        requests_logger.info('测试请求的结果是{0}'.format(res.text))
        return res


if __name__ == '__main__':
    url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/register'
    kv = {"mobilephone":"13433333341","pwd":"123456","regname":"test_zy"}
    r = HttpRequest().http_request('POST', url, params=kv)
    print(r)

