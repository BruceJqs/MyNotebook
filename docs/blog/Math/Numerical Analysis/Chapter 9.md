---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 09 : Approximating Eigenvalues

## The Power Method

### The Original Method

假设：$\mathbf{A}$ 是一个 $n\times n$ 的矩阵，且恰有一个特征值 $\lambda_1$ 的绝对值最大，有 $n$ 个特征值 $\lambda_1,\lambda_2,\cdots,\lambda_n$（$|\lambda_1|>|\lambda_2|\geq\cdots\geq|\lambda_n|$），对应为 $n$ 个线性独立的特征向量 $\mathbf{v}_1,\mathbf{v}_2,\cdots,\mathbf{v}_n$

思路：从任意一个 $\vec{x}^{(0)}\neq\vec{0}$ 和 $(\vec{x}^{(0)},\vec{v_1})\neq\vec{0}$ 出发

$$
\begin{aligned}
\vec{x}^{(0)}&=\sum\limits_{j=1}^n\beta_j\vec{v}_j,\beta_1\neq 0\\
\vec{x}^{(1)}&=\mathbf{A}\vec{x}^{(0)}=\sum\limits_{j=1}^n\beta_j\mathbf{A}\vec{v}_j=\sum\limits_{j=1}^n\beta_j\lambda_j\vec{v}_j\\
\vec{x}^{(2)}&=\mathbf{A}\vec{x}^{(1)}=\sum\limits_{j=1}^n\beta_j\mathbf{A}\vec{v}_j=\sum\limits_{j=1}^n\beta_j\lambda_j^2\vec{v}_j\\
\cdots\\
\vec{x}^{(k)}&=\mathbf{A}\vec{x}^{(k-1)}=\sum\limits_{j=1}^n\beta_j\mathbf{A}\vec{v}_j=\sum\limits_{j=1}^n\beta_j\lambda_j^k\vec{v}_j=\lambda_1^k\sum\limits_{j=1}^n\beta_j\left(\frac{\lambda_j}{\lambda_1}\right)^k\vec{v}_j\\
\therefore \lim\limits_{k\rightarrow\infty}\mathbf{A}^k\vec{x}&=\lim\limits_{k\rightarrow\infty}\lambda_1^k\sum\limits_{j=1}^n\beta_j\left(\frac{\lambda_j}{\lambda_1}\right)^k\vec{v}_j=\lim\limits_{k\rightarrow\infty}\lambda_1^k\beta_1\vec{v}_1
\end{aligned}
$$

如果 $|\lambda_1|<1$，则 $\lim\limits_{k\to\infty}\mathbf{A}^k\mathbf{x}=0$，即 $\mathbf{x}$ 收敛到 $\vec{0}$；如果 $|\lambda_1|>1$，则序列发散

对足够大的 $k$，$\mathbf{x}^{(k)},\mathbf{x}^{(k-1)}$ 可以近似地表示为：

$$
\mathbf{x}^{(k)}\approx\beta_1\lambda_1^k\mathbf{v}_1, \quad\mathbf{x}^{(k-1)}\approx\beta_1\lambda_1^{k-1}\mathbf{v}_1\quad
\Rightarrow\quad\frac{\mathbf{x}^{(k)}}{\mathbf{x}^{(k-1)}}\approx\lambda_1
$$

所以，我们可以通过迭代 $\mathbf{x}^{(k)}=\mathbf{A}\mathbf{x}^{(k-1)}$ 来逼近 $\lambda_1$
***
#### Normalization

实际计算时，为了避免计算过程中出现绝对值过大或过小的数参加运算，通常在每步迭代时，将向量“归一化”即用的按模最大的分量。

我们需要对 $\mathbf{x}^{(k)}$ 进行归一化，使得 $\|\mathbf{x}^{(k)}\|_\infty=1$，即

$$
\begin{aligned}
\mathbf{u}^{(k-1)}=\frac{\mathbf{x}^{(k-1)}}{\|\mathbf{x}^{(k-1)}\|_\infty},\quad \mathbf{x}^{(k)}=\mathbf{A}\mathbf{u}^{(k-1)}\\
\Rightarrow \mathbf{u}^{(k)}=\frac{\mathbf{x}^{(k)}}{\|\mathbf{x}^{(k)}\|_\infty},\quad \lambda_1\approx\frac{\mathbf{x}_{i}^{(k)}}{\mathbf{u}_{i}^{(k-1)}}=\|\mathbf{x}^{(k)}\|_\infty
\end{aligned}
$$

