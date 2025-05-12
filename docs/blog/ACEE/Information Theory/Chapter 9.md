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
## 离散无记忆信道的编码

![](../../../assets/Pasted%20image%2020250510105103.png)

$W=\{1,2,\cdots,M\}$

编码速率（传信率）：$R=\frac{\log M}{n}$

香农信道编码定理：如果信息传输速率 $R$ 小于信道容量 $C$，则总存在一种编码方法，使信息在该信道上无错误地可靠传输

所有低于信道容量 $C$ 的速率 $R$ 均是可达的，即当 $R<C$ 时，总存在一系列码 $(2^{nR},n)$，当 $n\rightarrow\infty$ 时，最大误码概率 $\lambda^{(n)}\rightarrow 0$，即可以任意小

逆定理：具有 $\lambda^{(n)}\rightarrow 0$ 的任何 $(2^{nR},n)$ 码必有 $R\leq C$

码率可达区 $\Leftrightarrow$ 容量区內界，容量区內界如果与容量区外界相等，则为容量区
***
### 直观说明

![](../../../assets/Pasted%20image%2020250510175452.png)

$M\approx\frac{2^{nH(Y)}}{2^{nH(Y|X)}}=2^{nI(X;Y)},R=\frac{\log M}{n}\approx I(X;Y)\leq C$
***
### 基本定义

- 离散无记忆信道 $\{\mathcal{X},p(y|x),\mathcal{Y}\}$ 上的一个 $(M,n)$ 码由如下组成：
	1. 一个与 $M$ 个消息相对应的标号集合 $W=\{1,2,\cdots,M\}$
	2. 一个编码器，把消息 $w\in\mathcal{W}$ 映射成码字 $x^n\in\mathcal{X}^n$，所得到的码字为 $X^n(1),X^n(2),\cdots,X^n(M)$；一个码的全体码字构成码书
	3. 一个译码器 $g_1:\mathcal{Y}^n\rightarrow\mathcal{W}$：对应于确定的译码法则， 帮助接收者根据接收到的序列 $Y_n$ 来确定发送消息是什么
- 发送第 $i$ 个消息所发生的错误概率定义为 $\lambda_i=P\{g(Y^n)\neq i|X^n=x^n(i)\}$，最大错误概率定义为 $\lambda^{(n)}=\max\limits_{i\in\{1,2,\cdots,M\}}\lambda_i$，平均错误概率定义为 $P_e^{(n)}=\frac{1}{M}\sum\limits_{i=1}^M\lambda_i$，编码速率定义为 $R=\frac{\log M}{n}$ 比特/传输
- 如果存在一系列 $(2^{nR},n)$ 码，当 $n\rightarrow\infty$ 时，最大错误概率 $\lambda^{(n)}\rightarrow 0$，则称 $R$ 是可达的
***
### 证明

证明思想：

1. 所谓可靠通信是指错误概率可以任意小，但并非为零
2. 信道上不是仅传输一个符号，而是传输一串很长的符号序列。由于多次使用信道，可以利用概率论中的大数定理
3. 计算在一类随机选择的码书上的平均错误概率，平均错误概率与最大错误概率具有一样的意义

如果 $(2^{nR},n)$ 码的平均错误概率 $\lambda^{(n)}<\epsilon$，则至少有一半的码字其最大错误概率小于 $2\epsilon$，意味着 $(2^{nR}−1, n)$ 码的最大错误概率 $\lambda(n)<2\epsilon\rightarrow 0$，则码率 $\frac{nR-1}{n}=R-\frac{1}{n}$ 是可达的
***
#### 联合典型列

相对于联合分布 $p(x,y)$ 的联合典型列集合 $A_{\epsilon}^{(n)}$ 是指具有下列性质的序列对 $(x^n,y^n)$ 的集合：

$$
\begin{aligned}
A_{\epsilon}^{(n)}=\{(x^n,y^n)\in\mathcal{X}^n\times\mathcal{Y}^n:\\
\big|-\frac{1}{n}\log p(x^n)-H(X)\big|<\epsilon\\
\big|-\frac{1}{n}\log p(y^n)-H(Y)\big|<\epsilon\\
\big|-\frac{1}{n}\log p(x^n,y^n)-H(XY)\big|<\epsilon\}
\end{aligned}
$$

设 $A_{\epsilon}^{(n)}$ 是与 $p(x,y)$ 对应的联合典型列集合，若联合序列 $(X^n,Y^n)$ 的每一个符号对 $(x_i,y_i)$ 均是 按照联合分布 $p(x,y)$ 独立选取，即 $(X^n,Y^n)∼p(x^n,y^n)$，则：

- $Pr((X^n,Y^n)\in A_{\epsilon}^{(n)})\rightarrow 1$
- $(1-\epsilon)2^{n(H(XY)-\epsilon)}\leq\big|A_{\epsilon}^{(n)}\big|\leq 2^{n(H(XY)+\epsilon)}$
- 随机选择 $y^n$，约有 $2^{-nI(X;Y)}$ 的概率与 $x^n$ 构成联合典型
- 如果联合序列 $(\tilde{Y^n},\tilde{Y^n})∼p(x^n)p(y^n)$，即 $\tilde{X^n}$ 和 $\tilde{Y^n}$ 分别按照 $p(x,y)$ 的边缘分布 $p(x)$ 和 $p(y)$ 来独立选取，则 $(1-\epsilon)2^{-n(I(X;Y)+3\epsilon)}\leq Pr\big((\tilde{X^n},\tilde{Y^n})\big)\leq 2^{-n(I(X;Y)-3\epsilon)}$

