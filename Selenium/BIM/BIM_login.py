from selenium import webdriver
import requests
## 获取token
def get_token():
    url = 'http://192.168.1.234:8086/bim/user/login'
    data = {
        "params": {
            "username": "zhangyi@huajie.com",
            "password": "f865b53623b121fd34ee5426c792e5c33af8c227",
            "app_id": 1,
            "app_version": "1.0.2"
        }
    }
    HEADER = {
        'Content-Type': 'application/json'
    }
    r = requests.post(url,json= data,headers = HEADER)
    return r.json()['data']

# def findId(id):
#     e = driver.find_element_by_id(id)
#     return e


driver = webdriver.Chrome()
driver.maximize_window()
# driver.get('http://192.168.1.234:8086/bimweb/')
url= 'http://192.168.1.234:8086/bimweb/main/home?token=' + get_token() + '&currOrgId=1&currOrgName=%E5%8D%8E%E6%9D%B0%E5%85%AC%E5%8F%B8&orgChangeType=0'""
driver.get(url)

## 此项为项本地缓存中添加，当前项目未使用该机制，因此无法使用该方法绕开登录
# driver.execute_script('localStorage.setItem("token", %s);'% get_token())

## 点击系统管理菜单
driver.find_element_by_id('menu-001').click()




