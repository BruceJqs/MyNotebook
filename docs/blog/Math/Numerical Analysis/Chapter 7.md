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

$\mathbf{A}\in\mathbf{R}^{n\times n}$ 的谱半径定义为 $\rho(\mathbf{A})=\max\limits_{1\leq i\leq n}|\lambda_i|$，其中 $\lambda_i$ 是$\mathbf{A}$的特征值

![](../../../assets/Pasted%20image%2020250319112403.png)

!!! note "Theorem"

	如果 $A$ 是一个 $n\times n$ 的矩阵，那么对于任意一个自然范数 $\|\cdot\|$，有$\rho(\mathbf{A})\leq\|\mathbf{A}\|$
	
	!!! note "Proof"
	
		对于 $A$ 的任何特征值 $\lambda$ 以及特征向量 $\|\pmb{x}\|$，且 $\|\pmb{x}\|=1$，有：
		
		$$
		|\lambda|·\|\pmb{x}\|=\|\lambda\pmb{x}\|=\|\pmb{Ax}\|\leq\|\pmb{A}\|·\|\pmb{x}\|
		$$
		
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
***
### Gauss-Seidel Iterative Method

我们可以改进 Jacobi 迭代法，使得每次迭代时，都使用已经算出来的 $\mathbf{x}^{(k)}$ 的元素来计算 $\mathbf{x}^{(k)}$ 之后的元素，我们看线性方程组的解：

$$
\begin{aligned}
x_2^{(k)}&=\frac{1}{a_{22}}(\textcolor{red}{-a_{21}x_1^{(k)}}-a_{23}x_3^{(k-1)}-a_{24}x_4^{(k-1)}-\cdots-a_{2n}x_n^{(k-1)}+b_2)\\
x_3^{(k)}&=\frac{1}{a_{33}}(\textcolor{red}{-a_{31}x_1^{(k)}-a_{32}x_2^{(k)}}-a_{34}x_4^{(k-1)}-\cdots-a_{3n}x_n^{(k-1)}+b_3)\\
\cdots\\
x_n^{(k)}&=\frac{1}{a_{nn}}(\textcolor{red}{-a_{n1}x_1^{(k)}-a_{n2}x_2^{(k)}-a_{n3}x_3^{(k)}\cdots-a_{n,n-1}x_{n-1}^{(k)}}+b_n)
\end{aligned}
$$

也就是说，我们可以利用下面的公式来计算 $x_i^{(k)}$：

$$
x_i^{(k)}=\frac{-\sum\limits_{j=1}^{i-1}a_{ij}x_j^{(k)}-\sum\limits_{j=i+1}^na_{ij}x_j^{(k-1)}+b_i}{a_{ii}}
$$

结合之前 $\mathbf{D}$，$\mathbf{L}$，$\mathbf{U}$ 的定义，我们可以得到：

$$(\mathbf{D}-\mathbf{L})\mathbf{x}^{(k)}=\mathbf{U}\mathbf{x}^{(k-1)}+\mathbf{b}$$

即：

$$\mathbf{x}^{(k)}=(\mathbf{D}-\mathbf{L})^{-1}\mathbf{U}\mathbf{x}^{(k-1)}+(\mathbf{D}-\mathbf{L})^{-1}\mathbf{b}$$

引入符号 $\mathbf{T}_{g}=(\mathbf{D}-\mathbf{L})^{-1}\mathbf{U}$，$\mathbf{c}_{g}=(\mathbf{D}-\mathbf{L})^{-1}\mathbf{b}$，则 $\mathbf{x}=\mathbf{T}_{g}\mathbf{x}^{(k-1)}+\mathbf{c}_{g}$

其中 $\mathbf{T}_{g}$ 被称为 Gauss-Seidel 迭代矩阵（Gauss-Seidel Iteration Matrix）
***
### Convergence of Matrix Sequences

