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
