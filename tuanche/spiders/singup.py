#! /usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
import sys #要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方 法
reload(sys)


print sys.getdefaultencoding()

sys.setdefaultencoding('utf-8')



class SignupSpider(scrapy.Spider):
    name = "signup"
    allowed_domains = ['tuanche.com']
    start_urls = [
        "http://bj.tuanche.com/b31/tuan/?pg=brandIndex&pl=brandImg"
    ]

    def parse(self, response):
        print response.url
        print response.url.split("/")
        filename = response.url.split("/")[-2]
        print filename
        with open(filename, 'wb') as f:
            f.write(response.body)