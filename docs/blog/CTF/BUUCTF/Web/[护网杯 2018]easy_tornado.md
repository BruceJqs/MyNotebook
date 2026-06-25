# [护网杯 2018]easy_tornado

## Tag

Tornado Python 模板 SSTI 注入

***

## Writeup

查询资料可以知道 Tornado 跟 Flask 类似，是一个 Python 框架，尝试 SSTI 注入：

![image-20260130112741030](../../../../assets/image-20260130112741030.png)

那我们针对 `error?msg=` 注入：

![image-20260130112807219](../../../../assets/image-20260130112807219.png)

注入 `{{handler.settings}}` 即可获得 cookie_secret：

![image-20260130112858986](../../../../assets/image-20260130112858986.png)

然后就可以通过它的加密方式获得 flag：

![image-20260130113342921](../../../../assets/image-20260130113342921.png)

![image-20260130113351644](../../../../assets/image-20260130113351644.png)