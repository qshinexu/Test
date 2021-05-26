import  requests,json
r = requests.post("http://httpbin.org/post",data={1:1,2:2})
obj=json.loads(text=r.content.decode("utf-8"))
print(r.text)
print(r.status_code)
