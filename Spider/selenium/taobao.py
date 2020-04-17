from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
KEYWORD = 'ipad'

def index_page(page):
    """
    抓取索引页
    :param page：页码
    """
    print("正在抓取第",page,"页")
    try:
        url = 'https://s.taobao.com/search?q='+ quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist > div > div > div:nth-child(1) > div.item')))
        get_products()
    except TimeoutException:
        index_page(page)

from pyquery import PyQuery as py
def get_products():
    """
    提取商品数据
    """
    html = browser.page_source
    doc = py(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pie .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal':item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location ':item.find('.location').text()
        }
        print(product)
        # save_to_mango(product)

import pymongo
MONGO_URL = "localhost"
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
def save_to_mango(product):
    """
    保存至MONGODB
    """
    try:
        if db[MONGO_COLLECTION].insert(product):
            print("保存成功")
    except Exception:
        print("保存失败")

MAX_PAGE = 5
def main():
    for i in range(1,MAX_PAGE+1):
        index_page(i)

if __name__ == '__main__':
    main()