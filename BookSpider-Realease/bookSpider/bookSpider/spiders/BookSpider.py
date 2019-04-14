# -*- coding: utf-8 -*-
import scrapy
from bookSpider.items import BookspiderItem
import pymysql
import pymysql.cursors
import bookSpider.settings as msg
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
	url_list = cur.execute("select * from ebookurl")
	url_list = list(cur.fetchall())
	cur.close()
	conn.close()

class BookspiderSpider(scrapy.Spider):
	name = 'BookSpider'
	#从数据库获取初始url

	#更改获取的url的页码
	url_list = get_url_list.url_list
	url_all_list = []
	#url_list =list(tuple)
	#print(type(url_list))
	for url in url_list:
		#print(str(url)[2:-4])#   2-77位
		for i in range(1,26):
			url_all_list.append((str(url)[2:-4])+str(i))
		#print(url)
	start_urls = url_all_list
	#保存数据

	def parse(self, response):
		item = BookspiderItem()
		book_list = response.css('ul.bang_list.clearfix.bang_list_mode').xpath('li')
		for book in book_list:
			item['rank'] = book.css('div.list_num').xpath('text()').extract_first()
			item['name'] = book.css('div.name').xpath('a/text()').extract_first()
			item['author'] = book.css('div.publisher_info')[0].xpath('a/text()').extract_first()
			item['press'] = book.css('div.publisher_info')[1].xpath('a/text()').extract_first()
			item['price'] = book.css('span.price_n').xpath('text()').extract_first()
			item['comments'] = book.css('div.star').xpath('a/text()').extract_first()
			yield item
# class ClassifySpider(scrapy.Spider):
# 	name = 'classify'
# 	start_urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-201%d-0-1-%d'%(i,j)for i in range(5,9) for j in range(1,26)]
# 	start_urls.append(['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-month-2019-1-1-1'])
# 	def parse(self, response):
# 		item = ClassifyItem()
# 		urls = response.css('div.bang_nav_box.bang_nav').xpath('div')
# 		for url in urls:
# 			item['url'] = urls.css('div.side_nav').xpath('a/href()').extract_first()
# 			yield item
#
# process = CrawlerProcess()
# process.crawl(BookspiderSpider)
# process.crawl(ClassifySpider)
# process.start()