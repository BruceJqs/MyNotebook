---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 06 :  Direct Methods for Solving Linear Systems

## Linear Systems of Equations

### Gaussian Elimination

**高斯消元法**（Gaussian Elimination）的基本思路：

- 首先将矩阵 $A$ 归约成一个**上三角**（Upper-triangular）矩阵
- 然后通过**反向代换**（Backward-substitution）来求解未知量

解方程组 $\mathbf{A}\vec{x}=\vec{b}$，记 $\mathbf{A}^{(1)}=\mathbf{A}=a_{ij}^{(1)}$，$\vec{b}^{(1)}=\vec{b}=\begin{pmatrix}b_{1}^{(1)}\\b_{2}^{(1)}\\\vdots\\b_{n}^{(1)}\end{pmatrix}$，$\vec{x}^{(1)}=\vec{x}=\begin{pmatrix}x_{1}^{(1)}\\x_{2}^{(1)}\\\vdots\\x_{n}^{(1)}\end{pmatrix}$，则增广矩阵 $\tilde{\mathbf{A}}$ 为：

$$
\tilde{\mathbf{A}}=\begin{bmatrix}
a_{11}^{(1)}&a_{12}^{(1)}&\cdots&a_{1n}^{(1)}&b_{1}^{(1)}\\
a_{21}^{(1)}&a_{22}^{(1)}&\cdots&a_{2n}^{(1)}&b_{2}^{(1)}\\
\vdots&\vdots&\ddots&\vdots&\vdots\\
a_{n1}^{(1)}&a_{n2}^{(1)}&\cdots&a_{nn}^{(1)}&b_{n}^{(1)}
\end{bmatrix}
$$

通过高斯消元我们可以得到新的增广矩阵 $\tilde{\mathbf{A}}^{(k)}$：

$$
\tilde{\mathbf{A}}^{(k)}=\begin{bmatrix}
a_{11}^{(k)}&a_{12}^{(k)}&\cdots&a_{1n}^{(k)}&b_{1}^{(k)}\\
0&a_{22}^{(k)}&\cdots&a_{2n}^{(k)}&b_{2}^{(k)}\\
\vdots&\vdots&\ddots&\vdots&\vdots\\
0&0&\cdots&a_{nn}^{(k)}&b_{n}^{(k)}
\end{bmatrix}
$$

第 $1$ 次迭代过程为：如果 $a_{11}^{(1)}\neq 0$ ，记 $m_{i1}= {a_{i1}^{(1)}}/{a_{11}^{(1)}}$ ，则

$$
\begin{cases}
a_{ij}^{(2)}=a_{ij}^{(1)}-m_{i1}a_{1j}^{(1)}\\
b_{i}^{(2)}=b_{i}^{(1)}-m_{i1}b_{1}^{(1)}
\end{cases}
$$

第$t$次迭代过程为：如果 $a_{tt}^{(t)}\neq 0$，记 $m_{it}={a_{it}^{(t)}}/{a_{tt}^{(t)}}$ ，则

$$
\begin{cases}
a_{ij}^{(t+1)}=a_{ij}^{(t)}-m_{it}a_{tj}^{(t)}\\
b_{i}^{(t+1)}=b_{i}^{(t)}-m_{it}b_{t}^{(t)}
\end{cases}$$

- 如果 $a_{tt}^{(t)}=0$，则交换第 $t$ 行与第 $k$ 行，使得 $a_{kk}^{(k)}\neq 0$，然后再进行第$k$次迭代
- 如果找不到 $a_{kk}^{(k)}\neq 0$，则方程组没有唯一解，算法停止
***
反向代换：

- $x_n=\frac{b_n^{(n)}}{a_{nn}^{(n)}}$
- $x_i=\frac{b_i^{(i)}-\sum\limits_{j=i+1}^{n}a_{ij}^{(i)}x_j}{a_{ii}^{(i)}},i=n-1,...,1$
- 我们必须找到最小的整数 $k\geq i$ 且 $a_{ki}^{(i)}\not=0$，然后交换第 $k$ 行和第 $i$ 行

整个算法伪代码如下：

![](../../../assets/Pasted%20image%2020250305130105.png)
***
### Amount of Computation

