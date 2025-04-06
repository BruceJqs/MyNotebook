---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 5 : 等长编码

## 信息论的信源问题

### 信源

![](../../../assets/Pasted%20image%2020250330100417.png)

- 信源是产生消息（包括消息序列）的源：图像、声波、符号，DNA序列等等。
***
### 信息论中的信源问题

- 构成描述信源的模型：随机变量序列或随机过程
- 计算信源输出的信息量，或者说信源的熵
- 如何有效地表示信源的输出，即信源编码

信源编码的目标：

- 在代价最小的意义上来最有效地表示一个信源。包括量化、压缩、映射、变换、自然语 言翻译等许多具体和抽象的过程。
	- 代价最小：最少的比特数；即到底用多少个比特可以对一个信源进行编码?

![](../../../assets/Pasted%20image%2020250330100723.png)
***
## 离散无记忆信源（DMS）

![](../../../assets/Pasted%20image%2020250330100805.png)

- $u^L=(u_1,u_2,\cdots,u_L)$：长度为 $L$ 的消息序列
- $x^N=(x_1,x_2,\cdots,x_N)$：长度为 $N$ 的码字
- $\mathcal{C}$：码书、码字的集合（标号的集合）
- $\mathcal{D}$：译码器
***
### 基本概念

一个离散无记忆信源，它的输出字符表为 $\mathcal{A} = \{a_1,a_2,\cdots,a_K\}$，相应的概率分布为 $\{p_1,p_2,\cdots,p_K\}$，满足 $\sum\limits_{i=1}^Kp_i=1$。如果信源输出长度为 $L$ 的消息序列为 $\pmb{u}^L=(u_1,u_2,\cdots,u_K)$，则信源可能输出 $K^L$ 种长度为 $L$ 的不同序列

另一个包含 $D$ 个符号的集合 $\mathcal{B} = \{b_1, b_2, \cdots, b_D\}$，称为编码字符表。现在要用长度为 $N$ 的编码字符序列（称为码字）来表示长度为 $L$ 的信源输出序列。这样的编码称为等长编码（因为所有待编码的消息序列都是等长的，所有码字长度也是一样的）

若这种表示是无损的，也就是说能从码字唯一正确地恢复出信源信息序列，则要求 $D^N\geq K^L\Rightarrow N\geq\frac{L\log K}{\log D}$
***
### 整数编码

- $\mathcal{A}=\{0,1,\cdots,9\},L=1$
	- 编码字符表 $\mathcal{B}=\{0,1\}$，则 $N\geq\log 10,N=4$
- $\mathcal{A}=\{0,1,\cdots,9\},L=2$，或者 $\mathcal{A}=\{0,1,\cdots,99\},L=1$
	- 则 $N\geq\log 100,N=7$，每个字符需要 3.5 个比特
- $\mathcal{A}=\{0,1,\cdots,9\},L=\infty$
	- $N_0=\frac{N}{L}\geq\log 10=3.322$

- 信源输出序列越长，编码效率越高，接近 $\log K$
- 实际实现过程中，编码序列越长，译码时延也越长
***
## 香农编码定理

!!! question "问题"

	码字长度与熵的关系：$N\geq\frac{L\log K}{\log D},H(U)\leq\log K$
	
	有没有可能 $N=\frac{LH(U)}{\log D}$？

香农编码定理：

- 当 $N>\frac{L(H(U)+\epsilon_L)}{\log D}$ 时，可以实现无损编码
- 当 $N<\frac{L(H(U)-\epsilon_L)}{\log D}$ 时，不存在无损编码
- 编码速率：$R=\frac{N}{L}\log D\rightarrow H(U)$
- 无损编码是指信源编码的错误概率可以任意小, 但并非为零
- 通常是对非常长的消息序列进行编码，特别当消息序列长度 $L$ 趋于无穷时，才能实现 Shannon 编码

!!! example "Example"

	例如，$\mathcal{A}=\{0,1,\cdots,9\},L=1$
	
	- 若 $p_0\rightarrow 0.5,p_1\rightarrow 0.5,p_i\rightarrow 0,i>2$，则 $H(A)\rightarrow 1$，每个符号的编码长度 $R\rightarrow 1$
	- 若 $p_0\rightarrow 1,p_i\rightarrow 0,i>1$，则 $H(A)\rightarrow 0$，每个符号的编码长度 $N\rightarrow 1,R\rightarrow 0$
