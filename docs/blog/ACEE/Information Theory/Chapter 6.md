---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Chapter 6 : 不等长编码

??? question "为什么需要不等长编码？"

	举一个例子：
	
	假设一个无记忆信源 $\{a_1,a_2,a_3\}$，概率密度为$\{0.5,0.25,0.25\}$，$H(U)=1.5\text{ bit}$
	
	- 如果用等长编码, 则 L 很大时才能达到最佳编码的效率
	- 如果用不等长编码,将 $\{a_1,a_2,a_3\}$ 分别编码成 $\{1,00,01\}$，译码器在收到 1 时，译码成 $a_1$，收到 00 时译码成 $a_2$，01 时译码成 $a_3$，比如：
	- $10001100001101\stackrel{译}{\Rightarrow}1,00,01,1,00,00,1,1,01=a_1a_2a_3a_1a_2a_2a_1a_1a_3$，平均码字长度为 $\overline{n}=\sum\limits_{k=1}^Kp_kn_k=1.5\text{ bit}$

## DMS 的不等长编码

![](../../../assets/Pasted%20image%2020250406110438.png)

一个好的不等长编码应该满足以下条件：

- 唯一可译性
- 即时可译性
***
### 唯一可译性

- 非奇异性：$x_i\neq x_j\Rightarrow C(x_i)\neq C(x_j)$
- 码扩展：$C^*(x_1x_2\cdots x_n)=C(x_1)C(x_2)\cdots C(x_n)$

如果码的任意扩展都是非奇异的, 则称码是唯一可译的

!!! example "Example"

	![](../../../assets/Pasted%20image%2020250406111308.png)
	
	上面的码 A 和码 B 都不是唯一可译的，因为对于 A 来说如果收到 10，可以是 $a_4$，也可以是 $a_3a_2$，也可以是 $a_3a_1$；对于 B 来说如果收到 11，可以是 $a_4$ 也可以是 $a_2a_2$
	
	码 C 和码 D 是唯一可译的
***
#### Sardinas & Petterson 判据

![](../../../assets/Pasted%20image%2020250406111755.png)

判据：一个码是唯一可译码的充分必要条件是除 $S_0$ 外没有任何一个后缀分解集中包含码字

- 如果 $S_1=\phi$ 则该码是即时可译并且唯一可译的
- 如果 $S_n=\phi,n\geq 1$，则该码是唯一可译，且译码延时有限

!!! example "Example"

	![](../../../assets/Pasted%20image%2020250406111806.png)
	
	可以看到，上面的这个码的后缀分解集中包含码字，因此不是唯一可译的
***
#### 异字头码

如果一个码中没有任何一个码字是其它码字的前缀, 则称该码是异字头码, 即 $S_1=\phi$

![](../../../assets/Pasted%20image%2020250406112821.png)

异字头码的树形表示：所有码字只出现在叶结点上
***
#### Kraft 不等式

存在长度为 $n_1,n_2,\cdots,n_K$ 的 D 元异字头码的充要条件为：$\sum\limits_{k=1}^KD^{-n_k}\leq 1$

![](../../../assets/Pasted%20image%2020250406113042.png)

??? note "Proof"

	=== "必要性"
	
		设 $n_1<n_2<\cdots<n_k$，可将异字头码的所有码字放置在码树的叶节点上，每放置一个长为 $n_k$ 的码字，相当于砍掉其下生长的子树的共 $D^{n_K−n_k}$ 个叶节点。为了保证放置过程可行，必须：
		
		$$
		\sum\limits_{n_k=1}^{n_K}D^{n_K-n_k}\leq D^{n_K} \Rightarrow \sum\limits_{n_k=1}^{n_K}D^{-n_k}\leq 1
		$$
		
	
	=== "充分性"
	
		可将所有码字依次放置在码树的叶节点上, 方法如下：
		
		对长为 $n_k$ 的码字在第 $n_k$ 层任选一个可用的叶节点，砍掉其下生长的子树，相当于砍掉第 $n_K$ 叶节点的 $\frac{1}{D_{n_k}}$，如果 $\sum\limits_{n_k=1}^{n_K}D^{−n_k}\leq 1$，则上述放置过程一直可以进行下去，即可以构成一个异字头码

- 任意唯一可译码必然满足 Kraft 不等式，即唯一可译码 $\Rightarrow$ Kraft 不等式成立 $\Rightarrow$ 存在一个同样长度的异字头码

