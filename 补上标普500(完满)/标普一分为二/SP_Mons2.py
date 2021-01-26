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
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='SPMons',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:

        f_505 = "%s," *220
        cursor.executemany('insert into sp_Mons2 ({0}) values ({1})'.format(sp500_forintoDB,f_505[:-1]), content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass



if __name__ == '__main__':
    s = datetime.datetime.now()
    big_list = []
    sp500_forSearch = 'LVS,TFX,CMS,AMCR,LH,INCY,CTXS,CDW,WY,K,AKAM,CAG,CBRE,ESS,PXD,MXIM,CAH,ODFL,WST,TTWO,KMX,FITB,FCX,PAYC,OKE,DGX,VMC,VTR,HIG,KSU,MTB,DPZ,ABC,TSCO,COO,DOV,ZBRA,HOLX,BR,PEAK,SYF,IP,BXP,IFF,EVRG,GRMN,NDAQ,MAA,MAS,VIAC,DRE,JKHY,GWW,HPE,KEY,LDOS,HRL,STE,ULTA,TIF,HES,QRVO,FMC,NUE,EXR,EXPD,WDC,GPC,MLM,ANET,OMC,WAT,ATO,SJM,BF.B,LNT,RF,STX,EXPE,CFG,XYL,NLOK,HAL,IEX,CXO,UDR,NVR,WAB,CBOE,SIVB,J,PFG,URI,ABMD,ETFC,PKI,CE,IT,IR,VAR,BKR,CHRW,HBAN,RCL,FOXA,MGM,JBHT,NTAP,XRAY,CTL,AVY,HAS,ALLE,LW,AAP,EMN,CINF,PKG,DRI,WU,CNP,PHM,RJF,HST,WYNN,RE,DISH,NI,PNW,L,FBHS,HSIC,AES,UAL,WRB,NRG,LKQ,FFIV,LNC,MYL,CPB,ALB,UHS,IRM,REG,JNPR,COG,WHR,TXT,FANG,GL,CCL,HII,SNA,WRK,TAP,PRGO,DVA,LYV,BWA,IPG,DISCK,AAL,AOS,AIZ,CF,VNO,PNR,FRT,BEN,ZION,RHI,ROL,MHK,AIV,CMA,IPGP,NWL,KIM,HWM,FLIR,PBCT,PWR,NLSN,MRO,APA,DVN,NBL,SEE,NOV,HFC,MOS,ALK,FOX,NWSA,LEG,NCLH,SLG,HBI,DXC,IVZ,TPR,HOG,PVH,RL,KSS,FLS,UNM,DISCA,LB,HRB,FTI,XRX,GPS,ADS,JWN,UAA,UA,NWS,COTY'
    sp500_forintoDB = 'LVS,TFX,CMS,AMCR,LH,INCY,CTXS,CDW,WY,K,AKAM,CAG,CBRE,ESS,PXD,MXIM,CAH,ODFL,WST,TTWO,KMX,FITB,FCX,PAYC,OKE,DGX,VMC,VTR,HIG,KSU,MTB,DPZ,ABC,TSCO,COO,DOV,ZBRA,HOLX,BR,PEAK,SYF,IP,BXP,IFF,EVRG,GRMN,NDAQ,MAA,MAS,VIAC,DRE,JKHY,GWW,HPE,_KEY,LDOS,HRL,STE,ULTA,TIF,HES,QRVO,FMC,NUE,EXR,EXPD,WDC,GPC,MLM,ANET,OMC,WAT,ATO,SJM,BF_B,LNT,RF,STX,EXPE,CFG,XYL,NLOK,HAL,IEX,CXO,UDR,NVR,WAB,CBOE,SIVB,J,PFG,URI,ABMD,ETFC,PKI,CE,IT,IR,VAR,BKR,CHRW,HBAN,RCL,FOXA,MGM,JBHT,NTAP,XRAY,CTL,AVY,HAS,ALLE,LW,AAP,EMN,CINF,PKG,DRI,WU,CNP,PHM,RJF,HST,WYNN,RE,DISH,NI,PNW,L,FBHS,HSIC,AES,UAL,WRB,NRG,LKQ,FFIV,LNC,MYL,CPB,ALB,UHS,IRM,REG,JNPR,COG,WHR,TXT,FANG,GL,CCL,HII,SNA,WRK,TAP,PRGO,DVA,LYV,BWA,IPG,DISCK,AAL,AOS,AIZ,CF,VNO,PNR,FRT,BEN,ZION,RHI,ROL,MHK,AIV,CMA,IPGP,NWL,KIM,HWM,FLIR,PBCT,PWR,NLSN,MRO,APA,DVN,NBL,SEE,NOV,HFC,MOS,ALK,FOX,NWSA,LEG,NCLH,SLG,HBI,DXC,IVZ,TPR,HOG,PVH,RL,KSS,FLS,UNM,DISCA,LB,HRB,FTI,XRX,GPS,ADS,JWN,UAA,UA,NWS,COTY'

    f_sp500_search =sp500_forSearch.split(",")
    for code in f_sp500_search:

        url = "http://gu.qq.com/us{0}.OQ/gg".format(code)
        html = call_page(url)
        parse_html(html)
        print(url)
        time.sleep(0.1)
    ff_l = []
    f_tup = tuple(big_list)
    ff_l.append((f_tup))
    print(ff_l)
    insertDB(ff_l)
    f = datetime.datetime.now()
    print(f-s)







#create table sp_Mons2(id int not null primary key auto_increment, LVS float,TFX float,CMS float,AMCR float,LH float,INCY float,CTXS float,CDW float,WY float,K float,AKAM float,CAG float,CBRE float,ESS float,PXD float,MXIM float,CAH float,ODFL float,WST float,TTWO float,KMX float,FITB float,FCX float,PAYC float,OKE float,DGX float,VMC float,VTR float,HIG float,KSU float,MTB float,DPZ float,ABC float,TSCO float,COO float,DOV float,ZBRA float,HOLX float,BR float,PEAK float,SYF float,IP float,BXP float,IFF float,EVRG float,GRMN float,NDAQ float,MAA float,MAS float,VIAC float,DRE float,JKHY float,GWW float,HPE float,_KEY float,LDOS float,HRL float,STE float,ULTA float,TIF float,HES float,QRVO float,FMC float,NUE float,EXR float,EXPD float,WDC float,GPC float,MLM float,ANET float,OMC float,WAT float,ATO float,SJM float,BF_B float,LNT float,RF float,STX float,EXPE float,CFG float,XYL float,NLOK float,HAL float,IEX float,CXO float,UDR float,NVR float,WAB float,CBOE float,SIVB float,J float,PFG float,URI float,ABMD float,ETFC float,PKI float,CE float,IT float,IR float,VAR float,BKR float,CHRW float,HBAN float,RCL float,FOXA float,MGM float,JBHT float,NTAP float,XRAY float,CTL float,AVY float,HAS float,ALLE float,LW float,AAP float,EMN float,CINF float,PKG float,DRI float,WU float,CNP float,PHM float,RJF float,HST float,WYNN float,RE float,DISH float,NI float,PNW float,L float,FBHS float,HSIC float,AES float,UAL float,WRB float,NRG float,LKQ float,FFIV float,LNC float,MYL float,CPB float,ALB float,UHS float,IRM float,REG float,JNPR float,COG float,WHR float,TXT float,FANG float,GL float,CCL float,HII float,SNA float,WRK float,TAP float,PRGO float,DVA float,LYV float,BWA float,IPG float,DISCK float,AAL float,AOS float,AIZ float,CF float,VNO float,PNR float,FRT float,BEN float,ZION float,RHI float,ROL float,MHK float,AIV float,CMA float,IPGP float,NWL float,KIM float,HWM float,FLIR float,PBCT float,PWR float,NLSN float,MRO float,APA float,DVN float,NBL float,SEE float,NOV float,HFC float,MOS float,ALK float,FOX float,NWSA float,LEG float,NCLH float,SLG float,HBI float,DXC float,IVZ float,TPR float,HOG float,PVH float,RL float,KSS float,FLS float,UNM float,DISCA float,LB float,HRB float,FTI float,XRX float,GPS float,ADS float,JWN float,UAA float,UA float,NWS float,COTY float,LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;


# drop table sp_Mons;


# mei
#*/3 * * * * /home/w/pyenv/bin/python /home/w/SP500_Nasdap100/SP500.py