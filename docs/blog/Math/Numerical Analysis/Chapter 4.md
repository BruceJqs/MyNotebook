---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 04 : Numerical Differentiation and Integration

## Numerical Differentiation

目标：对于给定的 $x_0$，近似计算 $f'(x_0)$（即**数值微分**，Numerical Differentiation）

事实上，微分有向前和向后两种计算公式：

- 向后：$f'(x_0)=\lim\limits_{h\rightarrow 0}\frac{f(x_0+h)−f(x_0)}{h}$
	
	![](../../../assets/Pasted%20image%2020250423112214.png)
	
- 向前：$f'(x_0)=\lim\limits_{h\rightarrow 0}\frac{f(x_0)−f(x_0−h)}{h}$
	
	![](../../../assets/Pasted%20image%2020250423112248.png)
	

现在我们用 $f(x)$ 的带有插值点 $x_0,x_0+h$ 的拉格朗日多项式来近似表示 $f(x)$：

$$
\begin{aligned}
f(x)&=\frac{f(x_0)(x-x_0-h)}{x-x_0-h}+\frac{f(x_0+h)(x-x_0)}{x_0+h-x_0}\\
&+\frac{(x-x_0)(x-x_0-h)}{2}f''(\xi_x)\\
f'(x)&=\frac{f(x_0+h)−f(x_0)}{h}+\frac{2(x-x_0)-h}{2}f''(\xi_x)\\
&+\frac{(x-x_0)(x-x_0-h)}{2}\frac{d}{dx}[f''(\xi_x)]\\
\Rightarrow f'(x_0)&=\frac{f(x_0+h)−f(x_0)}{h}\underbrace{-\frac{h}{2}f''(\xi_x)}_{O(h)}
\end{aligned}
$$

***
推广到一般情况，我们用 $n+1$ 个插值点 $\{x_0,x_1,\cdots,x_n\}$ 来近似表示 $f(x)$：

$$
\begin{aligned}
f(x)&=\sum\limits_{k=0}^nf(x_k)L_k(x)+\frac{(x-x_0)\cdots(x-x_n)}{(n+1)!}f^{(n+1)}(\xi_x)\\
f'(x_j)&=\sum\limits_{k=0}^nf(x_k)L_k'(x_j)+\frac{f^{(n+1)}(\xi_j)}{(n+1)!}\prod_{k = 0,k\neq j}^n(x_j-x_k)
\end{aligned}
$$

- 一般来说，更多的插值点会带来更大的近似精度
- 但另一方面，随着插值点的增加，舍入误差也在变大，因此数值微分是**不稳定的**！

!!! example "Examples"

	=== "Example 01"
	
		给定三个点 $x_0,x_0+h,x_0+2h$，请求得关于每个点的三点公式，然后选出对于 $f'(x)$ 而言最佳的三点公式
		
		??? note "Answer"
		
			$$
			\begin{aligned}
			f'(x_0​)&=\frac{1}{h}\big[-\frac{3}{2}f(x_0)+2f(x_0+h)-\frac{1}{2}f(x_0+2h)\big]+\frac{h^2}{3}f^{(3)}(\xi_0)\\
			f'(x_0+h)&=\frac{1}{h}\big[-\frac{1}{2}f(x_0)+\frac{1}{2}f(x_0+2h)\big]-\frac{h^2}{6}f^{(3)}(\xi_1)\\
			\Rightarrow f'(x_0)&=\frac{1}{2h}[f(x_0+h)-f(x_0-h)]-\frac{h^2}{6}f^{(3)}(\xi_1)
			\end{aligned}​
			$$
			
			![](../../../assets/Pasted%20image%2020250423113822.png)
	
	=== "Example 02"
	
		寻找近似计算 $f''(x0)$ 的方式
		
		??? note "Answer"
		
			考虑在 $x_0$​ 处 $f(x_0+h),f(x_0−h)$ 的泰勒展开式：
			
			$$
			\begin{aligned}
			f(x_0+h)&=f(x_0)+hf'(x_0)+\frac{h^2}{2}f''(x_0)+\frac{h^3}{6}f^{(3)}(x_0)+\frac{h^4}{24}f^{(4)}(\xi_1)\\
			f(x_0−h)&=f(x_0)−hf'(x_0)+\frac{h^2}{2}f''(x_0)−\frac{h^3}{6}f^{(3)}(x_0)+\frac{h^4}{24}f^{(4)}(\xi_{-1})\\
			\Rightarrow f''(x_0)&=\frac{f(x_0+h)−2f(x_0)+f(x_0−h)}{h^2}-\frac{h^2}{12}f^{(4)}(\xi_1)\\
			\end{aligned}
			$$
			
