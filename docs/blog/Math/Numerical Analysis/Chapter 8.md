---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Chapter 08 : Approximation Theory

!!! abstract "Introduction"

	这一整章的目的是给定 $x_1,\cdots,x_m$ 和 $y_1,\cdots,y_m$，寻找一个更为简单的函数 $P(x)\approx f(x)$
	
	但是，我们会碰到如下困难：
	
	- $m$ 可能会非常大
	- $y_i$ 会是实验性的数据，并不一定准确，即 $y_i\neq f(x_i)$
	
	那么看起来我们需要一个最贴近的 $P(x)$ 使得误差 $P(x_i)-y_i$ 比较小，即使有可能对于每个点都有 $P(x_i)\neq y_i$
	
	对于评判 $P(x_i)$ 的好坏，我们有几种方法：
	
	- 最小化误差的最大值（Minimax Problem）：即求 $\min\{\max\limits_{1\leq i\leq m}|P(x_i)-y_i|\}$
	- 最小化误差的和（Absolute Deviation）：即求 $\min\{\sum\limits_{i=1}^m|P(x_i)-y_i|\}$
	- 最小化误差的平方和（Least-Squares Method）：即求 $\min\{\sum\limits_{i=1}^m(P(x_i)-y_i)^2\}$（最为常用）
	
	看这三种方法眼熟吗？似乎分别就对应了我们先前所学的无穷范数、1 范数和 2 范数

## Discrete Least Squares Approximation

目标：确定一个多项式 $P_n(x)=a_0+a_1x+\cdots+a_nx^n$，用于近似表示一组数据 $\{(x_i,y_i)|i=1,2,\cdots,m\}$，使得最小二乘误差 $E_2=\sum\limits_{i=1}^m[P_n(x_i)−y_i]^2$ 最小化，其中 $n<<m$

$E_2​$ 实际上是一个关于 $a_0,a_1,\cdots,a_n$ 的函数，也就是说 $E_2(a_0,a_1,\cdots,a_n)=\sum\limits_{i=1}^m[a_0+a_1x_i+\cdots+a_nx_i^n−y_i]^2$。要想让 $E_2$​ 最小化，必要条件是 $\frac{\partial E_2}{\partial a_k}=0,k=0,\cdots,n$，所以我们有：

$$
\begin{aligned}
0&=\frac{\partial E_2}{\partial a_k}=2\sum\limits_{i=1}^m[P_n(x_i)-y_i]\frac{\partial P_n(x_i)}{\partial a_k}=2\sum\limits_{i=1}^m[\sum\limits_{j=0}^n a_jx_i^j-y_i]x_i^k\\
&=2\bigg\{\sum\limits_{j=0}^na_j(\sum\limits_{i=1}^mx_i^{j+k})-\sum\limits_{i=1}^my_ix_i^k\bigg\}
\end{aligned}
$$

我们令 $b_k=\sum\limits_{i=1}^mx_i^k,c_k=\sum\limits_{i=1}^my_ix_i^k$，那么上式可以化为矩阵形式：

$$
\begin{bmatrix}
b_{0+0} & \cdots & b_{0+n}\\
\vdots & \ddots & \vdots\\
b_{n+0} & \cdots & b_{n+n}
\end{bmatrix}\begin{bmatrix}
a_0\\
\vdots\\
a_n
\end{bmatrix}=\begin{bmatrix}
c_0\\
\vdots\\
c_n
\end{bmatrix}
$$

