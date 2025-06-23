---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 06 : RSA 算法

## RSA 算法简介

- RSA 算法是一种非对称密码体制（也叫公钥密码体制）
- RSA 利用了当前 $n$ 足够大时（比如达到 1024 位）无法进行分解

其主要方法如下：

1. 选取两个大素数 $p$ 和 $q$，计算乘积：$n=pq$
2. 随机选取加密密钥 $e$，使得 $e$ 和 $(p-1)(q-1)$ 互素
3. 找出 $d$，使得 $e*d=1\text{ mod } ((p-1)*(q-1))$
4. 按照 $c=m^e(\text{ mod }n)$ 进行加密，$m=c^d(\text{ mod }n)$ 进行解密
***
### 数学基础

#### 欧拉函数 & 欧拉定理

我们定义欧拉函数为 $\phi(n)$，代表小于 $n$ 且与 $n$ 互素的整数个数

对此我们有欧拉定理：若 $\gcd(x,n)=1$，则 $x^{\phi(n)}=1(\text{ mod }n)$

欧拉函数具有如下性质：

- 若 $n_1,n_2$ 互素，则 $\phi(n_1*n_2)=\phi(n_1)*\phi(n_2)$
- $\phi(n)=n\times\prod\limits_{p|n}\left( 1-\frac{1}{p} \right)$
***
#### 费马小定理

设 $p$ 为素数，且 $\gcd(x,p)=1$，则 $x^{p-1}=1(\text{ mod }p)$

- 这是因为当 $p$ 为素数时，显然有 $\phi(p)=p-1$
***
#### 中国剩余定理

见[离散笔记](https://brucejqs.github.io/MyNotebook/blog/Math/Discrete%20mathmatics/Discrete%20mathmatics%20notes-Ch04/#the-chinese-remainder-theorem)
***
### 算法证明

设 $m$ 是明文，$c$ 是密文，$c=m^e\text{ mod }n$

因为 $\phi(n)=\phi(p*q)=\phi(p)*\phi(q)=(p-1)(q-1)$，又因为 $ed=1\text{ mod }(p-1)(q-1)$，所以一定可以找到一个 $k$ 使得 $ed=1+k(p-1)(q-1)$

于是 $c^d=m^{ed}=m^{1+k(p-1)(q-1)}=m*(m^{\phi(n)})^k=m*1^k=m\text{ mod }n$