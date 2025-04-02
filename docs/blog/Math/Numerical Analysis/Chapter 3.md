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

### 构造 Lagrange 多项式

拉格朗日插值法就是构造一个次数至多为 $n$ 次的多项式，使它通过 $n+1$ 个给定的点，这个多项式就是拉格朗日多项式

!!! example "$n=1$ 情况"

	当 $n=1$ 时，构造 $P(x)=a_0+a_1x$，使得 $P(x_0)=y_0$，$P(x_1)=y_1$
    
    则 $P(x)=y_0+\frac{y_1-y_0}{x_1-x_0}(x-x_0)=\frac{x-x_1}{x_0-x_1}y_0+\frac{x-x_0}{x_1-x_0}y_1$。

    其中 $\frac{x-x_1}{x_0-x_1}$和$\frac{x-x_0}{x_1-x_0}$ 分别记作 $L_{1,0}(x)$和$L_{1,1}(x)$（第一个下标即为 $n$ 的值，第二个下标为样本点的序号），这称为拉格朗日基函数（Lagrange Basis）



