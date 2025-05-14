---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 05 : Initial-Value Problems for Ordinary Differential Equations

## The Elementary Theory of Initial-Value Problems

一般的一阶常微分方程初值问题表示如下：

$$
\begin{cases}
\frac{dy}{dt}=f(t,y) & t\in [a,b]\\
y(a)=\alpha
\end{cases}
$$

我们的目标是对给定的网格点集（通常是均匀分布的）$a=x_0<x_1<\cdots<x_n=b$ 估计 $y(x)$，即给出 $w_i\approx y(x_i)=y_i,i=0,1,\cdots,n$
***
### Lipschitz Condition

定义：对于集合 $D\subset R^2$ 的变量 $y$，如果存在常数 $L>0$，使得对任意 $(t,y_1),t(y_2)\in D$， $|f(t,y_1)-f(t,y_2)|\leq L|y_1-y_2|$，那么称函数 $f(t,y)$ 满足 Lipschitz 条件，其中 $L$ 被称为 $f$ 的 Lipschitz 常数

在 Lipschitz 条件下，初值问题的解是唯一的：

!!! note "Theorem"

	假设 $D=\{(t,y)|a\leq t\leq b,-\infty<y<\infty\}$，且 $f(t,y)$ 在 $D$ 上连续，如果 $f$ 在 $D$ 上对于变量 $y$ 满足 Lipschitz 条件，那么初值问题：
	
	$$
	y'(t)=f(t,y),a\leq t\leq b,y(a)=\alpha
	$$
	
	在 $a\leq t\leq b$ 有唯一解 $y(t)$
***
### Well-Posed Problem

如果一个初值问题满足以下条件：

1. 存在唯一解 $y(t)$
2. 对任意 $\epsilon>0$，存在一个正常数 $k(\epsilon)$，使得当 $|\epsilon_0|<\epsilon$，且 $\delta(t)$ 在 $[a,b]$ 上对于 $|\delta(t)|<\epsilon$ 是连续的，存在一个初值问题（原问题的摄动问题，Perturbed Problem，即在原式的基础上加上一个扰动项，假定微分方程可能有误差 $\delta$，或者初值有误差 $\epsilon$））$z'(t)=f(t,z)+\delta(t),a\leq t\leq b,z(a)=\alpha+\epsilon$ 的唯一解 $z(t)$ 使得对任意 $a\leq t\leq b,|z(t)-y(t)|<k(\epsilon)\epsilon$

那么称该初值问题为良态问题（Well-Posed Problem）

在 Lipschitz 条件下，初值问题是良态问题：

!!! note "Theorem"

	假设 $D=\{(t,y)|a\leq t\leq b,-\infty<y<\infty\}$，且 $f(t,y)$ 在 $D$ 上连续，如果 $f$ 在 $D$ 上对于变量 $y$ 满足 Lipschitz 条件，那么初值问题：
	
	$$
	y'(t)=f(t,y),a\leq t\leq b,y(a)=\alpha
	$$
	
	是良态问题
***
## Euler's Method

欧拉方法的重要思想是，因为我们有 $y'(t_0)\approx\frac{y(t_0+h)-y(t_0)}{h}\Rightarrow y(t_1)\approx y(t_0)+hy'(t_0)=\alpha+hf(t_0,\alpha)$，那么同理，我们就可以得到一般方程：$w_0=\alpha;w_{i+1}=w_i+hf(t_i,w_i),i=0,\cdots,n-1$，我们称其为**差分方程**（Difference Equation）

![](../../../assets/Pasted%20image%2020250514102510.png)
***
### Error Bound

!!! note "Theorem"

	假设 $f$ 是连续的，且满足 Lipschitz 条件，其中 $L$ 是 $D=\{(t,y)|a\leq t\leq b,-\infty<y<\infty\}$ 的 Lipschitz 常数，且存在一个常数 $M$ 使得 $\forall a\leq t\leq b,|y''(t)|\leq M$。令 $y(t)$ 为 IVP 问题 $y'(t)=f(t,y),a\leq t\leq b,y(a)=\alpha$ 的唯一解，且 $w_0,w_1,\cdots,w_n$ 为欧拉方法对正整数 $n$ 产生的近似估计，那么对于 $i=0,\cdots,n$，有：
	
	$$
	|y_i-w_i|\leq\frac{hM}{2L}[e^{L(t_i-\alpha)}-1]
	$$
	
	- 其中 $y''(t)$ 可以在不显式地知道 $y(t)$ 的情况下计算出来：$y''(t)=\frac{d}{dt}y'(t)=\frac{d}{dt}f(t,y(t))=\frac{\partial}{\partial t}f(t,y(t))+\frac{\partial}{\partial y}f(t,y(t))\cdot f(t,y(t))$

