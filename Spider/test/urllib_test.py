#直接引入urllib.request对象模块
#import urllib.request
#response = urllib.request.urlopen("http://www.baidu.com")
#print(response.read())

import urllib

request = urllib.Request()

response = request.urlopen("http://www.baidu.com")
print(response)


