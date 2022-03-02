#
#
# js   js_infos_finandata
# coding industry title market
import csv
import time

import pandas as pd
import pymysql
from data_config import *
import operator


def count_top30(filename):
    df = pd.read_excel(filename)
    data_list =[]
    for one_stock in a100_code:
        value = (float(list(df[one_stock])[-1])-list(df[one_stock])[0])/list(df[one_stock])[0]
        value_4 = round(value,4)
        new_dict = {"code":one_stock,"value":value_4}
        data_list.append(new_dict)
    sort_data = sorted(data_list,key=operator.itemgetter('value'), reverse=True)
    for item in sort_data[:30]:
        print(item["code"],item["value"])

        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Nas100_infos',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cur = connection.cursor()
        # sql 语句
        sql = "select code,title_zh_cn,industry_infos,sector_infos from nas100_industry_infos where code = '{0}'   ".format(
            item["code"])
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        print(data)
        try: #
            title_zh_cn = data["title_zh_cn"]
            industry_infos = data["industry_infos"]
            sector_infos = data["sector_infos"]
            detail_data = [item["code"],title_zh_cn, item["value"], industry_infos, sector_infos]
            print(detail_data)
            writeinto_detail("followed_detail.csv", detail_data)
            cur.close()
        except:
            pass

# select code,title_zh_cn,infos_zh_cn from nas100_industry_infos where code = "MELI"  ;








#
def writeinto_detail(filename,data):
    with open(filename,"a",newline="",encoding="utf-8-sig") as f:
        csv_out = csv.writer(f,delimiter=",")
        csv_out.writerow(data)


if __name__:= "__main__":
    writeinto_detail("followed_detail.csv",
                     ["code","title_zh_cn","value","industry_infos","sector_infos"])
    count_top30("demo.xlsx")