***
## Elements of Numerical Integration

目标：近似计算 $I=\int_a^bf(x)dx$ （即**数值积分**，Numerical Quadrature）

思路：使用 $f(x)$ 的**拉格朗日插值多项式**——从区间 $[a,b]$ 上选择一组不同的点 $a\leq x_0<x_1\cdots<x_n\leq b$。拉格朗日多项式为 $P_n(x)=\sum\limits_{k=0}^nf(x_k)L_k(x)$，因此：

$$
\int_a^bf(x)dx\approx\sum\limits_{k=0}^nf(x_k)\int_a^bL_k(x)dx
$$

我们令 $A_k=\int_a^bL_k(x)dx=\int_a^b\prod\limits_{j\neq k}\frac{x-x_j}{x_k-x_j}dx$，则误差 $R[f]$ 为：

$$
\begin{aligned}
R[f]&=\int_a^bf(x)dx-\sum\limits_{k=0}^nf(x_k)A_k\\
&=\int_a^b[f(x)-P_n(x)]dx=\int_a^bR_n(x)dx\\
&=\int_a^b\frac{f^{(n+1)}(\xi_x)}{(n+1)!}\prod\limits_{j=0}^n(x-x_j)dx\\
\end{aligned}
$$

定义：求积公式的**精度**（Degree of Accuracy/Precision）为最大的正整数 $n$，使得公式对于每个 $x^k(k=0,1,\cdots,n)$ 都是精确的

!!! example "Example"

	考虑在 $[a,b]$ 上的线性插值，我们有 $P_1(x)=\frac{x−b}{a−b}f(a)+\frac{x−a}{b−a}f(b)$。可以得到：
	
	- $A_1=A_2=\frac{b−a}{2}$
	- $\int_a^bf(x)dx\approx\frac{b−a}{2}[f(a)+f(b)]$
	
	请计算上述公式的精度
	
	??? note "Answer"
	
		考虑 $x^k(k=0,1,\cdots,n)$：
		
		- $x^0$：$\int_a^b1dx=b-a=\frac{b−a}{2}[1+1]$
		- $x^1$：$\int_a^bx dx=\frac{b^2-a^2}{2}=\frac{b−a}{2}[a+b]$
		- $x^2$：$\int_a^bx^2dx=\frac{b^3-a^3}{3}\neq\frac{b−a}{2}[a^2+b^2]$
		
		![](../../../assets/Pasted%20image%2020250430110723.png)
		
		因此精度阶数为 1

### Newton-Cotes Formula

对于等间距的节点：$x_i=a+ih,h=\frac{b-a}{n},i=0,1,\cdots,n$，我们有：

$$
\begin{aligned}
A_i&=\int_{x_0}^{x_n}\prod\limits_{j\neq i}\frac{x-x_j}{x_i-x_j}dx=\int_0^n\prod\limits_{i\neq j}\frac{(t-j)h}{(i-j)h}\cdot hdt\\
&=\frac{(b-a)(-1)^{n-i}}{ni!(n-i)!}\int_0^n\prod\limits_{i\neq j}(t-j)dt\\
\end{aligned}
$$

- 科茨系数不取决于 $f(x)$ 或 $[a,b]$，而仅由 $n,i$ 决定。因此我们可以从一张表中找出这些系数。上述公式称为**牛顿 - 科茨公式**（Newton-Cotes Formula）
***
### Trapezoidal Rule

对于 $n=1$，我们有：

- $C_0^{(1)}=\frac{1}{2},C_1^{(1)}=\frac{1}{2}$
- $\int_a^bf(x)dx\approx\frac{b-a}{2}[f(a)+f(b)]$（这被称为**梯形法则**，Trapezoidal Rule）
- $R[f]=\int_a^b​\frac{f''(\xi_x​)}{2!}​(x−a)(x−b)dx=−\frac{1}{12}​h^3f''(\xi),\xi\in [a,b],h=\frac{b-a}{1}$
- 精度阶数为 1
***
### Simpson's Rule

对于 $n=2$，我们有：

