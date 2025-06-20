---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 11

## 4.3.7

![](../../../assets/Pasted%20image%2020250619130130.png)

由 Trapezoidal Rule 条件可得 $\int_a^b f(x)dx\approx\frac{b-a}{2}[f(a)+f(b)]\Rightarrow f(0)+f(2)=4$

由 Simpson's Rule 条件可得 $\int_a^b f(x)dx\approx\frac{b-a}{6}[f(a)+4f(\frac{a+b}{2})+f(b)]\Rightarrow f(0)+4f(1)+f(2)=6$

解得 $f(1)=\frac{1}{2}$
***
## 4.3.9

![](../../../assets/Pasted%20image%2020250619130150.png)

对于 $f(x)=x^0$：$\int_{-1}^1 1dx=2=1+1$

对于 $f(x)=x^1$：$\int_{-1}^1 xdx=0=-\frac{\sqrt{3}}{3}+\frac{\sqrt{3}}{3}$

对于 $f(x)=x^2$：$\int_{-1}^1x^2dx=\frac{2}{3}=\frac{1}{3}+\frac{1}{3}$

对于 $f(x)=x^3$：$\int_{-1}^1x^3dx=0=-\frac{\sqrt{3}}{9}+\frac{\sqrt{3}}{9}$

对于 $f(x)=x^4$：$\int_{-1}^1x^4dx=\frac{2}{5}\neq\frac{1}{9}+\frac{1}{9}$

所以精度为 3
***
## 4.3.11

![](../../../assets/Pasted%20image%2020250619130208.png)

因为满足精度小于等于 2 的情况，所以有方程式：

$$
\begin{cases}
2=c_0+c_1+c_2\\
0=-c_0+c_2\\
\frac{2}{3}=c_0+c_2
\end{cases}
$$

解得 $c_0=\frac{1}{3},c_1=\frac{4}{3},c_2=\frac{1}{3}$
***
## 4.3.13

![](../../../assets/Pasted%20image%2020250619130226.png)

有三个未知数，我们取到精度为 2 构造三个方程：

$$
\begin{cases}
1=c_0+c_1\\
\frac{1}{2}=c_1x_1\\
\frac{1}{3}=c_1x_1^2
\end{cases}
$$

解得 $c_0=\frac{1}{4},c_1=\frac{3}{4},x_1=\frac{2}{3}$