如果考虑每次计算中的舍入误差，则有：

$$
\begin{aligned}
w_0&=\alpha+\delta_0\\
w_{i+1}&=w_i+hf(t_i,w_i)+\delta_{i+1}\quad i=0,\cdots,n-1
\end{aligned}
$$

那么我们有如下定理：

!!! note "Theorem"

	令 $y(t)$ 为 IVP 问题 $y'(t)=f(t,y),a\leq t\leq b,y(a)=\alpha$ 的唯一解，且 $w_0,w_1,\cdots,w_n$ 为上面考虑舍入误差计算方法对正整数 $n$ 产生的近似估计，如果对 $i=0,\cdots,n$ 有 $|\delta_i|<\delta$，那么对每一个 $i$ 有：
	
	$$
	|y_i-w_i|\leq\frac{1}{L}(\frac{hM}{2}+\frac{\delta}{h})[e^{L(t_i-\alpha)}-1]+|\delta_0|e^{L(t_i-\alpha)}
	$$
	
***
## Higher Order Taylor Methods

### Local Truncation Error

我们定义：差分方法 $w_0=\alpha,w_{i+1}=w_i+h\phi(t_i,w_i),i=0,1,\cdots,n-1$ 有局部截断误差（Local Truncation Error）$\tau_{i+1}(h)=\frac{y_{i+1}-(y_i+h\phi(t_i,y_i))}{h}=\frac{y_{i+1}-y_i}{h}-\phi(t_i,y_i),i=0,1,\cdots,n-1$

- 如果有 $w_i=y_i$，那么上面的局部截断误差就变为 $\frac{y_{i+1}-w_{i+1}}{h}$

