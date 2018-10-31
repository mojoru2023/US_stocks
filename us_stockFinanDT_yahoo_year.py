# -*- coding:utf-8 -*-
import datetime
import re
import time

import pymysql
import requests
from requests.exceptions import RequestException

from lxml import etree



def call_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre'
    }
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


# 可以尝试第二种解析方式，更加容易做计算
def parse_stock_note(html):
    big_list = []
    last_list = []
    selector = etree.HTML(html)
    name = selector.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1/text()')
    d1 = selector.xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[3]/table/tbody/tr[26]/td[2]/span/text()')
    d2 = selector.xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[3]/table/tbody/tr[26]/td[3]/span/text()')
    d3 = selector.xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[3]/table/tbody/tr[26]/td[4]/span/text()')
    d4 = selector.xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[3]/table/tbody/tr[26]/td[5]/span/text()')
    d_sp = d1 + d2 + d3 + d4
    for item in d_sp:
        i_sp = "".join(item.split(','))
        last_list.append(i_sp)
    all_content = name + last_list
    all_content_tuple = tuple(all_content)
    big_list.append(all_content_tuple)
    return big_list









def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='us_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    for i in range(1,5967):
        sql = 'select code from us_stock where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        num = data['code']
        url = 'https://finance.yahoo.com/quote/' + str(num) + '/financials?p=' + str(num)
        yield url



def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='us_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into us_FinData_yahoo_year (name,d1,d2,d3,d4) values (%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass






#
if __name__ == '__main__':
    for url_str in Python_sel_Mysql():
        html = call_page(url_str)
        content = parse_stock_note(html)
        insertDB(content)
        print(datetime.datetime.now())




#
# create table us_FinData_yahoo_year(
# id int not null primary key auto_increment,
# name varchar(120),
# d1 varchar(20),
# d2 varchar(20),
# d3 varchar(20),
# d4 varchar(20)
#  ) engine=InnoDB default charset=utf8;
# #
#
# drop table us_FinData_yahoo_year;


