import requests


class HttpRequest:
    def http_request(self, method, url, params):
        try:
            res = requests.request(method, url, params=params).json()
            # 读取code码,将code码作为判断结果比对标准
            res_code = res['code']
        except Exception as e:
            print('测试出错了'.format('e'))
        return res_code


if __name__ == '__main__':
    url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/register'
    kv = {"mobilephone":"13433333341","pwd":"123456","regname":"test_zy"}
    r = HttpRequest().http_request('POST', url, kv)
    print(r)
