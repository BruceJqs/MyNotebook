---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 07 : Iterative Techniques in Matrix Algebra

> 这一章和第六章类似，目标还是希望能解决线性方程组 $\pmb{A}\vec{x}=\vec{b}$

!!! abstract "Idea"

	类似求解 $f(x)=0$ 用的不动点迭代：
	
	- 先将 $\pmb{A}\vec{x}=\vec{b}$ 转化为等价的 $\vec{x}=\pmb{T}\vec{x}+\vec{c}$ 的形式
	- 然后从初始猜测值 $\vec{x}^{(0)}$ 开始 $\vec{x}^{(k+1)}=\pmb{T}\vec{x}^{(k)}+\vec{c}$ 的迭代，得到（收敛的）序列 ${\vec{x}^{(k)}}$

上述思路的优势在于：

- 可以通过迭代次数来控制精度
- 迭代技术被实际运用于求解**稀疏的**（Sparse）线性方程组
***
## Norms of Vectors and Matrices

### Vector Norms

$\mathbf{R}^n$ 上的向量范数是一个函数 $\|\cdot\|:\mathbf{R}^n\rightarrow\mathbf{R}$，满足下列条件：

1. 正定：$\|\vec{x}\|\geq 0$，且 $\|\vec{x}\|=0\Leftrightarrow\vec{x}=\vec{\mathbf{0}}$；（$\mathbf{x}\in\mathbf{R}^n$）
2. 齐次：$\|\alpha\vec{x}\|=|\alpha|\|\vec{x}\|$，其中 $\alpha\in\mathbf{R},\vec{x}\in\mathbf{R}^n$
3. 三角不等式：$\|\vec{x}+\vec{y}\|\leq\|\vec{x}\|+\|\vec{y}\|$（$\vec{x},\vec{y}\in\mathbf{R}^n$）

一些常用的范数：

- $\|\vec{x}\|_1=\sum\limits_{i=1}^n|x_i|$
- $\|\vec{x}\|_2=\sqrt{\sum\limits_{i=1}^n|x_i|^2}$（欧几里得范数）
- $\|\vec{x}\|_p=(\sum\limits_{i=1}^n|x_i|^p)^{\frac{1}{p}}$
- $\|\mathbf{x}\|_\infty=\max\limits_{1\leq i\leq n}|x_i|$
- $\lim\limits_{p\rightarrow\infty}\|\vec{x}\|_p=\|\vec{x}\|_{\infty}$
***
#### Convergence of Vector Sequences

$\mathbf{R}^n$ 上的向量序列 $\{\vec{x}^{(k)}\}_{k=1}^\infty$ 按照向量范数 $\|\cdot\|$ 收敛到向量 $\vec{x}$，当且仅当对于任意的 $\epsilon>0$，存在整数 $N(\epsilon)$，使得当 $k>N(\epsilon)$ 时，有 $\|\vec{x}^{(k)}-\vec{x}\|<\epsilon$。

对于无穷范数，如果向量序列 $\{\vec{x}^{(k)}\}_{k=1}^\infty$ 按照无穷范数 $\|\cdot\|_\infty$ 收敛到向量 $\vec{x}$，当且仅当对于任意 $i=1,2,...,n$，有 $\lim\limits_{k\rightarrow\infty}x_i^{(k)}=x_i$
***
#### Equivalence of Vector Norms

等价性定义：$\mathbf{R}^n$上的向量范数 $\|\cdot\|_A$ 和 $\|\cdot\|_B$ 等价，当且仅当存在正常数 $C_1,C_2$，使得对于任意的 $\vec{x}\in\mathbf{R}^n$，有 $C_1\|\vec{x}\|_B\leq\|\vec{x}\|_A\leq C_2\|\vec{x}\|_B$

实际上，$\mathbf{R}^n$ 上的所有范数都是等价的。也就是说，如果 $\|\cdot\|_A$ 和 $\|\cdot\|_B$ 是 $\mathbf{R}^n$ 上的任意两个范数，并且 $\{\vec{x}^{(k)}\}_{k=1}^\infty$ 按照 $\|\cdot\|$ 收敛到 $\vec{x}$，那么 $\{\vec{x}^{(k)}\}_{k=1}^\infty$ 也按照 $\|\cdot\|_B$ 收敛到 $\vec{x}$
***
### Matrix Norms

$\mathbf{R}^{n\times n}$ 上的矩阵范数是一个函数 $\|\cdot\|:\mathbf{R}^{n\times n}\rightarrow\mathbf{R}$，满足下列条件：

1. $\|\mathbf{A}\|\geq 0$，且 $\|\mathbf{A}\|=0$ 当且仅当 $\mathbf{A}$ 是零矩阵（$\mathbf{A}\in\mathbf{R}^{n\times n}$）
2. $\|\alpha\mathbf{A}\|=|\alpha|\|\mathbf{A}\|$，其中 $\alpha\in\mathbf{R},\mathbf{A}\in\mathbf{R}^{n\times n}$
3. $\|\mathbf{A}+\mathbf{B}\|\leq\|\mathbf{A}\|+\|\mathbf{B}\|$（$\mathbf{A},\mathbf{B}\in\mathbf{R}^{n\times n}$）
4. $\|\mathbf{AB}\|\leq\|\mathbf{A}\|\|\mathbf{B}\|$（$\mathbf{A},\mathbf{B}\in\mathbf{R}^{n\times n}$）

