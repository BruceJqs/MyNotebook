# Web-4｜第四章 金曦破禁与七绝傀儡阵

## 碎碎念

BurpSuite & HTTP 包进阶～

七道题并成一道题来干...
***
## WriteUp

### 第一关

可以看到，题目要求我们添加参数 `key=xdsec`，篡改请求即可

![](../../../../assets/Pasted%20image%2020250915142150.png)

获得碎片：`bW9lY3Rme0Mw`
***
### 第二关

第二关需要改为 POST 请求，并输入请求体 `declaration=织云阁=第一`，需要加上 `Content-Type: application/x-www-form-urlencoded` 的请求头，即可通过：

![](../../../../assets/Pasted%20image%2020250915142943.png)

获得碎片：`bjZyNDd1MTQ3`
***
### 第三关

有些神奇？还没搞清楚原理

在终端（而非 BurpSuite）使用 curl 添加请求头 `curl -H "X-Real-IP: 127.0.0.1" -H "X-Forwarded-For: 127.0.0.1"` 即可获得结果：

![](../../../../assets/Pasted%20image%2020250915171820.png)

获得碎片：`MTBuNV95MHVy` 且得到下一关路由 `soul_discerner`
***
### 第四关

修改请求包中的 User-Agent 为 moe browser 即可通关：

![](../../../../assets/Pasted%20image%2020250915172221.png)

得到碎片：`X2g3N1BfbDN2`
***
### 第五关

这关需要我们添加请求头的 Cookie 为 `user=xt` 即可通关：

![](../../../../assets/Pasted%20image%2020250915173035.png)

得到碎片 `M2xfMTVfcjM0` 以及第六关路由 `pathfinder`
***
### 第六关

伪造 Referer 为题目要求 `http://panshi/entry` 即可通关：

![](../../../../assets/Pasted%20image%2020250915173430.png)

得到碎片 `bGx5X2gxOWgh` 以及第七关路由 `void_rebirth`
***
### 第七关

将方式改为 PUT 最后加上 `新生！` 即可通关：

![](../../../../assets/Pasted%20image%2020250915173811.png)

得到碎片 `fQ==` ，可以看出为 base64，将所有碎片拼接后解码即可得到最终 flag：`moectf{C0n6r47u14710n5_y0ur_h77P_l3v3l_15_r34lly_h19h!}`