当满足以下条件时，矩阵$\mathbf{A}\in\mathbf{R}^{n\times n}$是收敛的：

$$\lim_{k\rightarrow\infty}(\mathbf{A}^k)_{ij}=\mathbf{0}$$

考虑我们上面得到的迭代式：$\mathbf{x}^{(k)}=\mathbf{T}\mathbf{x}^{(k-1)}+\mathbf{c}$

我们可以得到：

$$
\textcolor{red}{e^{(k)}}=\mathbf{x}^{(k)}-\mathbf{x}^*=\mathbf{T}(\mathbf{x}^{(k-1)}-\mathbf{x})=\textcolor{red}{\mathbf{T}e^{(k-1)}}
$$

根据上面的式子，我们有 $\mathbf{e}^{(k)}=\mathbf{T}^k\mathbf{e}^{(0)}$ ，因此：

$$
\|e^{(k)}\|\leq\|\mathbf{T}\|·\|e^{(k-1)}\|\leq\cdots\leq\|\mathbf{T}\|^k\|e^{(0)}\|
$$

- 充分条件：$\|\mathbf{T}\|<1\Rightarrow\|\mathbf{T}\|^k\rightarrow 0\text{ as }k\rightarrow\infty$
- 必要条件：$\pmb{e}^{(k)}\rightarrow\pmb{0}\text{ as }k\rightarrow\infty\Rightarrow\mathbf{T}^k\rightarrow\mathbf{O}$