!!! note "老师的推导方法"

	我们从一开始就用矩阵的形式来表示这个问题，即我们要求：
	
	$$
	\begin{aligned}
	\min P(\pmb{a})&=\bigg\|\begin{pmatrix}
	1 & x_1 & \cdots & x_1^n\\
	1 & x_2 & \cdots & x_2^n\\
	\vdots & \vdots & \ddots & \vdots\\
	1 & x_m & \cdots & x_m^n
	\end{pmatrix}_{m\times(n+1)}\begin{pmatrix}
	a_0\\
	a_1\\
	\vdots\\
	a_n
	\end{pmatrix}_{(n+1)}-\pmb{y}\bigg\|_2^2\\
	&=\min\|\pmb{X}\pmb{a}-\pmb{y}\|_2^2=\min(\pmb{a}^T\pmb{X}^T-\pmb{y}^T)(\pmb{X}\pmb{a}-\pmb{y})\\
	&=\min(\pmb{a}^T\pmb{X}^T\pmb{X}\pmb{a}-2\pmb{y}^T\pmb{X}\pmb{a}+\pmb{y}^T\pmb{y})\\
	\end{aligned}
	$$
	
	对 $\pmb{a}$ 求导：
	
	$$
	\begin{aligned}
	0&=\frac{\partial P(\pmb{a})}{\partial \pmb{a}}=\frac{\partial}{\partial \pmb{a}}(\pmb{a}^T\pmb{X}^T\pmb{X}\pmb{a}-2\pmb{y}^T\pmb{X}\pmb{a}+\pmb{y}^T\pmb{y})\\
	&=\frac{\partial}{\partial \pmb{a}}(\pmb{a}^T\pmb{X}^T\pmb{X}\pmb{a})-2\frac{\partial}{\partial \pmb{a}}(\pmb{y}^T\pmb{X}\pmb{a})\\
	&=2\pmb{X}^T\pmb{X}\pmb{a}-2\pmb{X}^T\pmb{y}\\
	\end{aligned}
	$$
	
	和我们上面的推导是一样的

!!! example "Example"

	我们有以下数据：
	
	![](../../../assets/Pasted%20image%2020250416105238.png)
	
	=== "法 1"
	
		我们用 $P(x)=\frac{x}{ax+b}$ 来近似，即寻找 $a,b$，使得 $E_2(a,b)=\sum\limits_{i=1}^m(\frac{x_i}{ax_i+b}−y_i)^2$ 最小化
		
		**线性化**（Linearization）：令 $Y=\frac{1}{y},X=\frac{1}{x}$​，那么 $Y\approx a+bX$ 就是一个线性问题了
		
		将 $(x_i,y_i)$ 转换为 $(X_i,Y_i)$，$a,b$ 就能被解出来了
	
	=== "法 2"
	
		我们用 $P(x)=ae^{-\frac{b}{x}}$ 来近似，不难发现 $\ln y\approx \ln a - \frac{b}{x}$
		
		**线性化**：令 $Y=\ln⁡ y,X=\frac{1}{x},A=\ln ⁡a,B=−b$，得到 $Y\approx A+BX$ 这样一个线性问题
		
		将 $(x_i,y_i)$ 转换为 $(X_i,Y_i)$，$a,b$ 就能被解出来了（$a=e^A,b=−B,P(x)=ae^{−\frac{b}{x}}$​）
***
## Orthogonal Polynomials and Least Squares Approximation

> 我们先前所讲的是离散版本的多项式近似问题，而接下来我们要讲的就是连续版本的多项式近似问题

连续版本：给定定义在 $[a,b]$ 上的函数 $f(x)$，我们希望找到一个更简单的函数 $P(x)\approx f(x)$，使得 $\int_{a}^{b}[P(x)-f(x)]^{2}dx$ 最小化

我们定义：对于一组在区间 $[a,b]$ 上的函数 $\{\varphi_0(x),\varphi_1(x),\cdots,\varphi_n(x)\}$，当 $\forall x\in[a,b]$，$a_0\varphi_0(x)+a_1\varphi_1(x)+\cdots+a_n\varphi_n(x)=0$ 时，有 $a_0=a_1=\cdots=a_n=0$，那么称这组函数是**线性独立**（Linearly Independent）的，否则称它们是**线性相关**（Linearly Dependent）的

!!! note "Theorems"

	=== "Theorem 1"
	
		如果 $\varphi_j(x)$ 是一个 $j$ 次多项式（$j=0,\cdots,n$），那么 $\{\varphi_0(x),\varphi_1(x),\cdots,\varphi_n(x)\}$ 在任意区间 $[a,b]$ 上都是线性独立的
		
		!!! note "Proof"
		
			假设结论不成立，根据定义，$\exists a_0,a_1,\cdots,a_n,\forall x\in [a,b]$ 使得 $P(x)=a_0\varphi_0(x)+a_1\varphi_1(x)+\cdots+a_n\varphi_n(x)=0$

			此时 $P(x)$ 是一个零多项式，$x_n$ 的系数为 0，即 $a_n=0$，那么 $P(x)=a_0\varphi_0(x)+a_1\varphi_1(x)+\cdots+a_{n−1}\varphi_{n−1}(x)=0$。同理可以推出 $a_{n−1}=0$，以此类推，最终发现所有系数均为 0。所以假设不成立，得证
	
	=== "Theorem 2"
	
		令 $\prod_n​$ 为一组次数至多为 $n$ 的多项式，如果 $\{\varphi_0(x),\varphi_1(x),\cdots,\varphi_n(x)\}$ 是 $\prod_n​$ 内一组线性独立的多项式，那么 $\prod_n​$ 内的任意多项式均可被唯一写做 $\varphi_0(x),\varphi_1(x),\cdots,\varphi_n(x)$ 的一个线性组合

