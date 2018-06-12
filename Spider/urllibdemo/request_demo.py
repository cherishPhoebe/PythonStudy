from urllib import request
from urllib import parse
from urllib import error
import socket

#response = request.urlopen("http://www.baidu.com")
#print(response.read().decode('utf-8'))
#print(response.status)
#print(type(response))
#print(response.getheaders())

# timeout 使用，try except 捕获异常
#data = bytes(parse.urlencode({'word':'hello'}),encoding='utf-8')
#try:
#    rsp = request.urlopen('http://httpbin.org/post',data=data,timeout=0.1)
#    print(rsp.read())
#except error.URLError as e:
#    if isinstance(e.reason,socket.timeout):
#        print("time out")

#request 对象使用
#req = request.Request('http://python.org')
#response = request.urlopen(req)
#print(response.read())
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
data = bytes(parse.urlencode({'word':'hello'}),encoding='utf-8')
req = request.Request('http://httpbin.org/post',data=data,method='POST')
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
rsp = request.urlopen(req)
print(rsp.read().decode('utf-8'))

