



import datetime
import time

import pymysql
import requests
from lxml import etree
import json
from queue import Queue
import threading
from requests.exceptions import RequestException



def run_forever(func):
    def wrapper(obj):
        while True:
            func(obj)
    return wrapper


def RemoveDot(item):
    f_l = []
    for it in item:

        f_str = "".join(it.split(","))
        ff_str = f_str +"00"
        f_l.append(ff_str)

    return f_l

def remove_douhao(num):
    num1 = "".join(num.split(","))
    f_num = str(num1)
    return f_num
def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items
def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


class Sp_plus_Nas_StockPool(object):

    def __init__(self,url):
        self.url = url

    def page_request(self):
        ''' 发送请求获取数据 '''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 4.2.1; M040 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Mobile Safari/537.36'
        }

        response = requests.get(self.url,headers=headers)
        if response.status_code == 200:
            html = response.text
            return html
        else:
            pass

    def page_parse_(self):
        '''根据页面内容使用lxml解析数据, 获取段子列表'''


        html  = self.page_request()
        element = etree.HTML(html)
        now_price = element.xpath(
            '//*[@id="spFP"]/div[1]/span[1]/text()')
        f_price = RemoveDot(remove_block(now_price))
        big_list.append(float(f_price[0]))
        print(f_price[0])
        return big_list