**广义多项式（Generalized Polynomial）**：对于一般的一组线性无关的函数 $\{\varphi_0(x), \varphi_1(x), \cdots, \varphi_n(x)\}$ ，它们的线性组合 $P(x)=\sum\limits_{i=0}^{n} a_{i} \varphi_{i}(x)$ 被称为广义多项式

其他多项式：

- $\{\varphi_j(x)=\cos ⁡jx\},\{\psi_j(x)=\sin⁡ jx\}\Rightarrow \{\varphi_j(x),\psi_j(x)\}$ 得到的是**三角多项式**（Trigonometric Polynomial）
- $\{\varphi_j(x)=e_{kjx},k_i\neq k_j\}$ 得到的是**指数多项式**（Exponential Polynomial）
***
### Weight Function

- 离散版本：当对一组离散点 $(x_i,y_i)(i=1,\cdots,n)$ 进行近似时，我们为每个点赋予一个误差项 $w_i$​，它是一个正实数。此时我们要考虑让 $E=\sum w_i[P(x_i)−y_i]^2$ 最小化。集合 $\{w_i\}$ 被称为**权重**（Weight）。设置权重的目标是为这些点赋予不同的“重要程度”，以便实现更好的近似
- 连续版本：一个在区间 $I$ 上的可积分的函数 $w$ 被称为权重函数，它满足 $\forall x\in I,w(x)\geq 0$，但 $w(x)$ 不会在 $I$ 的任意子区间上消失。此时我们要考虑让 $E=\int_a^bw(x)[P(x)−f(x)]^2dx$ 最小化

因此，我们也可以得到一般的最小二乘近似问题：

- 离散版本：给定一组离散点 $(x_i,y_i)$ 和一组对应的权重 $\{w_i\}$（$i=1,\cdots,m$）。我们要找到一个广义多项式 $P(x)$，使得误差 $E=\sum w_i[P(x_i)−y_i]^2$ 最小化
- 连续版本：给定定义在区间 $[a,b]$ 上的一个函数 $f(x)$ 和一个权重函数 $w(x)$。我们要找到一个广义多项式 $P(x)$，使得误差 $E=\int_a^bw(x)[P(x)−f(x)]^2dx$ 最小化
***
### Inner Product and Norm

我们定义内积为：

$$
\langle f, g\rangle=
\begin{cases}
\sum\limits_{i=1}^{m} w_i f(x_i) g(x_i) \\
\int_{a}^{b} w(x) f(x) g(x) dx 
\end{cases}
$$

如果 $\langle f, g\rangle = 0$，则称 $f$ 和 $g$ 正交，且 $\|f\|=\sqrt{\langle f, f\rangle}$ 是一个范数

因此一般的最小二乘近似问题可以被转换为：寻找一个广义多项式 $P(x)$，使得 $E = \langle P-y, P-y\rangle=\|P-y\|^2$ 最小

我们令 $P(x)=a_0\varphi_0(x)+a_1\varphi_1(x)+\cdots+a_n\varphi_n(x)$，和离散版本相似地，我们有：

$$
\begin{aligned}
\frac{\partial E}{\partial a_k}=0&\Rightarrow\sum\limits_{j=0}^n(\varphi_k,\varphi_j)a_j=(\varphi_k,f),k=0,\cdots,n\\
&\Rightarrow[b_{ij}=(\varphi_i,\varphi_j)]\begin{bmatrix}
a_0\\
\vdots\\
a_n
\end{bmatrix}=\begin{bmatrix}
(\varphi_0,f)\\
\vdots\\
(\varphi_n,f)
\end{bmatrix}=\vec{c}
\end{aligned}
$$

