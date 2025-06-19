---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 03 : Interpolation and Polynomial Approximation

!!! abstract "Abstract"

	对于一个函数 $y=f(x)$，如果它非常复杂，甚至是未知的，我们可以通过一些已知的点 $y_0=f(x_0),\cdots,y_n=f(x_n)$ 来建立一个相对更简单的估计函数 $g(x)\approx f(x)$
	
	如果 $g(x)$ 满足 $g(x_i)=f(x_i),i=0,\cdots,n$，那么称其为 $f(x)$ 的插值函数（Interpolating Function）。最常用的插值函数是线性多项式。

## Interpolation and the Lagrange Polynomial

### Lagrange Polynomial

拉格朗日插值法就是构造一个次数至多为 $n$ 次的多项式，使它通过 $n+1$ 个给定的点，这个多项式就是拉格朗日多项式

!!! example "$n=1$ 情况"

	当 $n=1$ 时，构造 $P_1(x)=a_0+a_1x$，使得 $P_1(x_0)=y_0$，$P_1(x_1)=y_1$
	
	构造函数 $P_1(x)$ 作为给定的两个点 $(x_0,y_0),(x_1,y_1)$ 的线性函数：
    
    则 $P_1(x)=y_0+\frac{y_1-y_0}{x_1-x_0}(x-x_0)=\frac{x-x_1}{x_0-x_1}y_0+\frac{x-x_0}{x_1-x_0}y_1=\sum\limits_{i=0}{1}L_{1,i}(x)y_i$
	
    其中 $\frac{x-x_1}{x_0-x_1}$ 和 $\frac{x-x_0}{x_1-x_0}$ 分别记作 $L_{1,0}(x)$和$L_{1,1}(x)$（第一个下标即为 $n$ 的值，第二个下标为样本点的序号），这称为拉格朗日基函数（Lagrange Basis）
    
    可以知道，拉格朗日基函数总是满足 Kronecker Delta 函数 $L_{1,i}(x_j)=\delta_{ij}$
	
    $$
    \delta_{ij} = \begin{cases}
    1, & i = j \\
	0, & i \neq j
	\end{cases}
    $$
    

推广到 $n$ 次插值，构造 $P(x)=a_0+a_1x+\cdots+a_nx^n$，使得 $P(x_i)=y_i$，$i=0,1,\cdots,n$。就是要找到 $L_{n,i}(x)$ 使得 $L_{n,i}(x_j) = \delta_{ij}$

分析可知，这里的 $L_{n,i}(x)$ 有 $n$ 个根，分别为 $x_0,x_1,\cdots,x_{i-1},x_{i+1},\cdots,x_n$。所以可以构造出：

$$
L_{n,i}(x)=C(x-x_0)(x-x_1)\cdots(x-x_{i-1})(x-x_{i+1})\cdots(x-x_n)
$$

又因为 $L_{n,i}(x_i)=1$，所以：

$$
L_{n,i}(x)=\frac{(x-x_0)(x-x_1)\cdots(x-x_{i-1})(x-x_{i+1})\cdots(x-x_n)}{(x_i-x_0)(x_i-x_1)\cdots(x_i-x_{i-1})(x_i-x_{i+1})\cdots(x_i-x_n)}=\prod\limits_{j=0,j\neq i}^n\frac{x-x_j}{x_i-x_j}
$$

于是我们根据拉格朗日基函数构造出了 $n$ 次拉格朗日插值多项式：

$$
P_n(x)=\sum\limits_{i=0}^nL_{n,i}(x)y_i
$$

!!! note "Theorem"

	对 $n$ 个不同的点 ， $n$ 次拉格朗日插值多项式是唯一的
	
	!!! note "Proof"
	
		如果不唯一，假设存在另一个多项式 $Q_n(x)$，使得 $Q_n(x_i)=y_i$，$i=0,1,\cdots,n$，且 $Q_n(x)\neq P_n(x)$。
	
		则 $R_n(x)=P_n(x)-Q_n(x)$ 是一个次数不超过 $n$ 的多项式，且 $R_n(x_i)=0$，$i=0,1,\cdots,n$。
		
		由于 $R_n(x)$ 的次数不超过 $n$，$n$ 次多项式不可能有 $n+1$ 个解，所以$R_n(x)=0$，即 $P_n(x)=Q_n(x)$，与假设矛盾。
	
	!!! tip "Tip"
	
	    如果对 $n$ 个点运用超过 $n$ 次的拉格朗日插值多项式，那么得到的多项式就不唯一了
		
	    例如 $P(x)=L_n(x)+p(x)\prod\limits_{i=0}^n(x-x_i)$
***
### Analyze the Remainder

假定 $a\leq x_0<x_1<\cdots<x_n\leq b$，$f\in C[a,b]$，$P_n(x)$ 是 $f(x)$ 在 $x_0,x_1,\cdots,x_n$ 上的拉格朗日插值多项式，则对任意 $x\in[a,b]$，存在 $\xi(x)\in(a,b)$，使得

$$
f(x)-P_n(x)=\frac{f^{(n+1)}(\xi(x))}{(n+1)!}\prod\limits_{i=0}^n(x-x_i)
$$

