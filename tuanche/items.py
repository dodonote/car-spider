# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class TuancheItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    date = scrapy.Field()
    signup_count = scrapy.Field()

