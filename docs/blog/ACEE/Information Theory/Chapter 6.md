---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
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
	&=-\sum\limits_{k=1}^Kp_k\log\frac{D^{-n_k}}{p_k}\leq -\sum\limits_{k=1}^Kp_k(\frac{D^{-n_k}}{p_k}-1)\\
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
	