!!! example "Example"

	使用 $y=a_0+a_1x+a_2x^2$ 近似点集 $\{(1,4),(2,10),(3,18),(4,26)\}$
	
	??? note "Answer"
	
		令 $\varphi_0(x)=1,\varphi_1(x)=x,\varphi_2(x)=x^2$，可以计算出：
		
		$$
		\begin{aligned}
		(\varphi_0,\varphi_0)&=\sum\limits_{i=1}^41·1=4 \quad (\varphi_1,\varphi_2)=\sum\limits_{i=1}^4x_i·x_i^2=100\\
		(\varphi_0,\varphi_1)&=\sum\limits_{i=1}^41·x_i=10 \quad (\varphi_1,\varphi_1)=\sum\limits_{i=1}^4x_i^2=30\\
		(\varphi_0,\varphi_2)&=\sum\limits_{i=1}^41·x_i^2=30 \quad (\varphi_2,\varphi_2)=\sum\limits_{i=1}^4x_i^4=354\\
		(\varphi_0,y)&=\sum\limits_{i=1}^4y_i·1=58 \quad (\varphi_1,y)=182 \quad (\varphi_2,y)=622\\
		&\therefore \begin{pmatrix}
		4 & 10 & 30\\
		10 & 30 & 100\\
		30 & 100 & 354
		\end{pmatrix}\begin{pmatrix}
		a_0\\
		a_1\\
		a_2
		\end{pmatrix}=\begin{pmatrix}
		58\\
		182\\
		622
		\end{pmatrix}\\
		&\Rightarrow a_0=-\frac{3}{2},a_1=\frac{49}{10},a_2=\frac{1}{2}\\
		&\therefore y=P(x)=\frac{1}{2}x^2+\frac{49}{10}x-\frac{3}{2}
		\end{aligned}
		$$
		
***
### Orthogonal Polynomial

事实上，由上面的例子，当使用 $\varphi_j(x)=x_j$ 和 $w(x)\equiv 1$ 来近似 $f(x)\in C[0,1]$ 时，$(\varphi_i,\varphi_j)=\int_0^1x^ix^jdx=\frac{1}{i+j+1}$（**希尔伯特矩阵**，Hilbert matrix）

而希尔伯特矩阵是一个条件数随着 $n$ 的增大而爆炸性增大的矩阵，我们可以计算一下上面的矩阵：$\|B\|_{\infty}=484,\|B^{-1}\|_{\infty}=\frac{63}{4}\Rightarrow K(B)=7623$，这仅仅只是三阶的情况

因此，我们需要一个更好的方法来求解这个问题，如果我们能找到一组一般的线性独立的函数 $\{\varphi_0(x),\varphi_1(x),\cdots,\varphi_n(x)\}$，使得任何函数对 $\varphi_i(x),\varphi_j(x)$ 是**正交的**（Orthogonal），那么范数矩阵将会是个**对角矩阵**。此时我们有 $a_k=\frac{(\varphi_k,f)}{\varphi_k,\varphi_k}$，那么我们就需要考虑构造正交多项式（Orthogonal Polynomial）

!!! note "Theorem"

	对于一组在 $[a,b]$ 的多项式函数 $\{\varphi_0(x),\varphi_1(x),\cdots,\varphi_n(x)\}$ 以及一个权重函数 $w$，当满足以下条件时，我们认为这些函数是正交的：
	
	$$
	\varphi_0(x)\equiv 1,\varphi_1(x)=x−B_1,\varphi_k(x)=(x−B_k)\varphi_{k−1}(x)−C_k\varphi_{k−2}(x)
	$$
	
	其中 $B_k=\frac{(x\varphi_{k−1},\varphi_{k−1})}{(\varphi_{k−1},\varphi_{k−1})},C_k=\frac{(x\varphi_{k−1},\varphi_{k−2})}{(\varphi_{k−2},\varphi_{k−2})}$

