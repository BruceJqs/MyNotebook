---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Chapter 4 : 平稳离散信源的熵

## 平稳随机过程

定义：对于任意的 $n$，任意的 $t_1,t_2,...,t_n\in T$ 和 $h$，若 $(X(t_1),X(t_2),...,X(t_n))$ 与 $(X(t_1+h),X(t_2+h),...,X(t_n+h))$ 具有同样的分布，则称随机过程 $\{X(t)\}$ 是平稳随机过程

性质：

- $E(X(t_n))=E(X(t_n+h))=E(X(0))=\text{const}$
- $X(t)$ 的均值和方差对于所有 $t$ 都一样
***
## 平稳信源

定义：如果有 $...,X_{-1},X_0,X_1,...,X_n,...$，且任意长度的片段的联合概率分布与时间起点无关，即 $\text{Pr}(X_1X_2...X_L)=\text{Pr}(X_{1+n}X_{2+n}...X_{L+n})$，则称信源是平稳信源

- 简单无记忆信源：不同时间的随机变量不相关，即 $\text{Pr}(X_1X_2...X_L)=\prod_{i=1}^L\text{Pr}(X_i)$
- $m$ 阶马尔科夫信源（当 $m=1$ 时称为马尔科夫信源）：$\text{Pr}(X_l|X_{l-1}X_{l-2}...X_0)=\text{Pr}(X_l|X_{l-1}X_{l-2}...X_{l-m})$
	- 说明当前状态只与前 $m$ 个状态有关
***
### 平稳信源的熵

如果一个平稳信源发出长度为 $n$ 的序列 $X_1X_2...X_n$，令 $n$ 维矢量 $\pmb{X}=\{X_1,X_2,...,X_n\}$，则 $H(\pmb{X})=H(X_1,X_2,...X_n)=-\sum p(x_1,x_2,...,x_n)\log p(x_1,x_2,...,x_n)$，$H(\pmb{X})$ 随 $n$ 增长而增长，趋向无穷大

- 平均每符号熵：$H_N(\pmb{X})\stackrel{\Delta}{=} \frac{1}{N}H(\pmb{X})=\frac{1}{N}H(X_1X_2...X_N)$
- 熵速率：$H_{\infty}(\pmb{X})=\lim\limits_{N\rightarrow\infty}H_N(\pmb{X})$
- 平均条件熵：$H(X_N|X_{N-1}X_{N-2}...X_1)$

性质：

- $H(X_N|X_{N-1}X_{N-2}...X_1)$ 随 $N$ 的增大而单调不增

??? note "Proof"

	利用 $H(X|Y)\leq H(X)$
	
	$$
	\begin{aligned}
	H(X_N|X_{1},X_{2},...,X_{N-1})&\leq H(X_N|X_{2},...,X_{N-1})\\
	&\leq H(X_{N-1}|X_{1},X_{2},...,X_{N-2})\\
	\end{aligned}
	$$
	

- $H_N(\pmb{X})$ 随 $N$ 的增大也单调不增

??? note "Proof"

	$$
	\begin{aligned}
	H_N(\pmb{X})&=\frac{1}{N}\{H(X_1,X_2,...X_{N-1})+H(X_N|X_1,X_2,...X_{N-1})\}\\
	&=\frac{1}{N}\{(N-1)H_{N-1}(\pmb{X})+H(X_N|X_1,X_2,...X_{N-1})\}\\
	&\leq\frac{1}{N}\{(N-1)H_{N-1}(\pmb{X})+H_N(\pmb{X})\}\\
	&\therefore H_N(\pmb{X})\leq H_{N-1}(\pmb{X})\\
	\end{aligned}
	$$
	

- $H_N(\pmb{X})\geq H(X_N|X_{N-1}X_{N-2}...X_1)$

??? note "Proof"

	$$
	\begin{aligned}
	H_N(\pmb{X})&=\frac{1}{N}H(X_1,X_2,...X_N)\\
	&=\frac{1}{N}\{H(X_1)+H(X_2|X_1)+...+H(X_N|X_{1},X_{2},...,X_{N-1})\}\\
	&\geq H(X_N|X_{1},X_{2},...,X_{N-1})\\
	\end{aligned}
	$$
	


- $H_{\infty}(\pmb{X})=\lim\limits_{N\rightarrow\infty}H_N(\pmb{X})=\lim\limits_{N\rightarrow\infty}H(X_N|X_{N-1}X_{N-2}...X_1)$

