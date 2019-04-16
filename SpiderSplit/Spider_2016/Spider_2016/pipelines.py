# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymysql.cursors
import Spider_2016.settings as msg
class Spider2016Pipeline(object):
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
                # """insert into paperbookinfo(rank,book,author,press,price,comments)
                # value(%s,%s,%s,%s,%s,%s)""",
                  """insert into 2016bookinfo(rank,book,author,press,price,comments,url)
                value(%s,%s,%s,%s,%s,%s,%s)""",
                (item['rank'],
                 item['name'],
                 item['author'],
                 item['press'],
                 item['price'],
                 item['comments'],
                 item['url']))
            self.connect.commit()
        except:
            self.connect.rollback()
        return item
    def close_spider(self):
        self.cursor.close()
        self.connect.close()