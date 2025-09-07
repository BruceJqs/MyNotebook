---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Chapter 8 : 离散无记忆信道的容量定理

!!! abstract "Abstract"

	优化目标：$C=\max\limits_{\{Q_k\}}I(X;Y)$
	
	约束条件：
	
	$$
	\begin{cases}
	\sum\limits_{k=0}^{K-1}Q_k=1\\
	Q_k\geq 0\\
	\end{cases}
	$$
	
	$I(X;Y)$ 是输入 $X$ 分布的上凸函数，因此极大值存在

## 凸优化

凸优化：凸函数在凸集上的极值

假定 $f(x)$ 是定义在所有分量为非负的 $K$ 维无穷凸集 $R$ 上的一个凸函数，则满足下式的点称为 $f(x)$ 的平稳点，$f(x)$ 在平稳点处取到极值：

$$
\nabla f(x)=\begin{bmatrix}
\frac{\partial f}{\partial x_1}\\
\frac{\partial f}{\partial x_2}\\
\vdots\\
\frac{\partial f}{\partial x_K}\\
\end{bmatrix}=0
$$

在该点处的 Hessian 矩阵，为对称矩阵：

$$
H(x)=\begin{pmatrix}
\frac{\partial^2 f}{\partial x_1^2}&\frac{\partial^2 f}{\partial x_1 \partial x_2}&\cdots&\frac{\partial^2 f}{\partial x_1 \partial x_K}\\
\frac{\partial^2 f}{\partial x_2 \partial x_1}&\frac{\partial^2 f}{\partial x_2^2}&\cdots&\frac{\partial^2 f}{\partial x_2 \partial x_K}\\
\vdots&\vdots&\ddots&\vdots\\
\frac{\partial^2 f}{\partial x_K \partial x_1}&\frac{\partial^2 f}{\partial x_K \partial x_2}&\cdots&\frac{\partial^2 f}{\partial x_K^2}\\
\end{pmatrix}
$$

如果是凸函数，则在其定义域内，Hessian 矩阵为半正定。Hessian 矩阵也是判断一个函数是否为凸函数的依据

需要注意的是，$\nabla f(x)=0$ 的取值不一定在非负的集合 R 上，我们有如下定理：

!!! note "Theorems"

	=== "Theorem 01"
	
		$f(x)$ 是定义在所有分量为非负的 $K$ 维无穷凸集 $R$ 上的一个凸函数，如果 $\nabla f(x)$ 在 $R$ 上连续，则 $f(x)$ 在 $R$ 上取极大值的充要条件是：
		
		$$
		\begin{aligned}
		f'(x)=0 \quad \forall x_k>0\\
		f'(x)<0 \quad \forall x_k=0
		\end{aligned}
		$$
		
		![](../../../assets/Pasted%20image%2020250505111108.png)
		
		??? tip "说明"
		
			如果在 $R$ 上能找到，$f'(x)=0$，则极大值必然在该点取到，否则取到边界点 $x_k=0$，且此时 $f'(x)<0$
	
	=== "Theorem 02"
	
		设 $f(x)$ 是定义在 $K$ 维概率空间 $R$ 上的一个凸函数，如果 $\nabla f(x)$ 在 $R$ 上连续，则 $f(x)$ 在 $R$ 上取极大值的充要条件是
		
		$$
		\begin{aligned}
		f'(x)=\lambda \quad \forall x_k>0\\
		f'(x)<\lambda \quad \forall x_k=0
		\end{aligned}
		$$
		
		其中 $\lambda$ 是拉格朗日乘数，由 $\sum_k x_k=1$ 决定
		
		??? tip "说明"
		
			问题就可以被抽象为一个目标函数为 $\max f(x)$，约束条件为 $x_k\geq 0,\forall k\sum_k x_k=1$ 的数学规划
			
			我们构造一个拉格朗日函数 $L(x,\lambda)=f(x)+\lambda\sum_k x_k$，要最大化 $f(x)$，即就要最大化 $L(x,\lambda)$，根据定理 1 我们就可以得到定理 2

??? note "凸优化一般问题"

	![](../../../assets/Pasted%20image%2020250505112110.png)