??? note "Proof"

	$$
	\begin{aligned}
	(\sum\limits_{k=1}^KD^{-n_k})^r&=(\sum\limits_{k_1=1}^KD^{-n_{k_1}})(\sum\limits_{k_2=1}^KD^{-n_{k_2}})\cdots(\sum\limits_{k_r=1}^KD^{-n_{k_r}})\\
	&=\sum\limits_{k_1=1}^K\sum\limits_{k_2=1}^K\cdots\sum\limits_{k_r=1}^KD^{-n_{k_1}-n_{k_2}-\cdots-n_{k_r}}\\
	&=\sum\limits_{i=1}^{rn_{\max}}A_iD^{-i}
	\end{aligned}
	$$
	
	由唯一可译性我们有 $A_i\leq D^i$，那么：
	
	$$
	\sum\limits_{k=1}^KD^{-n_k}\leq (\sum\limits_{i=1}^{rn_{\max}}1)^{\frac{1}{r}}\leq (rn_{\max})^{\frac{1}{r}}=2^{\frac{1}{r}\log_2(rn_{\max})}\stackrel{r\rightarrow\infty}{\rightarrow} 1
	$$
	
***
### 不等长编码定理

任何一个唯一可译码的平均码字长度必须满足 $\overline{n}\geq\frac{H(U)}{\log D}$，同时一定存在一个 D 元唯一可译码, 其平均长度满足 $\overline{n}\leq\frac{H(U)}{\log D}+1$

??? note "Proof"

	（1）
	
	$$
	\begin{aligned}
	H(U)-\overline{n}\log D&=-\sum\limits_{k=1}^K(p_k\log p_k+p_kn_k\log D)\\
	&=\sum\limits_{k=1}^Kp_k\log\frac{D^{-n_k}}{p_k}\leq \sum\limits_{k=1}^Kp_k(\frac{D^{-n_k}}{p_k}-1)\\
	&=\sum\limits_{k=1}^KD^{-n_k}-1\leq 0\\
	\end{aligned}
	$$
	
	当且仅当 $D^{-n_k}=p_k$ 时，等式成立
	
	（2）选择唯一的 $n_k$，使得 $D^{-n_k}\leq p_k\leq D^{-(n_k-1)}$
	
	对左边不等式两侧求和，得 $\sum\limits_{k=1}^K D^{-n_k}\leq\sum\limits_{k=1}^K p_k=1$
	
	因此，存在长度为 $n_k$ 的异字头码
	
	对右侧不等式取对数，并求期望值，得：
	
	$$
	\begin{aligned}
	\sum\limits_{k=1}^K p_k\log p_k&<-\sum\limits_{k=1}^K p_k(n_k-1)\log D\\
	\therefore H(U)&>(\overline{n}-1)\log D,\overline{n}<\frac{H(U)}{\log D}+1\\
	\end{aligned}
	$$
	

不等长编码定理也有扩展，对于长为 $L$ 的平稳信源 $U^L$，有：

$$
\begin{aligned}
\frac{H(U^L)}{\log D}&\leq\overline{n}(U^L)\leq\frac{H(U^L)}{\log D}+1\\
\Rightarrow \frac{H(U^L)}{L\log D}&\leq\overline{n}=\frac{\overline{n}(U^L)}{L}\leq\frac{H(U^L)}{L\log D}+\frac{1}{L}\\
\Rightarrow \overline{n}&\stackrel{r\rightarrow\infty}{\rightarrow}\frac{H(U)}{\log D}
\end{aligned}
$$

编码速率：$R\stackrel{\Delta}{=}\overline{n}\log D$，则 $R\stackrel{L\rightarrow\infty}{\rightarrow}H(U)$

编码效率：$\eta=\frac{H(U)}{R}$
***
## Huffman 编码（最佳不等长编码）

最佳不等长编码：给定信源分布，在平均码长最短的意义上最佳

二元最佳码：给定信源分布，其最佳二元编码必然满足：

- 其出现概率越小的消息所对应的码长越长
- 出现概率最小的两个消息所对应的码长相等，且码字最后一位不同

Huffman 编码有如下性质：

- $p_1\geq p_2\geq\cdots\geq p_K\Rightarrow n_1\leq n_2\leq\cdots\leq n_K$

![](../../../assets/Pasted%20image%2020250413102225.png)

- $n_{K-1}=n_K$

![](../../../assets/Pasted%20image%2020250413102252.png)

- 对 $a_{K-1}$ 和 $a_K$，有 $b_{K-1,n_K}\neq b_{K,n_K}$

![](../../../assets/Pasted%20image%2020250413102356.png)
***
### 辅助源

