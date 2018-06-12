import urllib.request,urllib.error,socket

try:
    response = urllib.request.urlopen('http://www.baidu.com')
except urllib.error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
except urllib.error.URLError as e:
    print(e.reason)
else:
    print("Successfully")