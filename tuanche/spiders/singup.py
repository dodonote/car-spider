#! /usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from ..items import TuancheItem
import sys #要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方法
import json
import os

reload(sys)


# print sys.getdefaultencoding()

sys.setdefaultencoding('utf-8')



class SignupSpider(scrapy.Spider):

    def __init__(self):
        '''
        初始化变量
        '''
        self.next_num = 1

    name = "signup"
    allowed_domains = ['tuanche.com']
    start_urls = [
        "http://bj.tuanche.com/tuan/"
    ]

    def parse(self, response):

        self.log("===========================| %s |" % response.url)
        con = response.css("div.hotCarList-img").xpath('a')

        # 清空文件内容

        with open('tuan.json', "r+") as f:
            f.seek(0)
            f.truncate()  # 清空文件
            f.close
        # exit()

        # print con
        for row in con:

            url = row.xpath('@href').extract()[0]
            self.log("con_url is %s" % url)

            yield scrapy.Request(url, callback=self.parse_content)

        ##是否有下一页，有则继续
        next_pages = response.css('div.tc_page_con').xpath('a')
        # self.log("next_pages_content %s" % next_pages)

        # self.log("next_page_a %s" % next_pages.xpath('text()')[-1].extract())
        if next_pages.xpath('text()')[-1].extract() == u"下一页":

            self.log("next_num %s" % self.next_num)
            if self.next_num < 2:

                self.next_num +=1
                next_page = next_pages.xpath('@href')[-1].extract()
                self.log('next_page_url: %s' % next_page)

                yield scrapy.Request(next_page, callback=self.parse)

    def parse_content(self, response):
        '''
        内容页，获取具体信息数据
        :param response:
        :return:
        '''
        item = TuancheItem()
        title = response.xpath("/html/head/title/text()").extract()
        url = response.url
        huodong = response.xpath('//div[@class="tgT"]/h2/text()')[0].extract()
        date = response.xpath('//div[@class="tgT"]/h2/span/i/text()')[0].extract()
        city = response.xpath('//input[@name="cityId"]/@value')[0].extract()
        brand = response.xpath('//input[@name="brandId"]/@value')[0].extract()
        model = response.xpath('//input[@name="styleId"]/@value')[0].extract()
        signup_count = response.xpath('//dl[@class="TopinpLTips"]/dd/span/i/text()')[0].extract()
        item['title'] = title[0]
        item['url'] = url
        item['huodong'] = huodong
        item['date'] = date
        item['city'] = city
        item['brand'] = brand
        item['model'] = model
        item['signup_count'] = signup_count
        # print title,title[0],title[0][-5]
        # print item
        # print json.loads(item)
        # print json.dumps(item)
        # print response.url
        # print response.url.split("/")
        # print "-".join(item)
        # print title+" - "+url
        # print str(title)+str(url)
        # print ''+title+''+url+''
        # print str(title)
        # print str(title).encode("utf-8")
        # print item['title'].item['url']
        # print item['title']+item['url']
        filename = response.url.split("/")[-2]
        self.log("filename %s" % filename)
        # print filename
        with open(filename + ".json", 'ab') as f:
            jsontext = json.dumps(dict(item), ensure_ascii=False) + ",\n\n\r\r"
            f.write(jsontext.encode("utf-8"))