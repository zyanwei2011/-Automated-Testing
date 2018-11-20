from zy_resquests.do_excel import Do_Excel
from zy_resquests.zy_re import Http_Request

test_data = Do_Excel().read_data('test_data.xlsx', 'register')
url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/register'
for item in test_data:
    res = Http_Request().http_request(item['method'], url, params=eval(item['param']))
    if int(res) == item['ExpectedResult(code)']:
        TestResult = 'PASS'
    else:
        TestResult = 'FAIL'
    Do_Excel().write_back('test_data.xlsx', 'register',item['id']+1, res,TestResult)


