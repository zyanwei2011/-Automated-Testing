import os

# 获取当前项目路径
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 拼接配置文件路径
config_path = os.path.join(project_path, 'config', 'case.config')

# 拼接测试数据文件路径
test_data_path = os.path.join(project_path, 'test_data', 'test_data.xlsx')

# 拼接测试报告文件路径
test_result_path = os.path.join(project_path, 'test_result', 'results', 'test_result.html')

# 拼接测试日志文件路径
test_log_path = os.path.join(project_path, 'test_result', 'logs', 'test_api_log.txt')



