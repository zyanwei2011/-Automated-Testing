import  requests

url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
kv = {"mobilephone": "13433333341", "pwd": "123456", "regname": "test_zy"}
method = 'POST'

res = requests.request(method, url, params=kv,cookies=None)
login_cookies = res.cookies
print(login_cookies)

url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
kv = {"mobilephone": "13433333341", "amount": "12"}
method = 'GET'

res = requests.request(method, url, params=kv, cookies=login_cookies)
print(res.json()['code'])







