# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymysql.cursors
import ebookSpider.settings as msg

class EbookspiderPipeline(object):
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
                "insert into ebookurl(url)value(%s)",(item['url']))
            self.connect.commit()
        except Exception as error:
            print(error)
        return item