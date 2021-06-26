# US_stocks

２０１８．１０．３０
数据量大了，必须使用SQL语句来提取数据了
SELECT name,round(((d1-d2)/d2),2),round(((d2-d3)/d3),2),round(((d3-d4)/d4),2),round(((d4-d5)/d5),2) FROM us_FinData_sina   
into outfile '/home/karson/tmp.csv';

2019.1.23 模型

![image](https://github.com/Greenbirch2007/US_stocks/blob/master/2019.1.23.png)


2021.6.26 想到找机会做吧
1. US:中概股(60)  VS  SP500   VS   Nas100   近10年股东分红状况
2. JP:  js400  VS   近10年股东分红状况
3.  US VS  JP 近10年股息状况与货币政策相关性