??? note "Proof"

	$$
	\begin{aligned}
	(N+K)H_{N+K}(\pmb{X})&=H(X_{N+K}X_{N+K-1}...X_2X_1)\\
	&=H(X_{N-1}X_{N-2}...X_2X_1)+H(X_{N}|X_{N-1}X_{N-2}...X_2X_1)\\
	&+...+H(X_{N+K}|X_{N+K-1}X_{N+K-2}...X_2X_1)\\
	&\leq H(X_{N-1}X_{N-2}...X_1)+(K+1)H(X_N|X_{N-1}X_{N-2}...X_1)\\
	\end{aligned}
	$$
	
	所以我们有 $H_{N+K}(\pmb{X})\leq\frac{1}{N+K}H(X_{N-1}X_{N-2}...X_1)+\frac{K+1}{N+K}H(X_N|X_{N-1}X_{N-2}...X_1)$
	
	令 $K\rightarrow\infty$，则 $H_{\infty}(\pmb{X})\leq H(X_N|X_{N-1}X_{N-2}...X_1)\leq H_N(\pmb{X})$
	
	再令 $N\rightarrow\infty$，则 $H_{\infty}(\pmb{X})\leq\lim\limits_{N\rightarrow\infty}H(X_N|X_{N-1}X_{N-2}...X_1)\leq H_{\infty}(\pmb{X})$
	
	即 $H_{\infty}(\pmb{X})=\lim\limits_{N\rightarrow\infty}H_N(\pmb{X})=\lim\limits_{N\rightarrow\infty}H(X_N|X_{N-1}X_{N-2}...X_1)$
***
## 熵速率（熵率）

> 对无记忆离散源，若 $X$ 在取值范围 $\mathcal{X}=\set{x_1,x_2,\cdots,x_K}$ 上等概分布，则 $H(X)=\log K\stackrel{\Delta}{=}H_0$

- 熵速率：

$$
\begin{aligned}
H_{\infty}(\pmb{X})&=\lim\limits_{N\rightarrow\infty}H_N(\pmb{X})=\lim\limits_{N\rightarrow\infty}H(X_N|X_{N-1}X_{N-2}...X_1)\\
H_{\infty}(\pmb{X})&\leq H(X_N|X_{N-1}X_{N-2}...X_1)\leq ...\leq H(X_2|X_1)\leq H(X_2)\leq\log K\\
\end{aligned}
$$

- 熵的相对率：$\eta=\frac{H_{\infty}(\pmb{X})}{\log K},\eta\leq 1$
- 信源的冗余度：$R=1-\eta$
***
## 马尔科夫信源

> 对于 $m$ 阶马尔科夫信源，$x_{i_{n}}$ 是 $n$ 时刻信源输出符号，$s_{i_{n}}$ 是 $n$ 时刻信源状态。每一个状态 $s_{i}$ 对应一个长度为 $m$ 的符号序列

- 马尔科夫信源的状态空间：$x^m=x_{i_{l-1}}x_{i_{l-2}}...x_{i_{l-m}}\in\mathcal{X}^m,|\mathcal{X}^m|=K^m$
- 马尔科夫信源的优点：
	- 状态空间有限
	- 由状态转移函数确定：$s_{i_{n+1}}=F(s_{i_n},x_{i_n})$

![](../../../assets/Pasted%20image%2020250323110811.png)

- $s_i=\pmb{x_i}=x_{i_1}x_{i_2}...x_{i_m}\in\mathcal{X}^m,s_j=\pmb{x_j}=x_kx_{i_1}x_{i_2}...x_{i_{m-1}}\in\mathcal{X}^m$
- $p_{ij}(n)=\text{Pr}(X_n=x_k|X_{n-1}X_{n-2}...X_{n-m}=x_{i_1}x_{i_2}...x_{i_m})=\text{Pr}(S_n=s_j|S_{n-1}=s_i)$
	-  $p_{ij}(n)$ 是 $n$ 时刻状态 $s_{i}$ 转移到 $s_{j}$ 的概率
***
### 时齐既约马尔科夫源的稳态状态分布

- 时齐（时不变）马尔科夫源：状态转移概率 $p_{ij}(n)$ 与时间 $n$ 无关
- 既约（不可约）马尔科夫源：从任意状态 $s_i$ 出发，经过有限步总可以转移到任意其他状态
- 状态转移概率矩阵：$P=[p_{ij}]_{K^m\times K^m}$
- $n$ 时刻的状态概率分布：$Q(n)=(q_1(n),q_2(n),...,q_{K^m}(n))$，其中 $q_i(n)=\text{Pr}(S_n=s_i)$
- 对于时齐既约马尔可夫源，状态的稳态分布存在：
	- $\overline{Q}=\lim\limits_{n\rightarrow\infty}Q(n+1)=\lim\limits_{n\rightarrow\infty}Q(n)P=\overline{Q}P$
- 对于既约的马尔可夫信源，存在一个唯一的平稳分布 $Q$，使得 $Q=P^{T}Q$
***
### 马尔可夫源的熵率

> 马尔可夫信源的熵率等于信源在各状态下的条件熵对状态概率求平均

$$
\begin{aligned}
H_{\infty}&=\lim\limits_{N\rightarrow\infty}\frac{1}{N}H(X_1,X_2,..,X_N)\\
&=\lim\limits_{N\rightarrow\infty}H(X_N|X_{N-1},X_{N-2},...,X_1)\\
&=\lim\limits_{N\rightarrow\infty}H(X_N|X_{N-1},X_{N-2},...,X_{N-m})\\
&=H(X_{m+1}|X_{m},X_{m-1},...,X_1)\\
&=\sum\limits_{i=1}^{K^m}q(S=s_i)H(X|S=s_i)=H(X|S)
\end{aligned}
$$