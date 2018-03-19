# -*- coding: utf-8 -*-


import numpy as np
import matplotlib
from matplotlib.ticker import FuncFormatter
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pymysql
import json
import sys #要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方法

import time
reload(sys)


# print sys.getdefaultencoding()

sys.setdefaultencoding('utf-8')

myfont = fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
# matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei'] #指定默认字体
# myfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simhei.ttf') #Windows系统，黑体
# #myfont = matplotlib.font_manager.FontProperties(fname='/home/Fonts/simhei.ttf') #Linux系统，黑体
# matplotlib.rcParams['axes.unicode_minus'] = False #坐标可显示‘—’号
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

# a = np.arange(0, 5, 0.01)
# plt.plot(a, 5*a)
# plt.axis([-1,5,-1,25]) #设置xy轴范围
# plt.xlabel(u'中文x坐标',fontproperties=myfont)
# plt.ylabel(u'英文y坐标',fontproperties=myfont)
# plt.show()


class TuanCheData(object):
    '''
    查看mysql数据库
    '''

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='pydata',
                                    use_unicode=True, charset="utf8")
        self.cursor = self.conn.cursor()

    def process_item(self):

        createDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = '''
               select * from signup where brand = %s
               '''

        self.cursor.execute(sql, 1)
        self.conn.commit() # 我们需要提交数据库，否则数据还是不能上传的
        #self.conn.close()  # 关闭游标
        #self.connect.close()  # 关闭数据库
        # return item

        # 获取查询结果
        result = self.cursor.fetchall()
        # print(result)

        for row in result:

            print row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[
                12],row[13]
            '''
          # fname = row[0]
          # lname = row[1]
          # age = row[2]
          # sex = row[3]
          # income = row[4]
          # # 打印结果
          # print "fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
          #    (fname, lname, age, sex, income )
            '''

    #统计一汽大众报名量
    def fawvwCount(self):
        sql = '''
                       SELECT *,COUNT(id) AS c,SUM(signup_count) AS zsum FROM signup WHERE brand = %s GROUP BY model order by zsum desc limit 6
                       '''

        self.cursor.execute(sql, 1)
        # 获取查询结果
        results = self.cursor.fetchall()
        self.conn.commit()  # 我们需要提交数据库，否则数据还是不能上传的
        # for result in results:
        #    print(str(result) + '\n')
        # print result
        # print json.loads(result)
        # print json.dumps(result)
        return results

    #每天报名总数
    def daySignup(self):
        sql = '''
                               SELECT FROM_UNIXTIME(UNIX_TIMESTAMP(create_time),"%Y-%m-%d") AS d,SUM(signup_count) AS c FROM signup GROUP BY d 
                               '''

        self.cursor.execute(sql)
        # 获取查询结果
        results = self.cursor.fetchall()
        self.conn.commit()  # 我们需要提交数据库，否则数据还是不能上传的
        # for result in results:
        #    print(str(result) + '\n')
        # print result
        # print json.loads(result)
        # print json.dumps(result)
        return results

    # 品牌对比
    def brandContrast(self,brandId):
        sql = 'SELECT brand,brand_name,FROM_UNIXTIME(UNIX_TIMESTAMP(create_time),"%Y-%m-%d") AS d,FROM_UNIXTIME(UNIX_TIMESTAMP(create_time),"%m-%d") AS md,SUM(signup_count) AS c FROM signup WHERE brand = '+str(brandId)+' GROUP BY d limit 5'

        #
        # print sql
        # print brandId
        self.cursor.execute(sql)
        # 获取查询结果
        results = self.cursor.fetchall()
        self.conn.commit()  # 我们需要提交数据库，否则数据还是不能上传的
        # for result in results:
        #    print(str(result) + '\n')
        # print result
        # print json.loads(result)
        # print json.dumps(result)
        return results

    #饼状图
    def matChart(self, results):

        # # The slices will be ordered and plotted counter-clockwise.
        # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        #
        # print type(labels)

        list = []
        sizes = []
        for row in results:
            list.append(row[5]+" - "+row[7])
            sizes.append(row[15])

        # print list
        # print type(list)
        labels = tuple(list)
        # print str(labels).decode('string_escape')

        # exit()
        # sizes =[15, 30, 45, 10]
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        explode = (0.1, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        # Set aspect ratio to be equal so that pie is drawn as a circle.
        plt.axis('equal')

        plt.xlabel(u"横轴", fontproperties=myfont)
        plt.ylabel(u"纵轴", fontproperties=myfont)
        plt.title("pythoner.com", fontproperties=myfont)
        # print(matplotlib.matplotlib_fname())

        plt.show()

    #报名趋势图
    def signupTrend(self, results):

        # x = [0, 1, 2, 4, 5, 6]
        # y = [1, 2, 3, 2, 4, 1]

        x = []
        y = []
        for row in results:
            x.append(row[0])
            y.append(row [1])

        plt.plot(x, y, '-*r')  # 虚线, 星点, 红色
        plt.xlabel(u"时间")
        plt.ylabel(u"报名量")
        plt.show()

    #折线图对比
    def  signupContrast(self,results,results2,results3):

        # x1 = [1, 2, 3, 4, 5]  # Make x, y arrays for each graph
        # y1 = [1, 4, 9, 16, 25]
        # x2 = [1, 2, 4, 6, 8]
        # y2 = [2, 4, 8, 12, 16]

        x1 = []
        y1 = []
        x2 = []
        y2 = []
        x3 = []
        y3 = []
        for row in results:
            x1.append(row[3])
            y1.append(row[4])

        for row in results2:
            x2.append(row[3])
            y2.append(row[4])

        for row in results3:
            x3.append(row[3])
            y3.append(row[4])

        # print x1
        # print y1
        # print x2
        # print y2

        plt.plot(x1, y1, 'r')  # use pylab to plot x and y
        plt.plot(x2, y2, 'g')
        plt.plot(x3, y3, 'b')

        plt.title('Plot of y vs.x')  # give plot a title
        plt.xlabel('x axis')  # make axis labels
        plt.ylabel('y axis')

        # plt.xlim(0.0, 9.0)  # set axis limits
        # plt.ylim(0.0, 30.)

        plt.show()  # show the plot on the screen

    #柱状图
    def dayCountBarGraph(self,results):

        x = [0, 6, 22, 6, 9, 10]
        # y = [12, 2, 312, 212, 4, 11]
        z = [1, 2, 3, 4, 5]


        print x
        # print y
        print z

        # x = []
        y = []
        # # z = []
        # for row in results:
        #     x.append(row[4])
        #
        for row in results:
            y.append(row[4])

        # for row in results3:
        #     z.append(row[4])

        print x
        print y
        # print z

        plt.bar(x, y)
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.show()

    #柱状图名字
    def barGraph(self,result):

        x = np.arange(len(result))
        print x
        # money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]


        money = []
        line = []
        for row in result:
            line.append(row[0])
            money.append(row [1])

        line = tuple(line)

        print money
        print line

        # def millions(x, pos):
        #     'The two args are the value and tick position'
        #     return '$%1.1fM' % (x * 1e-6)
        #
        # formatter = FuncFormatter(millions)
        #
        # fig, ax = plt.subplots()
        # ax.yaxis.set_major_formatter(formatter)
        plt.bar(x, money)
        plt.xticks(x, line)
        plt.show()




run = TuanCheData()
# result = run.fawvwCount()
# run.matChart(result)

#每日报名
# result = run.daySignup()
# run.signupTrend(result)

#折线图对比
result = run.brandContrast(1)
result2 = run.brandContrast(2)
result3 = run.brandContrast(3)
# run.signupContrast(result,result2,result3)

#柱状图
# run.dayCountBarGraph(result)

result = run.daySignup()
run.barGraph(result)