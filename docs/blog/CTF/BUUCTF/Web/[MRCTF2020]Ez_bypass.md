# [MRCTF2020]Ez_bypass

## Tag

MD5 强比较+PHP 弱比较

***

## Writeup

审计源码：

![image-20260130114850543](../../../../assets/image-20260130114850543.png)

传递 GET 参数 `id[]=1&gg[]=2` 和 POST 参数 `passwd=1234567abc` 即可：

![image-20260130115417616](../../../../assets/image-20260130115417616.png)
