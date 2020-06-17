# -*- coding:utf-8 -*-
import datetime
import re
import time

import pymysql

from lxml import etree
from selenium import webdriver






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







def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='us_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into us_FinData_sina (name,d1,d2,d3,d4,d5) values (%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass






#
if __name__ == '__main__':
    nasdap100 = 'AAPL,MSFT,AMZN,GOOG,GOOGL,FB,INTC,CMCSA,PEP,CSCO,ADBE,NVDA,NFLX,TSLA,COST,PYPL,AMGN,AVGO,TXN,CHTR,SBUX,QCOM,GILD,MDLZ,TMUS,FISV,BKNG,INTU,ADP,ISRG,VRTX,MU,CSX,BIIB,AMAT,AMD,ATVI,EXC,MAR,LRCX,WBA,ADI,ROST,ADSK,REGN,ILMN,CTSH,XEL,JD,MNST,MELI,NXPI,BIDU,KHC,SIRI,PAYX,EA,LULU,EBAY,CTAS,WDAY,ORLY,VRSK,WLTW,CSGP,PCAR,KLAC,SPLK,NTES,MCHP,VRSN,ANSS,IDXX,CERN,ALXN,ASML,SNPS,FAST,DLTR,CPRT,XLNX,CDNS,ALGN,SGEN,WDC,UAL,SWKS,CDW,CHKP,ULTA,INCY,TCOM,BMRN,EXPE,MXIM,CTXS,TTWO,FOXA,AAL,NTAP,FOX,LBTYK,LBTYA'
    # f_nasdap100 = [x for x in nasdap100 if x != ","]
    f_nasdap100 = nasdap100.split(",")
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)

    for url_code in f_nasdap100:

        url_f = 'http://quotes.sina.com.cn/usstock/hq/income.php?s=' + str(url_code) +'&t=quarter'


        html = get_first_page(url_f)
        content = parse_stock_note(html)
        print(content)
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
# drop table us_FinData_sina;





# a= ['6亿','6万','8亿']
# t = []
# for i in a:
#     b = "".join(re.split(r'亿|万|\s',a))
#     t.append(b)
#
# print(t)  # t = [6,6,8]