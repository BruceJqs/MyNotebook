---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
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
### 证明思想

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
#### 证明

码书矩阵:

$$
\begin{bmatrix}
x_1(1) & x_2(1) & \dots & x_n(1) \\
x_1(2) & x_2(2) & \dots & x_n(2) \\
\vdots & \vdots & \ddots & \vdots \\
x_1(2^{nR}) & x_2(2^{nR}) & \dots & x_n(2^{nR})
\end{bmatrix}
$$

码书随机产生，均匀分布

译码方法: 如果接收到的 $y^n$ 与某个码字 $x^n(\hat{w})$ 是联合典型的，即 $(x^n(\hat{w}), y^n) \in A_\epsilon^{(n)}$，就宣称发送的是第 $\hat{w}$ 个码字

译码错误: 

1. 译码错误事件: $\hat{w} \ne w$
2. 不可译事件: 不存在任何 $x^n(\hat{w})$，使 $(x^n(\hat{w}), y^n) \in A_\epsilon^{(n)}$

$$
\begin{aligned}
P(E) &= \sum_{\mathcal{L}} P(\mathcal{L}) P_e^n(\mathcal{L})\\
P_e^n(\mathcal{L}) &= \frac{1}{2^{nR}} \sum_{w=1}^{2^{nR}} \lambda_w(\mathcal{L})\\
P(E) &= \frac{1}{2^{nR}} \sum_{w=1}^{2^{nR}} \sum_{\mathcal{L}} P(\mathcal{L}) \lambda_w(\mathcal{L})\\
&= \sum_{\mathcal{L}} P(\mathcal{L}) \lambda_1(\mathcal{L}) \triangleq P(E|w=1)
\end{aligned}
$$

$P(E|w=1) = P\{\bar{E}_1 \cup E_2 \cup \dots \cup E_{2^{nR}}\} = P(\bar{E}_1) + \sum\limits_{i=2}^{2^{nR}} E_i$

1) 根据联合典型性质： $P(\overline{E_1}) \le \epsilon$
2) 由于 $x^n(i)$ 与 $x^n(1)$ 独立无关，意味着 $y^n$ 与 $x^n(i)$ 独立，因此，$P(E_i) \le 2^{-n(I(X;Y)-3\epsilon)}$

$P(E|w = 1) \le \epsilon + 2^{-n(I(X;Y)-R-3\epsilon)}$

当 $R < I(X;Y) - 3\epsilon$ 时，对于充分大的 $n$，有 $P(E|w = 1) \le 2\epsilon$

!!! note "逆定理证明"

	逆定理：具有 $\lambda^{(n)} \to 0$ 的任何 $(2^{nR}, n)$ 码必有 $R \le C$
	
	$$
	\begin{aligned}
	nR = H(W) &= H(W|\hat{W}) + I(W;\hat{W})\\
	&\le H(W|\hat{W}) + I(X^n;Y^n) \to \text{数据处理定理}\\
	&\le H(P_e^{(n)}) + P_e^{(n)} \cdot nR + I(X^n;Y^n) \to \text{Fano不等式}\\
	&\le 1 + P_e^{(n)} \cdot nR + nC\\
	R &\le P_e^{(n)}R + \frac{1}{n} + C
	\end{aligned}
	$$
	
	$P_e^{(n)} \ge 1 - \frac{C}{R} - \frac{1}{nR}$, 当 $R > C$, 则 $P_e^{(n)}$ 一定大于 0!
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
## 具有理想反馈的 DMC 的容量

![](../../../assets/Pasted%20image%2020250525101907.png)

- 反馈不能增加离散无记忆信道的容量，即 $C_{FB}=C=\max\limits_{p(x)}I(X;Y)$

!!! note "证明"

	显然 $C_{FB} \ge C$
	
	$$
	\begin{aligned}
	nR = H(W) &= H(W|Y^n) + I(W;Y^n)\\
	&\le H(W|\hat{W}) + I(W;Y^n)\\
	&\le 1 + P_e^{(n)} \cdot nR + I(W;Y^n)\\
	I(W;Y^n) &= H(Y^n) - H(Y^n|W)\\
	&= H(Y^n) - \sum_{i=1}^n H(Y_i|Y^{i-1}, W)\\
	&= H(Y^n) - \sum_{i=1}^n H(Y_i|Y^{i-1}, W, X_i)\\
	&= H(Y^n) - \sum_{i=1}^n H(Y_i|X_i) \le nC \implies C_{FB} \le C
	\end{aligned}
	$$
	

- 反馈不能提高离散无记忆信道的容量，但对于离散有记忆信道来说，反馈可以增加信道容量
- 虽然反馈不能提高 DMC 的容量，但是利用反馈可以较简单地实现性能好的编码，比如可以用码长较短的信道编码就可以达到很低的误码率
***
## 信源信道分离编码和联合编码

![](../../../assets/Pasted%20image%2020250525103403.png)

- 信源、信道分离编码：$H(W)<R_s<R_c<C\Rightarrow P_e^{(n)}\rightarrow 0$
- 信源、信道联合编码：在有限集上取值的信源 $\mathcal{V}$ 的熵速率为 $H(\mathcal{V})$，若 $H(\mathcal{V})<C$，则存在一个信源信道联合编码，使得 $P_e^{(n)}\rightarrow 0$；反之，若 $H(\mathcal{V})>C$，则不可能以任意小的错误概率传送信源

!!! note "信源信道联合编码定理的证明"

	=== "正定理"
	
		$H(\mathcal{V})<C\Rightarrow\exists\epsilon,H(\mathcal{V})+\epsilon<C$
		
		该源的典型列集合 $|A_{\epsilon}^{(n)}|<2^{n(H(\mathcal)+\epsilon)}<2^{nC}$
		
		所以可用不大于 $2^{nC}$ 个不同的码字表达典型列集合
		
		此时编码速率小于信道容量，故该码率可达
		
		对非典型列不予编码，由此引起的差错不多于 $\epsilon$
	
	=== "逆定理"
	
		反之，设信源信道联合编码为 $V^n\rightarrow X^n\rightarrow Y^n\rightarrow\hat{V}^n$
		
		则 $H(V^n|\hat{V}^n)\leq 1+p_e^{(n)}\log|\mathcal{V}^n|=1+np_e^{(n)}\log|\mathcal{V}|$
		
		$$
		\begin{aligned}
		H(\mathcal{V})&\leq\frac{H(V_1V_2\cdots V_n)}{n}=\frac{H(V^n)}{n}=\frac{1}{n}H(V^n|\hat{V}^n)+\frac{1}{n}I(V^n;\hat{V}^n)\\
		&\leq\frac{1}{n}(1+np_e^{(n)}\log|\mathcal{V}|)+\frac{1}{n}I(X^n;Y^n)\\
		&\leq\frac{1}{n}+p_e^{(n)}\log|\mathcal{V}|+C
		\end{aligned}
		$$
		
		若要求 $P_e^{(n)}\rightarrow 0$，则 $H(\mathcal{V})<C$

- 只要 $H < C$，总可以找到可行的信源信道联合编码；也可以分别构造最优的信源编码和信道编码，使信息传输可达
- 信源信道联合编码不能使得可行速率极限增加，但可以简化编码