!!! note "Theorems"

	=== "Theorem 01"
	
		以下命题是等价的：
		
		1. 矩阵 $\mathbf{A}\in\mathbf{R}^{n\times n}$ 是收敛的
		2. $\rho(\mathbf{A})<1$
		3. 对于某些自然范数 $\|\cdot\|$，有 $\lim\limits_{k\rightarrow\infty}\|\mathbf{A}^k\|=0$
		4. 对于任意的自然范数 $\|\cdot\|$，有 $\lim\limits_{k\rightarrow\infty}\|\mathbf{A}^k\|=0$
		5. 对于每一个 $\mathbf{x}\in\mathbf{R}^n$，有$\lim\limits_{k\rightarrow\infty}\mathbf{A}^k\mathbf{x}=\mathbf{0}$
	
	=== "Theorem 02"
	
		$\forall\pmb{x}^{(0)}\in\mathbf{R}^n$，由 $\mathbf{x}^{(k)}=\mathbf{T}\mathbf{x}^{(k-1)}+\mathbf{c}$ 定义的序列 $\{\pmb{x}^{(k)}\}_{k=0}^{\infty}$，当且仅当 $\rho(\mathbf{T})<1$ 时，会收敛到 $\pmb{x}=\mathbf{T}\pmb{x}+\pmb{c}$ 的唯一解
		
		??? note "Proof"
		
			$\Leftarrow$：
	
		    设 $\rho(\mathbf{T})<1$，那么
			
		    $$
		    \begin{aligned}
		    \mathbf{x}^{(k)}=&\mathbf{Tx}^{(k-1)}+\mathbf{c}\\
		    =&\mathbf{T}(\mathbf{Tx}^{(k-2)}+\mathbf{c})+\mathbf{c}\\
		    =&\mathbf{T}^2\mathbf{x}^{(k-2)}+(\mathbf{T}+\mathbf{I})\mathbf{c}\\
		    \vdots&\\
		    =&\mathbf{T}^k\mathbf{x}^{(0)}+(\mathbf{T}^{k-1}+\mathbf{T}^{k-2}+\cdots+\mathbf{T}+\mathbf{I})\mathbf{c}\\
		    \end{aligned}
		    $$
			
		    由于 $\rho(\mathbf{T})<1$，所以矩阵 $\mathbf{T}$ 是收敛的，且 $\lim\limits_{k\rightarrow\infty}\mathbf{T}^k\mathbf{x}^{(0)}=\mathbf{0}$
		    
		    由于 $\lim\limits_{k\rightarrow\infty}(\mathbf{T}^{k-1}+\mathbf{T}^{k-2}+\cdots+\mathbf{T}+\mathbf{I})\mathbf{c}=(\mathbf{I}-\mathbf{T})^{-1}\mathbf{c}$，所以 $\lim\limits_{k\rightarrow\infty}\mathbf{x}^{(k)}=(\mathbf{I}-\mathbf{T})^{-1}\mathbf{c}=\mathbf{x}$，这里的 $\mathbf{x}$ 就是$\mathbf{x}=\mathbf{Tx}+\mathbf{c}$ 的唯一解
			
		    $\Rightarrow$：
			
		    设 $\{\mathbf{x}^{(k)}\}_{k=0}^\infty$ 收敛到$\mathbf{x}=\mathbf{Tx}+\mathbf{c}$的唯一解，取任意一个向量$\mathbf{y}\in\mathbf{R}^n$，定义 $\mathbf{x}^{(0)}=\mathbf{x}-\mathbf{y}$，那么
		    
			$$
			\mathbf{x}-\mathbf{x}^{(k)}=(\mathbf{Tx}+\mathbf{c})-(\mathbf{Tx}^{(k-1)}+\mathbf{c})=\mathbf{T}(\mathbf{x}-\mathbf{x}^{(k-1)})
			$$
			
		    所以
			
		    $$
		    \mathbf{x}-\mathbf{x}^{(k)}=\mathbf{T}^k(\mathbf{x}-\mathbf{x}^{(0)})=\mathbf{T}^k\mathbf{y}
		    $$
		
		    因此
			
		    $$
		    \lim_{k\rightarrow\infty}\mathbf{T}^k\mathbf{y}=\lim_{k\rightarrow\infty}(\mathbf{x}-\mathbf{x}^{(k)})=\mathbf{0}
		    $$
		
		    由于 $\mathbf{y}$ 是任意的，根据矩阵的收敛性，$\rho(\mathbf{T})<1$
	
	=== "Theorem 03"
	
		如果对任意自然矩阵范数 $\|\mathbf{T}\|<1$，$\mathbf{c}$ 是给定的向量，那么由$\mathbf{x}^{(k+1)}=\mathbf{Tx}^{(k)}+\mathbf{c}$ 定义的序列 $\{\mathbf{x}^{(k)}\}_{k=0}^\infty$ 收敛到 $\mathbf{x}=\mathbf{Tx}+\mathbf{c}$ 的唯一解，且有误差界：

		- $\|\mathbf{x}-\mathbf{x}^{(k)}\|\leq\|\mathbf{T}\|^k\|\mathbf{x}^{(0)}-\mathbf{x}\|$
			- $\|\mathbf{x}-\mathbf{x}^{(k)}\|\approx\rho(\mathbf{T})^k\|\mathbf{x}^{(0)}-\mathbf{x}\|$
		- $\|\mathbf{x}-\mathbf{x}^{(k)}\|\leq\frac{\|\mathbf{T}\|^k}{1-\|\mathbf{T}\|}\|\mathbf{x}^{(1)}-\mathbf{x}^{(0)}\|$
		
		通过第二个式子，我们可以根据我们要的精度算出迭代次数 $k$
	
	=== "Theorem 04"
	
		如果 $\mathbf{A}$ 是一个严格对角占优矩阵，那么对于任意选择的初始近似解 $x^{(0)}$，无论使用 Jacobi 方法还是 Gauss-Seidel 方法，都可以让序列 $\{\pmb{x}^{(k)}\}_{k=0}^{\infty}$​ 收敛到 $\mathbf{A}\pmb{x}=\pmb{b}$ 的唯一解
		
		??? note "Proof(Hint)"
		
			只需证明 $\forall|\lambda|\geq 1$，有 $|\lambda I−T|\not=0$。也就是说，$\lambda$ 不能称为对应迭代矩阵 $T$ 的特征值
