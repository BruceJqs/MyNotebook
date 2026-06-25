# [MRCTF2020]你传你🐎呢

## Tag

.htaccess+一句话木马

***

## Writeup

题目应该是过滤了 Content-Type 一定要为 image/jpeg，并且过滤所有 php, phtml，因此上传 .htaccess：

![image-20260130104955997](../../../../assets/image-20260130104955997.png)

然后上传一句话木马伪装 jpg 即可：

![image-20260130105017178](../../../../assets/image-20260130105017178.png)

蚁剑一连即可获得 flag：

![image-20260130105033223](../../../../assets/image-20260130105033223.png)