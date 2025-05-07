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

我们的目标是对给定的网格点集（通常是均匀分布的）$a<x_0<x_1<\cdots<x_n<b$ 估计 $y(x_i),i=0,1,\cdots,n$，即给出 $w_i\approx y(x_i)=y_i,i=0,1,\cdots,n$
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