!!! example "对于欧拉法"

	对于欧拉法，它的局部截断误差为：
	
	$$
	\begin{aligned}
	\tau_{i+1}&=\frac{y_{i+1}-w_{i+1}}{h}=\frac{[y_i+hy'(t_i)+\frac{h^2}{2}y''(\xi_i)]-[y_i+hf(t_i,y_i)]}{h}\\
	&=\frac{h}{2}y''(\xi_i)=O(h)
	\end{aligned}
	$$
	
	- 事实上，欧拉方法就可以利用泰勒展开的一阶形式来估计 $y(t)$，即欧拉法就是高阶泰勒方法的一阶近似
***
### Higher Order Taylor Methods

$$
y_{i+1}=y_i+hf(t_i,y_i)+\frac{h^2}2f^{\prime}(t_i,y_i)+\cdots+\frac{h^n}{n!}f^{(n-1)}(t_i,y_i)+\frac{h^{n+1}}{(n+1)!}f^{(n)}(\xi_i,y(\xi_i))
$$

$n$ 阶的 Taylor 法：

$$
\begin{aligned}
w_{0}&=\alpha  \\
w_{i+1}&=w_{i}+hT^{(n)}(t_{i},w_{i})\quad(i=0,...,n-1) \\
\text{where}\quad T^{(n)}(t_i,w_i)&=f(t_i,w_i)+\frac{h}{2}f^{\prime}(t_i,w_i)+...+\frac{h^{n-1}}{n!}f^{(n-1)}(t_i,w_i)
\end{aligned}
$$

如果 $y\in C^{n+1}[a,b]$，其局部截断误差为 $O(h^{n})$

!!! example "Example"

	利用三阶的泰勒法，$n=10$，来求解 IVP 问题 $y'=y-t^2+1,0\leq t\leq 2,y(0)=0.5$
	
	??? note "Answer"
	
		首先我们来求 $f$ 的导数：
		
		$$
		\begin{aligned}
		f(t,y(t))&=y(t)-t^2+1\\
		f'(t,y(t))&=y'(t)-2t=y(t)-t^2+1-2t\\
		f''(t,y(t))&=y'(t)-2t-2=y(t)-t^2-2t-1
		\end{aligned}
		$$
		
		因此我们可以得到 Taylor 展开：
		
		$$
		\begin{aligned}
		T^{(3)}(t_i,w_i)&=f(t_i,w_i)+\frac{h}{2}f'(t_i,w_i)+\frac{h^2}{6}f''(t_i,w_i)\\
		&=(1+\frac{h}{2}+\frac{h^2}{6})(w_i-t_i^2+1)-(1+\frac{h}{3})ht_i-\frac{h^2}{3}
		\end{aligned}
		$$
		
		因此三阶的 Taylor 方法：
		
		$$
		\begin{aligned}
		w_0&=0.5\\
		w_{i+1}&=w_i+h[(1+\frac{h}{2}+\frac{h^2}{6})(w_i-t_i^2+1)-(1+\frac{h}{3})ht_i-\frac{h^2}{3}]
		\end{aligned}
		$$
		
		给定 $n=10$，那么 $h=0.2,t_i=0.2i$
		
		代入可得 $w_{i+1}=1.22133w_i-0.00885i^2-0.00853i+0.21867$
***
## Other Euler's Methods

### Implicit Euler's Method

类似地，由 $y'(t_0)=\frac{y(t_0)-y(t_0-h)}{h}$，我们还能得到 $\textcolor{red}{y(t_1)}\approx y(t_0)+h\textcolor{red}{y'(t_1)}=\alpha+hf(t_1,\textcolor{red}{y(t_1)})$，那么我们就可以得到差分方程 $w_0=\alpha,\textcolor{red}{w_{i+1}}=w_i+hf(t+1,\textcolor{red}{w_{i+1}}),i=0,\cdots,n-1$

![](../../../assets/Pasted%20image%2020250514110349.png)

通常 $w_{i+1}$ 需要迭代求解，需要有一个显式的方法给的初值

- 隐式欧拉法的局部截断误差为 $\tau_{i+1}=\frac{y_{i+1}-w_{i+1}}{h}=-\frac{h}{2}y''(\xi_i)=O(h)$
***
### Trapezoidal Method

梯形法的基本思想是用 $f(t_i,y_i)$ 和 $f(t_{i+1},y_{i+1})$ 的平均值来代替 $f(t,y)$，即：

$$
w_{i+1}=w_i+\frac{h}{2}(f(t_i,w_i)+f(t_{i+1},w_{i+1}))
$$

- 梯形法的局部截断误差为 $O(h^2)$，然而，隐式方程必须迭代求解
***
### Double-Step Method

双步法相较于之前的方法，需要两个初始值，即 $w_0$ 和 $w_1$，然后用这两个初始值来计算 $w_2$，再用 $w_1$ 和 $w_2$ 来计算 $w_3$，以此类推

$$
\begin{aligned}
y'(t_0)&=\frac{1}{2h}[y(t_0+h)-y(t_0-h)]-\frac{h^2}{6}y^{(3)}(\xi_1)\\
\Rightarrow y(t_2)&\approx y(t_0)+2hf(t_1,y(t_1))\\
w_0&=\alpha,w_{i+1}=w_{i-1}+2hf(t_i,w_i)\quad i=1,\cdots,n-1
\end{aligned}
$$

- 如果我们有假设 $w_{i-1}=y_{i-1},w_i=y_i$，那么局部截断误差为 $O(h^2)$

以上四种欧拉方法的对比如下：

![](../../../assets/Pasted%20image%2020250514111607.png)
***
## Runge-Kutta Methods

> Runge-Kutta 方法是一种具有高阶局部截断误差的单步方法，且无需计算 $f$ 的导数

Runge-Kutta 方法的整体思路是在这个单步方法中，我们考虑一条在点 $(t_i,w_i),(t_{i+1},w_{i+1})$ 之间的线段的斜率。我们可以通过找到更好的斜率来改善结果

对于欧拉法我们有：

$$
\begin{cases}
w_{i+1}=w_i+h\big[\frac{1}{2}K_1+\frac{1}{2}K_2\big]\\
K_1=f(t_i,w_1)\\
K_2=f(t_i+h,w_i+hK_1)
\end{cases}
$$

我们将其进一步泛化：

$$
\begin{cases}
w_{i+1}=w_i+h[{\color{red}{\lambda_1}}K_1+{\color{red}{\lambda_2}}K_2]\\
K_1=f(t_i,w_i)\\
K_2=f(t_i+{\color{red}{p}}h,w_i+{\color{red}{p}}hK_1)
\end{cases}
$$

对此我们需要找到合理的 $\lambda_1,\lambda_2,p$，使得该方法的局部阶段误差的阶数为 2

!!! note "寻找 $\lambda_1,\lambda_2,p$"

	1. 写出 $K_2$​ 在 $(t_i,y_i)$ 上的泰勒展开式：
	
	$$
	\begin{aligned}
	K_2&=f(t_1​+ph,y_i​+phK_1​)\\
	&=f(t_i​,y_i​)+phf_t​(t_i​,y_i​)+phK_1​f_y​(t_i​,y_i​)+O(h^2)\\
	&=y'(t_i​)+phy''(t_i​)+O(h^2)​
	\end{aligned}
	$$
	
	2. 将 $K_2$ 代入第一个公式当中：
	
	$$
	\begin{aligned}
	w_{i+1}​​&=y_i​+h\{\lambda_1​y'(t_i​)+\lambda_2​[y'(t_i​)+phy''(t_i​)+O(h^2)]\}\\
	&=y_i​+(\lambda_1​+\lambda_2​)hy'(t_i​)+\lambda_2​ph^2y''(t_i​)+O(h^3)
	\end{aligned}​
	$$
	
	3. 找到 $\lambda_1,\lambda_2,p$ 使得上面的公式的局部截断误差为 $\tau_{i+1}=(y_{i+1}-w_{i+1})/h=O(h^2)$，即：
	
	$$
	\begin{aligned}
	w_{i+1}&=y_i+(\lambda_1+\lambda_2)hy'(t_i)+\lambda_2ph^2y''(t_i)+O(h^3)\\
	y_{i+1}&=y_i+hy'(t_i)+\frac{h^2}{2}y''(t_i)+O(h^3)\\
	\end{aligned}
	$$
	
	可以解得 $\lambda_1+\lambda_2=1,\lambda_2 p=\frac{1}{2}$

