#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-10-24 23:01:31
# Project: tripadvisor

from pyspider.libs.base_handler import *
import pymongo

class Handler(BaseHandler):
    crawl_config = {
    }
    
    client = pymongo.MongoClient('localhost')
    db = client['fangchan']

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://cs.newhouse.fang.com/house/s/', callback=self.index_page, validate_cert = False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('#newhouse_loupai_list .nlcd_name a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert = False)
            
        next = response.doc("#sjina_C01_47 > ul > li.fr > a.active").next()
        print(next)
        if(next & next.attr.href):
            self.crawl(next.attr.href,callback=self.index_page,validate_cert=False)
        

    @config(priority=2)
    def detail_page(self, response):
        url = response.url
        title = response.doc('body > div.main_1200.tf > div.firstbox > div.firstright.fr > div.information > div.inf_left1 > div > h1 > strong').text()
        return {
            "url": response.url,
            "title": title,
        }
    
    
    def on_result(self,result):
        if(result):
            self.save_to_mongo(result)
    
    def save_to_mongo(self,result):
        print(result.title)
        if self.db['cs'].insert(result):
            print('saved to mongo',result)


