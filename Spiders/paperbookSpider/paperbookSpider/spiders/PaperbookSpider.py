# -*- coding: utf-8 -*-
import scrapy
from paperbookSpider.items import PaperbookspiderItem

class PaperbookspiderSpider(scrapy.Spider):
    name = 'PaperbookSpider'
    # start_urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-201%d-0-1-1' %i for i in
    #               range(5, 9)]
    start_urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-201%d-0-1-1'% i for i in range(5,9)]
    def parse(self, response):
        item = PaperbookspiderItem()
        url_list = response.css('div#sortRanking').xpath('div')
        for url in url_list:
            item['url'] = url.css('div.side_nav').xpath('a/@href').extract_first()
            yield item

       #将数据库中的链接拼接 225*25（1-26）
        # for url in url_list:
        #     for i in range(1,26):
        #         url = url[:-1].join(str(i))