***
### 直观说明

长度为 $L$ 的信源输出序列，个数为 $K^L$ 。当 $L$ 非常大时，根据大数定理，输出序列中符号 $a_i$ 的个数约为 $Lp_i$，具有这样构成成分的序列称为典型列。典型列出现的概率为：

$$
\prod\limits_{i=1}^Kp_i^{Lp_i}=2^{-LH(U)}
$$

典型列的个数：

$$
M=\frac{L!}{Lp_1!(L-Lp_1)!}\cdot\frac{(L-Lp_1)!}{Lp_2!(L-Lp_1-Lp_2)!}\cdots=\frac{L!}{\prod\limits_{i=1}^K(Lp_i)!}
$$

根据斯特林公式：$x!\approx(\frac{x}{e})^x\sqrt{2\pi x}$，有：

$$
\begin{aligned}
\log M&=L(\log L-1)+\frac{1}{2}\log(2\pi L)-\sum\limits_{i=1}^KLp_i(\log L+\log p_i-1)-\sum\limits_{i=1}^K\frac{1}{2}\log(2\pi Lp_i)\\
\frac{\log M}{L}&=H(U)-\frac{1}{2L}((K-1)\log(2\pi L)+\sum\limits_{i=1}^K\log p_i)\\
&\Rightarrow L\rightarrow\infty,M=2^{LH(U)}
\end{aligned}
$$

上面的证明说明：

- 典型列几乎等概
- 当 $L\rightarrow\infty$，输出非典型列的可能性趋于零
- 对于典型列编码，$R=H(U)$
***
### 渐进等分性质

长度为 $L$ 的输出序列 $\pmb{u}^L=(u_1,u_2,\cdots,u_L)$，序列发生的概率 $p(\pmb{u}^L)=\prod\limits_{l=1}^Lp(u_l)$，序列的自信息 $I(\pmb{u}^L)=-\log p(\pmb{u}^L)=\sum\limits_{l=1}^LI(u_l)$

定义随机变量：$I_L\stackrel{\Delta}{=}\frac{I(\pmb{u}^L)}{L}=\sum\limits_{l=1}^L\frac{I(u_l)}{L}$，则有：

$$
\begin{aligned}
E(I_L)&=E\{\frac{1}{L}\sum\limits_{l=1}^LI(u_l)\}=E(I(U))=H(U)\\
D(I_L)&=D\{\frac{1}{L}\sum\limits_{l=1}^LI(u_l)\}=\frac{1}{L^2}\sum\limits_{l=1}^LD(I(u^L))=\frac{1}{L}D(I(U))\stackrel{\Delta}{=}\frac{\sigma_1^2}{L}\\
\end{aligned}
$$

由切比雪夫不等式，对任意随机变量 $\xi$ 和 $\epsilon$：

$$
P\{|\xi-E(\xi)|>\epsilon\}\leq \frac{Var(\xi)}{\epsilon^2}
$$

则有：

$$
P\{|I_L-H(U)|>\epsilon\}\leq \frac{\sigma_1^2}{L\epsilon^2}
$$

给定 $\epsilon$，当 L 充分大时，$\frac{\sigma_1^2}{L\epsilon^2}\leq\epsilon$，所以有 $P\{|I_L-H(U)|>\epsilon\}\leq\epsilon$ 或 $P\{|I_L-H(U)|<\epsilon\}\geq 1-\epsilon$
***
### 典型列

令 $H(U)$ 为一个离散无记忆信源 $\text{DMS}\{U,p(·)\}$ 的熵，$\epsilon$ 为任意正数

$$
A_{\epsilon}^{(L)}(U)=\{\pmb{u}^L:|-\frac{1}{L}\log p(\pmb{u}^L)-H(U)|<\epsilon\}
$$

为给定 DMS 输出长度为 L 的 $\epsilon$ 典型列集合，简称典型列集，其中 $\pmb{u}^L\in U^L$

典型列性质：

- 当 L 足够大时：