***
### Relaxation Methods

我们从剩余向量的视角来看 Gauss-Seidel 迭代法：

$$
\begin{aligned}
x_i^{(k)}&=\frac{-\sum\limits_{j=1}^{i-1}a_{ij}x_j^{(k)}-\sum\limits_{j=i+1}^na_{ij}x_j^{(k-1)}+b_i}{a_{ii}} \\
&=x_i^{(k-1)}+\frac{1}{a_{ii}}(b_i-\sum\limits_{j=1}^{i-1}a_{ij}x_j^{(k)}-\sum\limits_{j=i}^na_{ij}x_j^{(k-1)}) \\
&=x_i^{(k-1)}+\frac{r_i^{(k)}}{a_{ii}}
\end{aligned}
$$

我们可以添加一个参数 $\omega$，使得

$$
x_i^{(k)}=x_i^{(k-1)}+\omega\frac{r_i^{(k)}}{a_{ii}}
$$

这就是松弛法的基本思想，可以用来减少剩余向量的范数和加速收敛

根据 $\omega$ 的取值，松弛法可以分为：

1. $\omega<1$：欠松弛法（Under-Relaxation Methods）；可使由 Gauss-Seidel 方法不能收敛的方程组收敛；
2. $\omega=1$：退化为 Gauss-Seidel 迭代法；
3. $\omega>1$：超松弛法（Successive Over-Relaxation Methods, SOR）；可使收敛速度加快

用矩阵形式可以表述为：

$$
\begin{aligned}
x_i^{(k)}&=x_i^{(k-1)}+\omega\frac{r_i^{(k)}}{a_{ii}}\\
&=x_i^{(k-1)}+\frac{\omega}{a_{ii}}(b_i-\sum\limits_{j=1}^{i-1}a_{ij}x_j^{(k)}-\sum\limits_{j=i}^na_{ij}x_j^{(k-1)}) \\
&=(1-\omega)x_i^{(k-1)}+\frac{\omega}{a_{ii}}(b_i-\sum\limits_{j=1}^{i-1}a_{ij}x_j^{(k)}-\sum\limits_{j=i+1}^na_{ij}x_j^{(k-1)}) \\
\Rightarrow\mathbf{x}^{(k)}&=(1-\omega)\mathbf{x}^{(k-1)}+\omega\mathbf{D}^{-1}(\mathbf{b}+\mathbf{L}\mathbf{x}^{(k)}+\mathbf{U}\mathbf{x}^{(k-1)}) \\
(\mathbf{I}-\omega\mathbf{D}^{-1}\mathbf{L})\mathbf{x}^{(k)}&=((1-\omega)\mathbf{I}+\omega\mathbf{D}^{-1}\mathbf{U})\mathbf{x}^{(k-1)}+\omega\mathbf{D}^{-1}\mathbf{b} \\
\mathbf{x}^{(k)}&=(\mathbf{I}-\omega\mathbf{D}^{-1}\mathbf{L})^{-1}((1-\omega)\mathbf{I}+\omega\mathbf{D}^{-1}\mathbf{U})\mathbf{x}^{(k-1)}+(\mathbf{I}-\omega\mathbf{D}^{-1}\mathbf{L})^{-1}\omega\mathbf{D}^{-1}\mathbf{b} \\
\mathbf{x}^{(k)}&=(\mathbf{D}-\omega\mathbf{L})^{-1}((1-\omega)\mathbf{D}+\omega\mathbf{U})\mathbf{x}^{(k-1)}+\omega(\mathbf{D}-\omega\mathbf{L})^{-1}\mathbf{b} \\
\end{aligned}
$$

