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

设 $\{Y_n,n\geq 1\}$ 为一**随机变量序列**，若对于 $\forall\epsilon>0$，均有 $\lim\limits_{n\rightarrow+\infty}P\{|Y_n−Y|\geq\epsilon\}=0$（或者 $\lim\limits_{n\rightarrow +\infty}P\{|Y_n−c|<\epsilon\}=1$），则称 $\{Y_n,n\geq 1\}$ **依概率收敛（Convergence in Probability）** 于 $Y$，记做 $Y_n\stackrel{P}{\rightarrow}Y,n\rightarrow+\infty$。

特别地，当 $Y=c$ 为一常数时，称 $\{Y_n,n\geq 1\}$ 依概率收敛于常数 $c$。

- 这种收敛不是数学意义上的一般收敛，而是概率意义下的一种收敛；
- 其含义是：$Y_n$ 对 $Y$ 的绝对偏差不小于任何一个给定量的可能性随 $n$ 的增大而越来越小；或者绝对偏差 $|Y_n−Y|$ 小于任何一个给定量的可能性随 $n$ 的增大时而越来越接近于 1；

***
依概率收敛有如下重要**性质**：

- 若 $X_n\stackrel{P}{\rightarrow}a，Y_n\stackrel{P}{\rightarrow}b$，当 $n\rightarrow+\infty$ 时，函数 $g(x,y)$ 在点 $(a,b)$ 连续，则：$g(X_n,Y_n)\stackrel{P}{\rightarrow}g(a,b),n\rightarrow+\infty$
	- 特别地，若 $X_n\stackrel{P}{\rightarrow}a$，$f(x)$ 在点 $a$ 连续，则：$f(X_n)\stackrel{P}{\rightarrow}f(a),n\rightarrow+\infty$
***
### 两个重要不等式

#### 马尔可夫不等式

- 考试不要求（）

若随机变量 $Y$ 的 $k$ 阶（原点）矩存在（$k\geq 1$），即 $E(Y_k)$ 存在，则对 $\forall\epsilon>0$，均有：

$P\{|Y|\geq\epsilon\}\leq \frac{E(|Y|^k)}{\epsilon^k}\text{ or }P\{|Y|<\epsilon\}\geq 1−\frac{E(|Y|^k)}{\epsilon^k}$；特别地，当 $Y$ 取非负值的随机变量且它的 $k$ 阶矩存在时，有：$P\{Y\geq\epsilon\}\leq \frac{E(Y^k)}{\epsilon^k}$
***
#### 切比雪夫不等式

若随机变量 $X$ 具有数学期望 $E(X)=\mu$，方差 $Var(X)=\sigma^2$，则对 $\forall\epsilon>0$，均有：

$P\{|X−\mu|\geq\epsilon\}\leq\frac{\sigma^2}{\epsilon^2}\text{ or }P\{|X−μ|<\epsilon\}\geq 1−\frac{\sigma^2}{\epsilon^2}$

- 切比雪夫不等式是马尔可夫不等式的推论；
- 切比雪夫不等式应用范围更广，但是计算结果更粗糙；
***
### 常见的几种大数定律

> 大数定律主要讨论什么条件下，随机变量序列的算术平均依概率收敛到一个稳定值

!!! note "大数定律的一般形式"

	设 $\{Y_i,i\geq1\}$ 为一随机变量**序列**，若存在**常数**序列 $\{c_n,n\geq 1\}$，使得 $\forall\epsilon>0$，均有：$\lim\limits_{n\rightarrow+\infty}P\{|\frac{1}{n}\sum\limits_{i=1}^nY_i−c_n|\geq\epsilon\}=0$ 或 $\lim\limits_{n\rightarrow+\infty}P\{|\frac{1}{n}\sum\limits_{i=1}^nY_i−c_n|<\epsilon\}=1$ 成立，即有 $(\frac{1}{n}\sum\limits_{i=1}^nY_i−c_n)\stackrel{P}{\rightarrow}0,n\rightarrow+\infty$，则称随机变量序列 $\{Y_i,i\geq1\}$ 服从**弱大数定理(Weak Law of Large Numbers)**，简称服从**大数定律**。
	
	特别地，若 $c_n\equiv c$ 无关，则可以写为：$\frac{1}{n}\sum\limits_{i=1}^nY_i\stackrel{P}{\rightarrow}c,n\rightarrow+\infty$

#### 切比雪夫大数定律

设 $\{X_i,i\geq 1\}$ 为相互独立的随机变量序列，若存在常数 $C$，使得 $Var(X_i)\leq C,i=1,2,...$，即所有的 $X_i$ 的方差有共同的上界，则对 $\forall\epsilon>0$，有 $\lim\limits_{n\rightarrow+\infty}P\{|\frac{1}{n}\sum\limits_{i=1}^nX_i−\frac{1}{n}E(X_i)|\geq\epsilon\}=0$ 成立，即随机变量 $\{X_i,i\geq1\}$ 服从大数定律。

对此我们有推论：设 $\{X_i,i\geq1\}$ 为相互独立的随机变量序列，若它们的方差存在且相同（记为 $\sigma^2$），则随机变量 $\{X_i,i\geq1\}$ 服从大数定律。