- $C_0^{(2)}=\frac{1}{6},C_1^{(2)}=\frac{2}{3},C_2^{(2)}=\frac{1}{6}$
- $\int_a^bf(x)dx\approx\frac{b-a}{6}[f(a)+4f(\frac{a+b}{2})+f(b)]$（这被称为**辛普森法则**，Simpson's Rule）
- $R[f]=-\frac{1}{90}​h^5f^{(4)}(\xi),\xi\in [a,b],h=\frac{b-a}{2}$
- 精度阶数为 3
***
### Simpson's 3/8 Rule

对于 $n=3$，我们有：

- 精度阶数为 3
- $R[f]=-\frac{3}{80}h^5f^{(4)}(\xi),\xi\in [a,b],h=\frac{b-a}{3}$
***
### Cotes Rule

对于 $n=4$，我们有：

- 精度阶数为 5
- $R[f]=-\frac{8}{945}h^7f^{(6)}(\xi),\xi\in [a,b],h=\frac{b-a}{4}$

!!! note "Theorem"

	对于使用 $n+1$ 个点的牛顿-科茨公式，$\exists\xi\in (a,b)$，使得：
	
	$$
	\int_a^bf(x)dx=\sum\limits_{k=0}^nA_kf(x_k)+\frac{h^{n+3}f^{(n+2)}(\xi)}{(n+2)!}\int_0^nt^2(t-1)\cdots(t-n)dt
	$$
	
	- 如果 $n$ 为偶数，那么 $f\in C^{n+2}[a,b]$ 且 $\int_a^bf(x)dx=\sum\limits_{k=0}^nA_kf(x_k)+\frac{h^{n+2}f^{(n+1)}(\xi)}{(n+1)!}\int_0^nt(t−1)…(t−n)dt$
	- 如果 $n$ 为奇数，那么 $f\in C^{n+1}[a,b]$
***
## Composite Numerical Integration

> 由于高次多项式的振荡性，这个过程在大的区间上是不精确的。为了解决这个问题，我们采用低阶 Newton-Cotes 的分段（Piecewise）方法

### Composite Trapezoidal Rule

我们令 $h=\frac{b-a}{n},x_i=a+kh,k=0,1,\cdots,n$，我们在每一个小区间 $[x_{k-1},x_k]$ 上应用梯形法则：

$$
\begin{aligned}
\int_{x_{k-1}}^{x_k}f(x)dx&\approx\frac{x_k-x_{k-1}}2[f(x_{k-1})+f(x_k)],k=1,...,n\\
\int_a^b f(x)dx&= \sum\limits_{i=0}^{n-1}\int_{x_i}^{x_{i+1}}f(x)dx=\frac{h}{2}[f(a)+2\sum\limits_{j=1}^{n-1}f(x_j)+f(b)]=\color{blue}{T_n}\\
R[f]&=\sum\limits_{k=1}^n[-\frac{h^3}{12}f''(\xi_k)]=-\frac{h^2}{12}(b-a)\frac{\sum\limits_{k=1}^nf''(\xi_k)}{n}\\
&=\frac{h^2}{12}(b-a)f''(\xi),\xi\in [a,b]
\end{aligned}
$$

***
### Composite Simpson's Rule

我们令 $h=\frac{b-a}{n},x_i=a+kh,k=0,1,\cdots,n$，我们在每一个小区间 $[x_{k-1},x_k]$ 上应用辛普森法则：

$$
\begin{aligned}
\int_{x_k}^{x_{k+1}}f(x)dx&\approx\frac{h}{6}[f(x_k)+4f(x_{k+\frac{1}{2}})+f(x_{k+1})]\\
\int_a^bf(x)dx&\approx\frac{h}{6}[f(a)+4\sum\limits_{k=0}^{n-1}f(x_{k+\frac{1}{2}})+f(b)]=\color{blue}{S_n}\\
R[f]&=-\frac{b-a}{180}(\frac{h}{2})^4f^{(4)}(\xi),\xi\in [a,b]\\
\end{aligned}
$$

