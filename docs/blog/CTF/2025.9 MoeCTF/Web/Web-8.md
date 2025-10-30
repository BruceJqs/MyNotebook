# Web-8｜第八章 天衍真言，星图显圣

## 碎碎念

嘶～好像非预期了 hhh
***
## WriteUp

妙妙工具箱，启动！

SqlMap 工具爆破直接出 flag：

![](../../../../assets/Pasted%20image%2020250916105602.png)

最终 flag：`moectf{un1On_ba5eD_sq1l-Ftw1124bf2c85a}`

应该是一个跟 union 有关系的注入题（flag 在 user database 的 flag 表里面），输入用户名 admin，密码 `' union select value,2 from flag--` 也可得到 flag：

![](../../../../assets/Pasted%20image%2020250916110055.png)