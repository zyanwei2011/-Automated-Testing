## 统一编码格式
# coding:utf-8
## 导入webdriver已备引用api
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


def findId(id):
    e = driver.find_element_by_id(id)
    return e

def findLinkText(text):
    e = driver.find_element_by_link_text(text)
    return e

def login(username,password):
    findLinkText('登录').click()
    findId('TANGRAM__PSP_10__footerULoginBtn').click()
    findId('TANGRAM__PSP_10__userName').send_keys(username)
    time.sleep(3)
    findId('TANGRAM__PSP_10__password').send_keys(password)
    ## 此处等待是为了避开百度的检查机制，太快会进行手机验证
    time.sleep(5)
    findId('TANGRAM__PSP_10__submit').click()




## 获取浏览器对象
driver = webdriver.Chrome()
## 浏览器全屏
driver.maximize_window()
## 隐式等待30s
driver.implicitly_wait(30)
driver.get('https://www.baidu.com')
## 搜索框输入内容
findId("kw").send_keys('selenium')
## 点击操作
findId("su").click()

## 登录
login('zyanwei2011','zy383417')
## 打印昵称
nickname = findId('user').text

## 进入个人中心
## ActionChains 定义鼠标事件
ActionChains(driver).move_to_element(findId('user')).perform()

findLinkText('个人中心').click()



## 退出
# driver.quit()