!!! note "Pseudo Code"

	从非零初始向量开始，近似求解规模为 $n\times n$ 的矩阵 $A$ 的主特征值及其特征向量
	
	- 输入：维度 $n$，矩阵 $a[][]$，初始向量 $x0[]$，容忍值 TOL，最大迭代次数 $N_{\max}$
	- 输出：近似特征值 $\lambda$，近似（规范化的）特征向量
	
	```c++
	Step 1  Set k = 1;
	Step 2  Find index such that [x0[index]] = || x0 ||_infty;
	Step 3  Set x0[] = x0[] / x0[index];    /* normalize x0 */
	Step 4  while (k <= N_max) do steps 5-11
	        Step 5  x[] = A * x0[];
	        Step 6  lambda = x[index]
	        Step 7  Find index such that [x[index]] = || x ||_infty;
	        Step 8  if x[index] == 0 then
	                    Output("A has the eigenvalue 0", x[0]);
	                    STOP.
	                /* the matrix is singular and user should try a new x0 */
	        Step 9  err = || x0 - x / x[index] ||_infty;
	                x0[] = x[] / x[index]      /* computer u^k */
	        Step 10 if (err < TOL) then
	                    Output(lambda, x0[]);
	                    STOP.
	        Step 11 Set k++;
	Step 12 Output(Maximum number of iterations exceeded);
	        STOP.    /* unsucessful */
	```

!!! tip "Tips"

	- 对唯一的主特征值 $\lambda_1$，如果其重数大于 1，则幂法仍然有效，因为：
	
	$$
	\mathbf{x}^{(k)}=\lambda_1^k[\sum\limits_{j=1}^r\beta_j\mathbf{v}_j+\sum\limits_{j=r+1}^n\beta_j(\frac{\lambda_j}{\lambda_1})^k\mathbf{v}_j]\approx\lambda_1^k(\sum\limits_{j=1}^r\beta_j\mathbf{v}_j))
	$$
	
    - 如果 $\lambda_1=-\lambda_2$，则幂法失效
    - 因为我们无法确保对于任意的初始向量 $\mathbf{x}^{(0)}$都有$\beta_1\neq 0$，所以迭代的结果可能不是 $\mathbf{v}_1$，而是满足 $(\mathbf{x}^{(0)},\mathbf{v}_m)\neq 0$ 的第一个向量 $\mathbf{v}_m$，相应地，得到的特征值为 $\lambda_m$ 。
    - Aitken's $\Delta^2$ 法可以加速收敛
***
### Rate of Convergence

因为 $\mathbf{x}^{(k)}=\lambda_1^k\sum\limits_{j=1}\limits^n\beta_j(\frac{\lambda_j}{\lambda_1})^k\mathbf{v}_j$，假设 $\lambda_1>\lambda_2\geq\cdots\geq\lambda_n$，且 $|\lambda_2|>|\lambda_n|$，则我们的目标就是让 $\frac{\lambda_2}{\lambda_1}$ 尽可能小，这样收敛速度更快

![](../../../assets/Pasted%20image%2020250326132312.png)

记 $\mathbf{B}=\mathbf{A}-p\mathbf{I}$，其中 $p=\frac{\lambda_2+\lambda_n}{2}$，那么有 $|\lambda\mathbf{I}-A|=|\lambda\mathbf{I}-(\mathbf{B}+p\mathbf{I})|=|(\lambda-p)\mathbf{I}-\mathbf{B}|$，则 $\mathbf{B}$ 的特征值为 $\lambda_1-p,\lambda_2-p,\cdots,\lambda_n-p$，因为 $|\frac{\lambda_2-p}{\lambda_1-p}|<|\frac{\lambda_2}{\lambda_1}|$，所以此时 $\mathbf{B}$ 的收敛速度更快
***
## Inverse Power Method

如果 $\mathbf{A}$ 有特征值 $|\lambda_1|\geq|\lambda_2|\geq\cdots >|\lambda_n|$，那么 $\mathbf{A}^{-1}$ 有 $|\frac{1}{\lambda_n}|>| \frac{1}{\lambda_{n-1}}|\geq\cdots>|\frac{1}{\lambda_1}|$，他们也对应着相同的特征向量

$A^{-1}$ 的主特征值 $\Leftrightarrow$ $A$ 的特征值中的最小值

??? question "我们如何在每一步当中计算 $\vec{x}^{(k+1)}=\mathbf{A}^{-1}\hat{x}^{(k)}$？"

	我们可以通过分解 $\mathbf{A}$ 求解线性方程组 $\mathbf{A}\vec{x}^{(k+1)}=\hat{x}^{(k)}$ 来计算 $\vec{x}^{(k+1)}$

如果我们知道 $A$ 的一个特征值 $\lambda_i$ 最接近一个指定值 $p$，那么对于任意的 $j\neq i$，我们有 $|\lambda_i−p|<<|\lambda_j−p|$。并且，如果存在 $(A−pI)^{−1}$，那么逆幂法能以更快的收敛速度寻找到 $(A−p)^{−1}$ 的主特征值 $\frac{1}{\lambda_i-p}$

