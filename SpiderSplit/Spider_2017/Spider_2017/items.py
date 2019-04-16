# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Spider2017Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    press = scrapy.Field()
    price = scrapy.Field()
    comments = scrapy.Field()
    url = scrapy.Field()
