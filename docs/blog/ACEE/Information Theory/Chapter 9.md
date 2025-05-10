---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 9 : 离散无记忆信道的编码定理

## 复制信道

![](../../../assets/Pasted%20image%2020250510104449.png)

$$
\begin{aligned}
I(X;Y)&=H(Y)-H(Y|X)=H(Y)-1\\
C&=\max\limits_{\{Q_k\}}I(X;Y)=\max\limits_{\{Q_k\}}H(Y)-1\\
&\leq\log 26 -1=\log 13
\end{aligned}
$$

***
## 二元对称信道

![](../../../assets/Pasted%20image%2020250510104818.png)

$$
\begin{aligned}
I(X;Y)&=H(Y)-H(Y|X)=H(Y)-\sum\limits_{x}p(x)H(Y|X=x)\\
&=H(Y)-\sum\limits_{x}p(x)H(p)\\
&=H(Y)-H(p)\leq 1-H(p)
\end{aligned}
$$

***
## 离散无记忆信道的编码

![](../../../assets/Pasted%20image%2020250510105103.png)

$W=\{1,2,\cdots,M\}$

编码速率（传信率）：$R=\frac{\log M}{n}$

香农信道编码定理：如果信息传输速率 $R$ 小于信道容量 $C$，则总存在一种编码方法，使信息在该信道上无错误地可靠传输
***
### 直观说明

![](../../../assets/Pasted%20image%2020250510175452.png)

$M\approx\frac{2^{nH(Y)}}{2^{nH(Y|X)}}=2^{nI(X;Y)},R=\frac{\log M}{n}\approx I(X;Y)\leq C$