我们定义矩阵 $\mathbf{A}$ 和 $\mathbf{B}$ 之间的距离为 $\|\mathbf{A}-\mathbf{B}\|$
***
#### Frobenius Norm

$\mathbf{A}\in\mathbf{R}^{n\times n}$的 Frobenius 范数是 $\mathbf{A}$ 的所有元素的平方和的平方根，即 $\|\mathbf{A}\|_F=\sqrt{\sum\limits_{i=1}^n\sum\limits_{j=1}^n|a_{ij}|^2}$
***
#### Natural Norm

如果 $\|\cdot\|$ 是 $\mathbf{R}^{n\times n}$ 上的向量范数，那么 $\|\mathbf{A}\|=\max\limits_{\|\mathbf{x}\|=1}\|\mathbf{A}\vec{x}\|$ 是 $\mathbf{R}^{n\times n}$上的矩阵范数，称为与向量范数 $\|\cdot\|$ 相关的自然矩阵范数

- $\|\mathbf{A}\|=\max\limits_{\|\mathbf{x}\|=1}\|\mathbf{A}\vec{x}\|$ 也可以写成 $\|\mathbf{A}\|=\max\limits_{\vec{x}\neq\vec{0}}\frac{\|\mathbf{A}\vec{x}\|}{\|\vec{x}\|}$

常用的自然矩阵范数有：

1. $p$-范数：$\|\mathbf{A}\|_p=\max\limits_{\mathbf{x}\neq\mathbf{0}}\frac{\|\mathbf{Ax}\|_p}{\|\mathbf{x}\|_p}$，其中 $p\geq 1$；
2. 无穷范数：$\|\mathbf{A}\|_\infty=\max\limits_{1\leq i\leq n}\sum\limits_{j=1}^n|a_{ij}|$；也就是 $\mathbf{A}$ 的所有行和的最大值；
3. $1$-范数：$\|\mathbf{A}\|_1=\max\limits_{1\leq j\leq n}\sum\limits_{i=1}^n|a_{ij}|$；也就是 $\mathbf{A}$ 的所有列和的最大值；
4. $2$-范数（Spectral Norm）：$\|\mathbf{A}\|_2=\sqrt{\lambda_{\max}(\mathbf{A}^T\mathbf{A})}$，其中 $\lambda_{\max}(\mathbf{A}^T\mathbf{A})$ 是 $\mathbf{A}^T\mathbf{A}$ 的最大特征值

!!! note "Proof for $\|\mathbf{A}\|_\infty=\max\limits_{1\leq i\leq n}\sum\limits_{j=1}^n|a_{ij}|$"

	1. 证明 $\|A\|_{\infty}=\max\limits_{\|\vec{x}\|_{\infty}=1}\|A\vec{x}\|_{\infty}\leq\max\limits_{1\leq i\leq n}\sum\limits_{j=1}^n|a_{ij}|$
    
    $$
	\|A\vec{x}\|_{\infty}=\max\limits_{⁡1\leq i\leq n}|(A\vec{x})_i|=\max\limits_{⁡1\leq i\leq n}\sum\limits_{j=1}^na_{ij}x_j|\leq\max\limits_{⁡1\leq i\leq n}\sum\limits_{j=1}^n|a_{ij}|⋅\max\limits_{1\leq i\leq n}|x_j|
	$$
	
    2. 证明 $\|A\|_{\infty}=\max\limits_{\|\vec{x}\|_{\infty}=1}\|A\vec{x}\|_{\infty}\geq\max\limits_{⁡1\leq i\leq n}\sum\limits_{j=1}^n|a_{ij}|$
    
    - 令第 $p$ 行为最大行，即满足 $\sum\limits_{j=1}^n|a_{pj}|=\max\limits_{⁡1\leq i\leq n}\sum\limits_{j=1}^n|a_{ij}|$
    - 取一个特殊的单位向量 $\vec{x}$ 使得 $x_j=\begin{cases}1,\text{if }a_{pj}\geq 0\\−1,\text{if }a_{pj}<0\end{cases}$
    
    $$
    \|A\vec{x}\|_{\infty}=\max\limits_{⁡1\leq i\leq n}|\sum\limits_{j=1}^na_{ij}x_j|\geq|\sum\limits_{j=1}^na_{pj}x_j|=|\sum\limits_{j=1}^n|a_{pj}||=\max\limits_{⁡1\leq i\leq n}\sum\limits_{j=1}^n|a_{ij}|
    $$
    
***
## Eigenvalues and Eigenvectors

$\mathbf{A}\in\mathbf{R}^{n\times n}$ 的谱半径定义为 $\rho(\mathbf{A})=\max\limits_{1\leq i\leq n}|\lambda_i|$，其中 $\lambda_i$ 是$\mathbf{A}$的特征值，这里的特征值可以是复数

