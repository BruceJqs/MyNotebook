# [ACTF2020 新生赛]BackupFile

## Tag

Dirsearch 大法

***

## Writeup

Dirsearch 只有一个路径 `/manager/jmxproxy/?get=BEANNAME&att=MYATTRIBUTE&key=MYKEY` 显示 200，但是访问：

![image-20260128212834784](../../../../assets/image-20260128212834784.png)

因此尝试把 key 改成 123 即可获得 flag：

![image-20260128212906000](../../../../assets/image-20260128212906000.png)

***

后记：其实是非预期了，dirsearch 没有搜到 index.php.bak：

![image-20260128213107400](../../../../assets/image-20260128213107400.png)

实际上只要传 key 参数为 123 才可以，属于是运气爆棚了