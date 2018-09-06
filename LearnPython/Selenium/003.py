import requests


def http_request(url, data, method='get'):
    if method == 'get':
        res = requests.get(url, data)
    else:
        res = requests.post(url, data)
    print(res.headers)


login_url = 'https://www.baidu.com'
login_data = ''
http_request(login_url, data=login_data)