# Web-1｜第一章 神秘的手镯

## 碎碎念

F12 是个好东西嘿嘿嘿……
***

## WriteUp

方法一：直接 F12 查看前端代码即可获得 flag：

![](../../../../assets/Pasted%20image%2020250915124057.png)

方法二：手动触发文本框输入事件：

阅读前端 js 代码我们可以发现输入从 `document.getElementById("passwordInput").value` 获取，且控制台是允许我们复制粘贴的，因此我们在控制台输入 `document.getElementById("passwordInput").value='password'` 即可将文本输入进去，点击按钮即可得到 flag。

![](../../../../assets/Pasted%20image%2020250915124728.png)

最终 flag：`moectf{f_i2_1s_Your_g00d_fri3nd!!}`