我们可以看到，有无穷多个解，而由这两个方程得到的一系列方法被称为**2 阶 Runge-Kutta 法**（Runge-Kutta Method of Order 2）

- 事实上欧拉法就是 2 阶 Runge-Kutta 法的一种特殊情况， 即 $\lambda_1=\lambda_2=\frac{1}{2},p=1$
***
Runge-Kutta 法有更高阶的形式：

$$
\begin{cases}
w_{i+1}=w_i+h({\color{red}{\lambda_1}}K_1+{\color{red}{\lambda_2}}K_2+\cdots+{\color{red}{\lambda_m}}K_m)\\
K_1=f(t_i,w_i)\\
K_2=f(t_i+{\color{red}{\alpha_2}}h,w_i+{\color{red}{\beta_{21}}}hK_1)\\
K_3=f(t_i+{\color{red}{\alpha_3}}h,w_i+{\color{red}{\beta_{31}}}hK_1+{\color{red}{\beta_{32}}}hK_2)\\
\vdots\\
K_m=f(t_i+{\color{red}{\alpha_m}}h,w_i+{\color{red}{\beta_{m1}}}hK_1+{\color{red}{\beta_{m2}}}hK_2+\cdots+{\color{red}{\beta_{m,m-1}}}hK_{m-1})
\end{cases}
$$

其中最常用的是**经典的四阶 Runge-Kutta 法**：

$$
\begin{cases}
w_{i+1}=w_i+\frac{h}{6}(K_1+2K_2+2K_3+K_4)\\
K_1=f(t_i,w_i)\\
K_2=f(t_i+\frac{h}{2},w_i+\frac{h}{2}K_1)\\
K_3=f(t_i+\frac{h}{2},w_i+\frac{h}{2}K_2)\\
K_4=f(t_i+h,w_i+hK_3)
\end{cases}
$$

!!! tip "Tip"

	- 在使用 Runge-Kutta 法时，主要的计算量在于求解 $f$。Butcher 已经建立了每步求解次数与局部截断误差（LTE）阶数之间的关系：
	
		![](../../../assets/Pasted%20image%2020250514165753.png)
	
	- 因为 Runge-Kutta 法是基于泰勒展开式的，所以 $y$ 不得不足够平滑，以获取在高阶方法下的更高的精度。通常低阶方法相比高阶方法会采用更小的步幅