> 由于在计算机上完成乘法或除法所需的时间大致相同，且大于完成加法或减法所需的时间，所以我们分开考虑乘法和除法的计算次数

对上述算法进行分析，可以得到计算次数如下：

#### Elimination

在每个 $i$ 中，

- `Step 5` 需要完成 $n-i$ 次除法
- `Step 6` 由 $E_j-m_{ji}E_i$ 代替方程 $E_j$ 的过程中，对每个 $j$ ，需要完成 $n-i+1$ 次乘法和 $n-i+1$ 次减法。所以共需要完成 $(n-i)(n-i+1)$ 次乘法和 $(n-i)(n-i+1)$ 次减法

所以，消元过程共需要完成 $\sum\limits_{i=1}^{n-1}((n-i)+(n-i)(n-i+1))$ 次乘法/除法和 $\sum\limits_{i=1}^{n-1}(n-i)(n-i+1)$ 次加法/减法

即消元过程共需要完成 $\frac{1}{3}n^3+\frac{1}{2}n^2-\frac{5}{6}n$ 次乘法/除法和 $\frac{1}{3}n^3-\frac{1}{3}n$ 次加法/减法

#### Backward Substitution

`Step 8` 需要完成 $1$ 次除法。

在每个 $i$ 中，

- `Step 9` 需要完成 $n-i$ 次乘法和 $n-i-1$ 次加法（对每个相加项），然后是一次减法和一次除法

所以，回代过程共需要完成 $1+\sum\limits_{i=1}^{n-1}((n-i)+1)$ 次乘法/除法和 $\sum\limits_{i=1}^{n-1}(n-i)$ 次加法/减法

即回代过程共需要完成 $\frac{1}{2}n^2+\frac{1}{2}n$ 次乘法/除法和 $\frac{1}{2}n^2-\frac{1}{2}n$ 次加法/减法

#### Summary

- 乘法/除法：$(\frac{1}{3}n^3+\frac{1}{2}n^2-\frac{5}{6}n)+(\frac{1}{2}n^2+\frac{1}{2}n)=\frac{1}{3}n^3+n^2-\frac{1}{3}n$
- 加法/减法：$(\frac{1}{3}n^3-\frac{1}{3}n)+(\frac{1}{2}n^2-\frac{1}{2}n)=\frac{1}{3}n^3+\frac{1}{2}n^2-\frac{5}{6}n$

!!! note ""

    从这里我们可以得知，高斯消元法的算法复杂度为 $O(N^3)$
***
## Pivoting Strategies

> 在上个算法中，我们观察到，如果与 $a_{jk}^{(k)}$ 相比，$|a_{kk}^{(k)}|$ 很小，那么乘数 $m_{ik}^{(k)}=\frac{a_{ik}^{(k)}}{a_{kk}^{(k)}}$ 就会很大，这样就会导致误差的积累。而且在代换时，$x_{k}^{(k)}$ 的值也会很大，这样就会导致误差的积累。所以我们需要选取一个合适的主元，使得误差的积累最小

### Partial Pivoting

部分主元法（Partial Pivorting，或称最大列主元法，Maximal Column Pivoting）考虑选择一个比较大的元素作为主元，这样就可以减小误差的积累

所以我们可以在每次迭代时，从第 $k$ 行开始，选取该列中绝对值最大的元素作为主元，然后再进行消元，用数学语言描述就是找到最小的 $p$，使得 $|a_{pk}^{(k)}|=\max\limits_{k\leq i\leq n}|a_{ik}^{(k)}|$，然后交换第 $p$ 行和第 $k$ 行

!!! example "Example"

	=== "Question"
	
		求解线性方程组 $\begin{cases}30.00x_1+594100x_2=591700\\5.291x_1-6.130x_2=46.78\end{cases}$，舍入精度为 4 位
	
	=== "Answer"
	
		在这种情况下，如果我们选择常规的消元顺序，我们会将第一个等式乘以 $\frac{5.291}{30.00}$，然后减去第二个等式，这样由于第一个等式第二项的系数很大，所以会导致误差被放大，所以我们需要选择一个合适的主元
		
		准确一点来说，我们需要让系数的分母尽量大，让分子尽量小，所以我们才需要找到最大的元素作为主元
***
### Scaled Partial Pivoting

