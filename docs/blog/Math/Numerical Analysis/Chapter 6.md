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

- `Step 5` 需要完成 $n-i$ 次除法，
- `Step 6` 由 $E_j-m_{ji}E_i$ 代替方程 $E_j$ 的过程中，对每个 $j$ ，需要完成 $n-i+1$ 次乘法和 $n-i+1$ 次减法。所以共需要完成 $(n-i)(n-i+1)$ 次乘法和 $(n-i)(n-i+1)$ 次减法。

所以，消元过程共需要完成 $\sum\limits_{i=1}^{n-1}((n-i)+(n-i)(n-i+1))$ 次乘法/除法和 $\sum\limits_{i=1}^{n-1}(n-i)(n-i+1)$ 次加法/减法。

即消元过程共需要完成 $\frac{1}{3}n^3+\frac{1}{2}n^2-\frac{5}{6}n$ 次乘法/除法和 $\frac{1}{3}n^3-\frac{1}{3}n$ 次加法/减法。

#### Backward Substitution

`Step 8` 需要完成 $1$ 次除法。

在每个 $i$ 中，

- `Step 9` 需要完成 $n-i$ 次乘法和 $n-i-1$ 次加法（对每个相加项），然后是一次减法和一次除法。

所以，回代过程共需要完成 $1+\sum\limits_{i=1}^{n-1}((n-i)+1)$ 次乘法/除法和 $\sum\limits_{i=1}^{n-1}(n-i)$ 次加法/减法。

即回代过程共需要完成 $\frac{1}{2}n^2+\frac{1}{2}n$ 次乘法/除法和 $\frac{1}{2}n^2-\frac{1}{2}n$ 次加法/减法。

#### Summary

- 乘法/除法：$(\frac{1}{3}n^3+\frac{1}{2}n^2-\frac{5}{6}n)+(\frac{1}{2}n^2+\frac{1}{2}n)=\frac{1}{3}n^3+n^2-\frac{1}{3}n$
- 加法/减法：$(\frac{1}{3}n^3-\frac{1}{3}n)+(\frac{1}{2}n^2-\frac{1}{2}n)=\frac{1}{3}n^3+\frac{1}{2}n^2-\frac{5}{6}n$

!!! note ""

    从这里我们可以得知，高斯消元法的算法复杂度为 $O(N^3)$






