import re
from bs4 import BeautifulSoup
import requests
import time
import json


class CarInfo:
    """
    车辆信息：
        型号，链接，用户评分，图片，级别，续航里程，发动机，充电时间，官方指导价，折扣后价格，颜色列表
    """
    seriesid = ''
    name = ''
    url = ''
    score = ''
    image = ''
    level = ''
    dist = ''
    motor = ''
    charge_time = ''
    official_price = ''
    discounted_price = ''
    colors = []


class BrandInfo:
    """
    品牌信息：
        名称，链接，车型列表
    """
    name = ''
    url = ''
    cars = []


def getUrlContent(url):
    """
    description: 获取指定url的内容\n
    param url: 链接地址\n
    return: 返回链接的页面内容，html文本。\n
        如果出错，返回None。
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def log(msg):
    print('[LOG] ' + ', ' + time.strftime('%H:%M:%S',time.localtime(time.time())) + ': ' + str(msg))


def getCarConfig(content):
    cars = []
    if content is not None:
        soup = BeautifulSoup(content, 'lxml')
        scripts = soup.find_all('script')
        
        seriesid = ''
        for index in range(len(scripts)):
            if(scripts[index] is not None and scripts[index].string is not None):                    
                configStr = re.findall('var config = (.*?)\};', scripts[index].string)          
                optionStr = re.findall('var option = (.*?)\};', scripts[index].string)
                if configStr is not None and len(configStr) > 0:
                    stocks = configStr[0] + "}"
                    carConfigModel = json.loads(stocks)
                    result = carConfigModel['result']
                    seriesid = result['seriesid']
                    log(type(carConfigModel))
                    with open(seriesid + '_config.json', 'w', encoding='utf-8') as cf:
                        json.dump(carConfigModel, cf)

                if optionStr is not None and len(optionStr) > 0:
                    stocks = optionStr[0] + "}"
                    carOptionModel = json.loads(stocks)
                    with open(seriesid + '_option.json', 'w', encoding='utf-8') as of:
                        json.dump(carOptionModel, of)
                        
                    #paramtypeitems = result['paramtypeitems']
                    #speclist = result['speclist']
                    #for i in range(len(speclist)):
                    #    car = carinfo()
                    #    car.specid = speclist[i]['specid']
                    #    cars.append(car)

                    # for pti in range(len(paramtypeitems)):
                    #     paramitems = paramtypeitems[pti]["paramitems"]
                    #     for pi in range(len(paramitems)):                            
                    #         if paramitems[pi]['name'].startswith('车型'):
                    #             valueitems = paramitems[pi]['valueitems']
                    #             for vi in range(len(valueitems)):
                    #                 cari = list(filter(lambda x : x.specid == valueitems[vi]['specid'] ,cars))[0]
                    #                 cari.name = valueitems[vi]['value']
                                        
            

                        #json.dump(cars, f)
                        # for c in cars:
                        #    log(c.name)
            pass


if __name__ == '__main__':
    url = 'https://car.autohome.com.cn/config/series/5824.html#pvareaid=3454437'
    content = getUrlContent(url)
    getCarConfig(content)
    # cars = list(getCarConfig(content))
    # print(cars)

