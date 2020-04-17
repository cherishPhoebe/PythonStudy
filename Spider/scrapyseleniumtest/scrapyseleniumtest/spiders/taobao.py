# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import quote
from scrapyseleniumtest.items import ProductItem

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    base_url = ['http://s.taobao.com/search?q=']

    def parse(self, response):
        pass

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1,self.settings.get('Max_page')+1):
                url = self.base_url + quote(keyword)
                yield scrapy.Request(url = url,callback=self.parse,meta={'page':page},dont_filter=True)