记 $\mathbf{T}_{\omega}=(\mathbf{D}-\omega\mathbf{L})^{-1}((1-\omega)\mathbf{D}+\omega\mathbf{U})$，$\mathbf{c}_{\omega}=\omega(\mathbf{D}-\omega\mathbf{L})^{-1}\mathbf{b}$，则 SOR 方法的迭代格式为$\mathbf{x}^{(k)}=\mathbf{T}_{\omega}\mathbf{x}^{(k-1)}+\mathbf{c}_{\omega}$

!!! note "Theorems"

	=== "Theorem 01"
	
		Kahan 定理：如果 $a_{ii}\neq 0(i=1,2,\cdots,n)$，那么 $\rho(\mathbf{T}_{\omega})\geq|\omega-1|$。这表明，SOR 方法当且仅当 $\omega\in(0,2)$ 时收敛
	
	=== "Theorem 02"
	
		Ostrowski-Reich 定理：如果 $\mathbf{A}$ 是一个正定矩阵，并且 $\omega\in(0,2)$，那么 SOR 方法对于任意的初始近似向量 $\mathbf{x}^{(0)}\in\mathbf{R}^n$ 都收敛
	
	=== "Theorem 03"
	
		如果 $\mathbf{A}$ 是一个正定的三对角矩阵，那么 $\rho(\mathbf{T}_{g})=[\rho(\mathbf{T}_{j})]^2<1$，并且 SOR 方法的最佳 $\omega$ 选择是：
		
		$$
		\omega_{\text{opt}}=\frac{2}{1+\sqrt{1-[\rho(\mathbf{T}_{j})]^2}}
		$$
		
		由此选择的 $\omega$，有 $\rho(\mathbf{T}_{\omega})=\omega-1$
***
## Error Bounds and Iterative Refinement

### Error Bounds

对于线性方程组 $\mathbf{Ax}=\mathbf{b}$ ，$\mathbf{A}$ 是非奇异的。如果 $\mathbf{A}$ 和 $\mathbf{b}$ 存在误差，那么解 $\mathbf{x}$ 也会存在误差

#### Accurate $\mathbf{A}$，Erroneous $\mathbf{b}$ 

即 $\mathbf{Ax}=\mathbf{b}$ 经过了扰动变为 $\mathbf{A(x+\delta x)}=\mathbf{b}+\delta\mathbf{b}$ 。所以有：

$$
\begin{aligned}
\mathbf{A}\delta\mathbf{x}&=\delta\mathbf{b}\\
\Rightarrow \delta\mathbf{x}&=\mathbf{A}^{-1}\delta\mathbf{b}\\
\end{aligned}
$$

