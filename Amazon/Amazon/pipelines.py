# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from googletrans import Translator

class AmazonPipeline(object):

    def open_spider(self, spider):
        # 实例化
        translator = Translator(service_urls=['translate.google.cn'])
        if not os.path.exists('./data'):
            os.makedirs('./data')

    def process_item(self, item, spider):
        sort_num = item['sort_num'] or '空'
        title = item['title'] or '空'
        pingfen = item['pingfen'] or '空'
        pingfen_people = item['pingfen_people'] or '空'
        price = item['price'] or '空'
        l = [sort_num,title,pingfen,pingfen_people,price]
        # print(l)
        with open("./data/data.csv",'a',encoding='utf8') as f :
            f.write(' '.join(l))
            f.write('\n')

        return item

    def close_spider(self, spider):
        pass
