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
    for item in Price:
        big_list.append(item)




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

        f_120 = "%s," *120
        cursor.executemany('insert into ZGG_ ({0}) values ({1})'.format(zgg120,f_120[:-1]), content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass



if __name__ == '__main__':
    big_list = []
    zgg120 = 'BABA,TSM,PDD,JD,CHL,BEKE,LFC,NIO,PTR,NTES,SNP,CEO,BIDU,TAL,LU,XPEV,EDU,CHT,LI,ZTO,TME,BGNE,CHA,YUMC,TCOM,FTNT,CHU,IQ,BILI,GSX,GDS,VIPS,HTHT,UMC,ATHM,ASX,WB,ZNH,ZLAB,MLCO,KC,YY,OCFT,CEA,DADA,HNP,FUTU,MNSO,CD,HUYA,ACH,JOBS,DOYU,FXI,CBPO,HCM,API,LEGN,SOGO,MOMO,BZUN,VNET,DAO,JKS,BNR,IMAB,SINA,NIU,CSIQ,EGO,SHI,NOAH,SONO,QFIN,KWEB,MSC,HLG,HKIB,LX,GHG,SY,YALA,SIMO,GSH,SVM,IH,BEST,BITA,NFH,CNR,GTH,OPRA,EBON,CANG,HMI,ASHR,TIGR,FANH,HIMX,BEDU,IMOS,SOHU,HOLI,CYD,ICLK,CBAT,ONE,QTT,NEW,COWN,FINV,EH,DQ,MGI,YI,DUO,CQQQ,COE,YIN,CAN'
    f_zgg120 =zgg120.split(",")
    for code in f_zgg120:

        url = "http://gu.qq.com/us{0}.OQ/gg".format(code)
        html = call_page(url)
        parse_html(html)
        print(big_list)
        print(url)
    ff_l = []
    f_tup = tuple(big_list)
    ff_l.append((f_tup))
    print(ff_l)
    insertDB(ff_l)






 # create table ZGG_(id int not null primary key auto_increment, BABA FLOAT,TSM FLOAT,PDD FLOAT,JD FLOAT,CHL FLOAT,BEKE FLOAT,LFC FLOAT,NIO FLOAT,PTR FLOAT,NTES FLOAT,SNP FLOAT,CEO FLOAT,BIDU FLOAT,TAL FLOAT,LU FLOAT,XPEV FLOAT,EDU FLOAT,CHT FLOAT,LI FLOAT,ZTO FLOAT,TME FLOAT,BGNE FLOAT,CHA FLOAT,YUMC FLOAT,TCOM FLOAT,FTNT FLOAT,CHU FLOAT,IQ FLOAT,BILI FLOAT,GSX FLOAT,GDS FLOAT,VIPS FLOAT,HTHT FLOAT,UMC FLOAT,ATHM FLOAT,ASX FLOAT,WB FLOAT,ZNH FLOAT,ZLAB FLOAT,MLCO FLOAT,KC FLOAT,YY FLOAT,OCFT FLOAT,CEA FLOAT,DADA FLOAT,HNP FLOAT,FUTU FLOAT,MNSO FLOAT,CD FLOAT,HUYA FLOAT,ACH FLOAT,JOBS FLOAT,DOYU FLOAT,FXI FLOAT,CBPO FLOAT,HCM FLOAT,API FLOAT,LEGN FLOAT,SOGO FLOAT,MOMO FLOAT,BZUN FLOAT,VNET FLOAT,DAO FLOAT,JKS FLOAT,BNR FLOAT,IMAB FLOAT,SINA FLOAT,NIU FLOAT,CSIQ FLOAT,EGO FLOAT,SHI FLOAT,NOAH FLOAT,SONO FLOAT,QFIN FLOAT,KWEB FLOAT,MSC FLOAT,HLG FLOAT,HKIB FLOAT,LX FLOAT,GHG FLOAT,SY FLOAT,YALA FLOAT,SIMO FLOAT,GSH FLOAT,SVM FLOAT,IH FLOAT,BEST FLOAT,BITA FLOAT,NFH FLOAT,CNR FLOAT,GTH FLOAT,OPRA FLOAT,EBON FLOAT,CANG FLOAT,HMI FLOAT,ASHR FLOAT,TIGR FLOAT,FANH FLOAT,HIMX FLOAT,BEDU FLOAT,IMOS FLOAT,SOHU FLOAT,HOLI FLOAT,CYD FLOAT,ICLK FLOAT,CBAT FLOAT,ONE FLOAT,QTT FLOAT,NEW FLOAT,COWN FLOAT,FINV FLOAT,EH FLOAT,DQ FLOAT,MGI FLOAT,YI FLOAT,DUO FLOAT,CQQQ FLOAT,COE FLOAT,YIN FLOAT,CAN FLOAT, LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;


# drop table ZGG_;


# mei
#*/3 * * * * /home/w/pyenv/bin/python /home/w/SP500_Nasdap100/SP500.py