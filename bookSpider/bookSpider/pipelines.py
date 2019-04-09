# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.crawler import Settings as settings
import pymysql
import pymysql.cursors
import bookSpider.settings as msg
class BookspiderPipeline(object):
    def process_item(self, item, spider):
        return item
class DBPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host = msg.MYSQL_HOST,
            db = msg.MYSQL_DBNAME,
            user = msg.MYSQL_USER,
            passwd = msg.MYSQL_PASSWD,
            charset = 'utf8',
            use_unicode = True
        )
        self.cursor = self.connect.cursor()
    def process_item(self,item,spider):
        try:
            self.cursor.execute(
                """insert into changxiao(rank,book,author,press,price,comments)
                value(%s,%s,%s,%s,%s,%s)""",
                (item['rank'],
                 item['name'],
                 item['author'],
                 item['press'],
                 item['price'],
                 item['comments']))
            self.connect.commit()
        except Exception as error:
            print(error)
        return item


