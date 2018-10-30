
# -*- coding:utf8 -*-

# 写个小脚本就搞定了！
import re

import pymysql

import time
from requests.exceptions import ConnectionError
from selenium import webdriver
from lxml import etree
import datetime
driver = webdriver.Chrome()


#请求

def get_first_page():
    url = 'http://finance.sina.com.cn/stock/usstock/sector.shtml'
    # driver = webdriver.PhantomJS(service_args=SERVICE_ARGS)
    driver.set_window_size(1200, 1200)  # 设置窗口大小
    driver.get(url)
    # time.sleep(3)
    html = driver.page_source
    # time.sleep(3)
    return html




def next_page():
    for i in range(1,457):  # selenium 循环翻页成功！
        driver.find_element_by_xpath('//*[@id="pages"]/a[last()]').click()
        time.sleep(1)
        html = driver.page_source
        return html




# 用遍历打开网页59次来处理

    # print(html)  #正则还是有问题，选择了一个动态变动的颜色标记是不好的 最近浏览不是每次都有的！所以用数字的颜色取判断吧

def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！
    selector = etree.HTML(html)
    big_list = []
    name = selector.xpath('//*[@id="data"]/table/tbody/tr/td[1]/a/text()')
    code = selector.xpath('//*[@id="data"]/table/tbody/tr/td[2]/a/text()')
    industry = selector.xpath('//*[@id="data"]/table/tbody/tr/td[5]/a/text()')
    market_value = selector.xpath('//*[@id="data"]/table/tbody/tr/th[6]/text()')
    long_tuple = (i for i in zip(name, code,industry, market_value))
    for i in long_tuple:
        big_list.append(i)
    return big_list



#存储到MySQL中

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='us_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into us_stock (name,code,industry,market_value) values (%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass

if __name__ == '__main__':
        html = get_first_page()
        content = parse_html(html)
        insertDB(content)
        while True:
            html = next_page()
            content = parse_html(html)
            insertDB(content)
            print(datetime.datetime.now())


# create table us_stock(
# id int not null primary key auto_increment,
# name varchar(88),
# code varchar(20) ,
# industry varchar(26),
# market_value varchar(20)
# ) engine=InnoDB  charset=utf8;