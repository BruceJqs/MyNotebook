# Web-15｜第十五章 归真关·竞时净魔

## 碎碎念

还是不太熟 Burp 的各种用法啊...
***
## Writeup

利用 Race Condition 疯狂给网址发上传 php 包：

![](../../../../assets/Pasted%20image%2020251029161021.png)

使用的是 Burp Intruder（Payload 设置成 Null Payload，然后循环发包），可以看到有些时候成功上传：

![](../../../../assets/Pasted%20image%2020251029160940.png)

另一边疯狂刷新界面，可以看到 flag：

![](../../../../assets/Pasted%20image%2020251029160647.png)


最终 flag：`moectf{ace7700f-f976-2430-f01f-3f053bf12b68}`