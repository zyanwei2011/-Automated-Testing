__author__ = 'zz'
import os
# print(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])
Project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#配置文件路径吗？
case_config_path=os.path.join(Project_path,'config','case.config')


#测试用例的路径
test_cases_path=os.path.join(Project_path,'test_data','api.xlsx')

#html报告的路径
report_path=os.path.join(Project_path,'test_result','report','test_api.html')


#日志文件路径
logs_path=os.path.join(Project_path,'test_result','logs','test_api.txt')
# print(logs_path)