!!! note "证明"

    记 $R_n(x)=f(x)-P_n(x)$，则 $R_n(x)$ 是一个次数不超过 $n$ 的多项式，且 $R_n(x_i)=0$，$i=0,1,\cdots,n$。所以 $R_n(x)$ 可记作 $K(x)\prod\limits_{i=0}^n(x-x_i)$

    固定一个点 $x$ ($x\neq x_i$) 时，记 $g(t)=R_n(t)-K(x)\prod\limits_{i=0}^n(t-x_i)$，则$g(x)=0$，$g(x_i)=0$，$i=0,1,\cdots,n$，所以 $g(t)$ 存在 $n+2$ 个不同的零点
    
    根据推广 Rolle 定理，存在 $\xi(x)\in(a,b)$，使得 $g^{(n+1)}(\xi(x))=0$，即
    
    $$
    \begin{aligned}
    0=g^{(n+1)}(\xi(x))&=(R_n(\xi(x))-K(x)\prod\limits_{i=0}^n(\xi(x)-x_i))^{(n+1)}\\&=(f(\xi(x))-P_n(\xi(x))-K(x)\prod\limits_{i=0}^n(t-x_i))^{(n+1)}\\
    &=f^{(n+1)}(\xi(x))-K(x)(n+1)! 
    \end{aligned}
    $$
    
    所以 $K(x)=\frac{f^{(n+1)}(\xi(x))}{(n+1)!}$，所以 $R_n(x)=\frac{f^{(n+1)}(\xi(x))}{(n+1)!}\prod\limits_{i=0}^n(x-x_i)$
    
    !!! note "Rolle 定理及其推广"
    
	    如果 $\varphi(x)$ 是光滑的且 $\varphi(x_0)=\varphi(x_1)=0$，那么存在 $\xi\in (x_0,x_1)$ 使得 $\varphi'(\xi)=0$
	    
	    推广情况，如果有 $\varphi(x_0)=\varphi(x_1)=\varphi(x_2)=0$，那么就存在 $\xi_0\in(x_0,x_1),\xi_1\in(x_1,x_2)$ 使得 $\varphi'(\xi_0)=\varphi'(\xi_1)=0$，进而就存在一个 $\xi\in(\xi_0,\xi_1)$ 使得 $\varphi''(\xi)=0$
	    
	    再做推广，如果有 $\varphi(x_0)=\cdots=\varphi(x_n)=0$，那么存在一个 $\xi\in(a,b)$ 使得 $\varphi^{(n)}(\xi)=0$

- 因为这里的 $f^{(n+1)}(\xi(x))$ 是不知道的，所以我们经常用 $f^{(n+1)}(x)$ 的上界来估计余项。即估计一个 $M_{n+1}$ 使得 $\forall x\in(a,b),|f^{(n+1)}(x)|\leq M_{n+1}$，将 $\frac{M_{n+1}}{(n+1)!}\prod_{i=0}^n|x-x_i|$ 作为总误差的上界
- 插值多项式对于所有 $n$ 次多项式函数来说都是准确的，因为 $f^{(n+1)}(x)=0$

