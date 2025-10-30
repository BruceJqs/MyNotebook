# Web-14｜第十四章 御神关·补天玉碑

## 碎碎念

比上一道题多了一步，Apache .htaccess+一句话木马
***
## Writeup

题目依然是文件上传，但是限制了 php，但是 Apache 有一个神奇的配置文件叫 .htaccess，是 Apache Web 服务器下用于**进行目录级别配置**的特殊配置文件，我们先上传一个 .htaccess 文件：

```
AddType application/x-httpd-php .txt
```

这句话的意思就是告诉 Apache 服务器将后缀名为 .txt 的文件当做 php 文件来解析，这样我们就可以以 txt 的形式上传一句话木马，用蚁剑一把梭得到 flag：

![](../../../../assets/Pasted%20image%2020251029144359.png)

最终 flag：`moectf{565a55b1-ee15-b8f3-636b-cfd3636ca933}`