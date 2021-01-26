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

        f_505 = "%s," *285
        cursor.executemany('insert into sp_Mons1 ({0}) values ({1})'.format(sp500_forintoDB,f_505[:-1]), content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass



if __name__ == '__main__':
    s = datetime.datetime.now()
    big_list = []
    sp500_forSearch = 'MSFT,AAPL,AMZN,FB,GOOGL,GOOG,JNJ,BRK.B,V,JPM,PG,UNH,MA,HD,INTC,VZ,NVDA,T,DIS,BAC,XOM,ADBE,CSCO,MRK,NFLX,PYPL,PFE,PEP,CMCSA,KO,CVX,WMT,ABBV,CRM,ABT,MCD,TMO,COST,AMGN,BMY,ACN,MDT,NKE,NEE,AVGO,LLY,UNP,AMT,TXN,C,ORCL,PM,LIN,WFC,DHR,IBM,HON,BA,QCOM,RTX,LOW,GILD,LMT,SBUX,MMM,FIS,BLK,CHTR,CVS,SPGI,MO,UPS,NOW,MDLZ,INTU,CI,AXP,PLD,CCI,D,BKNG,BDX,VRTX,CAT,ANTM,ISRG,GS,AMD,TJX,ADP,ZTS,DUK,GE,CME,CL,EQIX,SYK,TGT,REGN,SO,CB,FISV,ATVI,MS,USB,MU,CSX,GPN,MMC,TFC,AMAT,APD,ICE,ILMN,ADSK,BIIB,HUM,ECL,BSX,PNC,NOC,DE,ITW,DG,KMB,COP,SHW,NEM,PGR,NSC,MCO,ADI,AON,EW,BAX,EL,LRCX,SCHW,LHX,ROP,WM,AEP,TMUS,DD,EMR,EXC,EA,GIS,DLR,EBAY,DXCM,CNC,GD,ETN,SRE,GM,SBAC,PSX,XEL,COF,ROST,BK,FDX,ALL,ORLY,DOW,WBA,KMI,EOG,CTSH,MET,PSA,TRV,KLAC,STZ,TROW,AIG,APH,WEC,INFO,SYY,YUM,SNPS,HCA,MSCI,ES,JCI,AFL,VRSK,A,SLB,TEL,AZO,IDXX,TWTR,MNST,CMG,ZBH,CLX,VLO,PRU,CMI,KR,CDNS,PCAR,F,IQV,ED,PEG,HPQ,MAR,MPC,MCK,ALXN,PPG,WLTW,ROK,MCHP,PAYX,PH,MSI,ANSS,OTIS,RMD,AWK,FAST,WMB,SPG,TDG,XLNX,STT,WELL,AVB,BLL,FLT,CTAS,EQR,ADM,FE,HLT,TT,SWKS,O,CERN,EIX,VRSN,DLTR,GLW,MKC,VFC,PPL,SWK,DTE,EFX,ARE,CTVA,AME,KHC,ETR,FTNT,HSY,APTV,LUV,AMP,FTV,MKTX,MTD,DHI,ALGN,TSN,KEYS,BBY,FRC,CHD,CARR,LEN,CPRT,NTRS,AEE,AJG,DAL,LYB,RSG,DFS,OXY'
    sp500_forintoDB = 'MSFT,AAPL,AMZN,FB,GOOGL,GOOG,JNJ,BRK_B,V,JPM,PG,UNH,MA,HD,INTC,VZ,NVDA,T,DIS,BAC,XOM,ADBE,CSCO,MRK,NFLX,PYPL,PFE,PEP,CMCSA,KO,CVX,WMT,ABBV,CRM,ABT,MCD,TMO,COST,AMGN,BMY,ACN,MDT,NKE,NEE,AVGO,LLY,UNP,AMT,TXN,C,ORCL,PM,LIN,WFC,DHR,IBM,HON,BA,QCOM,RTX,LOW,GILD,LMT,SBUX,MMM,FIS,BLK,CHTR,CVS,SPGI,MO,UPS,NOW,MDLZ,INTU,CI,AXP,PLD,CCI,D,BKNG,BDX,VRTX,CAT,ANTM,ISRG,GS,AMD,TJX,ADP,ZTS,DUK,GE,CME,CL,EQIX,SYK,TGT,REGN,SO,CB,FISV,ATVI,MS,USB,MU,CSX,GPN,MMC,TFC,AMAT,APD,ICE,ILMN,ADSK,BIIB,HUM,ECL,BSX,PNC,NOC,DE,ITW,DG,KMB,COP,SHW,NEM,PGR,NSC,MCO,ADI,AON,EW,BAX,EL,LRCX,SCHW,LHX,ROP,WM,AEP,TMUS,DD,EMR,EXC,EA,GIS,DLR,EBAY,DXCM,CNC,GD,ETN,SRE,GM,SBAC,PSX,XEL,COF,ROST,BK,FDX,_ALL,ORLY,DOW,WBA,KMI,EOG,CTSH,MET,PSA,TRV,KLAC,STZ,TROW,AIG,APH,WEC,INFO,SYY,YUM,SNPS,HCA,MSCI,ES,JCI,AFL,VRSK,A,SLB,TEL,AZO,IDXX,TWTR,MNST,CMG,ZBH,CLX,VLO,PRU,CMI,KR,CDNS,PCAR,F,IQV,ED,PEG,HPQ,MAR,MPC,MCK,ALXN,PPG,WLTW,ROK,MCHP,PAYX,PH,MSI,ANSS,OTIS,RMD,AWK,FAST,WMB,SPG,TDG,XLNX,STT,WELL,AVB,BLL,FLT,CTAS,EQR,ADM,FE,HLT,TT,SWKS,O,CERN,EIX,VRSN,DLTR,GLW,MKC,VFC,PPL,SWK,DTE,EFX,ARE,CTVA,AME,KHC,ETR,FTNT,HSY,APTV,LUV,AMP,FTV,MKTX,MTD,DHI,ALGN,TSN,_KEYS,BBY,FRC,CHD,CARR,LEN,CPRT,NTRS,AEE,AJG,DAL,LYB,RSG,DFS,OXY'
    f_sp500_search = sp500_forSearch.split(",")
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







 #create table sp_Mons1(id int not null primary key auto_increment,MSFT float,AAPL float,AMZN float,FB float,GOOGL float,GOOG float,JNJ float,BRK_B float,V float,JPM float,PG float,UNH float,MA float,HD float,INTC float,VZ float,NVDA float,T float,DIS float,BAC float,XOM float,ADBE float,CSCO float,MRK float,NFLX float,PYPL float,PFE float,PEP float,CMCSA float,KO float,CVX float,WMT float,ABBV float,CRM float,ABT float,MCD float,TMO float,COST float,AMGN float,BMY float,ACN float,MDT float,NKE float,NEE float,AVGO float,LLY float,UNP float,AMT float,TXN float,C float,ORCL float,PM float,LIN float,WFC float,DHR float,IBM float,HON float,BA float,QCOM float,RTX float,LOW float,GILD float,LMT float,SBUX float,MMM float,FIS float,BLK float,CHTR float,CVS float,SPGI float,MO float,UPS float,NOW float,MDLZ float,INTU float,CI float,AXP float,PLD float,CCI float,D float,BKNG float,BDX float,VRTX float,CAT float,ANTM float,ISRG float,GS float,AMD float,TJX float,ADP float,ZTS float,DUK float,GE float,CME float,CL float,EQIX float,SYK float,TGT float,REGN float,SO float,CB float,FISV float,ATVI float,MS float,USB float,MU float,CSX float,GPN float,MMC float,TFC float,AMAT float,APD float,ICE float,ILMN float,ADSK float,BIIB float,HUM float,ECL float,BSX float,PNC float,NOC float,DE float,ITW float,DG float,KMB float,COP float,SHW float,NEM float,PGR float,NSC float,MCO float,ADI float,AON float,EW float,BAX float,EL float,LRCX float,SCHW float,LHX float,ROP float,WM float,AEP float,TMUS float,DD float,EMR float,EXC float,EA float,GIS float,DLR float,EBAY float,DXCM float,CNC float,GD float,ETN float,SRE float,GM float,SBAC float,PSX float,XEL float,COF float,ROST float,BK float,FDX float,_ALL float,ORLY float,DOW float,WBA float,KMI float,EOG float,CTSH float,MET float,PSA float,TRV float,KLAC float,STZ float,TROW float,AIG float,APH float,WEC float,INFO float,SYY float,YUM float,SNPS float,HCA float,MSCI float,ES float,JCI float,AFL float,VRSK float,A float,SLB float,TEL float,AZO float,IDXX float,TWTR float,MNST float,CMG float,ZBH float,CLX float,VLO float,PRU float,CMI float,KR float,CDNS float,PCAR float,F float,IQV float,ED float,PEG float,HPQ float,MAR float,MPC float,MCK float,ALXN float,PPG float,WLTW float,ROK float,MCHP float,PAYX float,PH float,MSI float,ANSS float,OTIS float,RMD float,AWK float,FAST float,WMB float,SPG float,TDG float,XLNX float,STT float,WELL float,AVB float,BLL float,FLT float,CTAS float,EQR float,ADM float,FE float,HLT float,TT float,SWKS float,O float,CERN float,EIX float,VRSN float,DLTR float,GLW float,MKC float,VFC float,PPL float,SWK float,DTE float,EFX float,ARE float,CTVA float,AME float,KHC float,ETR float,FTNT float,HSY float,APTV float,LUV float,AMP float,FTV float,MKTX float,MTD float,DHI float,ALGN float,TSN float,_KEYS float,BBY float,FRC float,CHD float,CARR float,LEN float,CPRT float,NTRS float,AEE float,AJG float,DAL float,LYB float,RSG float,DFS float,OXY float,LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;


# drop table sp_Mons;


# mei
#*/3 * * * * /home/w/pyenv/bin/python /home/w/SP500_Nasdap100/SP500.py