$$
\begin{aligned}
U&～\begin{pmatrix}
a_1&a_2&\cdots&a_{K-1}&a_K\\
p_1&\geq p_2&\cdots&\geq p_{K-1}&\geq p_K
\end{pmatrix}\\
U'&～\begin{pmatrix}
a_1'=a_1&a_2'=a_2&\cdots&a_{K-1}'=a_{K-1}\cup a_K\\
p_1'=p_1&p_2'=p_2&\cdots&p_{K-1}'=p_{K-1}+p_K
\end{pmatrix}
\end{aligned}
$$
***
### 可递归编码原理

对辅助源 $U'$ 的最佳编码也是对原始源的最佳编码

??? note "Proof"

	若 $C_1', C_2',\cdots C_{K−1}'$ 是辅助源的最佳编码，相应码长分别为 $n_1', n_2',\cdots,n_{K−1}'$。对应地，$U$ 的码字 $C_1,C_2,\cdots,C_K$ 的长度分别为：
	
	$$
	n_k=n_k',k=1,2,\cdots,K-2,n_k=n_{K-1}' + 1,k=K-1,K
	$$
	
	所以：
	
	$$
	\overline{n}=\sum\limits_{k=1}^Kp_kn_k=\sum\limits_{k=1}^{K-2}p_kn_k'+(p_{K-1}+p_K)(n_{K-1}' + 1)=\overline{n}' + (p_{K-1}+p_K)
	$$
	
	所以由 $\overline{n}'$ 最小也可得出 $\overline{n}$ 也是最小的
***
### D 元 Huffman 编码

- 若 $K=(D-1)i+1$，则每次均有 $D$ 个消息要合并，短标号得到充分利用
- 若 $K=(D-1)i+M$，则必须增补 $D − M$ 个概率为零的虚拟消息，使得最后一次合并仍有 $D$ 个消息要合并，从而充分利用短标号

![](../../../assets/Pasted%20image%2020250413103521.png)
***
## Shannon 编码

Shannon 编码定义 $a_k$ 的编码长度为：$l_k=\lceil\log\frac{1}{p_k}\rceil, 2^{-l_k}\leq p_k\leq 2^{-l_k+1}$

Shannon 编码方法：

$$
\begin{aligned}
U&～\begin{pmatrix}
a_1&a_2&\cdots&a_{K-1}&a_K\\
p_1&\geq p_2&\cdots&\geq p_{K-1}&\geq p_K
\end{pmatrix}\\
P_k&=\sum\limits_{i=1}^{k-1}p_i\quad P_1=0\\
&=0.\underbrace{c_1c_2\cdots c_{l_k-1}c_{l_k}}_{l_k=\lceil\log\frac{1}{p_k}\rceil\quad 2^{-l_k}\leq p_k<2^{-l_k+1}}c_{l_k+1}\cdots
\end{aligned}
$$

!!! example "Examples"

	=== "Example 01"
	
		![](../../../assets/Pasted%20image%2020250413105359.png)
		
		是一个前缀码，等同于最佳编码（Huffman 编码）
	
	=== "Example 02"
	
		![](../../../assets/Pasted%20image%2020250413110547.png)
		
		- 是一个前缀码，但不等同于最佳编码（Huffman 编码）

根据上面的例子我们可以得到 Shannon 编码是一个前缀码，但不一定等同于最佳编码（Huffman 编码）

!!! note "Shannon 编码是前缀码"

	引理：如果把长度为 $l$ 的二进制码字 $z=z_1z_2\cdots z_l$ 与一个区间 $(0.z_1z_2\cdots z_l,0.z_1z_2\cdots z_l+\frac{1}{2^L}]$ 对应，则一个码是前缀码就等价于这些码字所对应的区间彼此不相交
	
	??? note "Proof"
	
		如果 $\pmb{z}^{(1)}$ 是 $\pmb{z}^{(2)}$ 的前缀，且 $\pmb{z}^{(2)}=z_1z_2\cdots z_l$，则 $\pmb{z}^{(1)}=z_1z_2\cdots z_k,k<l$，$\pmb{z}^{(1)}$ 对应的区间包含 $\pmb{z}^{(2)}$，同样，如果两个区间相交，则必然一个码是另一个码的前缀
		
		![](../../../assets/Pasted%20image%2020250413111142.png)
	
	对于 Shannon 编码来说：
	
	$$
	\begin{aligned}
	[P_{k+1}]_{l_{k+1}}&=[P_k+p_k]_{l_{k+1}}\geq [P_k+\frac{1}{2^{l_k}}]_{l_{k+1}}\\
	&=[P_k]_{l_{k+1}}+\frac{1}{2^{l_k}}\geq [P_k]_{l_k}+\frac{1}{2^{l_k}}\\
	\end{aligned}
	$$
	
	每一个码对应的区间不相交，则 Shannon 编码是前缀码
