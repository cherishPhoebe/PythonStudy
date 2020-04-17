import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import re
import os
 
browser = webdriver.Chrome()
# 设置网站等待时间
wait = WebDriverWait(browser, 10)
 
def get_one(url):
    print('正在爬取 %s...' % (url))
    try:
        browser.get(url)
        html = browser.page_source
        if html:
            return html
    except EOFError:
        return None
 
def pares_one(html):
    soup = BeautifulSoup(html, 'lxml')
    imgs = soup.select('img')
    num = soup.select('#body #comments .comments .current-comment-page')[0].getText()[1:-1]
    print('num'+ num)
    next_url = 'http://jandan.net/ooxx/page-{}#comments'.format(int(num)-1)
    print("next_url" + next_url)
 
    count = 0
    for img in imgs:
        img_url = re.findall('src="(.*?)"', str(img))
        if not img_url[0][-3:] == 'gif':
            if not img_url[0][-3:] == 'png':
                if img_url[0][-3:] == 'jpg':
                    if img_url[0][0:4] == 'http':
                        print('正在下载：%s 第 %s 张' % (img_url[0], count))
                        write_fo_file(img_url[0], num, count)
        count += 1
    return next_url
 
def pares_one_of_num(html):
    soup = BeautifulSoup(html, 'lxml')
    imgs = soup.select('img')
 
    num = soup.select('#body #comments .comments .current-comment-page')[0].getText()[1:-1]
    print('num'+ num)
    next_url = 'http://jandan.net/ooxx/page-{}#comments'.format(int(num)-1)
 
    count = 0
    for img in imgs:
        img_url = re.findall('src="(.*?)"', str(img))
        if not img_url[0][-3:] == 'gif':
            if not img_url[0][-3:] == 'png':
                if img_url[0][-3:] == 'jpg':
                    if img_url[0][0:4] == 'http':
                        print('正在下载：%s 第 %s 张' % (img_url[0], count))
                        write_fo_file(img_url[0], num, count)
        count += 1
    return num, next_url
 
def write_fo_file(url, num, count):
    dirName = u'{}/{}'.format('jiandan', num)
    if not os.path.exists(dirName):
        os.makedirs(dirName)
 
    filename = '%s/%s/%s.jpg' % (os.path.abspath('.'), dirName, count)
    print(filename)
    with open(filename, 'wb+') as jpg:
        jpg.write(requests.get(url).content)
 
def next(url):
    html = get_one(url)
    percent_num, next_url = pares_one_of_num(html)
    while int(percent_num) > 0:
        next(next_url)
 
def main():
    url = 'http://jandan.net/ooxx/page-49#comments'
    html = get_one(url)
    next_url = pares_one(html)
    next(next_url)
 
if __name__ == '__main__':
    main()
