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
# 可以尝试第二种解析方式，更加容易做计算
# 净收入 d1距离最近，d5最远
# 对于脚本的符合太大！所以季度和年度数据暂时不加入板块
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
    nasdap100 = 'AAPL,MSFT,AMZN,GOOG,GOOGL,FB,INTC,CMCSA,PEP,CSCO,ADBE,NVDA,NFLX,TSLA,COST,PYPL,AMGN,AVGO,TXN,CHTR,SBUX,QCOM,GILD,MDLZ,TMUS,FISV,BKNG,INTU,ADP,ISRG,VRTX,MU,CSX,BIIB,AMAT,AMD,ATVI,EXC,MAR,LRCX,WBA,ADI,ROST,ADSK,REGN,ILMN,CTSH,XEL,JD,MNST,MELI,NXPI,BIDU,KHC,SIRI,PAYX,EA,LULU,EBAY,CTAS,WDAY,ORLY,VRSK,WLTW,CSGP,PCAR,KLAC,SPLK,NTES,MCHP,VRSN,ANSS,IDXX,CERN,ALXN,ASML,SNPS,FAST,DLTR,CPRT,XLNX,CDNS,ALGN,SGEN,WDC,UAL,SWKS,CDW,CHKP,ULTA,INCY,TCOM,BMRN,EXPE,MXIM,CTXS,TTWO,FOXA,AAL,NTAP,FOX,LBTYK,LBTYA'
    # f_nasdap100 = [x for x in nasdap100 if x != ","]
    f_nasdap100 = nasdap100.split(",")

    for url_code in f_nasdap100:
        url_f = 'https://finance.yahoo.com/quote/' + str(url_code) + '/financials?p=' + str(url_code)

        html = call_page(url_f)
        content = parse_stock_note(html)
        print(content)
        # insertDB(content)
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