!!! tip "Tips"

	为了简化表示，我们可以令 $n'=2n$，那么 $h'=\frac{b-a}{n'}=\frac{h}{2},x_k=a+kh'$，那么有：
	
	$$
	S_n=\frac{h'}{3}[f(a)+4\sum\limits_{\text{odd }k}f(x_k)+2\sum\limits_{\text{even }k}f(x_k)+f(b)]
	$$
	

- 所有的复合积分方法共有的一个重要性质是**舍入误差的稳定性**

!!! note "Proof"

	考虑在 $[a,b]$ 上的 $n$ 个子区间，我们假设 $f(x_i)$ 被估计为 $f^*(x_i)$，使得 $f(x_i)=f^*(x_i)+\epsilon_i,i=0,1,\cdots,n$，那么积累的误差 $e(h)$ 为：
	
	$$
	e(h)=\bigg|\frac{h}{3}[\epsilon_0+4\sum\limits_{\text{odd }k}\epsilon_k+2\sum\limits_{\text{even }k}\epsilon_k+\epsilon_n]\bigg|
	$$
	
	如果 $|\epsilon_i|<\epsilon,i=0,1,\cdots,n$，那么：
	
	$$
	e(h)<\frac{h}{3}[\epsilon+4(\frac{n}{2})\epsilon+2(\frac{n}{2}-1)\epsilon+\epsilon]=nh\epsilon=(b-a)\epsilon
	$$
	
	可见，误差界与 $h$ 和 $n$ 无关。这说明即使将一个区间分成更多子区间，也不会增加舍入误差

!!! example "Example"

	使用 $n=8$ 的梯形法则和辛普森法则来估计 $\pi=\int_0^1\frac{4}{1+x^2}dx$
	
	??? note "Answer"
	
		- 梯形法则：$T_8=\frac{1}{16}\big[f(0)+2\sum\limits_{k=1}^7f(x_k)+f(1)\big],x_k=\frac{k}{8}$，最后算得 $T_8=3.138988494$
		- 辛普森法则：$S_4=\frac{1}{24}\big[f(0)+4\sum\limits_{\text{odd }k}f(x_k)+2\sum\limits_{\text{even }k}f(x_k)+f(1)\big],x_k=\frac{k}{8}$，最后算得 $S_8=3.141592502$
		
		当我们编程的时候，我们通常会将子区间不断等分成更小的子区间，即我们取 $n=2^k,k=0,1,\cdots$
		
		当 $k=9$ 时，$T_{512}=3.14159202,\frac{4}{3}T_8-\frac{1}{3}T_4=3.14159202=S_4$
***
## Romberg Integration

考虑到梯形法则的误差为 $R_n[f]=-\frac{h^2}{12}(b-a)f''(\xi)$，当我们将区间的长度减半时：

$$
R_{2n}[f]=-\big(\frac{h}{2}\big)^2\frac{1}{12}(b-a))f''(\xi)\approx\frac{1}{4}R_n[f]
$$

得到：

$$
\begin{aligned}
\frac{I-T_{2n}}{I-T_n}&\approx\frac{1}{4}\\
I\approx\frac{4T_{2n}-T_n}{4-1}&=\frac43T_{2n}-\frac13T_n=\color{blue}{S_n}
\end{aligned}
$$

同理，总体上，我们有：

$$
\frac{4T_{2n}-T_n}{4-1}= S_n, \frac{4^2S_{2n}-S_n}{4^2-1}=C_n, \frac{4^3C_{2n}-C_n}{4^3-1}=R_n, ...
$$

其中的 $R_n$ 即为 Romberg 积分

![](../../../assets/Pasted%20image%2020250430145254.png)

***
## Richardson's Extrapolation

**目标**：使用低阶公式产生高精度的结果

假设对于某些 $h\neq 0$，我们用 $T_0(h)$ 来近似估计 $I$，使得最后的误差形式为 $T_0(h)-I=\alpha_1h+\alpha_2h^2+\alpha_3h^3+\cdots$

如果我们将 $h$ 换成 $\frac{h}{2}$，那么我们有 $T_0(\frac{h}{2})-I=\alpha_1(\frac{h}{2})+\alpha_2(\frac{h}{2})^2+\alpha_3(\frac{h}{2})^3+\cdots$

??? question "How to improve the accuracy from $O(h)$ to $O(h^2)$ ?"

	$$
	\begin{aligned}
	\frac{2T_0(\frac{h}{2})-T_0(h)}{2-1}&=-\frac{1}{2}\alpha_2h^2-\frac{3}{4}\alpha_3h^3-\cdots\\
	T_1(h)&=\frac{2T_0(\frac{h}{2})-T_0(h)}{2-1}=I+\beta_1h^2+\beta_2h^3+\cdots\\
	T_2(h)&=\frac{2^2T_1(\frac{h}{2})-T_1(h)}{2^2-1}=I+\gamma_1h^3+\gamma_2h^4+\cdots\\
	\Rightarrow T_m(h)&=\frac{2^mT_{m-1}(\frac{h}{2})-T_{m-1}(h)}{2^m-1}=I+\delta_1h^{m+1}+\delta_2h^{m+2}+\cdots\\
	\end{aligned}
	$$
	