![](../../../assets/Pasted%20image%2020250319112403.png)

!!! note "Theorem"

	如果 $A$ 是一个 $n\times n$ 的矩阵，那么对于任意一个自然范数 $\|\cdot\|$，有$\rho(\mathbf{A})\leq\|\mathbf{A}\|$
	
	!!! note "Proof"
	
		对于 $A$ 的任何特征值 $\lambda$ 以及特征向量 $\|\pmb{x}\|$，且 $\|\pmb{x}\|=1$，有：
		
		$$
		|\lambda|·\|\pmb{x}\|=\|\lambda\pmb{x}\|=\|\pmb{Ax}\|\leq\|\pmb{A}\|·\|\pmb{x}\|
		$$
		
***
### Convergence of Matrix Sequences

当满足以下条件时，矩阵$\mathbf{A}\in\mathbf{R}^{n\times n}$是收敛的：

$$\lim_{k\rightarrow\infty}(\mathbf{A}^k)_{ij}=\mathbf{0}$$

以下命题是等价的：

1. 矩阵 $\mathbf{A}\in\mathbf{R}^{n\times n}$ 是收敛的
2. $\rho(\mathbf{A})<1$
3. 对于某些自然范数 $\|\cdot\|$，有 $\lim\limits_{k\rightarrow\infty}\|\mathbf{A}^k\|=0$
4. 对于任意的自然范数 $\|\cdot\|$，有 $\lim\limits_{k\rightarrow\infty}\|\mathbf{A}^k\|=0$
5. 对于每一个 $\mathbf{x}\in\mathbf{R}^n$，有$\lim\limits_{k\rightarrow\infty}\mathbf{A}^k\mathbf{x}=\mathbf{0}$
***
## Iterative Techniques for Solving Linear Systems

### Jacobi Iterative Method

对于线性方程组 $\mathbf{A}\pmb{x}=\pmb{b}$，如果我们有 $a_{ii}\not=0$，可以解得：

$$
\begin{cases}
x_1=\frac{1}{a_{11}}(-a_{12}x_2-\cdots-a_{1n}x_n+b_1)\\
x_2=\frac{1}{a_{22}}(-a_{21}x_1-\cdots-a_{2n}x_n+b_2)\\
\cdots\\
x_n=\frac{1}{a_{nn}}(-a_{n1}x_1-\cdots-a_{n,n-1}x_{n-1}+b_n)
\end{cases}
$$

记矩阵 $\mathbf{A}\in\mathbf{R}^{n\times n}$ 的下三角部分为 $-\mathbf{L}$，上三角部分为 $-\mathbf{U}$，对角线部分为 $\mathbf{D}$，即 $\mathbf{A}=\mathbf{D}-\mathbf{L}-\mathbf{U}$

![](../../../assets/Pasted%20image%2020250319112354.png)

所以方程组 $\mathbf{Ax}=\mathbf{b}$ 可以写成 $\mathbf{Dx}=(\mathbf{L}+\mathbf{U})\mathbf{x}+\mathbf{b}$

即 $\mathbf{x}=\mathbf{D}^{-1}(\mathbf{L}+\mathbf{U})\mathbf{x}+\mathbf{D}^{-1}\mathbf{b}$，引入符号 $\mathbf{T}_j=\mathbf{D}^{-1}(\mathbf{L}+\mathbf{U})$，$\mathbf{c}_j=\mathbf{D}^{-1}\mathbf{b}$，则 $\mathbf{x}=\mathbf{T}_j\mathbf{x}+\mathbf{c}_j$

对于第 $k$ 次高斯消元，我们有 $\mathbf{x}^{(k+1)}=\mathbf{T}_j\mathbf{x}^{(k)}+\mathbf{c}_j$，其中 $\mathbf{x}^{(0)}$ 是初始猜测值，$\mathbf{T}_j$ 被称为 Jacobi 迭代矩阵（Jacobi Iteration Matrix）

!!! note "Jacobi Iterative Method"

	对于给定的初始近似解 $\pmb{x}^{(0)}$，求解 $\mathbf{A}\pmb{x}=\pmb{b}$
	
	- 输入：方程和未知数的个数 $n$，矩阵元素 $a[][]$，常数项 $b[]$，初始近似解 $X0[]$，容忍值 TOL，最大迭代次数 $N_{\max}$
	- 输出：近似解 $X[]$ 或错误信息
	
	```c
	Step 1  Set k = 1;
	Step 2  while (k <= N_max) do step 3-6
	        Step 3  for i = 1, ..., n
	                    Set X_i = (b_i - sum(j=1, j!=i, j<=n, a_ij X0_j)) / a_ii;  /* compute x_k */
	        Step 4  if norm(X - X_0)_infty = max(1<=i<=n, X_i - X0_i) < TOL then Output(X[]);
	                STOP;   /* successful */
	        Step 5  for i = 1, ..., n  Set X0[] = X[];  // update X0
	        Step 6  Set k++;
	Step 7  Output (Maximum number of iterations exceeded);
	        STOP.    /* unsuccessful */
	```







