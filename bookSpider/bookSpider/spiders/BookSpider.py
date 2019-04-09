# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from bookSpider.items import BookspiderItem
class BookspiderSpider(scrapy.Spider):
    name = 'BookSpider'
    start_urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-%d'%j for j in range(1,26)]

    def parse(self, response):
        item = BookspiderItem()
        #sel = selector(response)
        book_list = response.css('ul.bang_list.clearfix.bang_list_mode').xpath('li')
        for book in book_list:
        	item['rank'] = book.css('div.list_num').xpath('text()').extract_first()
        	item['name'] = book.css('div.name').xpath('a/text()').extract_first()
        	item['author'] = book.css('div.publisher_info')[0].xpath('a/text()').extract_first()
        	item['press'] = book.css('div.publisher_info')[1].xpath('a/text()').extract_first()
        	item['price'] = book.css('span.price_n').xpath('text()').extract_first()
        	item['comments'] = book.css('div.star').xpath('a/text()').extract_first()
        	yield item
