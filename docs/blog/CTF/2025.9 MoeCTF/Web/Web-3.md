# Web-3｜第三章 问剑石！篡天改命！

## 碎碎念

数据包拦截 & 篡改
***
## WriteUp

从题目意思很明显能看出需要我们进行数据包拦截和篡改，只要修改 POST 参数路由为 `/test_talent?level=S`，把请求包内的 json 中的 `manifestation` 改为 `flowing_azure_clouds` 即可获得 flag：

![](../../../../assets/Pasted%20image%2020250915140852.png)

![](../../../../assets/Pasted%20image%2020250915140538.png)

最终 flag：`moectf{get-P05t_TR@N5m1ssl0N-1S_A_Go0D-MEth0d1!!1b8}`