def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='ForLynne',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        f_ls = "%s," * 525
        print(len(f_ls[:-1].split(",")))
        cursor.executemany('insert into following_sp500_plus_nas100_20220412 ({0}) values ({1})'.format(sp500_plus_nas100_forDB,f_ls[:-1]),content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError:
        pass



def compare_(base_dt_list):
    print(len(base_dt_list[2:]))
    print(len(big_list[2:]))
    sp500_ = (float(big_list[0]) - float(base_dt_list[0])) / float(base_dt_list[0])
    nas100_ = (float(big_list[1]) - float(base_dt_list[1])) / float(base_dt_list[1])
    f_compare_content.append(str(round(sp500_, 5)))
    f_compare_content.append(str(round(nas100_, 5)))

    for i1, i2 in zip(big_list[2:], base_dt_list[2:]):
        if (((float(i1) - float(i2)) / float(i2)) - Alpha_dt) > max(float(f_compare_content[0]), float(f_compare_content[1])):
            print((float(i1) - float(i2)) / float(i2) - Alpha_dt)
            print(max(sp500_, nas100_))

            f_compare_content.append(round(((float(i1) - float(i2)) / float(i2)), 5))
        else:
            print(round(((float(i1) - float(i2)) / float(i2))))
            f_compare_content.append("")



if __name__ == "__main__":
    sp500_plus_nas100_forSearch = "INX,IXIC,AAPL,A,AAL,AAP,ABBV,ABC,ABMD,ABT,ACN,ADBE,ADI,ADM,ADP,ADS,ADSK,AEE,AEP,AES,AFL,AIG,AIV,AIZ,AJG,AKAM,ALB,ALGN,ALK,ALL,ALLE,ALXN,AMAT,AMCR,AMD,AME,AMGN,AMP,AMT,AMZN,ANET,ANSS,ANTM,AON,AOS,APA,APD,APH,APTV,ARE,ASML,ATO,ATVI,AVB,AVGO,AVY,AWK,AXP,AZO,BA,BAC,BAX,BBY,BDX,BEN,BF.B,BIDU,BIIB,BK,BKNG,BKR,BLK,BLL,BMRN,BMY,BR,BRK.B,BSX,BWA,BXP,C,CAG,CAH,CARR,CAT,CB,CBOE,CBRE,CCI,CCL,CDNS,CDW,CE,CERN,CF,CFG,CHD,CHKP,CHRW,CHTR,CI,CINF,CL,CLX,CMA,CMCSA,CME,CMG,CMI,CMS,CNC,CNP,COF,COG,COO,COP,COST,COTY,CPB,CPRT,CRM,CSCO,CSGP,CSX,CTAS,CTL,CTSH,CTVA,CTXS,CVS,CVX,CXO,D,DAL,DD,DE,DFS,DG,DGX,DHI,DHR,DIS,DISCA,DISCK,DISH,DLR,DLTR,DOV,DOW,DPZ,DRE,DRI,DTE,DUK,DVA,DVN,DXC,DXCM,EA,EBAY,ECL,ED,EFX,EIX,EL,EMN,EMR,EOG,EQIX,EQR,ES,ESS,ETFC,ETN,ETR,EVRG,EW,EXC,EXPD,EXPE,EXR,F,FANG,FAST,FB,FBHS,FCX,FDX,FE,FFIV,FIS,FISV,FITB,FLIR,FLS,FLT,FMC,FOX,FOXA,FRC,FRT,FTI,FTNT,FTV,GD,GE,GILD,GIS,GL,GLW,GM,GOOG,GOOGL,GPC,GPN,GPS,GRMN,GS,GWW,HAL,HAS,HBAN,HBI,HCA,HD,HES,HFC,HIG,HII,HLT,HOG,HOLX,HON,HPE,HPQ,HRB,HRL,HSIC,HST,HSY,HUM,HWM,IBM,ICE,IDXX,IEX,IFF,ILMN,INCY,INFO,INTC,INTU,IP,IPG,IPGP,IQV,IR,IRM,ISRG,IT,ITW,IVZ,J,JBHT,JCI,JD,JKHY,JNJ,JNPR,JPM,JWN,K,KEY,KEYS,KHC,KIM,KLAC,KMB,KMI,KMX,KO,KR,KSS,KSU,L,LB,LBTYA,LBTYK,LDOS,LEG,LEN,LH,LHX,LIN,LKQ,LLY,LMT,LNC,LNT,LOW,LRCX,LULU,LUV,LVS,LW,LYB,LYV,MA,MAA,MAR,MAS,MCD,MCHP,MCK,MCO,MDLZ,MDT,MELI,MET,MGM,MHK,MKC,MKTX,MLM,MMC,MMM,MNST,MO,MOS,MPC,MRK,MRO,MS,MSCI,MSFT,MSI,MTB,MTD,MU,MXIM,MYL,NBL,NCLH,NDAQ,NEE,NEM,NFLX,NI,NKE,NLOK,NLSN,NOC,NOV,NOW,NRG,NSC,NTAP,NTES,NTRS,NUE,NVDA,NVR,NWL,NWS,NWSA,NXPI,O,ODFL,OKE,OMC,ORCL,ORLY,OTIS,OXY,PAYC,PAYX,PBCT,PCAR,PEAK,PEG,PEP,PFE,PFG,PG,PGR,PH,PHM,PKG,PKI,PLD,PM,PNC,PNR,PNW,PPG,PPL,PRGO,PRU,PSA,PSX,PVH,PWR,PXD,PYPL,QCOM,QRVO,RCL,RE,REG,REGN,RF,RHI,RJF,RL,RMD,ROK,ROL,ROP,ROST,RSG,RTX,SBAC,SBUX,SCHW,SEE,SGEN,SHW,SIRI,SIVB,SJM,SLB,SLG,SNA,SNPS,SO,SPG,SPGI,SPLK,SRE,STE,STT,STX,STZ,SWK,SWKS,SYF,SYK,SYY,T,TAP,TCOM,TDG,TEL,TFC,TFX,TGT,TIF,TJX,TMO,TMUS,TPR,TROW,TRV,TSCO,TSLA,TSN,TT,TTWO,TWTR,TXN,TXT,UA,UAA,UAL,UDR,UHS,ULTA,UNH,UNM,UNP,UPS,URI,USB,V,VAR,VFC,VIAC,VLO,VMC,VNO,VRSK,VRSN,VRTX,VTR,VZ,WAB,WAT,WBA,WDAY,WDC,WEC,WELL,WFC,WHR,WLTW,WM,WMB,WMT,WRB,WRK,WST,WU,WY,WYNN,XEL,XLNX,XOM,XRAY,XRX,XYL,YUM,ZBH,ZBRA,ZION,ZTS"
    sp500_plus_nas100_forNetProfits = "AAPL,A,AAL,AAP,ABBV,ABC,ABMD,ABT,ACN,ADBE,ADI,ADM,ADP,ADS,ADSK,AEE,AEP,AES,AFL,AIG,AIV,AIZ,AJG,AKAM,ALB,ALGN,ALK,ALL,ALLE,ALXN,AMAT,AMCR,AMD,AME,AMGN,AMP,AMT,AMZN,ANET,ANSS,ANTM,AON,AOS,APA,APD,APH,APTV,ARE,ASML,ATO,ATVI,AVB,AVGO,AVY,AWK,AXP,AZO,BA,BAC,BAX,BBY,BDX,BEN,BF.B,BIDU,BIIB,BK,BKNG,BKR,BLK,BLL,BMRN,BMY,BR,BRK.B,BSX,BWA,BXP,C,CAG,CAH,CARR,CAT,CB,CBOE,CBRE,CCI,CCL,CDNS,CDW,CE,CERN,CF,CFG,CHD,CHKP,CHRW,CHTR,CI,CINF,CL,CLX,CMA,CMCSA,CME,CMG,CMI,CMS,CNC,CNP,COF,COG,COO,COP,COST,COTY,CPB,CPRT,CRM,CSCO,CSGP,CSX,CTAS,CTL,CTSH,CTVA,CTXS,CVS,CVX,CXO,D,DAL,DD,DE,DFS,DG,DGX,DHI,DHR,DIS,DISCA,DISCK,DISH,DLR,DLTR,DOV,DOW,DPZ,DRE,DRI,DTE,DUK,DVA,DVN,DXC,DXCM,EA,EBAY,ECL,ED,EFX,EIX,EL,EMN,EMR,EOG,EQIX,EQR,ES,ESS,ETFC,ETN,ETR,EVRG,EW,EXC,EXPD,EXPE,EXR,F,FANG,FAST,FB,FBHS,FCX,FDX,FE,FFIV,FIS,FISV,FITB,FLIR,FLS,FLT,FMC,FOX,FOXA,FRC,FRT,FTI,FTNT,FTV,GD,GE,GILD,GIS,GL,GLW,GM,GOOG,GOOGL,GPC,GPN,GPS,GRMN,GS,GWW,HAL,HAS,HBAN,HBI,HCA,HD,HES,HFC,HIG,HII,HLT,HOG,HOLX,HON,HPE,HPQ,HRB,HRL,HSIC,HST,HSY,HUM,HWM,IBM,ICE,IDXX,IEX,IFF,ILMN,INCY,INFO,INTC,INTU,IP,IPG,IPGP,IQV,IR,IRM,ISRG,IT,ITW,IVZ,J,JBHT,JCI,JD,JKHY,JNJ,JNPR,JPM,JWN,K,KEY,KEYS,KHC,KIM,KLAC,KMB,KMI,KMX,KO,KR,KSS,KSU,L,LB,LBTYA,LBTYK,LDOS,LEG,LEN,LH,LHX,LIN,LKQ,LLY,LMT,LNC,LNT,LOW,LRCX,LULU,LUV,LVS,LW,LYB,LYV,MA,MAA,MAR,MAS,MCD,MCHP,MCK,MCO,MDLZ,MDT,MELI,MET,MGM,MHK,MKC,MKTX,MLM,MMC,MMM,MNST,MO,MOS,MPC,MRK,MRO,MS,MSCI,MSFT,MSI,MTB,MTD,MU,MXIM,MYL,NBL,NCLH,NDAQ,NEE,NEM,NFLX,NI,NKE,NLOK,NLSN,NOC,NOV,NOW,NRG,NSC,NTAP,NTES,NTRS,NUE,NVDA,NVR,NWL,NWS,NWSA,NXPI,O,ODFL,OKE,OMC,ORCL,ORLY,OTIS,OXY,PAYC,PAYX,PBCT,PCAR,PEAK,PEG,PEP,PFE,PFG,PG,PGR,PH,PHM,PKG,PKI,PLD,PM,PNC,PNR,PNW,PPG,PPL,PRGO,PRU,PSA,PSX,PVH,PWR,PXD,PYPL,QCOM,QRVO,RCL,RE,REG,REGN,RF,RHI,RJF,RL,RMD,ROK,ROL,ROP,ROST,RSG,RTX,SBAC,SBUX,SCHW,SEE,SGEN,SHW,SIRI,SIVB,SJM,SLB,SLG,SNA,SNPS,SO,SPG,SPGI,SPLK,SRE,STE,STT,STX,STZ,SWK,SWKS,SYF,SYK,SYY,T,TAP,TCOM,TDG,TEL,TFC,TFX,TGT,TIF,TJX,TMO,TMUS,TPR,TROW,TRV,TSCO,TSLA,TSN,TT,TTWO,TWTR,TXN,TXT,UA,UAA,UAL,UDR,UHS,ULTA,UNH,UNM,UNP,UPS,URI,USB,V,VAR,VFC,VIAC,VLO,VMC,VNO,VRSK,VRSN,VRTX,VTR,VZ,WAB,WAT,WBA,WDAY,WDC,WEC,WELL,WFC,WHR,WLTW,WM,WMB,WMT,WRB,WRK,WST,WU,WY,WYNN,XEL,XLNX,XOM,XRAY,XRX,XYL,YUM,ZBH,ZBRA,ZION,ZTS"
    sp500_plus_nas100_forDB = "INX,IXIC,AAPL,A,AAL,AAP,ABBV,ABC,ABMD,ABT,ACN,ADBE,ADI,ADM,ADP,ADS,ADSK,AEE,AEP,AES,AFL,AIG,AIV,AIZ,AJG,AKAM,ALB,ALGN,ALK,_ALL,ALLE,ALXN,AMAT,AMCR,AMD,AME,AMGN,AMP,AMT,AMZN,ANET,ANSS,ANTM,AON,AOS,APA,APD,APH,APTV,ARE,ASML,ATO,ATVI,AVB,AVGO,AVY,AWK,AXP,AZO,BA,BAC,BAX,BBY,BDX,BEN,BF_B,BIDU,BIIB,BK,BKNG,BKR,BLK,BLL,BMRN,BMY,BR,BRK_B,BSX,BWA,BXP,C,CAG,CAH,CARR,CAT,CB,CBOE,CBRE,CCI,CCL,CDNS,CDW,CE,CERN,CF,CFG,CHD,CHKP,CHRW,CHTR,CI,CINF,CL,CLX,CMA,CMCSA,CME,CMG,CMI,CMS,CNC,CNP,COF,COG,COO,COP,COST,COTY,CPB,CPRT,CRM,CSCO,CSGP,CSX,CTAS,CTL,CTSH,CTVA,CTXS,CVS,CVX,CXO,D,DAL,DD,DE,DFS,DG,DGX,DHI,DHR,DIS,DISCA,DISCK,DISH,DLR,DLTR,DOV,DOW,DPZ,DRE,DRI,DTE,DUK,DVA,DVN,DXC,DXCM,EA,EBAY,ECL,ED,EFX,EIX,EL,EMN,EMR,EOG,EQIX,EQR,ES,ESS,ETFC,ETN,ETR,EVRG,EW,EXC,EXPD,EXPE,EXR,F,FANG,FAST,FB,FBHS,FCX,FDX,FE,FFIV,FIS,FISV,FITB,FLIR,FLS,FLT,FMC,FOX,FOXA,FRC,FRT,FTI,FTNT,FTV,GD,GE,GILD,GIS,GL,GLW,GM,GOOG,GOOGL,GPC,GPN,GPS,GRMN,GS,GWW,HAL,HAS,HBAN,HBI,HCA,HD,HES,HFC,HIG,HII,HLT,HOG,HOLX,HON,HPE,HPQ,HRB,HRL,HSIC,HST,HSY,HUM,HWM,IBM,ICE,IDXX,IEX,IFF,ILMN,INCY,INFO,INTC,INTU,IP,IPG,IPGP,IQV,IR,IRM,ISRG,IT,ITW,IVZ,J,JBHT,JCI,JD,JKHY,JNJ,JNPR,JPM,JWN,K,_KEY,_KEYS,KHC,KIM,KLAC,KMB,KMI,KMX,KO,KR,KSS,KSU,L,LB,LBTYA,LBTYK,LDOS,LEG,LEN,LH,LHX,LIN,LKQ,LLY,LMT,LNC,LNT,LOW,LRCX,LULU,LUV,LVS,LW,LYB,LYV,MA,MAA,MAR,MAS,MCD,MCHP,MCK,MCO,MDLZ,MDT,MELI,MET,MGM,MHK,MKC,MKTX,MLM,MMC,MMM,MNST,MO,MOS,MPC,MRK,MRO,MS,MSCI,MSFT,MSI,MTB,MTD,MU,MXIM,MYL,NBL,NCLH,NDAQ,NEE,NEM,NFLX,NI,NKE,NLOK,NLSN,NOC,NOV,NOW,NRG,NSC,NTAP,NTES,NTRS,NUE,NVDA,NVR,NWL,NWS,NWSA,NXPI,O,ODFL,OKE,OMC,ORCL,ORLY,OTIS,OXY,PAYC,PAYX,PBCT,PCAR,PEAK,PEG,PEP,PFE,PFG,PG,PGR,PH,PHM,PKG,PKI,PLD,PM,PNC,PNR,PNW,PPG,PPL,PRGO,PRU,PSA,PSX,PVH,PWR,PXD,PYPL,QCOM,QRVO,RCL,RE,REG,REGN,RF,RHI,RJF,RL,RMD,ROK,ROL,ROP,ROST,RSG,RTX,SBAC,SBUX,SCHW,SEE,SGEN,SHW,SIRI,SIVB,SJM,SLB,SLG,SNA,SNPS,SO,SPG,SPGI,SPLK,SRE,STE,STT,STX,STZ,SWK,SWKS,SYF,SYK,SYY,T,TAP,TCOM,TDG,TEL,TFC,TFX,TGT,TIF,TJX,TMO,TMUS,TPR,TROW,TRV,TSCO,TSLA,TSN,TT,TTWO,TWTR,TXN,TXT,UA,UAA,UAL,UDR,UHS,ULTA,UNH,UNM,UNP,UPS,URI,USB,V,VAR,VFC,VIAC,VLO,VMC,VNO,VRSK,VRSN,VRTX,VTR,VZ,WAB,WAT,WBA,WDAY,WDC,WEC,WELL,WFC,WHR,WLTW,WM,WMB,WMT,WRB,WRK,WST,WU,WY,WYNN,XEL,XLNX,XOM,XRAY,XRX,XYL,YUM,ZBH,ZBRA,ZION,ZTS"
    Alpha_dt = 0.05
    list_sp500_plus_nas100_forSearch = sp500_plus_nas100_forSearch.split(",")
    s = datetime.datetime.now()
    big_list = []
    f_compare_content = []
    _2022_4_12= [('4412.53', '13411.96', '165.75', '131.26', '16.97', '220.97', '169.83', '162.65', '299.76', '120.04', '327.27', '434.44', '154.89', '94.57', '230.96', '56.80', '199.03', '96.48', '101.40', '24.69', '65.19', '62.58', '6.76', '186.85', '183.22', '118.01', '206.00', '409.69', '52.82', '142.90', '106.52', '182.50', '116.24', '11.73', '97.37', '129.88', '250.87', '290.76', '263.31', '3022.44', '127.16', '294.70', '510.64', '333.61', '63.36', '41.07', '249.83', '71.74', '108.21', '198.55', '597.74', '120.51', '79.48', '246.25', '580.61', '175.58', '169.22', '177.57', '2158.48', '175.03', '39.59', '78.77', '94.16', '270.01', '26.18', '68.44', '133.05', '210.62', '48.07', '2169.21', '36.47', '728.38', '88.05', '83.27', '76.50', '154.83', '352.02', '44.22', '36.85', '123.11', '50.55', '35.00', '61.38', '42.44', '216.05', '13.90', '116.75', '86.63', '196.06', '18.54', '153.74', '172.21', '144.98', '93.10', '107.05', '41.82', '103.98', '140.39', '102.62', '559.91', '254.12', '136.48', '80.44', '147.75', '89.09', '47.61', '239.84', '1511.47', '192.93', '72.24', '86.90', '32.23', '131.23', '22.25', '406.96', '97.98', '584.67', '8.69', '45.77', '123.37', '195.45', '52.88', '63.63', '34.24', '418.01', '11.00', '87.21', '59.75', '101.14', '104.45', '165.56', '65.60', '87.52', '38.21', '68.48', '418.51', '111.17', '240.77', '137.39', '72.17', '291.12', '130.65', '24.43', '24.42', '32.18', '145.47', '165.49', '149.23', '61.95', '387.92', '58.72', '126.54', '136.86', '114.23', '119.39', '60.03', '30.88', '492.49', '122.58', '54.89', '180.54', '96.60', '218.26', '70.80', '262.28', '107.51', '93.18', '121.34', '751.61', '89.85', '91.78', '344.55', '49.26', '142.27', '121.79', '70.58', '121.50', '48.24', '96.92', '177.30', '210.60', '15.28', '135.11', '57.97', '216.46', '71.35', '47.72', '204.12', '46.88', '207.49', '101.92', '100.60', '40.49', '57.34', '34.60', '250.17', '136.58', '35.51', '38.72', '157.51', '120.60', '7.71', '328.07', '58.85', '243.55', '89.67', '61.89', '70.51', '102.82', '33.67', '40.33', '2595.93', '2576.47', '130.66', '136.21', '13.57', '111.74', '320.76', '518.66', '39.06', '83.60', '13.80', '14.33', '258.18', '306.72', '111.76', '36.39', '74.12', '205.24', '143.70', '38.22', '76.52', '189.27', '15.81', '38.19', '26.92', '53.11', '90.21', '17.85', '223.93', '451.33', '34.23', '126.37', '128.10', '514.48', '195.13', '125.67', '351.28', '80.95', '108.61', '46.57', '473.34', '46.67', '34.13', '100.01', '242.98', '46.42', '55.53', '278.96', '288.79', '200.81', '21.48', '142.69', '170.70', '63.34', '56.83', '198.55', '179.84', '34.41', '133.00', '27.84', '67.86', '20.86', '147.40', '41.25', '24.47', '331.47', '126.53', '19.26', '103.17', '63.81', '60.65', '57.24', '293.59', '64.66', '40.48', '25.45', '25.96', '108.17', '35.95', '76.32', '272.42', '256.57', '317.15', '45.48', '308.96', '464.25', '63.81', '64.35', '204.59', '475.76', '368.74', '42.62', '35.04', '65.96', '101.39', '107.88', '347.37', '207.87', '162.45', '50.14', '250.45', '65.81', '320.67', '334.37', '63.41', '111.52', '1125.69', '70.58', '39.51', '124.30', '102.09', '280.84', '369.89', '170.74', '150.12', '82.17', '54.45', '73.91', '84.88', '86.63', '25.22', '84.02', '486.09', '285.26', '233.35', '163.53', '1348.00', '72.03', '103.14', '15.86', '8.46', '20.26', '182.33', '84.58', '81.34', '348.00', '31.89', '124.98', '26.61', '27.40', '462.14', '19.41', '511.42', '38.54', '255.81', '77.12', '95.01', '114.77', '152.80', '219.17', '4324.68', '22.18', '21.48', '21.10', '165.52', '71.52', '258.10', '70.26', '78.17', '79.76', '723.94', '76.37', '57.92', '316.73', '136.84', '19.41', '82.58', '34.84', '71.73', '172.60', '53.93', '73.30', '159.49', '118.43', '270.42', '41.47', '154.91', '165.77', '165.73', '101.24', '183.98', '52.56', '78.21', '131.75', '28.91', '36.72', '116.50', '401.80', '82.49', '75.00', '133.03', '246.49', '109.81', '135.36', '114.88', '78.75', '296.96', '70.03', '722.37', '21.14', '111.31', '108.10', '105.04', '242.15', '266.08', '35.56', '480.78', '99.71', '135.77', '102.11', '361.30', '80.68', '81.58', '67.68', '144.29', '261.10', '6.53', '516.03', '139.43', '41.33', '75.47', '210.78', '309.77', '74.48', '126.78', '405.61', '133.28', '168.25', '247.23', '82.72', '84.52', '247.51', '141.00', '120.94', '36.52', '263.34', '84.71', '19.63', '52.84', '21.49', '633.53', '123.22', '53.64', '338.88', '229.31', '131.46', '61.86', '585.67', '130.42', '33.55', '143.07', '185.64', '235.11', '975.93', '93.82', '147.86', '140.53', '47.01', '171.94', '67.83', '14.68', '15.90', '42.42', '57.50', '147.86', '403.78', '537.44', '32.15', '243.11', '190.84', '316.03', '51.72', '214.75', '177.07', '55.30', '29.58', '100.90', '176.17', '41.59', '216.45', '213.85', '281.09', '60.82', '53.90', '89.01', '302.58', '44.43', '227.21', '47.02', '103.66', '96.37', '49.33', '176.43', '231.56', '164.16', '34.40', '154.29', '67.46', '47.60', '398.50', '19.03', '39.02', '71.29', '74.36', '194.92', '83.85', '48.48', '19.42', '85.73', '118.31', '126.90', '408.70', '64.23', '192.50')][0]
    for it in list_sp500_plus_nas100_forSearch:
        url = "http://gu.qq.com/us{0}.OQ/gg".format(it)
        print(url)
        sp_nas = Sp_plus_Nas_StockPool(url)
        sp_nas.page_parse_()
    ff_l = []
    compare_(_2022_4_12)
    f_tup = tuple(f_compare_content)
    print(f_tup)
    ff_l.append((f_tup))
    print(ff_l)
    print(big_list)
    print(f_compare_content)
    insertDB(ff_l)
    e = datetime.datetime.now()
    print(e-s)






# create table following_sp500_plus_nas100_20220412(id int not null primary key auto_increment,INX float,IXIC float,AAPL float,A float,AAL float,AAP float,ABBV float,ABC float,ABMD float,ABT float,ACN float,ADBE float,ADI float,ADM float,ADP float,ADS float,ADSK float,AEE float,AEP float,AES float,AFL float,AIG float,AIV float,AIZ float,AJG float,AKAM float,ALB float,ALGN float,ALK float,_ALL float,ALLE float,ALXN float,AMAT float,AMCR float,AMD float,AME float,AMGN float,AMP float,AMT float,AMZN float,ANET float,ANSS float,ANTM float,AON float,AOS float,APA float,APD float,APH float,APTV float,ARE float,ASML float,ATO float,ATVI float,AVB float,AVGO float,AVY float,AWK float,AXP float,AZO float,BA float,BAC float,BAX float,BBY float,BDX float,BEN float,BF_B float,BIDU float,BIIB float,BK float,BKNG float,BKR float,BLK float,BLL float,BMRN float,BMY float,BR float,BRK_B float,BSX float,BWA float,BXP float,C float,CAG float,CAH float,CARR float,CAT float,CB float,CBOE float,CBRE float,CCI float,CCL float,CDNS float,CDW float,CE float,CERN float,CF float,CFG float,CHD float,CHKP float,CHRW float,CHTR float,CI float,CINF float,CL float,CLX float,CMA float,CMCSA float,CME float,CMG float,CMI float,CMS float,CNC float,CNP float,COF float,COG float,COO float,COP float,COST float,COTY float,CPB float,CPRT float,CRM float,CSCO float,CSGP float,CSX float,CTAS float,CTL float,CTSH float,CTVA float,CTXS float,CVS float,CVX float,CXO float,D float,DAL float,DD float,DE float,DFS float,DG float,DGX float,DHI float,DHR float,DIS float,DISCA float,DISCK float,DISH float,DLR float,DLTR float,DOV float,DOW float,DPZ float,DRE float,DRI float,DTE float,DUK float,DVA float,DVN float,DXC float,DXCM float,EA float,EBAY float,ECL float,ED float,EFX float,EIX float,EL float,EMN float,EMR float,EOG float,EQIX float,EQR float,ES float,ESS float,ETFC float,ETN float,ETR float,EVRG float,EW float,EXC float,EXPD float,EXPE float,EXR float,F float,FANG float,FAST float,FB float,FBHS float,FCX float,FDX float,FE float,FFIV float,FIS float,FISV float,FITB float,FLIR float,FLS float,FLT float,FMC float,FOX float,FOXA float,FRC float,FRT float,FTI float,FTNT float,FTV float,GD float,GE float,GILD float,GIS float,GL float,GLW float,GM float,GOOG float,GOOGL float,GPC float,GPN float,GPS float,GRMN float,GS float,GWW float,HAL float,HAS float,HBAN float,HBI float,HCA float,HD float,HES float,HFC float,HIG float,HII float,HLT float,HOG float,HOLX float,HON float,HPE float,HPQ float,HRB float,HRL float,HSIC float,HST float,HSY float,HUM float,HWM float,IBM float,ICE float,IDXX float,IEX float,IFF float,ILMN float,INCY float,INFO float,INTC float,INTU float,IP float,IPG float,IPGP float,IQV float,IR float,IRM float,ISRG float,IT float,ITW float,IVZ float,J float,JBHT float,JCI float,JD float,JKHY float,JNJ float,JNPR float,JPM float,JWN float,K float,_KEY float,_KEYS float,KHC float,KIM float,KLAC float,KMB float,KMI float,KMX float,KO float,KR float,KSS float,KSU float,L float,LB float,LBTYA float,LBTYK float,LDOS float,LEG float,LEN float,LH float,LHX float,LIN float,LKQ float,LLY float,LMT float,LNC float,LNT float,LOW float,LRCX float,LULU float,LUV float,LVS float,LW float,LYB float,LYV float,MA float,MAA float,MAR float,MAS float,MCD float,MCHP float,MCK float,MCO float,MDLZ float,MDT float,MELI float,MET float,MGM float,MHK float,MKC float,MKTX float,MLM float,MMC float,MMM float,MNST float,MO float,MOS float,MPC float,MRK float,MRO float,MS float,MSCI float,MSFT float,MSI float,MTB float,MTD float,MU float,MXIM float,MYL float,NBL float,NCLH float,NDAQ float,NEE float,NEM float,NFLX float,NI float,NKE float,NLOK float,NLSN float,NOC float,NOV float,NOW float,NRG float,NSC float,NTAP float,NTES float,NTRS float,NUE float,NVDA float,NVR float,NWL float,NWS float,NWSA float,NXPI float,O float,ODFL float,OKE float,OMC float,ORCL float,ORLY float,OTIS float,OXY float,PAYC float,PAYX float,PBCT float,PCAR float,PEAK float,PEG float,PEP float,PFE float,PFG float,PG float,PGR float,PH float,PHM float,PKG float,PKI float,PLD float,PM float,PNC float,PNR float,PNW float,PPG float,PPL float,PRGO float,PRU float,PSA float,PSX float,PVH float,PWR float,PXD float,PYPL float,QCOM float,QRVO float,RCL float,RE float,REG float,REGN float,RF float,RHI float,RJF float,RL float,RMD float,ROK float,ROL float,ROP float,ROST float,RSG float,RTX float,SBAC float,SBUX float,SCHW float,SEE float,SGEN float,SHW float,SIRI float,SIVB float,SJM float,SLB float,SLG float,SNA float,SNPS float,SO float,SPG float,SPGI float,SPLK float,SRE float,STE float,STT float,STX float,STZ float,SWK float,SWKS float,SYF float,SYK float,SYY float,T float,TAP float,TCOM float,TDG float,TEL float,TFC float,TFX float,TGT float,TIF float,TJX float,TMO float,TMUS float,TPR float,TROW float,TRV float,TSCO float,TSLA float,TSN float,TT float,TTWO float,TWTR float,TXN float,TXT float,UA float,UAA float,UAL float,UDR float,UHS float,ULTA float,UNH float,UNM float,UNP float,UPS float,URI float,USB float,V float,VAR float,VFC float,VIAC float,VLO float,VMC float,VNO float,VRSK float,VRSN float,VRTX float,VTR float,VZ float,WAB float,WAT float,WBA float,WDAY float,WDC float,WEC float,WELL float,WFC float,WHR float,WLTW float,WM float,WMB float,WMT float,WRB float,WRK float,WST float,WU float,WY float,WYNN float,XEL float,XLNX float,XOM float,XRAY float,XRX float,XYL float,YUM float,ZBH float,ZBRA float,ZION float,ZTS float,LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;



# drop table following_sp500_plus_nas100_20220412;
