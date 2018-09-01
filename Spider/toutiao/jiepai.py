from multiprocessing.pool import Pool
from urllib.parse import urlencode
import requests
import os
from hashlib import md5

def get_page(offset):
    params = {
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':20,
        'cur_tab':'1',
        'from':'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/?'+urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            if item.get('image_list'):
                title = item.get('title')
                images = item.get('image_list')
                for image in images:
                    yield{
                        'title':title,
                        'image':image.get('url')
                    }

def save_image(item):
    if not os.path.exists('jiepai'):
        os.mkdir('jiepai')
    dirName = u'{0}/{1}'.format('jiepai', item.get('title'))
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    try:
        response = requests.get('http:'+item.get('image').replace('list', 'origin'))
        if response.status_code == 200:
            file_path = '{0}/{1}/{2}.{3}'.format('jiepai',item.get('title'), md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    print('Save image to ',file_path)
                    f.write(response.content)
            else:
                print('Alread Downloaded',file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')

def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x*20 for x in range(GROUP_START,GROUP_END+1)])
    pool.map(main,groups)
    pool.close()
    pool.join()
