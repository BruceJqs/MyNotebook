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
	
		给定 $\sin\frac{⁡\pi}{6}=\fraC{1}{2},\sin\frac{⁡\pi}{4}=\frac{1}{\sqrt{2}},\sin\frac{⁡\pi}{3}=\frac{\sqrt{3}}{2}$。使用关于 $\sin ⁡x$ 的线性和二次拉格朗日多项式，计算 $\sin ⁡50\degree$ 并评估误差。（已知 $\sin ⁡50\degree=0.7660444...$）
		
		??? note "Answer"
		
			  我们先使用 $x_0,x_1$​ 和 $x_1,x_2$ 计算线形插值
			  
			  - 使用 $x_0=\frac{\pi}{6},x_1=\frac{\pi}{4}$
				  - $P_1(x)=\frac{x−\frac{\pi}{4}}{\frac{\pi}{6}−\frac{\pi}{4}}\times\frac{1}{2}+\frac{x−\frac{\pi}{6}}{\frac{\pi}{4}−\frac{\pi}{6}}\times\frac{1}{\sqrt{2}}$
				  - $\sin ⁡50\degree\approx P_1(\frac{5\pi}{18})\approx 0.77614$
				  - $f(x)=\sin ⁡x,f''(x)=−\sin\xi_x,\xi_x\in(\frac{pi}{6},\frac{\pi}{3}​$，且 $\frac{1}{2}<\sin⁡\xi_x<\frac{\sqrt{3}}{2}$
				  - $R_1(x)=\frac{f''(\xi_x)}{2!}(x−\frac{\pi}{6})(x−\frac{\pi}{4})$，得到 $−0.01319<R_1(\frac{5\pi}{18})<−0.00762$，因此外推误差 $\approx −0.01001$
			  - 使用 $x_1=\frac{\pi}{4},x_2=\frac{\pi}{3}$
				  - 计算得到 $\sin ⁡50\degree\approx 0.76008,0.00538<\widetilde{R_1}(\frac{5\pi}{18})<0.00660$，因此插值误差 $\approx 0.00596$
			
			再使用 $x_0,x_1,x_2$​ 计算二次插值
		    
		    - $P_2(x)=\frac{(x−\frac{\pi}{4})(x-\frac{\pi}{3})}{(\frac{\pi}{6}−\frac{\pi}{4})(\frac{\pi}{6}-\frac{\pi}{2})}\times\frac{1}{2}+\frac{(x−\frac{\pi}{6})(x-\frac{\pi}{3})}{(\frac{\pi}{4}−\frac{\pi}{6})(\frac{\pi}{4}−\frac{\pi}{3})}\times\frac{1}{\sqrt{2}}+\frac{(x−\frac{\pi}{6})(x−\frac{\pi}{4})}{(\frac{\pi}{3}−\frac{\pi}{6})(\frac{\pi}{3}−\frac{\pi}{4})}\times\frac{\sqrt{3}}{2}​​$
		    - $\sin 50\degree\approx P_2(\frac{5\pi}{18})\approx 0.76543$
		    - $R_2(x)=−\frac{\cos\xi_x}{3!}(x−\frac{\pi}{6})(x−\frac{\pi}{4})(x−\frac{\pi}{3}),\frac{1}{2}<\cos\xi_x<\frac{\sqrt{3}}{2}$
		    - $0.00044<R_2(\frac{5\pi}{18})<0.00077$，所以二次插值的误差 $\approx 0.00061$
		    
		    更高次的插值法通常会带来更好的结果，但并不总是如此
***
## Neville 迭代插值法

**记号说明：** 设 $f$ 在 $x_0,x_1,\cdots,x_n$ 上有定义，$m_1,m_2,\cdots,m_k$ 是 $k$ 个不同的整数，$0\leq m_i\leq n$，$i=1,2,\cdots,k$。记在这 $k$ 个点上与 $f(x)$ 相同的拉格朗日多项式为 $P_{m_1,m_2,\cdots,m_k}(x)$

**定理：** 设 $f$ 在 $x_0,x_1,\cdots,x_n$ 上有定义，让 $x_i$ 和 $x_j$ 是这个集合中的两个不同的数。则

$$P(x)=\frac{(x-x_j)P_{0,1,...,j-1,j+1,...,k}(x)-(x-x_i)P_{0,1,...,i-1,i+1,...,k}(x)}{(x_i-x_j)}$$

描述了对 $f$ 在 $x_0,x_1,\cdots,x_k$ 这 $k+1$ 个点上的 $k$ 次插值多项式

![](../../../assets/Pasted%20image%2020250402141858.png)

**证明：**

对于任意 $0\leq r\leq k$，$r\neq i$ 和 $r\neq j$，分子上的两个插值多项式在 $x_r$ 处都等于 $f(x_r)$，所以 $P(x_r)=f(x_r)$

分子上的第一个多项式在 $x_i$ 处等于 $f(x_i)$，而第二个多项式在 $x_i$ 处为0，所以 $P(x_i)=f(x_i)$。同理 $P(x_j)=f(x_j)$

所以 $P(x)$ 在 $x_0,x_1,\cdots,x_k$ 上与 $f(x)$ 相同，因为 $P(x)$ 是 $k$ 次多项式，所以 $P(x)=P_{0,1,\cdots,k}(x)$









