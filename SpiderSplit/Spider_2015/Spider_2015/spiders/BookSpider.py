# -*- coding: utf-8 -*-
import scrapy
import pymysql
from Spider_2015.items import Spider2015Item
import Spider_2015.settings as msg
class get_url_list():
	conn = pymysql.Connect(
		host=msg.MYSQL_HOST,
		db=msg.MYSQL_DBNAME,
		user=msg.MYSQL_USER,
		passwd=msg.MYSQL_PASSWD,
		charset='utf8',
		use_unicode=True
	)
	cur = conn.cursor()
	#url_list = cur.execute("select * from paperbookurl")
	url_list = cur.execute("SELECT * FROM paperbookurl WHERE url LIKE '%2015%' UNION SELECT * FROM ebookurl WHERE url LIKE '%2015%'")
	url_list = list(cur.fetchall())
	cur.close()
	conn.close()


class BookspiderSpider(scrapy.Spider):
    name = 'BookSpider'
    url_list = get_url_list.url_list
    url_all_list = []
    for url in url_list:
        # print(str(url)[2:-4])#   2-77位
        for i in range(1, 26):
            url_all_list.append((str(url)[2:-4]) + str(i))
    # print(url)
    start_urls = url_all_list

    def parse(self, response):
        item = Spider2015Item()
        book_list = response.css('ul.bang_list.clearfix.bang_list_mode').xpath('li')
        for book in book_list:
            item['rank'] = book.css('div.list_num').xpath('text()').extract_first()
            item['name'] = book.css('div.name').xpath('a/text()').extract_first()
            item['author'] = book.css('div.publisher_info')[0].xpath('a/text()').extract_first()
            item['press'] = book.css('div.publisher_info')[1].xpath('a/text()').extract_first()
            item['price'] = book.css('span.price_n').xpath('text()').extract_first()
            item['comments'] = book.css('div.star').xpath('a/text()').extract_first()
            item['url'] =book.css('div.pic').xpath('a/@href').extract_first()
            yield item
