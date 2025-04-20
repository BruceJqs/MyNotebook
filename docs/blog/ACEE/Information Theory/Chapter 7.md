---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 7 : 信道模型

!!! abstract "Introduction"

	研究信道容量对于通信有及其重要的意义：
	
	- 通信的数学理论：功率和带宽等通信资源的效用极限
	- 随机编码、联合译码、注水法则等重要思想
	- 具体通信体制（CDMA/OFDM/MIMO）的理论基础
	
	信息论中的信道模型是对实际物理信道的一个数学抽象，实际物理信道：噪声信道、干扰信道、无线衰落信道、存储信道等等。实际物理信道类型很多，建立信道的数学模型非常重要
***
## 信道的抽象数学模型

信道传输过程可以抽象为输入量（随机过程）$X$ 经过输入/输出统计关系（信道）变为输出量（随机过程）$Y$ 的过程，即 $\{\mathcal{X};p(y|x);\mathcal{Y}\}$

![](../../../assets/Pasted%20image%2020250420102021.png)


- 离散无记忆信道：$p_N(y^N|x^N)=\prod_{n=1}^Np(y_n|x_n),\forall N$
- 平稳信道：$p(y_n=j|x_n=k)=p(y_m=j|x_m=k),\forall m,n$
***
## 信道的分类

- 按输入/输出信道在幅度和时间上取值
	- 幅度离散，时间离散信道
	- 幅度连续，时间离散信道
	- 幅度连续，时间连续信道
	- 幅度离散，时间连续信道
- 按输入/输出之间的记忆性
	- 有记忆信道
	- 无记忆信道
- 按输入/输出之间关系的确定性
	- 确定信道
	- 随机信道
***
## 信道容量

信道容量为输出序列对不同输入序列所提供的最大互信息：

$$
C=\lim\limits_{n\rightarrow\infty}\frac{1}{n}\max\limits_{Q(x^n)}I(X_1X_2\cdots X_n;Y_1Y_2\cdots Y_n)
$$

 - 这个式子表示平均每次利用信道，在输入和输出符号之间所能相互提供的互信息的最大值的极限
 - 该信道容量定义对所有形式信道均成立
***
### 离散无记忆信道容量

对于离散无记忆信道（DMC）：

$$
I(X_1X_2\cdots X_n;Y_1Y_2\cdots Y_n)\leq\sum\limits_{n=1}^NI(X_n;Y_n)
$$

其中等号在输入为独立随机序列时达到

??? note "Proof"

	$$
	\begin{aligned}
	H(\pmb{Y})&=H(Y_1,Y_2,\cdots,Y_n)\\
	&=H(Y_1)+H(Y_2|Y_1)+\cdots+H(Y_n|Y_1,Y_2,\cdots,Y_{n-1})\\
	&\leq\sum\limits_{i=1}^nH(Y_i)\\
	H(\pmb{Y}|\pmb{X})&=-E\{\log p(y^n|x^n)\}=-E\bigg\{\log\prod\limits_{i=1}^np(y_i|x_i)\bigg\}\\
	&=-\sum\limits_{i=1}^nE\{\log p(y_i|x_i)\}=\sum\limits_{i=1}^nH(Y_i|X_i)\\
	\therefore I(\pmb{X};\pmb{Y})&=H(\pmb{Y})-H(\pmb{Y}|\pmb{X})\\
	&\leq\sum\limits_{i=1}^n\{H(Y_i)-H(Y_i|X_i)\}=\sum\limits_{i=1}^nI(X_i;Y_i)
	\end{aligned}
	$$
	
	等号在输出 Y 为独立分布时成立。当 X 独立分布时，Y 也独立分布

因此：

$$
C=\lim\limits_{n\rightarrow\infty}\frac{1}{n}\max\limits_{Q(x^n)}I(X_1X_2\cdots X_n;Y_1Y_2\cdots Y_n)=\max\limits_{\{Q_k\}}I(X;Y)
$$

