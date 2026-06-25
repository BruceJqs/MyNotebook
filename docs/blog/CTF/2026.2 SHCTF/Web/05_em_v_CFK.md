# 05_em_v_CFK

## Tag

源码审计 RCE

***

## Writeup

源码里面有一串字符串：

![image-20260202230818492](../../../../assets/image-20260202230818492.png)

Magic 一解：

![image-20260202230856054](../../../../assets/image-20260202230856054.png)

Dirsearch 能搜到有 uploads 这个目录，因此访问 /uploads/shell.php?show=1：

![image-20260202230927359](../../../../assets/image-20260202230927359.png)

MD5 解密可以得到 114514 因此传参 key=114514&cmd=ls 和 key=114514&cmd=ls ..：

![image-20260202231007894](../../../../assets/image-20260202231007894.png)

![image-20260202231012415](../../../../assets/image-20260202231012415.png)

有一个 connect.php，其他什么都没有，先看一下 index.php：

![image-20260202231641402](../../../../assets/image-20260202231641402.png)

那我们也可以仿照着去修改 flag 的 price：

![image-20260202231809041](../../../../assets/image-20260202231809041.png)

![image-20260202231822058](../../../../assets/image-20260202231822058.png)

购买即可：

![image-20260202231833508](../../../../assets/image-20260202231833508.png)