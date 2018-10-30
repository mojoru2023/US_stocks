# US_stocks

２０１８．１０．３０
数据量大了，必须使用SQL语句来提取数据了
SELECT name,round(((d1-d2)/d2),2),round(((d2-d3)/d3),2),round(((d3-d4)/d4),2),round(((d4-d5)/d5),2) FROM us_FinData_sina   
into outfile '/home/karson/tmp.csv';