!!! example "Example"

	还是利用上面的例子，使用 $y=a_0+a_1x+a_2x^2$ 近似点集 $\{(1,4),(2,10),(3,18),(4,26)\}$
	
	??? note "Answer"
	
		首先构造正交多项式 $\varphi_0(x),\varphi_1(x),\varphi_2(x)$，令 $y=a_0\varphi_0(x)+a_1\varphi_1(x)+a_2\varphi_2(x)$（$a_k=\frac{(\varphi_k,y)}{(\varphi_k,\varphi_k)}$​），我们有：
		
		$$
		\begin{aligned}
		\varphi_0(x)&=1 \Rightarrow a_0=\frac{(\varphi_0,y)}{(\varphi_0,\varphi_0)}=\frac{29}{2} \quad B_1=\frac{(x\varphi_0,\varphi_0)}{(\varphi_0,\varphi_0)}=\frac{5}{2}\\
		\varphi_1(x)&=x-B_1=x-\frac{5}{2}\Rightarrow a_1=\frac{(\varphi_1,y)}{(\varphi_1,\varphi_1)}=\frac{37}{5} \\ B_2&=\frac{(x\varphi_1,\varphi_1)}{(\varphi_1,\varphi_1)}=\frac{5}{2} \quad C_2=\frac{(x\varphi_1,\varphi_0)}{(\varphi_0,\varphi_0)}=\frac{5}{4}\\
		\varphi_2(x)&=(x-B_2)\varphi_1(x)-C_2\varphi_0(x)=(x-\frac{5}{2})(x-\frac{5}{2})-\frac{5}{4}=x^2-5x+5 \\
		a_2&=\frac{(\varphi_2,y)}{(\varphi_2,\varphi_2)}=\frac{1}{2}\\
		\end{aligned}
		$$
		
		最终解得 $y=\frac{1}{2}x^2+\frac{49}{10}x-\frac{3}{2}$

伪代码：

![](../../../assets/Pasted%20image%2020250416145541.png)

其中误差推导如下：

![](../../../assets/Pasted%20image%2020250416145553.png)

****
## Chebyshev Polynomials and Economization of Power Series

一般的最小二乘近似问题是要找到一个广义多项式 $P(x)$，使得 $E=(P−y,P−y)=\|P−y\|^2$ 最小化

现在的目标是最小化 $\|P−y\|_{\infty}$​，我们称之为**极小化极大问题**（Minimax Problem）
***
### Targets

#### Target 1

目标 1.0：找到 $n$ 阶多项式 $P_n(x)$ 使得 $\|P_n−f\|_{\infty}$ 最小化

定义：如果 $P(x_0)−f(x_0)=\pm\|P−f\|_{\infty}$，那么此时 $x_0$ 被称为（$\pm$）**偏差点**（Deviation Point）

从任意地方构造出多项式并不容易，但我们能够检验多项式的一些特征：

- 如果 $f\in C[a,b]$ 且 $f$ **不是**一个 $n$ 阶多项式，那么存在一个唯一的多项式 $P_n(x)$，使得 $\|P_n−f\|_{\infty}​$ 最小化
- $P_n(x)$ 存在，且必须同时有正负偏差点
- **切比雪夫定理**（Chebyshev Theorem）：$P_n(x)$ 最小化 $\|P_n−f\|_{\infty}\Leftrightarrow P_n(x)$ 至少有 $n+2$ 个关于 $f$ 的正负偏差点。也就是说，存在一组点 $a\leq t_1<\cdots<t_{n+2}\leq b$ 使得 $P_n(t_k)−f(t_k)=\pm(−1)^k\|P_n−f\|_{\infty}$​。集合 $\{t_k\}$ 被称为**切比雪夫交替序列**（Chebyshev Alternating Sequence）

![](../../../assets/Pasted%20image%2020250423101625.png)

其中 $P_n(x)$ 被称为 $f(x)$ 的插值多项式（Interpolating Polynomial），由上图我们可以发现，$P_n(x)-f(x)$ 有至少 $n+1$ 个根
***
#### Target 2

目标 2.0：找到插值点 $\{x_0,\cdots,x_n\}$ 使得 $P_n(x)$ 最小化余项 $|P_n(x)−f(x)|=|R_n(x)|=|\frac{f^{(n+1)}(\xi)}{(n+1)!}\prod\limits_{i=0}^n(x−x_i)|$

对此，我们也可以进一步得到下一个目标 2.1：我们需要找到 $\{x_1,\cdots,x_n\}$ 使得 $\|w_n\|_{\infty}$ 在 $[-1,1]$ 上最小，其中 $w_n(x)=\prod\limits_{i=1}^n(x-x_i)$