根据[定理](https://brucejqs.github.io/MyNotebook/blog/Math/Numerical%20Analysis/Chapter%207/#eigenvalues-and-eigenvectors)，我们有：

$$
\begin{aligned}
\|\delta\mathbf{x}\|&\leq\|\mathbf{A}^{-1}\|\|\delta\mathbf{b}\|\\
\mathbf{b}=\mathbf{Ax}\Rightarrow\|&\mathbf{b}\|=\|\mathbf{Ax}\|\leq\|\mathbf{A}\|\|\mathbf{x}\|\\
\therefore \frac{\|\delta\mathbf{x}\|}{\|\mathbf{x}\|}&\leq\|\mathbf{A}\|\|\mathbf{A}^{-1}\|\frac{\|\delta\mathbf{b}\|}{\|\mathbf{b}\|}
\end{aligned}
$$

其中 $\|\mathbf{A}\|\|\mathbf{A}^{-1}\|$ 被称为相对放大因子（Relative Amplification Factor），也称为非奇异矩阵 $A$ 相对于范数 $\|\cdot\|$ 的条件数（记为 $K(\mathbf{A})$）

当 $K(\mathbf{A})$ 很大时，$\mathbf{A}$ 是病态的，当 $K(\mathbf{A})$ 接近于 $1$ 时，$\mathbf{A}$ 是良态的
***
#### Erroneous $\mathbf{A}$，Accurate $\mathbf{b}$

即 $\mathbf{Ax}=\mathbf{b}$ 经过了扰动变为 $\mathbf{(A+\delta A)(x+\delta x)}=\mathbf{b}$ 。所以有：

$$(\mathbf{A}+\delta\mathbf{A})\delta\mathbf{x}+\mathbf{x}\delta\mathbf{A}=0$$

这里的 $\delta\mathbf{A}$ 往往是一个小量，我们有如下定理：

!!! note "Theorems"

	=== "Theorem 01"

		对于矩阵 $\mathbf{F}$，若 $\|\mathbf{F}\|<1$，则 $\mathbf{I}\pm\mathbf{F}$ 是非奇异的，且
	
		$$
		\left\|\left(\mathbf{I}\pm \mathbf{F}\right)^{-1}\right\|\leq\frac1{1-\left\|\mathbf{F}\right\|}
		$$
	
		??? note "$\mathbf{I} - \mathbf{F}$ 情况的证明"
		
			因为 $\|\mathbf{-F}\|=\|\mathbf{F}\|<1$，所以我们将 $\mathbf{-F}$ 替换 $\mathbf{F}$ ，就可以得到 $\mathbf{I+F}$ 情况的证明
			
			![](../../../assets/Pasted%20image%2020250326102437.png)
	
	=== "Theorem 02"
	
		$$
		\|\mathbf{A}^{-1}\|_{p}=\frac{1}{\min\frac{\left|\left|\mathbf{A}\mathbf{x}\right|\right|p}{\left|\left|\mathbf{x}\right|\right|p}}
		$$
	
		??? note "证明"
	
			$$
			\begin{aligned}
			&\|\mathbf{A}^{-1}\|_{p}=\max_{\mathbf{x}\neq0}\frac{\|\mathbf{A}^{-1}\mathbf{x}\|_{p}}{\|\mathbf{x}\|_{p}})=\max_{\mathbf{A}\mathbf{x}\neq0}\frac{\| \mathbf{A}^{-1}\mathbf{A}\mathbf{x}\|p}{\parallel \mathbf{A}^{-1}\mathbf{x}\|p} \\
			=&\max_{\mathbf{x}\neq0}\frac{\|\mathbf{x}\|p}{\|\mathbf{A}\mathbf{x}\|p}=\max_{\mathbf{x}\neq0}\frac{1}{\frac{\|\mathbf{A}\mathbf{x}\|p}{\|\mathbf{x}\|p}}=\frac{1}{\min\frac{\left|\left|\mathbf{A}\mathbf{x}\right|\right|p}{\left|\left|\mathbf{x}\right|\right|p}}
			\end{aligned}
			$$


我们有 $\mathbf{(A+\delta A)}=\mathbf{A}\mathbf{(I+A^{-1}\delta A)}$，根据上面的定理 2：

$$
\|\mathbf{A^{-1}\delta A}\|\leq\|\mathbf{A^{-1}}\|\|\mathbf{\delta A}\|=\frac{\|\mathbf{\delta A}\|}{\min\frac{\left|\left|\mathbf{A}\mathbf{x_1}\right|\right|p}{\left|\left|\mathbf{x_1}\right|\right|p}}
$$

因为 $\|\delta\mathbf{A}\|$ 相对于 $\|\mathbf{A}\|$ 很小，往往有 $\|\mathbf{A^{-1}\delta A}\|\leq 1$，所以 $\mathbf{I+A^{-1}\delta A}$ 是非奇异的，由定理 1：

$$
\|\mathbf{(I+A^{-1}\delta A)^{-1}}\|\leq\frac{1}{1-\|\mathbf{A^{-1}\delta A}\|}
$$

因此我们有：

