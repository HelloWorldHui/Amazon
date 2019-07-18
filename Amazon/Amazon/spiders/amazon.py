# -*- coding: utf-8 -*-
import scrapy
from Amazon.items import AmazonItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.com']
    start_urls = ['http://www.amazon.com/']
    url = 'https://www.amazon.com/gp/new-releases/wireless/2407749011/ref=zg_bs_tab_t_bsnr?language=zh_CN'

    def start_requests(self):
        yield scrapy.Request(self.url, callback=self.parse, cookies={'lc-main': 'zh-CN'})

    def parse(self, response):
        # with open('test.html', 'w', encoding='utf8') as f:
        #     f.write(response.text)
        li_list = response.xpath('//*[@id="zg-ordered-list"]/li')
        # print(li_list)
        for li in li_list:
            item = AmazonItem()
            sort_num = li.xpath('.//span/div/div/span[1]/span/text()').extract_first()
            title= li.xpath('.//span/div/span/a/div/text()').extract_first()
            pingfen = li.xpath('.//span/div/span/div[1]/a[1]/i/span/text()').extract_first()
            pingfen_people = li.xpath('.//span/div/span/div[1]/a[2]/text()').extract_first()
            price = li.xpath('.//span/div/span/div[2]/a/span/span/text()').extract_first()
            price = price or li.xpath('.// span / div / span / div / a / span / span/text()').extract_first()
            item['sort_num'] = sort_num
            item['title'] = title.strip()
            item['pingfen'] = pingfen
            item['pingfen_people'] = pingfen_people
            item['price'] = price
            yield item