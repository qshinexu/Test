import requests
def test_get():
    url= 'https://www.baidu.com'
    r = requests.post(url)
    print(r.cookies)
