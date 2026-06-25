# [ACTF2020 新生赛]Include

## Tag

文件注释，Base64

***

## Writeup

看 flag.php 什么都没有，合理猜测被注释了，`?file=php://filter/read=convert.base64-encode/resource=flag.php` 直接提取 Base64 解密：

![image-20260120103214914](../../../../assets/image-20260120103214914.png)