# Web-24｜Moe 笑传之猜猜爆

## 碎碎念

还得是 AI 来看代码……
***
## Writeup

查看开发者，可以看到：

![](../../../../assets/Pasted%20image%2020250927192337.png)

其中它把随机数的生成判断放到了前端执行，这导致我们可以用 console 来获得 randomNumber 的值：

![](../../../../assets/Pasted%20image%2020250927192426.png)

输入即可一次猜对获得 flag：

![](../../../../assets/Pasted%20image%2020250927192450.png)

flag 为：`moectf{dca89f77-0428-e4ea-3bc0-67e1a7cb04f3}`