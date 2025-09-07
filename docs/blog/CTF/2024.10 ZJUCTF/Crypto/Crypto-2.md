---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
---  

# Crypto｜Shad0wTime

## 做题历程 & 感想

手速题（x）笑死我了 Bruce 莫名其妙的就这么秒了……

初看是一个 ECDSA（椭圆曲线加密算法），查资料看晕的 Bruce 觉得这事绝对不对劲哪来的这么复杂的加密算法还是个 easy 难度 hhh

Crypto 题咋都这么奇奇怪怪的还没准备好呢 flag 就来了（bushi）
***
## Writeup

很简单，它既然能同时进行加解密，那同样的道理先加密得到信息再解密回去不就好了？

然后 flag 就爆出来了……都不需要 payload……（让 Bruce 猝不及防）

![](../../../../assets/Pasted%20image%2020241017105121.png)

最终 flag: `ZJUCTF{w31l_you_a!re4d7_kn0w_T0__name__[[vaRIabLes]]_properly}`
