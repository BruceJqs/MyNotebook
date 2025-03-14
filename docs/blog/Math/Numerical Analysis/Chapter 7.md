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