注意到 $w_n(x)=x^n-P_{n-1}(x)$，那么整个问题就可以进一步简化成目标 3.0
***
#### Target 3

目标 3.0：找到一个多项式 $P_{n-1}(x)$ 使得 $\|x^n-P_{n-1}(x)\|_{\infty}$ 在 $[-1,1]$ 最小化

根据切比雪夫定理，我们知道 $P_{n−1}(x)$ 相对于 $x^n$ 有 $n+1$ 个偏差点，也就是说 $w_n(x)$ 在 $n+1$ 个点上交替获得最大值和最小值
***
### Chebyshev Polynomials

为了实现上面的目标，我们先想到三角函数。$cos(n\theta)$ 在 $[-1,1]$ 上有 $n+1$ 个交替的最大值和最小值，但是 $cos(n\theta)$ 并不是多项式，又由于 $cos(n\theta)$ 可以表示为 $\sum\limits_{k=0}^{n} a_k (\cos\theta)^k$，这就是我们想要的多项式形式

令 $x=\cos\theta$，则 $x \in [-1,1]$，所以我们可以把 $cos(n\theta)$ 写成 $T_n(x)$ 的形式，$T_n(x)=\cos(n\theta)=\cos(n\cdot\arccos x)$ 称为**切比雪夫多项式（Chebyshev Polynomial）**

切比雪夫多项式有如下性质：

- $T_n​(x)$ 在 $t_k=\cos⁡(\frac{k}{n}\pi)(k=0,1,\cdots,n)$ 情况下，在最大值 1 和最小值 -1 之间交替变换，也就是说 $T_n(t_k)=(−1)^k\|T_n(x)\|_{\infty}$
- $T_n​(x)$ 有 $n$ 个根 $x_k=\cos⁡(\frac{2k−1}{2n}\pi)(k=1,\cdots,n)$
- 切比雪夫多项式有递推公式：
	
	$$
	\begin{aligned}
	T_{0}(x)&=1\\
	T_{1}(x)&=x\\
	T_{n}(x)&=2 x T_{n-1}(x)-T_{n-2}(x), \quad n=2,3, \cdots
	\end{aligned}
	$$
	
	- 由递推公式我们可以得到最高阶项的系数为 $2^{n-1}$
- 在 $[-1,1]$ 上，$T_0(x), T_1(x), \cdots, T_n(x)$ 关于权重函数 $\frac{1}{\sqrt{1-x^2}}$ 正交，即：
	
	$$
	(T_n,T_m)=\int_{-1}^1\frac{T_n(x)T_m(x)}{\sqrt{1-x^2}}dx=\begin{cases}
	0 & n\neq m\\
	\frac{\pi}{2} & n=m\neq 0\\
	\pi & n=m=0
	\end{cases}
	$$
	
***
### Back to Targets

#### Target 3

我们回到之前我们设下的目标，对于目标 3.0 来说，可以把 $w_n$ 写成 $T_n(x)$ 的形式：

$$
w_{n}(x)=x^{n}-P_{n-1}(x)=\frac{T_{n}(x)}{2^{n-1}}
$$
***
#### Target 2

对于目标 2.1 来说，也将 $w_n$ 写成 $T_n(x)$ 的形式：

$$
\min_{w_n\in \tilde\Pi_n} \|w_{n}\|_{\infty}=\big\|\frac{T_{n}(x)}{2^{n-1}}\big\|_{\infty}=\frac{1}{2^{n-1}}
$$

我们称 $\tilde{\Pi_n}$ 为 n 阶的**首一切比雪夫多项式（The Monic Chebyshev Polynomial）**，其中我们所取的插值点 $\{x_1,\cdots,x_n\}$ 是 $T_n(x)$ 的 $n$ 个根

对于目标 2.0 来说，取 $T_{n+1}(x)$ 上的 $n+1$ 个根作为插值点 $\{x_0,\cdots,x_n\}$，然后关于 $f(x)$ 的插值多项式 $P_n(x)$ 假设绝对误差的最小上界为 $\frac{M}{2^n(n+1)!}$

