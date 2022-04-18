# -*- coding:utf-8 -*-
import datetime
import os
import re
import time
import pymysql



#http://chromedriver.storage.googleapis.com/index.html
# centos chrome
#https://jingyan.baidu.com/article/03b2f78c546d951fa237ae99.html

#google-chrome --version



# 1 删除数据表
# 2 新建数据表
# 3 计划任务执行采集数据

connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db="ForLynne",
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
cursor.execute("drop table sp_nas_netprofits_fromsina;")
print('删除财务数据表成功!')
time.sleep(1)
cursor.execute("create table sp_nas_netprofits_fromsina(id int not null primary key auto_increment,code varchar(10),name varchar(80), current_dt varchar(10),current_dt_minus1 varchar(10),current_dt_minus2 varchar(10), current_dt_minus3 varchar(10), current_dt_minus4 varchar(10),sina_stock_url text) engine=InnoDB default charset=utf8;")
connection.commit()
connection.close()
print('新建财务数据表成功!')

# 3 计划任务执行采集数据
os.system("python3 sp500_plus_nas100_netprofits_from_sina.py")

# * 6 * * 7：每周三和周日8点和20

# /usr/bin/python3 /root/everySunday_reset_dt.py

# sp500_plus_nas100_netprofits_from_sina.py

# Min2020@$$

# reset db
