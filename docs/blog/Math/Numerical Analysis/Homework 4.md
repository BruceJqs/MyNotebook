---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 04

## 6.5.7

![](../../../assets/Pasted%20image%2020250315011317.png)

![](../../../assets/Pasted%20image%2020250620113138.png)

![](../../../assets/Pasted%20image%2020250620113154.png)

（a）乘/除法：

- Step 2 : $n-1$
- Step 3,4,5 : $\sum\limits_{i=2}^{n-1}(i-1+\sum\limits_{j=i+1}^n(i+i-1))=\frac{1}{3}n^3-\frac{7}{3}n+2$
- Step 6 : $n-1$

加/减法：

- Step 3,4,5 : $\sum\limits_{i=2}^{n-1}(1+n-i)$
- Step 6 : 1

所以乘/除法需要的计算次数为 $\frac{1}{3}n^3-\frac{1}{3}n$，加/减法需要的计算次数为 $\frac{1}{2}n^2-\frac{1}{2}n$
***
（b）乘/除法：$\frac{n(n-1)}{2}=\frac{1}{2}n^2-\frac{1}{2}n$

加减法同理
***
（c）

|                     | Multiplications/Divisions         | Additions/Subtractions                       |
| ------------------- | --------------------------------- | -------------------------------------------- |
| Factorizing into LU | $\frac{1}{3}n^3-\frac{1}{3}n$     | $\frac{1}{3}n^3-\frac{1}{2}n^2+\frac{1}{6}n$ |
| Solving Ly=b        | $\frac{1}{2}n^2-\frac{1}{2}n$     | $\frac{1}{2}n^2-\frac{1}{2}n$                |
| Solving Ux=y        | $\frac{1}{2}n^2+\frac{1}{2}n$     | $\frac{1}{2}n^2-\frac{1}{2}n$                |
| Total               | $\frac{1}{3}n^3+n^2-\frac{1}{3}n$ | $\frac{1}{3}n^3+\frac{1}{2}n^2-\frac{5}{6}n$ |

***
（d）


|                            | Multiplications/Divisions          | Additions/Subtractions                               |
| -------------------------- | ---------------------------------- | ---------------------------------------------------- |
| Factorizing into LU        | $\frac{1}{3}n^3-\frac{1}{3}n$      | $\frac{1}{3}n^3-\frac{1}{2}n^2+\frac{1}{6}n$         |
| Solving $Ly^{(k)}=b^{(k)}$ | $(\frac{1}{2}n^2-\frac{1}{2}n)m$   | $(\frac{1}{2}n^2-\frac{1}{2}n)m$                     |
| Solving $Ux^{(k)}=y^{(k)}$ | $(\frac{1}{2}n^2+\frac{1}{2}n)m$   | $(\frac{1}{2}n^2-\frac{1}{2}n)m$                     |
| Total                      | $\frac{1}{3}n^3+mn^2-\frac{1}{3}n$ | $\frac{1}{3}n^3+(m-\frac{1}{2})n^2-(m-\frac{1}{6})n$ |

***
## 6.6.17

![](../../../assets/Pasted%20image%2020250315011423.png)

（a）$|A|=3\alpha-2\beta=0\Rightarrow\alpha=\frac{2}{3}\beta$

（b）$|\alpha|>1,|\beta|<1$

（c）$\beta=1$

（d）$\alpha>\frac{2}{3},\beta=1$
***
## 7.1.5(a)

![](../../../assets/Pasted%20image%2020250315011539.png)

$$
\begin{aligned}
\|\pmb{x}-\tilde{\pmb{x}}\|_{\infty}&=\max(\frac{1}{7}-0.142,-\frac{1}{6}+0.166)=8.57\times 10^{-4}\\
\|A\tilde{\pmb{x}}-\pmb{b}\|_{\infty}&=\max(\frac{1}{2}*0.142-\frac{1}{3}*0.166-\frac{1}{63},\frac{1}{3}*0.142-\frac{1}{3}*0.166-\frac{1}{168})\\
&=2.06\times 10^{-4}
\end{aligned}
$$
***
## 7.1.7

![](../../../assets/Pasted%20image%2020250315011618.png)

令 $A=\begin{pmatrix}1 & 1\\0 & 1\end{pmatrix},B=\begin{pmatrix}1 & 0\\1 & 1\end{pmatrix}$，那么此时 $\|AB\|_{\infty}=2$，但是 $\|A\|_{\infty}\|B\|_{\infty}=1$，不满足矩阵范数的性质
***
## 7.1.13

![](../../../assets/Pasted%20image%2020250315011659.png)

（1）$\|A\|=0\Leftrightarrow A=\pmb{0}$

- 如果 $A=\pmb{0}$，很显然 $\|A\|=0$
- 如果 $\|A\|=0,A\not=\pmb{0}$，那么我们可以找到一个非零向量 $\pmb{x}=\{0,0,...,1,0,0,0\}$，其中 1 正好对应 A 中含有不为 0 的数的一行，使得 $\|A\|\not=0$，矛盾

（2）$\|\alpha A\|=|\alpha|\|A\|$，显然成立

（3）$\|A+B\|\leq\|A\|+\|B\|$

我们有 $\|(A+B)\pmb{x}\|\leq\|A\pmb{x}\|+\|B\pmb{x}\|$

那么 $\|(A+B)\pmb{x}\|=\max\limits_{\|\pmb{x}\|=1}\|(A+B)\pmb{x}\|\leq\max\limits_{\|\pmb{x}\|=1}\|A\pmb{x}\|+\max\limits_{\|\pmb{x}\|=1}\|B\pmb{x}\|$

（4）$\|AB\|\leq\|A\|\|B\|$

我们有 $\|AB\pmb{x}\|\leq\|A\|\|B\pmb{x}\|$

那么 $\|AB\pmb{x}\|=\max\limits_{\|\pmb{x}\|=1}\|AB\pmb{x}\|\leq\max\limits_{\|\pmb{x}\|=1}\|A\|\|B\pmb{x}\|\leq\max\limits_{\|\pmb{x}\|=1}\|A\|\|B\|\|\pmb{x}\|=\|A\|\|B\|$
