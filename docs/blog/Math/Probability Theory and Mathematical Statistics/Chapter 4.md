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
