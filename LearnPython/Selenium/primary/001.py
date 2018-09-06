import  requests
url = 'http://192.168.1.234:8086/bim/user/login'
data = {
    "params": {
        "username": "1212@qq.com",
        "password": "f865b53623b121fd34ee5426c792e5c33af8c227",
        "app_id": 1,
        "app_version": "1.0.2"
    }
    }
HEADER = {
        'Content-Type': 'application/json'
    }

r = requests.post(url = url,json = data,headers = HEADER)
print(r.status_code)
print(r.text)
print(r.json()['data'])