***
## 离散无记忆信道的容量定理

概率分布 $\{Q_0,Q_1,\cdots,Q_{K−1}\}$ 达到转移概率为 $\{p(j|k)\}$ 的离散无记忆信道容量 $C$ 的充要条件为：

$$
\begin{aligned}
I(X=k;Y)=C \quad \forall k,Q_k>0\\
I(X=k;Y)<C \quad \forall k,Q_k=0
\end{aligned}
$$

其中 $I(X=k;Y)$ 表示通过信道传送字符 $X=k$ 时，信道的输入与输出之间可获得的互信息的期望值，即：

$$
I(X=k;Y)=\sum\limits_{j=0}^{J-1}p(j|k)\log\frac{p(j|k)}{p(j)}=\sum\limits_{j=0}^{J-1}p(j|k)\log\frac{p(j|k)}{\sum\limits_{i=0}^{K-1}p(j|i)Q_i}
$$

??? note "Proof"

	$$
	\begin{aligned}
	I(X=l;Y)&=\sum\limits_{j=0}^{J-1}p(j|l)\log\frac{p(j|l)}{\sum\limits_{i=0}^{K-1}p(j|i)Q_i}\\
	\frac{\partial I(X=l;Y)}{\partial Q_k}&=-\sum\limits_{j=0}^{J-1}p(j|l)\frac{p(j|k)}{\sum\limits_{i=0}^{K-1}p(j|i)Q_i}\\
	\sum\limits_{l=0}^{K-1}Q_l\frac{\partial I(X=l;Y)}{\partial Q_k}&=\sum\limits_{l=0}^{K-1}Q_l\sum\limits_{j=0}^{J-1}p(j|l)\frac{p(j|k)}{\sum\limits_{i=0}^{K-1}p(j|i)Q_i}\\
	&=\sum\limits_{j=0}^{J-1}\frac{p(j|k)}{\sum\limits_{i=0}^{K-1}p(j|i)Q_i}\sum\limits_{l=0}^{K-1}Q_lp(j|l)=1\\
	J(\{Q_k\})&=I(X;Y)-\lambda(\sum\limits_{k=0}^{K-1}Q_k)\\
	&=\sum\limits_{k=0}^{K-1}Q_kI(X=k;Y)-\lambda(\sum\limits_{k=0}^{K-1}Q_k)\\
	\end{aligned}
	$$
	
	由 KKT 条件，我们有：
	
	$$
	\begin{aligned}
	\frac{\partial J(\{Q_k\})}{\partial Q_k}&\begin{cases}
	=0 & \forall Q_k>0\\
	<0 & \forall Q_k=0
	\end{cases}\\
	\frac{\partial J(\{Q_k\})}{\partial Q_k}&=I(X=k;Y)+\sum\limits_{l=0}^{K-1}Q_l\frac{\partial I(X=l;Y)}{\partial Q_k}-\lambda\\
	&=I(X=k;Y)-(\lambda-1)
	\end{aligned}
	$$
	
	令 $C=\lambda-1$，得：
	
	$$
	\begin{aligned}
	I(X=k;Y)&=C & \forall k, Q_k>0\\
	I(X=k;Y)&<C & \forall k, Q_k=0
	\end{aligned}
	$$
	

这个定理说明，取到离散无记忆信道的容量的充要条件是对于好的 $I(X = k; Y)$，其值均相等，对于不好的 $I(X = k; Y)$，其值均为 0

$$
C=I(X;Y)=\sum\limits_{k}Q_kI(X=k;Y)
$$
***
## 对称离散无记忆信道

离散无记忆信道的转移概率可用 $K\times J$ 矩阵表示：

$$
\mathbf{P}=\{p(j|k)\}=\begin{bmatrix}
p(0|0)&p(1|0)&\cdots&p(J-1|0)\\
p(0|1)&p(1|1)&\cdots&p(J-1|1)\\
\vdots&\vdots&\ddots&\vdots\\
p(0|K-1)&p(1|K-1)&\cdots&p(J-1|K-1)\\
\end{bmatrix}
$$

向量 $\mathbf{x}=\{x_1,x_2,\cdots,x_N\}$ 的置换向量定义为：

