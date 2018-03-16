# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import time

class TuanchePipeline(object):
    '''
    插入mysql数据库
    '''

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='pydata',
                                    use_unicode=True, charset="utf8")
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):

        createDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        insert_sql = '''
               insert into signup(city,city_name,title,brand,brand_name,model,model_name,signup_count,tuangou_date,huodong_title,page_count,url,create_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
               '''

        self.cursor.execute(insert_sql, (
        item["city"], item['cityName'], item["title"], item["brand"], item['brandName'], item["model"], item['modelName'], item["signup_count"],
        item["date"], item["huodong"], item['page_count'], item["url"], createDate))
        self.conn.commit() # 我们需要提交数据库，否则数据还是不能上传的
        #self.conn.close()  # 关闭游标
        #self.connect.close()  # 关闭数据库
        return item