??? note "Proof"

	$(\tilde{Y^n},\tilde{Y^n})$ 与 $(X^n,Y^n)$ 有相同的边缘分布 $p(x^n)$ 和 $p(y^n)$，故：
	
	$$
	\begin{aligned}
	Pr\big((\tilde{X^n},\tilde{Y^n})\in A_{\epsilon}^{(n)}\big)&=\sum\limits_{A_{\epsilon}^{(n)}}p(x^n)p(y^n)\\
	&\leq|A_{\epsilon}^{(n)}|2^{-n(H(X)-\epsilon)}2^{-n(H(Y)-\epsilon)}\\
	&\leq2^{n(H(XY)+\epsilon)}2^{-n(H(X)-\epsilon)}2^{-n(H(Y)-\epsilon)}\\
	&=2^{-n(I(X;Y)-3\epsilon)}\\
	Pr\big((\tilde{X^n},\tilde{Y^n})\in A_{\epsilon}^{(n)}\big)&=\sum\limits_{A_{\epsilon}^{(n)}}p(x^n)p(y^n)\\
	&\geq |A_{\epsilon}^{(n)}|2^{-n(H(X)+\epsilon)}2^{-n(H(Y)+\epsilon)}\\
	&\geq(1-\epsilon)2^{n(H(XY)-\epsilon)}2^{-n(H(X)-\epsilon)}2^{-n(H(Y)-\epsilon)}\\
	&=(1-\epsilon)2^{-n(I(X;Y)+3\epsilon)}\\
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

码书矩阵：

$$
\begin{bmatrix}
x_1(1) & x_2(1) & \cdots & x_n(1)\\
x_1(2) & x_2(2) & \cdots & x_n(2)\\
\vdots & \vdots & \ddots & \vdots\\
x_1(2^{nR}) & x_2(2^{nR}) & \cdots & x_n(2^{nR})
\end{bmatrix}
$$

译码方法：如果接收到的 $y^n$ 与某个码字 $x_n(i)$ 的 Hamming 距离小于 $r=n(p+\epsilon_2)$ 时，就宣称发送的是第 $i$ 个码字，其中$\epsilon_2$ 是任意小数，且满足 $p+\epsilon_2<0.5$

译码错误：$y^n$ 与 $x^n(i)$ 的 Hamming 距离大于 $r=n(p+\epsilon_2)$，或者 $y^n$ 与其它 $x^n(j)$ 的 Hamming 距离小于 $r=n(p+\epsilon_2)$

$$
\begin{aligned}
P(E)&=\sum\limits_{\mathcal{L}}P(\mathcal{L})P_e^n(\mathcal{L})\\
P_e^n(\mathcal{L})&=\frac{1}{2^{nR}}\sum\limits_{i=1}^{2^{nR}}\lambda_i(\mathcal{L})\\
\therefore P(E)&=\frac{1}{2^{nR}}\sum\limits_{i=1}^{2^{nR}}\sum\limits_{\mathcal{L}}P(\mathcal{L})\lambda_i(\mathcal{L})\\
&=\sum\limits_{\mathcal{L}}P(\mathcal{L})\lambda_1(\mathcal{L})\stackrel{\Delta}{=}P(E|i=1)
\end{aligned}
$$

$P(E|i=1)=P\{\overline{E_1}\cup E_2\cup\cdots\cup E_{2^{nR}}\}=P(\overline{E_1})+\sum\limits_{i=2}^{2^{nR}}E_i$

- 不妨令 $i=1$ 为全 0 序列，则 $P(\overline{E_1})$ 表示输出序列中 $1$ 的个数超过 $np$ 的概率，根据切比雪夫不等式，该概率可以任意小，即 $P(\overline{E_1})<\frac{\epsilon}{2}$
- 发送其它序列时，输出序列有 $2^n$ 个，但只有 $\sum\limits_{t=0}^r C_n^t$ 个落在半径为 $r$ 的 Hamming 球内
	
	$$
	\begin{aligned}
	P(E_1)&<\frac{\epsilon}{2}+(2^{nR}-1)\frac{1}{2^n}\sum\limits_{t=0}^rC_n^t\\
	&=\frac{\epsilon}{2}+(2^{nR}-1)\frac{1}{2^n}\sum\limits_{t=0}^{n\lambda}C_n^t,\lambda<\frac{1}{2}\\
	&=\frac{\epsilon}{2}+2^{nR}2^{-n[1-H(\lambda)]}=\frac{\epsilon}{2}+2^{n(R-C)}\\
	r&=n\lambda=n(p+\epsilon_2)\\
	1&\geq\sum\limits_{t=0}^{n\lambda}C_n^t\lambda^t(1-\lambda)^{n-t}\geq\sum\limits_{t=0}^{n\lambda}C_n^t\lambda^{n\lambda}(1-\lambda)^{n-n\lambda}=\sum\limits_{t=0}^{n\lambda}C_n^t2^{-nH(\lambda)}
	\end{aligned}
	$$
	
***



