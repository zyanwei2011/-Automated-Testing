# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 21:51
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : http_request.py
import requests

#python requests 参数都是字典的形式传递
url='https://www.ketangpai.com/UserApi/login'
params={'email':'1255811581@qq.com',
        'password':'huahua90!@',
        'remember':0}
res=requests.post(url,params)#https://www.ketangpai.com/UserApi/login

#响应头
# print("响应头:",res.headers)

#状态码
# print("状态码:",res.status_code)

#响应报文 text--返回的是字符串  text-->html  json xml
# print("响应报文1:",res.text)

#响应报文 json()--返回的是字典  可以根据key去取值  json()-->json
# print("响应报文2:",res.json())
# print("响应报文2:",res.json()['info'])

#cookie
# print("cookies",res.cookies)
#错误示范
# res_2=requests.get("http://www.baidu.com")
# print(res_2.json())

requests.request()