!!! example "例题"

	=== "例题 1"
	
		假设为 $x\in [0,1]$ 的函数 $f(x)=e^x$ 做一个表格。设表中每一项精确的位数是 $d\geq 8$，相邻 $x$ 值之差即步长为 $h$。为使线性插值（即一次 Lagrange 插值）的误差不超过 $10^{-6}$，$h$ 应该是多少？
		
		??? note "Answer"
		
			假设 $[0, 1]$ 被分成 $n$ 个等距的子区间 $[x_0, x_1], [x_1, x_2], \cdots, [x_{n-1} , x_n]$，$x$ 在区间 $[x_k, x_{k+1}]$ 中。则误差估计为
			
			$$
			\begin{aligned}
			|f(x)-P_1(x)| &= |\frac{f''(\xi(x))}{2!}(x-x_k)(x-x_{k+1})| \\
			&\leq |\frac{e^\xi}{2}(x-kh)(x-(k+1)h)| \\
			&\leq \frac{e}{2}\cdot \frac{h^2}{4} \\
			&\leq 10^{-6}
			\end{aligned}
			$$
			
			所以 $h\leq 1.72\times 10^{-3}$。我们不妨取 $h=10^{-3}$，则 $n=1000$
	
	=== "例题 2"
	
		给定 $\sin\frac{⁡\pi}{6}=\frac{1}{2},\sin\frac{⁡\pi}{4}=\frac{1}{\sqrt{2}},\sin\frac{⁡\pi}{3}=\frac{\sqrt{3}}{2}$。使用关于 $\sin ⁡x$ 的线性和二次拉格朗日多项式，计算 $\sin ⁡50°$ 并评估误差。（已知 $\sin ⁡50°=0.7660444...$）
		
		??? note "Answer"
		
			  我们先使用 $x_0,x_1$​ 和 $x_1,x_2$ 计算线形插值
			  
			  - 使用 $x_0=\frac{\pi}{6},x_1=\frac{\pi}{4}$
				  - $P_1(x)=\frac{x−\frac{\pi}{4}}{\frac{\pi}{6}−\frac{\pi}{4}}\times\frac{1}{2}+\frac{x−\frac{\pi}{6}}{\frac{\pi}{4}−\frac{\pi}{6}}\times\frac{1}{\sqrt{2}}$
				  - $\sin ⁡50°\approx P_1(\frac{5\pi}{18})\approx 0.77614$
				  - $f(x)=\sin ⁡x,f''(x)=−\sin\xi_x,\xi_x\in(\frac{pi}{6},\frac{\pi}{3}​$，且 $\frac{1}{2}<\sin⁡\xi_x<\frac{\sqrt{3}}{2}$
				  - $R_1(x)=\frac{f''(\xi_x)}{2!}(x−\frac{\pi}{6})(x−\frac{\pi}{4})$，得到 $−0.01319<R_1(\frac{5\pi}{18})<−0.00762$，因此外推误差 $\approx −0.01001$
			  - 使用 $x_1=\frac{\pi}{4},x_2=\frac{\pi}{3}$
				  - 计算得到 $\sin ⁡50°\approx 0.76008,0.00538<\widetilde{R_1}(\frac{5\pi}{18})<0.00660$，因此插值误差 $\approx 0.00596$
			
			再使用 $x_0,x_1,x_2$​ 计算二次插值
		    
		    - $P_2(x)=\frac{(x−\frac{\pi}{4})(x-\frac{\pi}{3})}{(\frac{\pi}{6}−\frac{\pi}{4})(\frac{\pi}{6}-\frac{\pi}{2})}\times\frac{1}{2}+\frac{(x−\frac{\pi}{6})(x-\frac{\pi}{3})}{(\frac{\pi}{4}−\frac{\pi}{6})(\frac{\pi}{4}−\frac{\pi}{3})}\times\frac{1}{\sqrt{2}}+\frac{(x−\frac{\pi}{6})(x−\frac{\pi}{4})}{(\frac{\pi}{3}−\frac{\pi}{6})(\frac{\pi}{3}−\frac{\pi}{4})}\times\frac{\sqrt{3}}{2}​​$
		    - $\sin 50°\approx P_2(\frac{5\pi}{18})\approx 0.76543$
		    - $R_2(x)=−\frac{\cos\xi_x}{3!}(x−\frac{\pi}{6})(x−\frac{\pi}{4})(x−\frac{\pi}{3}),\frac{1}{2}<\cos\xi_x<\frac{\sqrt{3}}{2}$
		    - $0.00044<R_2(\frac{5\pi}{18})<0.00077$，所以二次插值的误差 $\approx 0.00061$
		    
		    更高次的插值法通常会带来更好的结果，但并不总是如此
***
## Neville's Method

**记号说明：** 设 $f$ 在 $x_0,x_1,\cdots,x_n$ 上有定义，$m_1,m_2,\cdots,m_k$ 是 $k$ 个不同的整数，$0\leq m_i\leq n$，$i=1,2,\cdots,k$。记在这 $k$ 个点上与 $f(x)$ 相同的拉格朗日多项式为 $P_{m_1,m_2,\cdots,m_k}(x)$

**定理：** 设 $f$ 在 $x_0,x_1,\cdots,x_n$ 上有定义，让 $x_i$ 和 $x_j$ 是这个集合中的两个不同的数。则

$$P(x)=\frac{(x-x_j)P_{0,1,...,j-1,j+1,...,k}(x)-(x-x_i)P_{0,1,...,i-1,i+1,...,k}(x)}{(x_i-x_j)}$$

描述了对 $f$ 在 $x_0,x_1,\cdots,x_k$ 这 $k+1$ 个点上的 $k$ 次插值多项式

![](../../../assets/Pasted%20image%2020250402144825.png)

![](../../../assets/Pasted%20image%2020250402141858.png)

**证明：**

对于任意 $0\leq r\leq k$，$r\neq i$ 和 $r\neq j$，分子上的两个插值多项式在 $x_r$ 处都等于 $f(x_r)$，所以 $P(x_r)=f(x_r)$

分子上的第一个多项式在 $x_i$ 处等于 $f(x_i)$，而第二个多项式在 $x_i$ 处为0，所以 $P(x_i)=f(x_i)$。同理 $P(x_j)=f(x_j)$

所以 $P(x)$ 在 $x_0,x_1,\cdots,x_k$ 上与 $f(x)$ 相同，因为 $P(x)$ 是 $k$ 次多项式，所以 $P(x)=P_{0,1,\cdots,k}(x)$
***
## Divided Differences

- 第一差商（Divided Difference）：$f[x_i,x_j]=\frac{f(x_j)-f(x_i)}{x_j-x_i}(i\neq j,x_i\neq x_j)$
- 第二差商：$f[x_i,x_j,x_k]=\frac{f[x_i,x_j]-f[x_j,x_k]}{x_i-x_k}(i\neq k)$
- 第 $k+1$ 差商：$f[x_0,x_1,\cdots,x_{k+1}]=\frac{f[\textcolor{red}{x_0},x_1,\cdots,x_{k}]-f[x_1,x_2,\cdots,\textcolor{red}{x_{k+1}}]}{\textcolor{red}{x_0-x_{k+1}}}=\frac{f[x_0,x_1,\cdots,\textcolor{red}{x_{k}}]-f[x_0,x_1,\cdots,x_{k-1},\textcolor{red}{x_{k+1}}]}{\textcolor{red}{x_k-x_{k+1}}}$

事实上，$f[x_0,\cdots,x_k]=\sum\limits_{i=0}^kf(x_i)\omega_{k+1}'(x_i)$，其中 $\omega_{k+1}(x)=\prod_{i=0}^k(x−x_i),\omega_{k+1}'(x_i)=\prod_{j=0,j\neq i}^k(x_i−x_j)$。这个公式的要点在于：$f[x_0,\cdots,x_k]$ 的值和 $x_0,\cdots,x_k$ 的顺序无关
***
### Newton Interpolation

> 牛顿插值法是拉格朗日插值法的推广，希望能在不断增加精度的情况下，增加多项式的次数，同时还不改变前面已经计算好的低次多项式，即 $f(x)\approx P^{(0)}(x)+P^{(1)}(x)+\cdots$，其中 $P^{(i)}(x)$ 是 $i$ 次多项式

### Simple Idea

给定 $x_0,x_1,\cdots,x_n$：

- 首先满足 $x_0$：$f(x)\approx f_0,f_0=f(x_0)$
- 然后满足 $x_1,f_1=f(x_1)$：$f(x)\approx f_0+\alpha_1(x-x_0),\alpha_1=\frac{f_1-f_0}{x_1-x_0}$
- 更多的点：$f(x)\approx f_0+\alpha_1(x-x_0)+\alpha_2(x-x_0)(x-x_1)+\cdots$

从另一个角度来看，牛顿插值法更像是一个渐进的线性估计（很像递归）：

$$
\begin{aligned}
f(x)&=f(x_0)+(x-x_0)f^{(1)}(\xi_1)\\
&=f(x_0)+(x-x_0)(\frac{f(x_1)-f(x_0)}{x_1-x_0}+(x-x_1)f^{(2)}(\xi_2))\\
&=\cdots
\end{aligned}
$$

***
### The Pattern and Coefficients

根据上面的想法我们有：

$$
f(x)=\sum\limits_{i=0}^n\alpha_i\prod\limits_{j=0}^{j<i}(x-x_j)=\sum\limits_{i=0}^n\alpha_iN^{(i)}(x)
$$

或者可以写为：

$$
\begin{pmatrix}
f_0\\
f_1\\
\vdots\\
f_n
\end{pmatrix}=\begin{pmatrix}
N^{(0)}(x_0) & N^{(1)}(x_0) & \cdots & N^{(n)}(x_0)\\
N^{(0)}(x_1) & N^{(1)}(x_1) & \cdots & N^{(n)}(x_1)\\
\vdots & \vdots & \ddots & \vdots\\
N^{(0)}(x_n) & N^{(1)}(x_n) & \cdots & N^{(n)}(x_n)
\end{pmatrix}\begin{pmatrix}
\alpha_0\\
\alpha_1\\
\vdots\\
\alpha_n
\end{pmatrix}
$$

其中 $N^{(i)}(x_k)=\begin{cases}0 & k<i\\\prod\limits_{j=0}^{j<i}(x_k-x_j) & k\geq i\end{cases},N^{(0)}=1$

因此事实上中间那个大矩阵可以写为：

$$
\begin{pmatrix}
1 & 0 & \cdots & 0\\
1 & (x_1-x_0) & \cdots & 0\\
\vdots & \vdots & \ddots & \vdots\\
1 & (x_n-x_0) & \cdots & \prod\limits_{j=0}^{j<n}(x_n-x_j)
\end{pmatrix}
$$

这显然是一个下三角矩阵！它的逆矩阵也很特殊：

$$
\begin{pmatrix}
1 & 0 & \cdots & 0\\
\frac{1}{x_0-x_1} & \frac{1}{x_1-x_0} & \cdots & 0\\
\vdots & \vdots & \ddots & \vdots\\
\frac{1}{\omega'_{n+1}(x_0)} & \frac{1}{\omega'_{n+1}(x_1)} & \cdots & \frac{1}{\omega'_{n+1}(x_n)}
\end{pmatrix}
$$

!!! note "Lagrange Interpolation"

	如果我们把拉格朗日插值法也写成矩阵的形式：
	
	$$
	\begin{pmatrix}
	f_0\\
	f_1\\
	\vdots\\
	f_n
	\end{pmatrix}=\begin{pmatrix}
	L^{(0)}(x_0) & L^{(1)}(x_0) & \cdots & L^{(n)}(x_0)\\
	L^{(0)}(x_1) & L^{(1)}(x_1) & \cdots & L^{(n)}(x_1)\\
	\vdots & \vdots & \ddots & \vdots\\
	L^{(0)}(x_n) & L^{(1)}(x_n) & \cdots & L^{(n)}(x_n)
	\end{pmatrix}\begin{pmatrix}
	\alpha_0\\
	\alpha_1\\
	\vdots\\
	\alpha_n
	\end{pmatrix}
	$$
	
	中间这个矩阵显然是一个单位矩阵

我们有：

$$
\require{empheq}
\begin{empheq}[left=\empheqlbrace]{align}
f(x) &= f(x_0)+(x-x_0)f[x,x_0] && \tag{1} \\
f[x,x_0] &= f[x_0,x_1]+(x-x_1)f[x,x_0,x_1] \tag{2} \\
&\cdots\\
f[x,x_0,\cdots,x_{n-1}] &= f[x_0,x_1,\cdots,x_n]+(x-x_n)f[x,x_0,x_1,\cdots,x_n] \tag{n-1}
\end{empheq}
$$

将 $(1)+(x-x_0)\times(2)+\cdots+(x-x_0)\cdots(x-x_{n-1})\times (n-1)$ 可得：

$$
\begin{aligned}
f(x)&=\textcolor{red}{f(x_0)+f[x_0,x_1](x-x_0)+f[x_0,x_1,x_2](x-x_0)(x-x_1)+\cdots}\\
&\textcolor{red}{+f[x_0,\cdots,x_n](x-x_0)\cdots(x-x_{n-1})}\\
&\textcolor{blue}{+f[x_0,x_1,\cdots,x_n](x-x_0)\cdots(x-x_{n-1})(x-x_n)}\\
\end{aligned}
$$

其中红色部分为我们要求的 $N_n(x)$，蓝色部分为余项 $R_n(x)$

!!! note "Note"

	- 因为第 $n$ 个插值多项式是唯一的，所以 $N_n(x)\equiv P_n(x)$
	- 它们必须有相同的截断误差，即：
	
	$$
	\begin{aligned}
	&f[x,x_0,\cdots,x_n]\omega_{n+1}(x)=\frac{f^{(n+1)}(\xi_x)}{(n+1)!}\omega_{n+1}(x)\\
	\Rightarrow&f[x_0,\cdots,x_k]=\frac{f^{(k)}(\xi)}{k!},\xi\in(x_{\min},x_{\max})\\
	\end{aligned}
	$$
	
	- 这个过程跟 Neville's Method 类似：
	
	$$
	\begin{aligned}
	&f(x_0)\\
	&f(x_1) \quad f[x_0,x_1]\\
	&f(x_2) \quad f[x_1,x_2] \quad f[x_0,x_1,x_2]\\
	&\cdots\\
	&f(x_{n-1}) \quad \cdots\\
	&f(x_n) \quad f[x_{n-1},x_n] \quad f[x_{n-2},x_{n-1},x_n] \quad \cdots \quad f[x_0,\cdots,x_n]\\
	&f(x_{n+1}) \quad f[x_{n},x_{n+1}] \quad f[x_{n-1},x_{n+1}] \quad \cdots \quad f[x_1,\cdots,x_n,x_{n+1}] \quad f[x_0,\cdots,x_{n+1}]
	\end{aligned}
	$$
	
***
### Formulae with Equal Spacing

如果每个点都连续等步长排列，记步长为 $h$，令 $x_i=x_0+ih(i=0,1,\cdots,n)$，则

引入**向前差分（Forward Difference）**记号：

$$\begin{aligned}
\Delta f_i&=f_{i+1}-f_i\\
\Delta^2 f_i&=\Delta f_{i+1}-\Delta f_i\\
\cdots\\
\Delta^kf_i&=\Delta(\Delta^{k-1}f_i)=\Delta^{k-1} f_{i+1}-\Delta^{k-1} f_i
\end{aligned}$$

引入**向后差分（Backward Difference）**记号：

$$\begin{aligned}
\nabla f_i&=f_i-f_{i-1}\\
\nabla^2 f_i&=\nabla f_i-\nabla f_{i-1}\\
\cdots\\
\nabla^k f_i&=\nabla^{k-1} f_i-\nabla^{k-1} f_{i-1}\\
\end{aligned}$$

引入**中心差分（Central Difference）**记号：

$$
\delta^k f_i = \delta^{k-1}f_{i+\frac{1}{2}}-\delta^{k-1}f_{i-\frac{1}{2}}
$$

其中 $f_{i\pm\frac{1}{2}}=f(x_i\pm\frac{h}{2})$

!!! note "Some Import Properties"

	- 线性：$\Delta(a·f(x)+b·g(x))=a\Delta f+b\Delta g$
	- 如果 $f(x)$ 是一个 $m$ 阶多项式，那么 $\Delta^kf(x)(0\leq k\leq m)$ 是一个 $m−k$ 阶多项式且 $\Delta^kf(x)=0(k>m)$
	- 差值还能从以下函数得到：
		- $\Delta^n f_k=\sum\limits_{j=0}^n(-1)^jC_n^jf_{n+k-j}$
		- $\nabla^n f_k=\sum\limits_{j=0}^n(-1)^{n-j}C_n^jf_{k+j-n}$
	- 反之亦然：$f_{n+k}=\sum\limits_{j=0}^nC_n^j\Delta^j f_k$
	- $f[x_0,\cdots,x_k]=\frac{\Delta^k f_0}{k!h^k},f[x_n,x_{n-1},\cdots,x_{n-k}]=\frac{\nabla^k f_n}{k!h^k}$，从 $R_n$ 可以得到：$f^{(k)}(\xi)=\frac{\Delta^k f_0}{h^k}$
***
### Newton's Formulae

- 牛顿向前差分公式：令 $x=x_0+th$，则 $N_n(x)=N_n(x_0+th)=\sum\limits_{k=0}^nC_t^k\Delta^kf(x_0),R_n(x)=\frac{f^{(n+1)(\xi)}}{n+1!}t(t-1))\cdots(t-n)h^{n+1},\xi\in(x_0,x_n)$
- 牛顿向后差分公式：颠倒点的顺序，即计算 $N_n(x)=f(x_n)+f[x_n,x_{n-1}](x-x_n)+\cdots+f[x_n,\cdots,x_0](x-x_n)\cdots(x-x_1)$，令 $x=x_n+th$，那么 $N_n(x)=N_n(x_n+th)=\sum\limits_{k=0}^n(-1)^kC_{-t}^k\nabla^kf(x_n)$
***
## Hermite Interpolation

> Hermite 插值法的目标是找到一个密切多项式（Osculating Polynomial）$P(x)$，使得 $\forall i=0,1,\cdots,n,P(x_i)=f(x_i),P'(x_i)=f'(x_i),…,P^{(m_i)}(x_i)=f^{(m_i)}(x_i)$

- 给定 $N$ 个条件（即 $N$ 个方程），$N-1$ 次多项式就能够确定下来
- 与 $f$ 以及所有在一个点 $x_0$ 上的 $\leq m_0$ 阶的导数吻合的密切多项式就是一个泰勒多项式：

$$
\begin{aligned}
P(x)&=f(x_0)+f'(x_0)(x-x_0)+\cdots+\frac{f^{(m_0)}(x_0)}{m_0!}(x-x_0)^{m_0}+\frac{f^{(m_0+1)}(\xi)}{(m_0+1)!}(x-x_0)^{(m_0+1)}\\
&=f(x_0)+f'(x_0)(x-x_0)+\cdots+\frac{f^{(m_0)}(x_0)}{m_0!}(x-x_0)^{m_0}+R(x)
\end{aligned}
$$

- 当 $\forall i=0,1,\cdots,n,m_i=1$ 时，此时的多项式为**埃尔米特多项式**（Hermite Polynomials）

!!! example "Example"

	假设 $x_0\neq x_1\neq x_2​$。给定 $f(x_0),f(x_1),f(x_2)$ 和 $f'(x_1)$，寻找多项式 $P(x)$，满足 $P(x_i)=f(x_i),i=0,1,2$，且 $P'(x1)=f'(x1)$。并分析误差
	
	??? note "Answer"
	
		首先，$P(x)$ 的阶必须 $\leq 3$
		
		与拉格朗日多项式类似，我们待定埃尔米特多项式：$P_3(x)=\sum\limits_{i=0}^2 f(x_i)h_i(x)+f'(x_1)\hat{h_1}(x)$
		
		其中 $h_i(x_j)=\delta_{ij},h_i'(x_1)=0,\hat{h_1}(x_i)=0,\hat{h_1}'(x_1)=1$
		
		- $h_0(x)$：有根 $x_1,x_2$，且 $h_0'(x_1)=0\Rightarrow x_1$ 是一个重根
			- $\begin{cases}h_0(x)=C_0(x-x_1)^2(x-x_2)\\h_0(x_0)=1\Rightarrow C_0\end{cases} \Rightarrow h_0(x)=\frac{(x-x_1)^2(x-x_2)}{(x_0-x_1)^2(x_0-x_2)}$
		- $h_2(x)$：与 $h_0(x)$ 类似
		- $\hat{h_1}(x)$：有根 $x_0,x_2\Rightarrow h_1(x)=(Ax+B)(x-x_0)(x-x_2)$。$A,B$ 可通过 $h_1(x_1)=0$ 和 $h_1'(x_1)=0$ 求解
		- $\hat{h_1}(x)$：有根 $x_0,x_1,x_2\Rightarrow\hat{h_1}(x)=C_1(x-x_0)(x-x_1)(x-x_2)$。$h_1(x_1)=1\Rightarrow C_1$ 能被求解
		
		和拉格朗日误差分析相似，$R_3(x)=f(x)-P_3(x)=K(x)(x-x_0)(x-x_1)^2(x-x_2)\Rightarrow K(x)=\frac{f^{(4)}(\xi_x)}{4!}$

一般情况下，给定 $x_0,\cdots,x_n;y_0,\cdots,y_n$ 以及 $y_0',\cdots,y_n'$，有且仅有唯一的埃尔米特多项式 $H_{2n+1}(x)$ 满足对于所有的 $i,H_{2n+1}(x_i)=y_i$ 且 $H_{2n+1}'(x_i)=y_i'$

!!! note "求解过程"

	令 $H_{2n+1}(x)=\sum\limits_{i=0}^ny_ih_i(x)+\sum\limits_{i=0}^ny_i'\hat{h_i}(x)$，其中 $h_i(x_j)=\delta_{ij},h_i'(x_j)=0,\hat{h_i}(x_j)=0,\hat{h_i}'(x_j)=\delta_{ij}$
	
	- $h_i(x)$：
		- $x_0,\cdots,\hat{x_i},\cdots,x_n$ 是重数为 2 的根 $\Rightarrow h_i(x)=(A_ix+B_i)L_{n,i}^2(x)$
		- $A_i,B_i$ 能通过 $h_i(x_i)=1,h_i'(x_i)=0$ 求解
		- $h_i(x)=[1-2L_{n,i}'(x_i)(x-x_i)L_{n,i}^2(x)]$
	- $\hat{h_i}(x)$：
		- 除了 $x_i$ 外，所有的根 $x_0,\cdots,x_n$ 的重数均为 2，得到：
		- $\begin{cases}\hat{h_i}(x)=C_i(x-x_i)L_{n,i}^2(x)\\\hat{h_i}'(x_i)=1\Rightarrow C_i=1\end{cases} \Rightarrow\hat{h_i}(x)=(x-x_i)L_{n,i}^2(x)$
	
	如果 $a=x_0<x_1<\cdots<x_n=b,f\in C^{2n}[a,b]$，那么 $R_n(x)=\frac{f^{(2n+2)}(\xi_x)}{(2n+2)!}[\prod_{i=0}^n(x-x_i)]^2$

!!! example "Example"

	给定 $x_i=i+1,i=0,1,2,3,4,5$，那么下面哪个是 $\hat{h_2}(x)$？
	
	![](../../../assets/Pasted%20image%2020250409190255.png)
	
	??? note "Answer"
	
		根据上面的求解过程我们可以得到除了 $x_2=3$ 所有根的重数均为 2，且 $\hat{h_2}'(x_2)=1$
		
		由图得知右边这个图符合条件
***
## Cubic Spline Interpolation

!!! example "Example"

	考虑关于函数 $f(x)=\frac{1}{1+x^2}$ 在点 $x_i=-5+\frac{10}{n}i(i=0,\cdots,n)$ 的拉格朗日多项式 $P_n(x)$
	
	![](../../../assets/Pasted%20image%2020250409192142.png)
	
	可以看到 $P_n(x)\not\rightarrow f(x)$，这说明我们需要找其他方法来拟合函数
	
	!!! warning "不好的尝试"
	
		=== "分段线性插值"
		
			分段线性插值（Piecewise Linear Interpolation）是指在每个子区间 $[x_i,x_{i+1}]$ 上，通过线性多项式近似表示 $f(x)$，即：
			
			$$
			f(x)\approx P_1(x)=\frac{x-x_{i+1}}{x_i-x_{i+1}}y_i+\frac{x-x_i}{x_{i+1}-x_i}y_{i+1}\text{ for } x\in [x_i,x_{i+1}]
			$$
			
			令 $h=\max|x_{i+1}-x_i|$，那么 $P_1^h(x)\stackrel{\text{uniform}}{\rightarrow},h\rightarrow 0$
			
			但是，这样的方法逼近的函数并不光滑，所以我们希望用更高次的多项式来逼近 $f$
			
			![](../../../assets/Pasted%20image%2020250409194231.png)
		
		=== "Hermite 分段多项式"
		
			给定 $x_0,\cdots,x_n;y_0,\cdots,y_n;y_0',\cdots,y_n'$，在区间 $[x_i,x_{i+1}]$ 的两个端点上构造一个关于 $y,y'$ 的 3 阶 Hermite 多项式
			
			但是这样的逼近是光滑的，但是为了将该多项式应用于一般插值，需要知道所有的 $f'$ 的值，这是不现实的
***
### Cubic Spline

给定在 $[a,b]$ 上的 $n+1$ 个点 $x_0,x_1,\cdots,x_n$，$a=x_0<x_1<\cdots<x_n=b$，以及 $f$。三次样条插值是一个函数 $S(x)$，满足以下条件：

1. $S(x)$ 在每个子区间 $[x_i,x_{i+1}]$ 上是一个三次多项式，记作 $S_i(x)$，$i=0,1,\cdots,n-1$
2. $S(x_i)=f(x_i)$，$i=0,1,\cdots,n$
3. $S_{i+1}(x_{i+1})=S_i(x_{i+1})$，$i=0,1,\cdots,n-2$
4. $S'_{i+1}(x_{i+1})=S'_i(x_{i+1})$，$i=0,1,\cdots,n-2$
5. $S''_{i+1}(x_{i+1})=S''_i(x_{i+1})$，$i=0,1,\cdots,n-2$
6. 下列的边界条件之一成立：
    1. $S''(x_0)=S''(x_n)=0$，称为**自由或自然边界（Free or Natural Boundary）**
    2. $S'(x_0)=f'(x_0)$，$S'(x_n)=f'(x_n)$，称为**固支边界（Clamped Boundary）**
***
### Method of Bending Moment

记 $h_j=x_j-x_{j-1}$，在 $x\in[x_{j-1},x_j]$ 上，$S(x)=S_j(x)$，$S'(x)=S'_j(x)$，$S''(x)=S''_j(x)$。

因为 $S(x)$ 是一个三次多项式，所以 $S''_j(x)$ 是一个一次多项式，由端点值决定，假设 $S''_j(x_{j-1})=M_{j-1}$，$S''_j(x_j)=M_j$。那么对于 $x\in[x_{j-1},x_j]$，有

$$S''_j(x)=M_{j-1}\frac{x_j-x}{h_j}+M_j\frac{x-x_{j-1}}{h_j}$$

积分得到

$$S'_j(x)=-M_{j-1}\frac{(x_j-x)^2}{2h_j}+M_j\frac{(x-x_{j-1})^2}{2h_j}+A_j$$

再积分得到

$$S_j(x)=M_{j-1}\frac{(x_j-x)^3}{6h_j}+M_j\frac{(x-x_{j-1})^3}{6h_j}+A_jx+B_j$$

$A_j$ 和 $B_j$ 是常数，可以通过 $S_j(x_{j-1})=y_{j-1}$ 和 $S_j(x_j)=y_{j}$ 得到。

$$\begin{aligned}
\begin{cases}
S_j(x_{j-1})=y_{j-1}\\
S_j(x_j)=y_{j}
\end{cases}
&\Rightarrow
\begin{cases}
M_{j-1}\frac{h_j^2}{6}+A_jx_{j-1}+B_j=y_{j-1}\\
M_j\frac{h_j^2}{6}+A_jx_j+B_j=y_{j}
\end{cases}\\
&\Rightarrow
\begin{cases}
A_j=\frac{y_j-y_{j-1}}{h_j}-\frac{M_j-M_{j-1}}{6}h_j\\
B_j=\frac{y_{j-1}x_j-y_jx_{j-1}}{h_j}-\frac{M_{j-1}x_j-M_jx_{j-1}}{6}h_j
\end{cases}\\
\end{aligned}$$

所以

$$
\begin{aligned}
A_jx+B_j&=\frac{y_j-y_{j-1}}{h_j}x+\frac{y_{j-1}x_j-y_jx_{j-1}}{h_j}-\frac{M_j-M_{j-1}}{6}h_jx-\frac{M_{j-1}x_j-M_jx_{j-1}}{6}h_j\\
&=(y_{j-1}-\frac{M_{j-1}}{6}h_j^2)\frac{x_j-x}{h_j}+(y_j-\frac{M_j}{6}h_j^2)\frac{x-x_{j-1}}{h_j}
\end{aligned}
$$

所以，我们的目的就是求出 $M_j$，$j=0,1,\cdots,n$。

因为 $S'$ 是连续的，所以

在 $[x_{j-1},x_j]$ 上，$S'_j(x)=-M_{j-1}\frac{(x_j-x)^2}{2h_j}+M_j\frac{(x-x_{j-1})^2}{2h_j}+f[x_{j-1},x_j]-\frac{M_j-M_{j-1}}{6}h_j$

在 $[x_j,x_{j+1}]$ 上，$S'_{j+1}(x)=-M_{j}\frac{(x_{j+1}-x)^2}{2h_{j+1}}+M_{j+1}\frac{(x-x_{j})^2}{2h_{j+1}}+f[x_j,x_{j+1}]-\frac{M_{j+1}-M_{j}}{6}h_{j+1}$

有 $S'_{j+1}(x_j)=S'_j(x_j)$，所以我们可以得到 $M_{j-1}, M_j, M_{j+1}$ 之间的关系：

记 $\lambda_j=\frac{h_{j+1}}{h_j+h_{j+1}}$，$\mu_j=\frac{h_{j}}{h_j+h_{j+1}}$，$g_j=\frac{6}{h_j+h_{j+1}}(f[x_j,x_{j+1}]-f[x_{j-1},x_j])$，则

$$
\mu_jM_{j-1}+2M_j+\lambda_jM_{j+1}=g_j
$$

其中 $j=1,2,\cdots,n-1$。

$$
\begin{bmatrix}
\mu_1 & 2 & \lambda_1 &  & & \\
& \mu_2 & 2 & \lambda_2 &  & \\
& & \ddots & \ddots & \ddots & \\
& & & \mu_{n-1} & 2 & \lambda_{n-1} \\
\end{bmatrix}
\begin{bmatrix}
M_0\\
M_1\\
\vdots\\
M_n\\
\end{bmatrix}=
\begin{bmatrix}
g_1\\
g_2\\
\vdots\\
g_{n-1}\\
\end{bmatrix}
$$

我们有 $n+1$ 个未知数，$n-1$ 个方程 $\rightarrow$ 由边界条件增加两个方程
***
##### Clamped boundary

此时我们知道 $S'(x_0)=f'(x_0)$，$S'(x_n)=f'(x_n)$，所以

在 $[x_0,x_1]$ 上，$S'_1(x)=-M_0\frac{(x_1-x)^2}{2h_1}+M_1\frac{(x-x_0)^2}{2h_1}+f[x_0,x_1]-\frac{M_1-M_0}{6}h_1$

在 $[x_{n-1},x_n]$ 上，$S'_n(x)=-M_{n-1}\frac{(x_n-x)^2}{2h_n}+M_n\frac{(x-x_{n-1})^2}{2h_n}+f[x_{n-1},x_n]-\frac{M_n-M_{n-1}}{6}h_n$

所以我们额外有两个方程：

$$
\begin{aligned}
\begin{cases}
f'(x_0)=-M_0\frac{h_1}{2}+f[x_0,x_1]-\frac{M_1-M_0}{6}h_1\\
f'(x_n)=M_{n }\frac{h_n}{2}+f[x_{n-1},x_n]-\frac{M_n-M_{n-1}}{6}h_n
\end{cases}\\
\Rightarrow
\begin{cases}
2M_0+M_1=\frac{6}{h_1}(f[x_0,x_1]-f'(x_0))\triangleq g_0\\
M_{n-1}+2M_n=\frac{6}{h_n}(f'(x_n)-f[x_{n-1},x_n]) \triangleq g_n
\end{cases}
\end{aligned}
$$

所以我们可以得到

$$
\begin{bmatrix}
2 & 1 &  & & &\\
\mu_1 & 2 & \lambda_1 &  & &\\
& \ddots & \ddots & \ddots & &\\
& & \mu_{n-1} & 2 & \lambda_{n-1} &\\
& &   & 1  & 2
\end{bmatrix}
\begin{bmatrix}
M_0\\
M_1\\
\vdots\\
M_n\\
\end{bmatrix}=
\begin{bmatrix}
g_0\\
g_1\\
\vdots\\
g_n
\end{bmatrix}
$$
***
##### Natural boundary

根据之前的假设 $M_0=S''(x_0)=y''_0$，$M_n=S''(x_n)=y''_n$，则

$$ \lambda_0 = 0, g_0 = 2y''_0, \mu_n = 0, g_n = 2y''_n $$

当 $S''(x_0)=S''(x_n)=0$，我们称之为**自由边界（Free Boundary）**，此时 $g_0=g_n=0$。

$$
\begin{bmatrix}
2 & 0 & 0 & & &\\
\mu_1 & 2 & \lambda_1 &   \\
 & \ddots & \ddots & \ddots & \\
 & & \mu_{n-1} & 2 & \lambda_{n-1} \\
 & &   0& 0  & 2
\end{bmatrix}_{(n+1)\times (n+1)}
\begin{bmatrix}
M_0\\
M_1\\
\vdots\\
M_{n-1}\\
M_n\\
\end{bmatrix}_{(n+1)\times 1}=
\begin{bmatrix}
g_0\\
g_1\\
\vdots\\
g_{n-1}\\
g_n
\end{bmatrix}_{(n+1)\times 1}
$$

自由边界的情况下，有 $S''(x_0)=S''(x_n)=0$。
****
##### Periodic boundary

如果 $f$ 是周期函数，即 $y_n=y_0$​ 且 $S'(a^+)=S'(b^−)\Rightarrow M_0=M_n$

$$
\begin{bmatrix}
2 & \lambda_1 & & & \mu_1\\
\mu_2 & 2 & \lambda_2 &   \\
 & \ddots & \ddots & \ddots & \\
 & & \mu_{n-1} & 2 & \lambda_{n-1} \\
\lambda_n & &  & \mu_n  & 2
\end{bmatrix}_{n\times n}
\begin{bmatrix}
M_1\\
\vdots\\
M_{n-1}\\
M_n\\
\end{bmatrix}_{n\times 1}=
\begin{bmatrix}
g_1\\
\vdots\\
g_{n-1}\\
g_n
\end{bmatrix}_{n\times 1}
$$

!!! note "Note"

	- 只要系数矩阵是严格对角占优的，那么三次样条能通过边界被唯一确定
	- 如果 $f\in C[a,b]$ 且 $\frac{\max⁡ h_i}{\min ⁡h_i}\leq C<\infty$，那么当 $h_i\rightarrow 0$ 时，$S(x)\stackrel{\text{uniform}}{\rightarrow}f(x)$。也就是说，在保证不增加样条阶数的情况下，可通过增加节点个数来提升近似精度
	
	执行三次样条插值法的步骤如下：
	
	1. 计算 $\mu_j,\lambda_j,g_j$
	2. 求解 $M_j$
	3. 找到包含 $x$ 的子区间，即找到相应的 $j$
	4. 通过 $S_j(x)$ 得到 $f(x)$ 的近似值
