---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 01 : Mathematical Preliminaries

## Roundoff Errors and Computer Arithmetic

- 截断误差（Truncation Error）：使用截断的（或者说有限的）求和来近似无穷级数的和产生的误差
- 舍入误差（Roundoff Error）：当计算机执行实数计算时产生的误差。这是因为计算机中的算术运算涉及到的数字只有有限位数

> 理论上截断误差和舍入误差有一定的重合（比如 $\frac{1}{3}=0.3333...\approx 0.3333$），那么如何区分呢？截断误差更注重级数的“和”而舍入误差更注重数字的运算

!!! note "Normalized Decimal Floating-point Form of a Real Number"

	对于一个 $k$ 位十进制机器数（$k-$ digit Decimal Machine Number）都可以被表示为 $\pm 0.d_1d_2...d_k\times 10^n$，其中 $1\leq d_1\leq 9,0\leq d_i\leq 9(i=2,...,k)$ 
	
	那么对于一个实数 $y=0.d_1d_2...d_kd_{k+1}d_{k+2}...\times 10^n$ 来说，截断法和舍入法可以表示为：
	
	$$
	fl(y)=\begin{cases}
	0.d_1d_2...d_k\times 10^n(\text{Chopping})\\
	\text{Chop}(y+5\times 10^{n-(k+1)})=0.\delta_1\delta_2...\delta_k\times 10^n
	\end{cases}
	$$
	
***
## Absolute Error and Relative Error

- 如果 $p^*$ 是 $p$ 的近似值，定义 $|p^*-p|$ 为绝对误差（Absolute Error）， $\frac{|p^*-p|}{|p|}(p\not=0)$ 为相对误差（Relative Error）
- 如果有 $t$ 是满足 $\frac{|p^*-p|}{|p|}<5\times 10^{-t}$ 的最大非负整数，那么称 $p^*$ 是 $p$ 精确到 $t$ 位有效数字（Significant Digits/Figures）的估计值

!!! note "近似产生的误差"

	- Chopping : $|\frac{y-fl(y)}{y}|=|\frac{0.d_1d_2...d_kd_{k+1}...\times 10^n-0.d_1d_2...d_k\times 10^n}{0.d_1d_2...d_kd_{k+1}...\times 10^n}|=|\frac{0.d_{k+1}d_{k+2}...}{0.d_1d_2...}|\times 10^{-k}\leq\frac{1}{0.1}\times 10^{-k}=10^{-k+1}$
	- Rounding : $|\frac{y-fl(y)}{y}|\leq\frac{0.5\times 10^{n-k}}{0.d_1d_2...d_k\times 10^{n}}=\frac{0.5}{0.1}\times 10^{-k}=0.5\times 10^{-k+1}$

!!! note "误差的产生"

	- 两个近乎相等的数相减会导致有效数字的相消，会有较大的相对误差
	
	!!! note ""
	
		例如：$a_1=0.12345,a_2=0.12346$（这里的等号并非真实“等号”），两者本来都有 $5$ 位有效数字，但是相减后只剩下 $1$ 位有效数字
		
		 我们记 $a_1=0.12345+\epsilon_1,a_2=0.12346+\epsilon_2(\epsilon_1,\epsilon_2\in [-5\times 10^{-6},5\times 10^{-6}])$（这里的等号才是真正的等号），那么有 $e=\epsilon_2-\epsilon_1\in [-10^{-5},10^{-5}]$
		
		这时候 $a_2-a_1$ 的近似值为 $0.00001$，真实值为 $0.00001+e$，相对误差 $e_{\text{rel}}=\frac{e}{0.00001+e}\leq 0.5$
	
	- 如果有限位的表示或计算产生了误差，则除以一个小数（或者乘以一个大数）会放大绝对误差
	
	!!! note ""
	
		例如，对于一个实数 $\frac{p}{q}$，如果 $q$ 有一定的扰动 $\epsilon_q$，那么绝对误差 $e=\frac{p}{q+\epsilon_q}-\frac{p}{q}$，这可以近似视为 $(\frac{p}{q})'=-\frac{p}{q^2}$，那么可以看到如果 $q$ 比较小的话那么绝对误差会较大

!!! example "误差计算举例"

	=== "Question"
	
		计算 $f(x)=x^3-6.1x^2+3.2x+1.5$ 在 $x=4.71$ 的值，精确到三位有效数字
	
	=== "正常算法"
	
		|          | $x$    | $x^2$     | $x^3$                           | $6.1x^2$                      | $3.2x$   |
		| -------- | ------ | --------- | ------------------------------- | ----------------------------- | -------- |
		| Exact    | $4.71$ | $22.1841$ | $104.487111$                    | $135.32301$                   | $15.072$ |
		| Chopping | $4.71$ | $22.1$    | $104.$                          | $6.1*22.1=134.81\approx 134.$ | $15.0$   |
		| Rounding | $4.71$ | $22.2$    | $22.2*4.71=104.562\approx 105.$ | $6.1*22.2=135.42\approx 135.$ | 15.1     |
		
		- Exact Value : $f(4.71)=104.487111−135.32301+15.072+1.5=−14.263899$
		- Chopping : $f(4.71)=104−134+15.0+1.5=−13.5$
			- Relative Error : $\frac{|-14.263899+13.5|}{|-14.263899|}\approx 5.35\%$
		- Rounding : $f(4.71)=105−135+15.1+1.5=−13.4$
			- Relative Error : $\frac{|−14.263899+13.4|}{|−14.263899|}\approx 6.06\%$
		
		可以看到，有时候舍入误差比截断误差更大，但是这样的算法误差还是太大了。


***