***
### 编码效率

$$
\begin{aligned}
H(U)&\leq\overline{n}=\sum\limits_{k=1}^Kl_kp_k=\sum\limits_{k=1}^K\lceil\log\frac{1}{p_k}\rceil p_k\\
&\leq\sum\limits_{k=1}^K(\log\frac{1}{p_k}+1)p_k=H(U)+1\\
\end{aligned}
$$

- 与 Huffman 码相比，Shannon 码渐进收敛性能较差

!!! example "Example"

	如果我们有 $p_1=0.9999,p_2=0.0001$
	
	则 $l_1=1\text{ bit},l_2=14\text{ bit}$

- Shannon 码逼近 Shannon 信源编码定理

!!! example "Example"

	如果有两个符号 $p_1,p_2$，序列 $\pmb{u}^{(k)}$ 含有 $k$ 个 1，$n-k$ 个 0，则序列出现的概率为 $p(\pmb{u}^k)=p^k(1-p)^{n-k}$
	
	编码长度为 $l_k=\lceil\log\frac{1}{p(\pmb{u}^k)}\rceil\leq k\log\frac{1}{p}+(n-k)\log\frac{1}{1-p}+1$
	
	平均码长为：
	
	$$
	\begin{aligned}
	\overline{L}&\leq\sum\limits_{k=0}^nC_n^kp^k(1-p)^{n-k}(k\log\frac{1}{p}+(n-k)\log\frac{1}{1-p}+1)\\
	&=\log\frac{1}{p}·(1-p)^n\sum\limits_{k=0}^nC_n^kk(\frac{p}{1-p})^k+\log\frac{1}{1-p}·p^n\sum\limits_{k=0}^nC_n^kk(\frac{1-p}{p})^{n-k}+1\\
	&=n\log\frac{1}{p}·(1-p)^n\frac{p}{1-p}(\frac{p}{1-p}+1)^{n-1}+n\log\frac{1}{1-p}·p^n\frac{1-p}{p}(\frac{1-p}{p}+1)^{n-1}+1\\
	&=nH(U)+1
	\end{aligned}
	$$
	
	其中第二个等号的原理是：
	
	$$
	\begin{aligned}
	\sum\limits_{k=0}^nC_n^kkx^k&=\sum\limits_{k=0}^n\frac{n!}{k!(n-k)!}kx^k=n\sum\limits_{k=0}^n\frac{(n-1)!}{(k-1)!(n-k)!}x^k\\
	&=nx\sum\limits_{k=0}^{n-1}C_{n-1}^{k}x^k=nx(1+x)^{n-1}
	\end{aligned}
	$$
	
***
## Fano 编码

![](../../../assets/Pasted%20image%2020250413113019.png)
***
### 编码效率

![](../../../assets/Pasted%20image%2020250413113124.png)
***
## Shannon-Fano-Elias 编码

- 特点：不需要对概率进行排序

![](../../../assets/Pasted%20image%2020250413113216.png)
***
### 编码效率

$$
\overline{n}=\sum\limits_{x}p(x)l(x)=\sum\limits_{x}p(x)\{\lceil\log\frac{1}{p(x)}\rceil+1\}<H(U)+2
$$

![](../../../assets/Pasted%20image%2020250413113346.png)
***
## 平稳信源的编码

离散有记忆信源：令 $\epsilon$ 为任意小正数，对平稳有记忆信源 $\{u^L,p(u^L)\}$ 进行 $D$ 元不等长编码, 则总可以找到一个 $L(\epsilon)$，当 $L>L(\epsilon)$ 时，平均编码码长 $\overline{n}$ 满足：

$$
\frac{H(U|U^{\infty})}{\log D}\leq\overline{n}<\frac{H(U|U^{\infty})}{\log D}+\epsilon
$$

编码方法：Shannon 码
***
### 马尔科夫信源编码

$$
H_{\infty}(U)=\sum\limits_{s}q(s)H(U|s)=H(U|S)
$$

编码思路：

- 用 $\lceil\log|S|\rceil$ 个比特对初始状态 $S$ 进行编码
- 对状态的输出长度为 $L$ 的消息序列进行不等长编码，当 $L$ 足够大时，平均码长 $\overline{n}$ 满足：

$$
\frac{H(U|U^{\infty})}{\log D}\leq\overline{n}<\frac{H(U|U^{\infty})}{\log D}+\frac{1}{L}
$$

!!! example "Example"

	![](../../../assets/Pasted%20image%2020250413142851.png)

