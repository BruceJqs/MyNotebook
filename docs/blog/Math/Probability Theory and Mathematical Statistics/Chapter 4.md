---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  
# Chapter 04 : 随机变量的数字特征

## 数学期望

### 离散型随机变量的数学期望

设离散型随机变量 $X$ 的概率分布率为 $P\{X=x_i\}=p_i,i=1,2,..$.，若级数 $\sum\limits_{i=1}^{+\infty}=|x_i|p_i<+\infty$（绝对收敛），则称级数 $\sum\limits_{i=1}^{+\infty}=|x_i|p_i$ 为 $X$ 的数学期望（Mathematical Expectation）或均值（Mean），简称为期望，记 $E(X)=\sum\limits_{i=1}^{+\infty}x_ip_i$。

如果 $\sum\limits_{i=1}^{+\infty}=|x_i|p_i=+\infty$ 则称随机变量 $X$ 的数学期望不存在。
***
#### 0-1 分布的数学期望

设随机变量 $X$ 服从 0-1 分布 $B(1,p)(0<p<1)$，则：

$$
E(X)=\sum\limits_{k=0}^1k·P\{X=k\}=0·P\{X=0\}+1·P\{X=1\}=0·(1-p)+1·p=p
$$

***
#### 二项分布的数学期望

设随机变量 $X$ 服从二项分布 $B(n,p)(n\in\mathbb{N}^∗,0<p<1)$，则：

$$
E(X)=\sum\limits_{k=0}^nk⋅P\{X=k\}=\sum\limits_{k=0}^nk⋅C_n^kp^k(1−p)^{n−k}=np\sum\limits_{k=1}^nC_{n−1}^{k−1}p^{k−1}(1−p)^{n−k}=np
$$


或者，我们引入随机变量 $X_i=\begin{cases}1,第i次试验成功\\0,第i次试验失败\end{cases}$，则 $X=\sum\limits_{i=1}^nX_i$，且 $X_i$ 相互独立，且 $X_i∼B(1,p)$，则：

$$
E(X)=E(\sum\limits_{i=1}^nX_i)=\sum\limits_{i=1}^nE(X_i)=\sum\limits_{i=1}^np=np
$$

***
#### 泊松分布的数学期望

设随机变量 $X$ 服从泊松分布 $P(\lambda)(\lambda>0)$，则：

$$
E(X)=\sum\limits_{k=0}^{+\infty}k⋅P{X=k}=\sum\limits_{k=0}^{+\infty}k⋅\frac{\lambda ^k}{k!}e^{−\lambda}=\lambda e^{−\lambda}\sum\limits_{k=1}^{+\infty}\frac{\lambda^{k−1}}{(k−1)!}=\lambda
$$

由此式可知，已知泊松分布的数学期望可以确定泊松分布。
***
### 连续型随机变量的数学期望

设连续型随机变量 $X$ 的密度函数为 $f(x)$，若 $\int_{−\infty}^{+\infty}|x|f(x)dx<+\infty$，则称积分$\int_{−\infty}^{+\infty}xf(x)dx$ 为 $X$ 的数学期望或均值，简称为期望，记 $E(X)=\int_{−\infty}^{+\infty}xf(x)dx$。

如果 $\int_{−\infty}^{+\infty}|x|f(x)dx=+\infty$ 则称随机变量 $X$ 的数学期望不存在。
***
#### 均匀分布的数学期望

设随机变量 $X$ 服从均匀分布 $U(a,b)(a<b)$，则：

$$
E(X)=\int_{−\infty}^{+\infty}xf(x)dx=\int_{−\infty}^{+\infty}x\frac{1}{b−a}dx=\frac{1}{b−a}\int\limits_{−\infty}^{+\infty}xdx=\frac{1}{b−a}⋅\frac{x^2}{2}|_a^b=\frac{a+b}{2}
$$

***
#### 指数分布的数学期望

设随机变量 $X$ 服从指数分布 $E(\lambda)(\lambda>0)$，则：

$$
E(X)=\int_{−\infty}^{+\infty}xf(x)dx=\int_0^{+\infty}x\lambda e^{−λx}dx=−\int_0^{+\infty}xd(e^{−\lambda x})=−(xe^{−\lambda x})|_0^{+\infty}+\int_0^{+\infty}e^{−\lambda x}dx=\frac{1}{\lambda}
$$

由此式可知，已知指数分布的数学期望可以确定指数分布。
***
#### 标准正态分布的数学期望

设随机变量 $X$ 服从标准正态分布 $N(0,1)$，注意到其密度函数 $\varphi(x)=\frac{1}{\sqrt{2\pi}}e^{−\frac{x^2}{2}},x\in\mathbb{R}$ 为偶函数，那么$x\varphi(x)$ 是奇函数，所以 $E(X)=0$
***
#### 正态分布的数学期望

设随机变量X服从正态分布 $N(\mu,\sigma^2)(\sigma>0)$，则：

$$
\begin{gather}
Z=\frac{X−\mu}{\sigma}∼N(0,1)\\
E(X)=E(\sigma Z+\mu)=\sigma E(Z)+\mu=\mu
\end{gather}
$$

***
### 随机变量函数的数学期望

对于随机变量函数，在保证期望存在的情况下，只需要将定义中 $x_i$ 换为 $g(x_i)$ 即可，但我们不需要计算 $g(x_i)$ 的概率分布率：

离散型：$Z=g(X)$，则 $E(Z)=E[g(X)]=\sum\limits_{i=1}^{+\infty}g(x_i)p_i$

连续型：$Z=g(X)$，则 $E(Z)=E[g(X)]=\int g(x)f(x)dx$

二元离散型：$Z=h(X,Y)$，则 $E(Z)=E[h(X,Y)]=\sum\limits_{i=1}^{+\infty}\sum\limits_{j=1}^{+\infty}h(x_i,y_j)p_{ij}$

二元连续型：$Z=h(X,Y)$，则 $E(Z)=E[h(X,Y)]=\int_{−\infty}^{+\infty}\int_{−\infty}^{+\infty}h(x,y)f(x,y)dxdy$

!!! tip

	以上所有的 $p_i,p_{ij},f(x),f(x,y)$ 均为 $X,Y$ 本来的联合分布率，而不是 $Z$ 的联合分布率
***
### 数学期望的性质

除了使用定义计算，还有一些性质可以简化计算：

- 若 $C$ 是常数，则 $E(C)=C$；
- 设 $X$ 是随机变量，$C$ 是常数，则 $E(C⋅X)=C⋅E(X)$；
- 设 $X,Y$ 是两个随机变量，则 $E(X+Y)=E(X)+E(Y)$； 
	- 这一性质可以推广到任意有限个随机变量线性组合的情况：$E(\sum\limits_i^nc_i⋅X_i)=\sum\limits_i^nc_i⋅E(X_i)$；

!!! tip

	上述三条合并起来就是 $E(aX+bY+c)=aE(X)+bE(Y)+c$

- 设 $X,Y$ 是相互独立的随机变量，则 $E(X⋅Y)=E(X)⋅E(Y)$，但**逆命题不成立**；
	- 更一般地，对于任意有限个独立的随机变量，$E(\prod\limits_i^nX_i)=\prod\limits_i^nE(X_i)$

