# -*- coding: utf-8 -*-
import scrapy
from ebookSpider.items import EbookspiderItem

class EbookspiderSpider(scrapy.Spider):
    name = 'EbookSpider'
    start_urls = ['http://bang.dangdang.com/books/ebooks/98.01.00.00.00.00-year-201%d-0-1-1' %i for i in range(5, 9)]

    def parse(self, response):
        item = EbookspiderItem()
        url_list = response.css('#sortRanking > ul').xpath('li')
        for url in url_list:
            item['url'] = url.xpath('a/@href').extract_first()
            yield item