缩放部分主元法（Scaled Partial Pivoting，或称缩放列主元法，Scaled-Column Pivoting）通过比较"每一行的元素都除以该行的最大元素的绝对值"，然后通过这个结果进行部分主元选取策略，再对原方程组部分进行行交换，从而选取主元。

- 第一步：计算每一行的比例因子 $s_{i}=\max\limits_{1\leq j\leq n}|a_{ij}|$
- 第二步：在第 $k$ 次高斯消元时，找到最小的 $p\geq k$，使得 $\frac{|a_{pk}^{(k)}|}{s_{p}}=\max\limits_{k\leq i\leq n}\frac{|a_{ik}^{(k)}}{s_{i}}$，然后交换第 $p$ 行和第 $k$ 行

> 为确保计算效率，比例因子只在初始过程中计算一次，在每次迭代过程中，比例因子也需要参与交换
***
### Complete Pivoting

在缩放部分主元法中，比例因子只在初始过程中计算一次。如果考虑到过程被修改，使得每次作行变换的决定时，要确定新的比例因子，那么这样就是完全主元法

完全主元法（Complete Pivoting，或称最大主元法，Maximal Element Pivoting）在每次迭代过程中，搜索所有的元素 $a_{ij}(i,j=k,...,n)$ 找到一个绝对值最大的元素作为主元，然后进行行列交换使其来到主元的位置上

![](../../../assets/Pasted%20image%2020250314211533.png)
***
### Amount of Computation

- 部分主元法：需要 $O(n^2)$ 次额外的**比较**
- 缩放部分主元法：需要 $O(n^2)$ 次额外的**比较**，以及 $O(n^2)$ 次**除法**
	- 如果新的缩放因子在行交换的时候才被确定，那么缩放部分主元法需要 $O(\frac{n^3}{3})$ 次额外的**比较**，以及 $O(n^2)$ 次**除法**
- 完全主元法：需要 $O(\frac{n^3}{3})$ 次额外的**比较**
***
## Matrix Factorization

我们也可以用矩阵来表示高斯消元：

- 第一步：
	- $m_{i1}=\frac{a_{i1}}{a_{11}}(a_{11}\not=0)$
	- 令 $L_1=\begin{pmatrix}1\\-m_{21} & 1\\\vdots & & \ddots\\-m_{n1} & & & 1\end{pmatrix}$，那么有 $L_1\begin{bmatrix}\pmb{A} & \vec{\pmb{b}}^{(1)}\end{bmatrix}=\begin{pmatrix}a_{11}^{(1)} & \cdots & a_{1n}^{(1)} & b_1^{(1)}\\ & & \pmb{A}^{(2)} & \vec{\pmb{b}}^{(2)}\end{pmatrix}$
- 第 $n-1$ 步：
	- $L_{n-1}L_{n-2}...L_1\begin{bmatrix}\pmb{A} & \vec{\pmb{b}}^{(1)}\end{bmatrix}=\begin{pmatrix}a_{11}^{(1)} & a_{12}^{(1)} & ... & a_{1n}^{(1)} & b_1^{(1)}\\ & a_{22}^{(2)} & ... & a_{2n}^{(2)} & b_2^{(2)}\\ & & ... & \vdots & \vdots\\ & & & a_{nn}^{(n)} & b_n^{(n)}\end{pmatrix}$，其中 $L_k=\begin{pmatrix}1\\ & \ddots\\ & & 1\\ & & -m_{k+1,k}\\ & & \vdots & \ddots\\ & & -m_{n,k} & & 1\end{pmatrix}$

我们不难得到 $L_k^{-1}=\begin{pmatrix}1\\ & \ddots\\ & & 1\\ & & m_{k+1,k}\\ & & \vdots & \ddots\\ & & m_{n,k} & & 1\end{pmatrix}$，$L_1^{-1}L_2^{-1}...L_{n-1}^{-1}=\begin{pmatrix}1\\ & 1\\ & m_{i,j} & \ddots\\ & & & 1\end{pmatrix}=L$

那我们令 $U=\begin{pmatrix}a_{11}^{(1)} & a_{12}^{(1)} & ... & a_{1n}^{(1)}\\ & a_{22}^{(2)} & ... & a_{2n}^{(2)}\\ & & ... & \vdots & \vdots\\ & & & a_{nn}^{(n)}\end{pmatrix}$，那么我们有 $\pmb{A}=\pmb{L}\pmb{U}$，这便是矩阵的 LU 分解

