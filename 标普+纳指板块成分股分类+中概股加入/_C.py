# coding=utf-8
import time

import xlrd
import pandas as pd
import os

# 创建的目录

def mkdir():
    loc_getcwd = os.getcwd()
    path = "{0}\Outputs".format(loc_getcwd)
    #如果存在目录先删除，如果不存在就创建
    if os.path.exists(path):
        os.removedirs(path)
    else:
        os.mkdir(path)
    return path

def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
       # if 去掉表头
       if rowNum > 0:
          dataFile.append(table.row_values(rowNum))

    return dataFile


if __name__ == '__main__':
    names_list = set()
    loc_getcwd = os.getcwd()
    # excelFile = '{0}\a.xlsx'.format(loc_getcwd) # windows and linux！
    excelFile = '{0}/自制跟踪成分股清单.xlsx'.format(loc_getcwd) # 处理了文件属于当前目录下！

    f_list=[]

    big_l = []
    small_l = []


    full_items = read_xlrd(excelFile=excelFile)
    for item in full_items:
        big_l.append(item[1:4])
        small_l.append(item[-1])


    for i1 in small_l:
        for i2 in big_l:

            if i1 == i2[1] and i2[1] != '' and i2[2] != ""  :
                f_list.append(i2)





    columns = ["名称", "代码", "板块"]
    allC_dt = pd.DataFrame(f_list,columns=columns)
    allC_dt.to_excel("{0}/C_.xlsx".format(loc_getcwd), index=0)