- 特别地，设 $X_1,X_2,...,X_n,...$ 相互独立，具有相同的数学期望 $\mu$ 和相同的方差 $\sigma^2$，则当 $n\rightarrow+\infty$ 时，$\frac{1}{n}\sum\limits_{k=1}^nX_k\stackrel{P}{\rightarrow}\mu$（这个结论比较常用）
	
	!!! note "证明"
	
		$\because E(\frac{1}{n}\sum\limits_{i=1}^nX_i)=\mu,D(\frac{1}{n}\sum\limits_{i=1}^nX_i)=\frac{\sigma^2}{n}$
		
		利用切比雪夫不等式：
		
		$P(|\frac{1}{n}\sum\limits_{i=1}^nX_i-\mu|\geq\epsilon)\leq\frac{D(\frac{1}{n}\sum\limits_{i=1}^nX_i)}{\epsilon^2}=\frac{\sigma^2}{n\epsilon^2}\rightarrow 0$

接下来给出几种常见的大数定律，它们的区别体现在**条件**上：有些是相互独立的随机变量，有些是相依的随机变量；有些是同分布的随机变量，有些是不同分布的随机变量。
***
#### 辛钦大数定律

设 $X_1,X_2,...,X_n,...$ 独立同分布，$E(X_i)=\mu$，则当 $n\rightarrow+\infty,\forall\epsilon>0$ 时，有 $\frac{1}{n}\sum\limits_{k=1}^nX_k\stackrel{P}{\rightarrow}\mu$ 或 $\lim\limits_{n\rightarrow+\infty}P\{|\frac{1}{n}\sum\limits_{k=1}^nX_k-\mu|\geq\epsilon\}=0$ 成立，即随机变量序列 $\{X_i,i\geq1\}$ 服从大数定律。

对此我们有推论：设 $\{X_i,i\geq 1\}$ 为独立同分布的随机变量序列，若 $h(x)$ 为连续函数，且 $E(|h(X_1)|)<+\infty$，则对于 $\forall\epsilon>0$，有：$\lim\limits_{n\rightarrow+\infty}P\{|\frac{1}{n}\sum\limits_{i=1}^nh(X_i)−a|≥\epsilon\}=0$ 或 $\frac{1}{n}\sum\limits_{i=1}^nh(X_i)\stackrel{P}{\rightarrow}a,n\rightarrow+\infty$ 成立，其中 $a=E(|h(X_1)|)$，即随机变量 $\{h(X_i),i\geq 1\}$ 也服从大数定律。
***
#### 贝努里大数定律

设 $n_A$ 为 $n$ 重贝努里试验中事件 $A$ 发生的次数，并记事件 $A$ 在每次试验中发生的概率为 $p$，则当 $n\rightarrow+\infty$ 时，有 $\frac{n_A}{n}\stackrel{P}{\rightarrow}p$

- 伯努利大数定律建立了在大量重复试验中事件出现频率的稳定性，正因为这种稳定性，**概率**的概念才有客观意义；
- 伯努利大数定律还提供了通过试验来确定事件概率的方法：既然频率 $\frac{n_A}{n}$ 与概率 $p$ 有较大偏差的可能性很小，因此可以通过做试验来确定某事件发生的**频率**，并把它作为相应的**概率**估计。这是一种参数估计法，该方法的重要理论基础之一就是大数定律
***
## 中心极限定理

> 中心极限定理讨论什么条件下，独立随机变量的和的分布函数 $Y=\sum X_i$ 会收敛于正态分布。

### 独立同分布情形

**林德伯格-莱维中心极限定理**：设 $X_1,X_2,...,X_n,...$ 独立同分布，$E(X_i)=\mu,D(X_i)=\sigma^2(\sigma>0)$，则当 $\forall x\in\mathbb{R}$ 时，有：

$$
\begin{aligned}
\lim\limits_{n\rightarrow+\infty}P\Bigg\{\frac{\sum\limits_{i=1}^nX_i-E(\sum\limits_{i=1}^nX_i)}{\sqrt{Var(\sum\limits_{i=1}^nX_i)}}\leq x\Bigg\}&=\lim\limits_{n\rightarrow+\infty}P\Bigg\{\frac{\sum\limits_{i=1}^nX_i-n\mu}{\sigma\sqrt{n}}\leq x\Bigg\}\\
&=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^xe^{-\frac{t^2}{2}}dt=\Phi(x)
\end{aligned}
$$

换句话来说，当 $n$ 足够大时 $\sum\limits_{i=1}^nX_i\stackrel{近似}{～}N(n\mu,n\sigma^2)$，即 $\frac{1}{n}\sum\limits_{i=1}^nX_i\stackrel{近似}{～}N(\mu,\frac{\sigma^2}{n})$，也可以写成：

$$
\frac{\sum\limits_{i=1}^nX_i-n\mu}{\sigma\sqrt{n}}\stackrel{近似}{～}N(0,1)\text{ 或 }\frac{\frac{1}{n}\sum\limits_{i=1}^nX_i-\mu}{\frac{\sigma}{\sqrt{n}}}\stackrel{近似}{～}N(0,1)
$$

!!! note "推论（棣莫弗-拉普拉斯中心极限定理）"

	设 $n_A$ 为 $n$ 重贝努里试验中 $A$ 发生的次数，$P(A)=p(0<p<1)$，则对任何实数 $x$，有：
	
	$$
	\lim\limits_{n\rightarrow+\infty}P\bigg(\frac{n_A-np}{\sqrt{np(1-p)}}\leq x\bigg)=\int_{-\infty}^x\frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}}dt=\Phi(x)
	$$
	
	即当 $n$ 充分大时，$B(n,p)\stackrel{近似}{～}N(np,np(1-p))$
***