$$
\mathbf{x}'=\{x_{\pi(1)},x_{\pi(2)},\cdots,x_{\pi(N)}\}
$$

其中 $\mathbf{\pi}=\{\pi(1),\pi(2),\cdots,\pi(N)\}$ 是 $\{1,2,\cdots,N\}$ 的任意排列

例如 $\mathbf{x}=\{0.2,0.3,0.1,0.4\},\mathbf{x}'=\{0.1,0.2,0.3,0.4\}$

- 若 P 中每一行都是第一行的一个置换，则该信道关于输入对称
	
	$$
	H(Y|X)=H(Y|X=k)=-\sum\limits_{j=0}^{J-1}p(j|k)\log p(j|k)
	$$
	
	![](../../../assets/Pasted%20image%2020250505144358.png)
	
- 若 P 中每一列都是第一列的一个置换，则该信道关于输出对称
	
	$$
	\sum\limits_{k=0}^{K-1}p(j|k)=\frac{K}{J},j=0,1,\cdots,J-1
	$$
	
	![](../../../assets/Pasted%20image%2020250505144509.png)
	
- 若一个信道既关于输入对称，又关于输出对称，即 P 中每一行都是第一行的一个置换，每一列都是第一列的一个置换，则该信道是对称的，例如：
	
	$$
	\mathbf{x}=\begin{bmatrix}
	0.2&0.3&0.1&0.4\\
	0.3&0.2&0.4&0.1\\
	0.1&0.4&0.2&0.3\\
	0.4&0.1&0.3&0.2\\
	\end{bmatrix}
	$$
	
- 对一个信道的转移概率矩阵 P 按列划分，得到若干个子信道，若划分出的所有子信道均是对称的，则称该信道是准对称的

![](../../../assets/Pasted%20image%2020250505145028.png)
***
### 准对称离散无记忆信道的容量定理

达到准对称离散无记忆信道容量的输入分布为均匀分布

??? note "Proof"

	若 $Q_k=\frac{1}{K},k=0,1,\cdots,K-1$
	
	$$
	\begin{aligned}
	I(X=k;Y)&=\sum\limits_{j=0}^{J-1}p(j|k)\log\frac{p(j|k)}{\frac{1}{K}\sum\limits_{i=0}^{K-1}p(j|i)}\\
	&=\sum\limits_{s}\sum\limits_{j\in y_s}p(j|k)\log\frac{p(j|k)}{\frac{1}{K}\sum\limits_{i=0}^{K-1}p(j|i)}\\
	&=\text{constant}
	\end{aligned}
	$$
	
	因而满足 KKT 条件
***
### 具有不同对称性的信道的容量

- 若信道关于输入对称，则 $I(X;Y)=H(Y)-H(Y|X)=H(Y)+\sum\limits_{j=0}^{J-1}p(j|k)\log p(j|k)$
- 若信道同时也关于输出对称（即信道对称），则 $C=\log J+\sum\limits_{j=0}^{J-1}p(j|k)\log p(j|k)$
- 若信道只关于输入对称，则 $C\leq\log J+\sum\limits_{j=0}^{J-1}p(j|k)\log p(j|k)$
- $K$ 元对称信道：
	
	![](../../../assets/Pasted%20image%2020250505150834.png)
	
	$$
	\begin{aligned}
	p(j|k)&=\begin{cases}
	1-p & k=j\\
	\frac{p}{K-1} & k\neq j
	\end{cases}\\
	C&=\log K+\sum\limits_{j=0}^{J-1}p(j|k)\log p(j|k)\\
	&=\log K+(1-p)\log(1-p)+p\log\frac{p}{K-1}\\
	&=\log K-H(p)-p\log(K-1)\\
	\end{aligned}
	$$
	
***
## 除删信道（BEC）

![](../../../assets/Pasted%20image%2020250505151158.png)

$$
\begin{aligned}
\mathbf{P}&=\begin{pmatrix}
1-p-q & q & p\\
p & q & 1-p-q\\
\end{pmatrix}\\
Q_0&=Q_1=0.5\\
C&=I(X=0;Y)=I(X=1;Y)\\
&=(1-p-q)\log\frac{1-p-q}{(1-q)/2}+q\log\frac{q}{q}+p\log\frac{p}{(1-q)/2}\\
&=(1-p-q)\log(1-p-q)+p\log p-(1-q)\log\frac{1-q}{2}
\end{aligned}
$$