!!! example "Example"

	找到在 $[0,1]$ 上关于 $f(x)=e^x$ 的最佳近似多项式，使得绝对误差不超过 $0.5\times 10^{−4}$
	
	??? note "Answer"
	
		首先我们要确定 $n$：
		
		- 改写变量 $x=\frac{a+b}{2}+\frac{b-a}{2}t=\frac{1}{2}(t+1)$
		- 那么 $|R_n|\leq\frac{e}{(n+1)!}\times\frac{1}{2^{2n+1}}<\frac{1}{2}\times 10^{-4}$，解得 $n=4$
		
		接着我们找到 $T_5(t)$ 的根：$t_0=\frac{\cos⁡\pi}{10},\frac{\cos ⁡3\pi}{10},\frac{\cos⁡ 5\pi}{10},\frac{\cos ⁡7\pi}{10},\frac{\cos⁡ 9\pi}{10}$
		
		最后对变量做一点改变，得到：
		
		$$
		\begin{aligned}
		x_0&=\frac{1}{2}(\frac{\cos⁡\pi}{10}+1)\approx 0.98\\
		x_1&=\frac{1}{2}(\frac{\cos⁡3\pi}{10}+1)\approx 0.79\\
		x_2&=\frac{1}{2}(\frac{\cos⁡5\pi}{10}+1)\approx 0.50\\
		x_3&=\frac{1}{2}(\frac{\cos⁡7\pi}{10}+1)\approx 0.21\\
		x_4&=\frac{1}{2}(\frac{\cos⁡9\pi}{10}+1)\approx 0.02\\
		\end{aligned}
		$$
		
		最后使用插值点 $x_0,x_1,x_2,x_3,x_4$ 计算 $L_4(x)$
***
### Economization of Power Series

目标：给定 $P_n(x)\approx f(x)$，幂级数**经济化**（Economization）的目标是在确保精度损失最小的情况下，降低多项式的次数

考虑一个任意的 $n$ 阶多项式 $P_n(x)=a_nx^n+a_{n−1}x^{n−1}+\cdots+a_1x+a_0$​，对应的多项式 $P_{n−1}(x)$ 通过移除 $n$ 阶多项式 $Q_n(x)$（$x^n$ 项的系数为 $a_n​$）得到。那么：

$$
\begin{aligned}
\max _{x \in[-1,1]}\left|f(x)-P_{n-1}(x)\right| &\leq \max _{x \in[-1,1]}\left|f(x)-P_{n}(x)\right|+\max _{x \in[-1,1]}\left|Q_{n}(x)\right|\\&+\max _{x \in[-1,1]}\left|P_{n}(x)-P_{n-1}(x)-Q_{n}(x)\right|\\
&\leq \max _{x \in[-1,1]}\left|f(x)-P_{n}(x)\right|+\max _{x \in[-1,1]}\left|Q_{n}(x)\right|
\end{aligned}
$$

其中 $Q_n(x)$ 能够反映精度的损失，为了使得精确度的损失最小， $Q_n(x)$ 必须为 $a_n \cdot \frac{T_n(x)}{2^{n-1}}$

!!! example "Example"

	已知 $f(x)=e^x$ 在 $[−1,1]$ 上的 4 阶泰勒多项式为 $P4=1+x+\frac{x^2}{2}+\frac{x^3}{6}+\frac{x^4}{24}$​。它的截断误差的上界为 $|R_4(x)|\leq\frac{e}{5!}|x^5\approx 0.023$。请将这个近似多项式的次数降至 2
	
	??? note "Answer"
	
		$$
		\begin{aligned}
		T_4&=8x^4-8x^2+1\Rightarrow Q_4=\frac{1}{24}\times\frac{1}{2^3}T_4(x)=\frac{1}{24}(x^4-x^2+\frac{1}{8})\\
		P_3&=P_4-Q_4=\frac{1}{6}x^3+\frac{13}{24}x^2+x+\frac{191}{192}\\
		T_3&=4x^3-3x\Rightarrow Q_3=\frac{1}{6}\times\frac{1}{2^2}T_3(x)=\frac{1}{6}(x^3-\frac{3}{4}x)\\
		P_2&=P_3-Q_3=\frac{13}{24}x^2+\frac{9}{8}x+\frac{191}{192}\quad \|e^x-P_2(x)\|\approx 0.057
		\end{aligned}
		$$
		
		如果我们单纯取 $P_2(x)=1+x+\frac{x^2}{2}$，那么误差为 $\frac{e}{3!}\approx 0.45$