$$
\begin{aligned}
(\mathbf{A}+\delta\mathbf{A})\delta\mathbf{x}+\mathbf{x}\delta\mathbf{A}&=0\\
\mathbf{A}(I+\mathbf{A}^{-1}\delta\mathbf{A})\delta\mathbf{x}&=-\mathbf{x}\delta\mathbf{A}\\
 \delta\mathbf{x} &= -(I+\mathbf{A}^{-1}\delta\mathbf{A})^{-1}\mathbf{A}^{-1}\mathbf{x}\delta\mathbf{A}\\
 \therefore\|\delta\mathbf{x}\| &\leq\|\mathbf{(I+A^{-1}\delta A)^{-1}}\|\|\mathbf{A}^{-1}\|\|\mathbf{x}\|\|\delta\mathbf{A}\|\\
&\leq \frac{\|\mathbf{A}^{-1}\|\|\mathbf{x}\|\|\delta\mathbf{A}\|}{1-\|\mathbf{A}^{-1}\|\|\delta\mathbf{A}\|}=\frac{K(\mathbf{A})\frac{\|\delta\mathbf{A}\|}{\|\mathbf{A}\|}}{1-K(\mathbf{A})\frac{\|\delta\mathbf{A}\|}{\|\mathbf{A}\|}}
\end{aligned}
$$

***
#### Erroneous $\mathbf{A}$，Erroneous $\mathbf{b}$

即 $\mathbf{Ax}=\mathbf{b}$ 经过了扰动变为 $\mathbf{(A+\delta A)(x+\delta x)}=\mathbf{b}+\delta\mathbf{b}$ 。所以有：

$$
\begin{aligned}
(\mathbf{A}+\delta\mathbf{A})\delta\mathbf{x}+\mathbf{x}\delta\mathbf{A}&=\delta\mathbf{b}\\
\end{aligned}
$$

所以，当 $\|\delta\mathbf{A}\|<\frac{1}{\|\mathbf{A}^{-1}\|}$时，有：

$$
\begin{aligned}
\delta\mathbf{x}&=(I+\mathbf{A}^{-1}\delta\mathbf{A})^{-1}\mathbf{A}^{-1}(\delta\mathbf{b}-\mathbf{x}\delta\mathbf{A})\\
\therefore\|\delta\mathbf{x}\|&\leq \frac{\|\mathbf{A}^{-1}\|}{1-\|\mathbf{A}^{-1}\|\|\delta\mathbf{A}\|}\|\delta\mathbf{b}-\mathbf{x}\delta\mathbf{A}\|\\
&\leq \frac{\|\mathbf{A}^{-1}\|}{1-\|\mathbf{A}^{-1}\|\|\delta\mathbf{A}\|}(\|\delta\mathbf{b}\|+\|\mathbf{x}\|\|\delta\mathbf{A}\|)\\
&\leq \frac{K(\mathbf{A})}{1-K(\mathbf{A})\frac{\|\delta\mathbf{A}\|}{\|\mathbf{A}\|}}(\frac{\|\delta\mathbf{b}\|}{\|\mathbf{A}\|}+\frac{\|\mathbf{x}\|\|\delta\mathbf{A}\|}{\|\mathbf{A}\|})\\
&\leq \frac{K(\mathbf{A})}{1-K(\mathbf{A})\frac{\|\delta\mathbf{A}\|}{\|\mathbf{A}\|}}(\frac{\|\delta\mathbf{b}\|}{\|\mathbf{A}\|\|\mathbf{x}\|}+\frac{\|\delta\mathbf{A}\|}{\|\mathbf{A}\|})\|\mathbf{x}\|\\
&\leq \frac{K(\mathbf{A})}{1-K(\mathbf{A})\frac{\|\delta\mathbf{A}\|}{\|\mathbf{A}\|}}(\frac{\|\delta\mathbf{b}\|}{\|\mathbf{A}\mathbf{x}\|}+\frac{\|\delta\mathbf{A}\|}{\|\mathbf{A}\|})\|\mathbf{x}\|\\
&\leq \frac{K(\mathbf{A})}{1-K(\mathbf{A})\frac{\|\delta\mathbf{A}\|}{\|\mathbf{A}\|}}(\frac{\|\delta\mathbf{b}\|}{\|\mathbf{b}\|}+\frac{\|\delta\mathbf{A}\|}{\|\mathbf{A}\|})\|\mathbf{x}\|\\
\therefore\frac{\|\delta\mathbf{x}\|}{\|\mathbf{x}\|}&\leq\frac{K(\mathbf{A})}{1-K(\mathbf{A})\frac{\|\delta\mathbf{A}\|}{\|\mathbf{A}\|}}(\frac{\|\delta\mathbf{b}\|}{\|\mathbf{b}\|}+\frac{\|\delta\mathbf{A}\|}{\|\mathbf{A}\|})
\end{aligned}
$$

