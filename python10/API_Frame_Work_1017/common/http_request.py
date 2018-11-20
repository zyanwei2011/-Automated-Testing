# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 20:45
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : http_request.py
import requests
#语法：数字字母下划线组成 不能以数字开头
#规范：变量名 模块名。包名 最好都是小写字母 不同的字母之间用下划线区别开
#类名 首字母大写 驼峰

class HttpRequest:
    def http_request(self,url,param,http_method):
        if http_method.upper()=='POST':
            try:
                res=requests.post(url,param)
            except Exception as e:
                print("post请求出现了异常:{0}".format(e))
        else:
            try:
                res=requests.get(url,param)
            except Exception as e:
                print("get请求出现了异常:{0}".format(e))
        print("http请求的结果是:{0}".format(res.json()))
        return res.json()#返回结果

if __name__ == '__main__':
    url='http://119.23.241.154:8080/futureloan/mvc/api/member/register'
    param={"mobilephone":"13667670001","pwd":"123456","regname":"lemonban001"}
    HttpRequest().http_request(url,param,'post')