$$
\begin{aligned}
Pr(\pmb{u}^L\in A_{\epsilon}^{(L)}(U))&\geq 1-\epsilon\\
Pr(A_{\epsilon}^{(L)}(U)) &= \sum\limits_{\pmb{u}^L\in A_{\epsilon}^{(L)}(U)}p(\pmb{u}^L)=\sum\limits_{\pmb{u}^L\in U^L}p(\pmb{u}^L)I(\pmb{u}^L\in A_{\epsilon}^{(L)}(U))\\
&=E\{I(\pmb{u}^L\in A_{\epsilon}^{(L)}(U))\}=Pr(\pmb{u}^L\in A_{\epsilon}^{(L)}(U))>1-\epsilon\\
\end{aligned}
$$

- 如果 $\pmb{u}^L\in A_{\epsilon}^{(L)}(U)$，则有 $2^{-L(H(U)+\epsilon)}\leq p(\pmb{u}^L)\leq 2^{-L(H(U)-\epsilon)}$
- $(1-\epsilon)2^{L(H(U)-\epsilon)}\leq |A_{\epsilon}^{(L)}(U)|\leq (1+\epsilon)2^{L(H(U)+\epsilon)}$

??? note "Proof"

	$$
	\begin{aligned}
	1&=\sum\limits_{\pmb{u}^L\in U^L}p(\pmb{u}^L)\geq \sum\limits_{\pmb{u}^L\in A_{\epsilon}^{(L)}(U)}p(\pmb{u}^L)\\
	&\geq \sum\limits_{\pmb{u}^L\in A_{\epsilon}^{(L)}(U)}2^{-L(H(U)+\epsilon)}=|A_{\epsilon}^{(L)}(U)|2^{-L(H(U)+\epsilon)}\\
	&\therefore |A_{\epsilon}^{(L)}(U)|\leq 2^{L(H(U)+\epsilon)}\\
	1-\epsilon&\leq \sum\limits_{\pmb{u}^L\in A_{\epsilon}^{(L)}(U)}p(\pmb{u}^L)\\
	&\leq \sum\limits_{\pmb{u}^L\in A_{\epsilon}^{(L)}(U)}2^{-L(H(U)-\epsilon)}=|A_{\epsilon}^{(L)}(U)|2^{-L(H(U)-\epsilon)}\\
	&\therefore |A_{\epsilon}^{(L)}(U)|\geq (1-\epsilon)2^{L(H(U)-\epsilon)}\\
	\end{aligned}
	$$
	

离散无记忆源的输出序列分为两类：

- $A_{\epsilon}^{(L)}(U)$：典型列集合，高概率集
- $\overline{A_{\epsilon}^{(L)}(U)}$：非典型列集合，低概率集

!!! tip "Tips"

	- 个别非典型列出现的概率不一定比典型列出现概率小
		- e.g. $p_0 = p > 0.5, p_1 = 1 − p < 0.5$ 全 0 序列的自信息为 $−L\log p\neq H(U)$，因此不是典型列，但是全 0 序列出现的概率为 $p^L > p^{Lp}(1 − p)^{L(1−P)}$；全 1 序列也不是典型列，但是全 1 序列出现的概率小于典型列出现概率
	- 非典型列的数目不一定比典型列的数目小
		- e.g. $p=0.25,H(U)=0.81$，当 $L=100$ 时，$|A_{\epsilon}^{(L)}(U)|=2^{81}$，仅占所有序列的 $2^{-19}$
***
### 香农编码定理证明

由于典型列的个数 $|A_{\epsilon}^{(L)}(U)|\leq 2^{L(H(U)+\epsilon)}$，所以当 $N\geq\frac{L(H(U)+\epsilon)}{\log D}$ 时，可以对所有的典型列进行编码，而对所有的非典型列用统一的一个序列(比如全 D 序列)编码, 当接收端收到全 D 序列时，声称译码错误

$$
p_e=p\{\pmb{\hat{u}}^L\neq\pmb{u}^L\}=p\{\pmb{u}^L\not\in A_{\epsilon}^{(L)}(U)\}<\epsilon
$$

香农编码定理的逆定理：

当 $N<\frac{L(H(U)-\epsilon)}{\log D}$ 时，记 $D^N=2^{L(H(U)-\epsilon-\epsilon_1)}$，则每个典型列找到编码序列的概率为:

$$
\frac{D^N}{A_{\epsilon}^{(L)}(U)}\leq\frac{2^{L(H(U)-\epsilon-\epsilon_1)}}{(1-\epsilon)2^{L(H(U)-\epsilon)}}=\frac{2^{-L\epsilon_1}}{(1-\epsilon)}\stackrel{L\rightarrow\infty}{\rightarrow}0
$$