***
#### Properties of $K(\mathbf{A})$

我们记非奇异矩阵 $A$ 相对于范数 $\|\cdot\|$ 的条件数为：

$$
K(\mathbf{A})=\|\mathbf{A}\|\|\mathbf{A}^{-1}\|
$$

当 $K(\mathbf{A})$ 很大时，$\mathbf{A}$ 是病态的，当 $K(\mathbf{A})$ 接近于 $1$ 时，$\mathbf{A}$ 是良态的

我们有如下性质：

- $K(\mathbf{A})_p\geq 1$ 对所有的自然范数 $\|\cdot\|_p$ 成立
- 如果 $\mathbf{A}$ 是对称的，那么 $K(\mathbf{A})_2=\frac{|\lambda_{max}|}{|\lambda_{min}|}$，其中 $\lambda_{max}$ 和 $\lambda_{min}$ 分别是 $\mathbf{A}$ 的最大和最小特征值
- $K(a\mathbf{A})=K(\mathbf{A})$，其中 $a$ 是一个非零常数
- $K(\mathbf{A})_2=1$ 当且仅当 $\mathbf{A}$ 是正交矩阵($\mathbf{A}^T\mathbf{A}=\mathbf{I}$)
- $K(\mathbf{RA})_2 =K(\mathbf{AR})_2 = K(\mathbf{A})_2$，其中 $\mathbf{R}$ 是一个正交矩阵
***
### Iterative Refinement

!!! note "Theorem"

	假设 $\vec{x}^*$ 是 $\mathbf{A}\vec{x}=\vec{b}$ 的估计解，其中 $\mathbf{A}$ 是一个非奇异矩阵，$\vec{r}=\vec{b}-\mathbf{A}\vec{x}$ 是 $\vec{x}^*$ 的残差向量，那么对于所有的范式，$\|\vec{x}-\vec{x}^*\|\leq\|\vec{r}\|·\|\mathbf{A}^{-1}\|$，并且如果 $\vec{x}\neq\vec{0}$ 且 $\vec{b}\neq\vec{0}$：
	
	$$
	\frac{\|\vec{x}-\vec{x}^*\|}{\|\vec{x}\|}\leq K(\mathbf{A})\frac{\|\vec{r}\|}{\|\vec{b}\|}
	$$
	

对于迭代计算，我们有以下步骤：

1. $\mathbf{A}\vec{x}=\vec{b}\Rightarrow\text{ approximation }\vec{x_1}$
2. $\vec{r_1}=\vec{b}-\mathbf{A}\vec{x_1}$
3. $\mathbf{A}\vec{d_1}=\vec{r_1}\Rightarrow\vec{d_1}$（如果 $\vec{d_1}$ 是精确的，那么 $\vec{x_2}=\vec{x_1}+\mathbf{A}^{-1}(\vec{b}-\mathbf{A}\vec{x_1})=\mathbf{A}^{-1}\vec{b}$ 是精确的）
4. $\vec{x_2}=\vec{x_1}+\vec{d_1}$