!!! example "Example"

	=== "无噪信道"
	
		![](../../../assets/Pasted%20image%2020250420105256.png)
		
		$$
		\begin{aligned}
		H(X|Y)&=0\\
		I(X;Y)&=H(X)\\
		C&=\max\limits_{\{Q_k\}}I(X;Y)=\max\limits_{\{Q_k\}}H(X)=\log M\text{ bit}
		\end{aligned}
		$$
		
	
	=== "无损信道"
	
		![](../../../assets/Pasted%20image%2020250420105440.png)
		
		$$
		\begin{aligned}
		H(X|Y)&=0\\
		I(X;Y)&=H(X)\\
		C&=\max\limits_{\{Q_k\}}I(X;Y)=\max\limits_{\{Q_k\}}H(X)=\log M\text{ bit}
		\end{aligned}
		$$
		
	
	=== "确定信道"
	
		![](../../../assets/Pasted%20image%2020250420105547.png)
		
		$$
		\begin{aligned}
		p(y_j|x_i)&=0\text{ or }1\\
		I(X;Y)&=H(Y)-H(Y|X)=H(Y)\\
		C&=\max\limits_{\{Q_k\}}I(X;Y)=\max\limits_{\{Q_k\}}H(Y)=\log m\text{ bit}
		\end{aligned}
		$$
		
	
	=== "无用信道"
	
		![](../../../assets/Pasted%20image%2020250420105724.png)
		
		$$
		\begin{aligned}
		p(y_j|x_i)&=p(y_j)\\
		p(x_i|y_j)&=p(x_i)\\
		H(X|Y)&=H(X)\\
		I(X;Y)&=H(X)-H(X|Y)=0\\
		C&\equiv 0
		\end{aligned}
		$$
		
	
	=== "复制信道"
	
		![](../../../assets/Pasted%20image%2020250420105850.png)
		
		$$
		\begin{aligned}
		I(X;Y)&=H(Y)-H(Y|X)=H(Y)-1\\
		C&=\max\limits_{\{Q_k\}}I(X;Y)=\max\limits_{\{Q_k\}}H(Y)-1\\
		&\leq\log 26-1=\log 13
		\end{aligned}
		$$
		
	
	=== "二元对称信道（BSC）"
	
		![](../../../assets/Pasted%20image%2020250420110028.png)
		
		$$
		\begin{aligned}
		I(X;Y)&=H(Y)-H(Y|X)\\
		&=H(Y)-\sum\limits_{x}p(x)H(Y|X=x)\\
		&=H(Y)-\sum\limits_{x}p(x)H(p)\\
		&=H(Y)-H(p)\\
		&\leq 1-H(p)
		\end{aligned}
		$$
		
		当输入取等概分布时，输出 Y 也是等概分布，故等号可以成立；特殊情况：$p=1, 0, \frac{1}{2}$
	
	=== "二元除删信道（BEC）"
	
		![](../../../assets/Pasted%20image%2020250420110239.png)
		
		$$
		\begin{aligned}
		C&=\max\limits_{\{Q_k\}}I(X;Y)\\
		&=\max\limits_{\{Q_k\}}\{H(Y)-H(Y|X)\}\\
		&=\max\limits_{\{Q_k\}}H(Y)-H(p)\\
		H(Y)&=H(q(1-p),p,(1-q)(1-p))\\
		&=H(p)+(1-p)H(q)\\
		\therefore C&=\max\limits_{\{Q_k\}}H(Y)-H(p)\\
		&=\max\limits_{q}(1-p)H(q)\\
		&=1-p
		\end{aligned}
		$$
		
		当输入取等概分布时，等号成立
		
		- BSC 和 BEC 的容量比较和启示：
		
		![](../../../assets/Pasted%20image%2020250420110607.png)
***
## 信道的组合

![](../../../assets/Pasted%20image%2020250420111312.png)

### 平行信道（积信道）