!!! note "Theorem"

	若高斯消元法能够在不使用行互换的基础上求解线性方程组 $\pmb{A}\vec{x}=\vec{b}$，那么矩阵 $A$ 可以被因式分解为一个下三角矩阵 $L$ 和上三角矩阵 $U$ 的乘积
	
	如果 $L$ 是单位下三角矩阵，则这个分解是唯一的
	
	!!! note "Proof"
	
		用反证法。如果$\mathbf{A}=\mathbf{L}_1\mathbf{U}_1=\mathbf{L}_2\mathbf{U}_2$，其中$\mathbf{L}_1$和$\mathbf{L}_2$是单位下三角矩阵，$\mathbf{U}_1$和$\mathbf{U}_2$是上三角矩阵。则有 $\mathbf{U_1}\mathbf{U_2}^{-1}=\mathbf{L_1}^{-1}\mathbf{L_2}$
		
		因为上三角阵的逆依然是上三角阵，下三角阵同理。所以等式左右分别为上三角阵和下三角阵。又因为$\mathbf{L_1}^{-1}\mathbf{L_2}$的对角线上的元素均为$1$，所以两式相等当且仅当 $\mathbf{U_1}\mathbf{U_2}^{-1}=\mathbf{L_1}^{-1}\mathbf{L_2}=\mathbf{I}$
		
		即 $\mathbf{U_1}=\mathbf{U_2}$，$\mathbf{L_1}=\mathbf{L_2}$
		
		所以这个分解是唯一的
	
	如果 $U$ 是单位下三角矩阵，那么这样的分解被称为 **Crout 分解**。Crout 分解能够通过对 $A^T$ LU 分解。也就是说，找到 $A^T=LU$，那么 $A=U^TL^T$ 就是 $A$ 的 Crout 分解
***
## Special Types of Matrices

### Strictly Diagonally Dominant Matrices

如果对矩阵 $\mathbf{A}$ 的每一行，对角线上的元素的绝对值大于该行上其他元素的绝对值之和，即有 $|a_{ii}|>\sum\limits_{j=1,j\not=i}^n|a_{ij}|$，则称 $\mathbf{A}$ 为严格对角占优矩阵（Strictly Diagonally Dominant Matrix）

定理：严格对角占优矩阵是非奇异的（即矩阵并非满秩）。而且，在此情况下，Gauss 消元法可用在形如 $\mathbf{A}\vec{x}=\vec{b}$ 的方程组中以得到唯一解，而且不需要进行行或列交换，并且对于舍入误差的增长而言计算是稳定的

??? note "Proof"

	- $A$ 是非奇异的——反证法证明
	- 高斯消元法无需行或列的交换——归纳法证明：通过高斯消元法得到的每一个矩阵 $A^{(2)},A^{(3)},...,A^{(n)}$ 都是严格对角占优的
***
### Choleski's Method for Positive Definite Matrix

对于一个矩阵 $A$，如果它是**对称的**，且 $\forall\vec{\pmb{x}}\not=\pmb{0},\vec{\pmb{x}}^TA\vec{\pmb{x}}>0$ 成立，那么称该矩阵是正定（Positive Definite）矩阵

- 需要注意的是，本课程的正定矩阵是指对称正定矩阵，与我们在线代学的不同

!!! note "Properties"

	如果 $\mathbf{A}$ 是 $n\times n$ 的正定矩阵，则：
	
	- $\mathbf{A}$是非奇异的
	- $a_{ii}>0$，$i=1,2,\cdots,n$
	- $\max\limits_{1\leq k,j\leq n}|a_{kj}|<\max\limits_{1\leq i\leq n}|a_{ii}|$，其中 $k\neq j$
	- $(a_{ij})^2<a_{ii}a_{jj}$，$i\neq j$
	- $A$ 的所有主子式都是正的

考虑正定矩阵 $A$ 的 $LU$ 分解，将其中的 $U$ 进一步分解为对角矩阵 $D$ 和单位上三角矩阵 $\widetilde{U}$，如下图所示：

![[docs/assets/Pasted image 20250314231055.png]]













