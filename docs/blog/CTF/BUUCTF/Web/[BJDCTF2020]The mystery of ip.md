# [BJDCTF2020]The mystery of ip

## Tag

SSTI 注入

***

## Writeup

根据提示，合理猜想和 X-Forwarded-For 有关系，尝试修改成功：

![image-20260212175813453](../../../../assets/image-20260212175813453.png)

尝试 SSTI 注入：

![image-20260212175944000](../../../../assets/image-20260212175944000.png)

成功，那么注入 `{{system('cat /flag')}}` 即可：

![image-20260212180521225](../../../../assets/image-20260212180521225.png)

后记：本来想用 MoeCTF SSTI 注入的方法的，但是都不可行，会报错

![image-20260212181058775](../../../../assets/image-20260212181058775.png)

里面提到了一个叫 Smarty Compiler，说明是一个叫 Smarty 的模板