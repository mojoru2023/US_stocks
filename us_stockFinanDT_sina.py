# -*- coding:utf-8 -*-
import datetime
import re
import time

import pymysql

from lxml import etree
from selenium import webdriver

driver = webdriver.Chrome()


def get_first_page(url):

    driver.get(url)
    html = driver.page_source
    return html



# 可以尝试第二种解析方式，更加容易做计算
def parse_stock_note(html):
    big_list = []
    last_list = []
    selector = etree.HTML(html)
    name = selector.xpath('/html/body/div[2]/div[5]/h3/text()')
    profits= selector.xpath('/html/body/div[2]/div[7]/div[2]/table[2]/tbody/tr[15]/td/text()')
    contents = name + profits
    big_tuple_list = list(contents)
    for i in big_tuple_list:
        b = "".join(re.split(r'亿|万|\s',i))  #同时去除了空格，亿，万３个标签
        big_list.append(b)
    big_list_tuple = tuple(big_list)
    last_list.append(big_list_tuple)
    return last_list







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
        url = 'http://quotes.sina.com.cn/usstock/hq/income.php?s=' + str(num) +'&t=quarter'
        yield url



def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='us_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into us_FinData (name,d1,d2,d3,d4,d5) values (%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass






#
if __name__ == '__main__':
    for url_str in Python_sel_Mysql():
        html = get_first_page(url_str)
        content = parse_stock_note(html)
        insertDB(content)
        print(datetime.datetime.now())
        time.sleep(1)



#
# create table us_FinData_sina(
# id int not null primary key auto_increment,
# name varchar(80),
# d1 varchar(10),
# d2 varchar(10),
# d3 varchar(10),
# d4 varchar(10),
# d5 varchar(10)
#  ) engine=InnoDB default charset=utf8;
#
#
# drop table us_FinData;





# a= ['6亿','6万','8亿']
# t = []
# for i in a:
#     b = "".join(re.split(r'亿|万|\s',a))
#     t.append(b)
#
# print(t)  # t = [6,6,8]