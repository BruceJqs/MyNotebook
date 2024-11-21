---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---
# Chapter 05 : 大数定律和中心极限定理

## 大数定律

### 依概率收敛

设 $\{Y_n,n\geq 1\}$ 为一**随机变量序列**，若对于 $\forall\epsilon>0$，均有 $\lim\limits_{n\rightarrow+\infty}P\{|Y_n−Y|\geq\epsilon\}=0$（或者 $\lim\limits_{n\rightarrow +\infty}P\{|Y_n−c|<\epsilon\}=1$），则称 $\{Y_n,n\geq 1\}$ **依概率收敛(Convergence in Probability)** 于 $Y$，记做 $Y_n\stackrel{P}{\rightarrow}Y,n\rightarrow+\infty$。

特别地，当 $Y=c$ 为一常数时，称 $\{Y_n,n\geq 1\}$ 依概率收敛于常数 $c$。

- 这种收敛不是数学意义上的一般收敛，而是概率意义下的一种收敛；
- 其含义是：$Y_n$ 对 $Y$ 的绝对偏差不小于任何一个给定量的可能性随 $n$ 的增大而越来越小；或者绝对偏差 $|Y_n−Y|$ 小于任何一个给定量的可能性随 $n$ 的增大时而越来越接近于 1；

***
依概率收敛有如下重要**性质**：

- 若 $X_n\stackrel{P}{\rightarrow}a，Y_n\stackrel{P}{\rightarrow}b$，当 $n\rightarrow+\infty$ 时，函数 $g(x,y)$ 在点 $(a,b)$ 连续，则：$g(X_n,Y_n)\stackrel{P}{\rightarrow}g(a,b),n\rightarrow+\infty$
	- 特别地，若 $X_n\stackrel{P}{\rightarrow}a$，$f(x)$ 在点 $a$ 连续，则：$f(X_n)\stackrel{P}{\rightarrow}f(a),n\rightarrow+\infty$
***
### 两个重要不等式

#### 马尔可夫（Markov）不等式

- 考试不要求（）

若随机变量 $Y$ 的 $k$ 阶（原点）矩存在（$k\geq 1$），即 $E(Y_k)$ 存在，则对 $\forall\epsilon>0$，均有：

$P\{|Y|\geq\epsilon\}\leq \frac{E(|Y|^k)}{\epsilon^k}\text{ or }P\{|Y|<\epsilon\}\geq 1−\frac{E(|Y|^k)}{\epsilon^k}$；特别地，当 $Y$ 取非负值的随机变量且它的 $k$ 阶矩存在时，有：$P\{Y\geq\epsilon\}\leq \frac{E(Y^k)}{\epsilon^k}$
***
#### 切比雪夫（Chebyshev）不等式

若随机变量 $X$ 具有数学期望 $E(X)=\mu$，方差 $Var(X)=\sigma^2$，则对 $\forall\epsilon>0$，均有：

$P\{|X−\mu|\geq\epsilon\}\leq\frac{\sigma^2}{\epsilon^2}\text{ or }P\{|X−μ|<\epsilon\}\geq 1−\frac{\sigma^2}{\epsilon^2}$

- 切比雪夫不等式是马尔可夫不等式的推论；
- 切比雪夫不等式应用范围更广，但是计算结果更粗糙；
***
### 常见的几种大数定律

> 大数定律主要讨论什么条件下，随机变量序列的算术平均依概率收敛到一个稳定值

!!! note “大数定律的一般形式”

	设 $\{Y_i,i\geq1\}$ 为一随机变量**序列**，若存在**常数**序列 $\{c_n,n\geq 1\}$，使得 $\forall\epsilon>0$，均有：$\lim\limits_{n\rightarrow+\infty}P\{|\frac{1}{n}\sum\limits_{i=1}^nY_i−c_n|\geq\epsilon\}=0$ 或 $\lim\limits_{n\rightarrow+\infty}P\{|\frac{1}{n}\sum\limits_{i=1}^nY_i−c_n|<\epsilon\}=1$ 成立，即有 $(\frac{1}{n}\sum\limits_{i=1}^nY_i−c_n)\stackrel{P}{\rightarrow}0,n\rightarrow+\infty$，则称随机变量序列 $\{Y_i,i\geq1\}$ 服从**弱大数定理(Weak Law of Large Numbers)**，简称服从**大数定律**。
	
	特别地，若 $c_n\equiv c$ 无关，则可以写为：$\frac{1}{n}\sum\limits_{i=1}^nY_i\stackrel{P}{\rightarrow}c,n\rightarrow+\infty$

#### 切比雪夫大数定律

设 $\{X_i,i\geq 1\}$ 为相互独立的随机变量序列，若存在常数 $C$，使得 $Var(X_i)\leq C,i=1,2,...$，即所有的 $X_i$ 的方差有共同的上界，则对 $\forall\epsilon>0$，有 $\lim\limits_{n\rightarrow+\infty}P\{|\frac{1}{n}\sum\limits_{i=1}^nX_i−\frac{1}{n}E(X_i)|\geq\epsilon\}=0$ 成立，即随机变量 $\{X_i,i\geq1\}$ 服从大数定律。

对此我们有推论：设 $\{X_i,i\geq1\}$ 为相互独立的随机变量序列，若它们的方差存在且相同（记为 $\sigma^2$），则随机变量 $\{X_i,i\geq1\}$ 服从大数定律。

- 特别地，设 $X_1,X_2,...,X_n,...$ 相互独立，具有相同的数学期望 $\mu$ 和相同的方差 $\sigma^2$，则当 $n\rightarrow+\infty$ 时，$\frac{1}{n}\sum\limits_{k=1}^nX_k\stackrel{P}{\rightarrow}\mu$（这个结论比较常用）
***
#### 辛钦大数定律

设 $X_1,X_2,...,X_n,...$ 独立同分布，$E(X_i)=\mu$，则当 $n\rightarrow+\infty,\forall\epsilon>0$ 时，有 $\frac{1}{n}\sum\limits_{k=1}^nX_k\stackrel{P}{\rightarrow}\mu$ 或 $\lim\limits_{n\rightarrow+\infty}P\{|\frac{1}{n}\sum\limits_{k=1}^nX_k-\mu|\geq\epsilon\}=0$ 成立，即随机变量序列 $\{X_i,i\geq1\}$ 服从大数定律。

对此我们有推论：设 $\{X_i,i\geq 1\}$ 为独立同分布的随机变量序列，若 $h(x)$ 为连续函数，且 $E(|h(X_1)|)<+\infty$，则对于 $\forall\epsilon>0$，有：$\lim\limits_{n\rightarrow+\infty}P\{|\frac{1}{n}\sum\limits_{i=1}^nh(X_i)−a|≥\epsilon\}=0$ 或 $\frac{1}{n}\sum\limits_{i=1}^nh(X_i)\stackrel{P}{\rightarrow}a,n\rightarrow+\infty$ 成立，其中 $a=E(|h(X_1)|)$，即随机变量 $\{h(X_i),i\geq 1\}$ 也服从大数定律。

