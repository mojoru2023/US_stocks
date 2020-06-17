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
        cursor.executemany('insert into SP500_FinData_sina (name,d1,d2,d3,d4,d5) values (%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass






#
if __name__ == '__main__':
    sp500 = 'MSFT,AAPL,AMZN,FB,GOOGL,GOOG,JNJ,BRK.B,V,JPM,PG,UNH,MA,HD,INTC,VZ,NVDA,T,DIS,BAC,XOM,ADBE,CSCO,MRK,NFLX,PYPL,PFE,PEP,CMCSA,KO,CVX,WMT,ABBV,CRM,ABT,MCD,TMO,COST,AMGN,BMY,ACN,MDT,NKE,NEE,AVGO,LLY,UNP,AMT,TXN,C,ORCL,PM,LIN,WFC,DHR,IBM,HON,BA,QCOM,RTX,LOW,GILD,LMT,SBUX,MMM,FIS,BLK,CHTR,CVS,SPGI,MO,UPS,NOW,MDLZ,INTU,CI,AXP,PLD,CCI,D,BKNG,BDX,VRTX,CAT,ANTM,ISRG,GS,AMD,TJX,ADP,ZTS,DUK,GE,CME,CL,EQIX,SYK,TGT,REGN,SO,CB,FISV,ATVI,MS,USB,MU,CSX,GPN,MMC,TFC,AMAT,APD,ICE,ILMN,ADSK,BIIB,HUM,ECL,BSX,PNC,NOC,DE,ITW,DG,KMB,COP,SHW,NEM,PGR,NSC,MCO,ADI,AON,EW,BAX,EL,LRCX,SCHW,LHX,ROP,WM,AEP,TMUS,DD,EMR,EXC,EA,GIS,DLR,EBAY,DXCM,CNC,GD,ETN,SRE,GM,SBAC,PSX,XEL,COF,ROST,BK,FDX,ALL,ORLY,DOW,WBA,KMI,EOG,CTSH,MET,PSA,TRV,KLAC,STZ,TROW,AIG,APH,WEC,INFO,SYY,YUM,SNPS,HCA,MSCI,ES,JCI,AFL,VRSK,A,SLB,TEL,AZO,IDXX,TWTR,MNST,CMG,ZBH,CLX,VLO,PRU,CMI,KR,CDNS,PCAR,F,IQV,ED,PEG,HPQ,MAR,MPC,MCK,ALXN,PPG,WLTW,ROK,MCHP,PAYX,PH,MSI,ANSS,OTIS,RMD,AWK,FAST,WMB,SPG,TDG,XLNX,STT,WELL,AVB,BLL,FLT,CTAS,EQR,ADM,FE,HLT,TT,SWKS,O,CERN,EIX,VRSN,DLTR,GLW,MKC,VFC,PPL,SWK,DTE,EFX,ARE,CTVA,AME,KHC,ETR,FTNT,HSY,APTV,LUV,AMP,FTV,MKTX,MTD,DHI,ALGN,TSN,KEYS,BBY,FRC,CHD,CARR,LEN,CPRT,NTRS,AEE,AJG,DAL,LYB,RSG,DFS,OXY,LVS,TFX,CMS,AMCR,LH,INCY,CTXS,CDW,WY,K,AKAM,CAG,CBRE,ESS,PXD,MXIM,CAH,ODFL,WST,TTWO,KMX,FITB,FCX,PAYC,OKE,DGX,VMC,VTR,HIG,KSU,MTB,DPZ,ABC,TSCO,COO,DOV,ZBRA,HOLX,BR,PEAK,SYF,IP,BXP,IFF,EVRG,GRMN,NDAQ,MAA,MAS,VIAC,DRE,JKHY,GWW,HPE,KEY,LDOS,HRL,STE,ULTA,TIF,HES,QRVO,FMC,NUE,EXR,EXPD,WDC,GPC,MLM,ANET,OMC,WAT,ATO,SJM,BF.B,LNT,RF,STX,EXPE,CFG,XYL,NLOK,HAL,IEX,CXO,UDR,NVR,WAB,CBOE,SIVB,J,PFG,URI,ABMD,ETFC,PKI,CE,IT,IR,VAR,BKR,CHRW,HBAN,RCL,FOXA,MGM,JBHT,NTAP,XRAY,CTL,AVY,HAS,ALLE,LW,AAP,EMN,CINF,PKG,DRI,WU,CNP,PHM,RJF,HST,WYNN,RE,DISH,NI,PNW,L,FBHS,HSIC,AES,UAL,WRB,NRG,LKQ,FFIV,LNC,MYL,CPB,ALB,UHS,IRM,REG,JNPR,COG,WHR,TXT,FANG,GL,CCL,HII,SNA,WRK,TAP,PRGO,DVA,LYV,BWA,IPG,DISCK,AAL,AOS,AIZ,CF,VNO,PNR,FRT,BEN,ZION,RHI,ROL,MHK,AIV,CMA,IPGP,NWL,KIM,HWM,FLIR,PBCT,PWR,NLSN,MRO,APA,DVN,NBL,SEE,NOV,HFC,MOS,ALK,FOX,NWSA,LEG,NCLH,SLG,HBI,DXC,IVZ,TPR,HOG,PVH,RL,KSS,FLS,UNM,DISCA,LB,HRB,FTI,XRX,GPS,ADS,JWN,UAA,UA,NWS,COTY'

    f_sp500 = sp500.split(",")
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)

    for url_code in f_sp500:

        url_f = 'http://quotes.sina.com.cn/usstock/hq/income.php?s=' + str(url_code) +'&t=quarter'


        html = get_first_page(url_f)
        content = parse_stock_note(html)
        print(content)
        insertDB(content)
        print(datetime.datetime.now())
        time.sleep(30)



#
# create table SP500_FinData_sina(
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