特殊情况：当 $p = 0$ 时为二元除删信道；当 $q = 0$ 时为二元对称信道
***
## 模 K 加法信道

模 $K$ 加法信道定义为 $Y=X+Z\text{ mod }K,X,Y,Z\in\{0,1,2,\cdots,K-1\}$，$p(z)$ 为任意分布

![](../../../assets/Pasted%20image%2020250505153456.png)

该信道是一个对称信道

$$
\begin{aligned}
H(Y|X)&=-\sum\limits_{x}\sum\limits_{y}Q(x)p(y|x)\log p(y|x)\\
&=-\sum\limits_{x}\sum\limits_{z}Q(x)p(z)\log p(z)\\
&=H(z)
\end{aligned}
$$

所以：$C=\log K−H(z)$，当 $Z$ 为等概分布时，信道容量为 0，当 $Z$ 为确定性分布时，信道容量为$\log K$
***
## 转移概率矩阵可逆信道的容量计算

若 $Q_k>0$，则 $I(X=k;Y)=\sum\limits_{j=0}^{J-1}p(j|k)\log\frac{p(j|k)}{\sum\limits_{i=0}^{K-1}p(j|i)Q_i}=C$

令 $w_j=\sum\limits_{i=0}^{K-1}p(j|i)Q_i$，则 $\sum\limits_{j=0}^{J-1}p(j|k)\log p(j|k)-\sum\limits_{j=0}^{J-1}p(j|k)\log w_j=C$

即 $\sum\limits_{j=0}^{K-1}p(j|k)\underbrace{[C+\log w_j]}_{\beta_j}=\underbrace{\sum\limits_{j=0}^{K-1}p(j|k)\log p(j|k)}_{\alpha_k},k=0,1,\cdots,K-1$

亦即 $\mathbf{P}\beta=\alpha$，若 $\mathbf{P}$ 可逆则可解出唯一的 $\beta$，进一步可得 $w_j=2^{\beta_j-C}$，再由 $\sum\limits_{j}w_j=1$，得 $C=\log\sum_j 2^{\beta_j}$

进一步，再由 $w_j=\sum\limits_{i=0}^{K-1}Q_ip(j|k),j=0,1,\cdots,K-1$，可以求出 $\{Q_k\}$

- 若存在某个 $Q_k < 0$，则原假设前提不满足，必须尝试令其中某个符号不发送（不一定是符号 $k$），再用上述过程重新计算

!!! example "Example"

	![](../../../assets/Pasted%20image%2020250505155607.png)
	
	$$
	\begin{aligned}
	\mathbf{P}\beta&=\alpha\\
	\begin{bmatrix}
	1&0\\
	p&1-p\\
	\end{bmatrix}\begin{bmatrix}
	\beta_0\\
	\beta_1\\
	\end{bmatrix}&=\begin{bmatrix}
	\alpha_0\\
	\alpha_1\\
	\end{bmatrix}=\begin{bmatrix}
	0\\
	-H(p)\\
	\end{bmatrix}\\
	\begin{bmatrix}
	\beta_0\\
	\beta_1\\
	\end{bmatrix}&=\begin{bmatrix}
	0\\
	-H(p)/(1-p)\\
	\end{bmatrix}\\
	C=\log\sum\limits_{j=0}^{K-1}2^{\beta_j}&=\log(1+2^{-H(p)/(1-p)})\\
	\therefore w_0=2^{\beta_0-C}&=\frac{1}{1+2^{-H(p)/(1-p)}}=q+(1-q)p\\
	w_1=2^{\beta_1-C}&=\frac{2^{-H(p)/(1-p)}}{1+2^{-H(p)/(1-p)}}=(1-p)(1-q)\\
	\therefore q&=\frac{1-(\frac{p}{1-p})2^{-H(p)/(1-p)}}{1+2^{-H(p)/(1-p)}}\\
	\end{aligned}
	$$
	




