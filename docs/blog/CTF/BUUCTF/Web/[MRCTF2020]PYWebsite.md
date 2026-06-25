# [MRCTF2020]PYWebsite

## Tag

MD5+

***

## Writeup

查看前端代码看到有检查逻辑：

![image-20260216103047722](../../../../assets/image-20260216103047722.png)

MD5 解密的可以得到授权码应该为 `ARandomString`，输入后看到：

![image-20260216103122751](../../../../assets/image-20260216103122751.png)

添加头 X-Forwarded-For: 127.0.0.1 即可获得 flag：

![image-20260216104053650](../../../../assets/image-20260216104053650.png)