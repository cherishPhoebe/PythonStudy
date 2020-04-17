import requests,os

# res = requests.get('https://www.baidu.com/')
# print(type(res))
# print(res.status_code)
# print(type(res.text))
# print(res.text)
# print(res.cookies)

# data = {
#     'name':'ziye',
#     'age':18
# }
# r = requests.get('http://httpbin.org/get',params=data)
# print(r.text)

# path = os.getcwd()
# r = requests.get("https://github.com/favicon.ico")
# with open(path+r"\favicon.ico","wb") as f:
#     f.write(r.content)

# headers = {
#     "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'

# }
# r = requests.get("https://www.zhihu.com/explore",headers=headers)
# print(r.text)

# session 会话保持
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)


