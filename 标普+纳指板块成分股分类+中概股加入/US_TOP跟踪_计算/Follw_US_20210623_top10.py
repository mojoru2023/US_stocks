#! -*- coding:utf-8 -*-


import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException

def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

# 正则和lxml混用
def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！



    selector = etree.HTML(html)
    Price = selector.xpath('//*[@id="spFP"]/div[1]/span[1]/text()')
    MV = selector.xpath('//*[@id="hqpanel"]/div[2]/div[3]/ul[2]/li[4]/span[2]/text()')
    for item in  MV:
        f_=item[:-1]
        mv_l.append(float(f_))


    for i1,i2 in zip(Price,MV):
        sum_mv = sum(mv_l)
        count_l.append(float(i1)*(float(i2[:-1])/float(sum_mv)))






def RemoveDot(item):
    f_l = []
    for it in item:

        f_str = "".join(it.split(","))
        f_l.append(f_str)

    return f_l




def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items






def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='us_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:

        f_10 = "%s," *10
        cursor.executemany('insert into us_top10_0623 ({0},top10_ave) values ({1},%s)'.format(US_top10_DB,f_10[:-1]), content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass



if __name__ == '__main__':
    big_list=[]
    mv_l = []
    count_l = []

    US_top10_WEB ='NVDA,BIIB,F,RMD,TWTR,ADBE,FTNT,INTU,IDXX,EW'

    US_top10_DB ='NVDA,BIIB,F,RMD,TWTR,ADBE,FTNT,INTU,IDXX,EW'



    f_ustop10 = US_top10_WEB.split(",")
    for code in f_ustop10:
        url = "http://gu.qq.com/us{0}.OQ/gg".format(code)
        html = call_page(url)
        selector = etree.HTML(html)
        Price = selector.xpath('//*[@id="spFP"]/div[1]/span[1]/text()')
        big_list.append(float(Price[0]))








    ff_l = []

    ff_laverage = sum(big_list)/len(big_list)

    big_list.append(ff_laverage)
    f_tup = tuple(big_list)
    ff_l.append((f_tup))
    print(ff_l)
    print(len(f_tup))
    insertDB(ff_l)






 # create table us_top10_0623(id int not null primary key auto_increment, NVDA FLOAT ,BIIB FLOAT ,F FLOAT ,RMD FLOAT ,TWTR FLOAT ,ADBE FLOAT ,FTNT FLOAT ,INTU FLOAT ,IDXX FLOAT ,EW FLOAT ,top10_ave FLOAT, LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;






# mei
#*/3 * * * * /home/w/pyenv/bin/python /home/w/SP500_Nasdap100/SP500.py