---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 02

## 2.1.13

![](../../../assets/Pasted%20image%2020250227220401.png)

$\because |p_n-p|\leq\frac{b-a}{2^n}=\frac{1}{2^n}\leq 10^{-4}$

$\therefore n\geq\log_{2}{10^4}\approx 13.28$

所以需要至少 14 次迭代，$p_{14}=1.32477$

***
## 2.1.15

![](../../../assets/Pasted%20image%2020250227221659.png)

$\lim\limits_{n\rightarrow\infty}(p_n-p_{n-1})=\lim\limits_{n\rightarrow\infty}\frac{1}{n}=0$

而 $\sum\limits_{k=1}^n\frac{1}{k}=(1)+(\frac{1}{2}+\frac{1}{3})+(\frac{1}{4}+\frac{1}{5}+\frac{1}{6}+\frac{1}{7})+...\geq\frac{1}{2}+\frac{1}{2}+...$

$\therefore\lim\limits_{n\rightarrow\infty}p_n=\infty$
***
## 2.2.3

![](../../../assets/Pasted%20image%2020250227221747.png)

（a）$g(x)=\frac{20x+21/x^2}{21},g'(x)=\frac{20}{21}-\frac{2}{x^3}\leq\frac{20}{21}$

（b）$g(x)=x-\frac{x^3-21}{3x^2},g'(x)=\frac{2}{3}-\frac{14}{x^3}\leq\frac{2}{3}$

（c）$g(x)=x-\frac{x^4-21x}{x^2-21},g'(x)=1-\frac{(4x^3-21)(x^2-21)-(x^4-21x)(2x)}{(x^2-21)^2}=1-\frac{2x^5-84x^3+21x^2+441}{(x^2-21)^2}$ ，并不收敛

（d）$g(x)=\sqrt{\frac{21}{x}},|g'(x)|=|\frac{1}{2\sqrt{\frac{21}{x}}}\times(-\frac{21}{x^2})|=\frac{21}{2\sqrt{21x^3}}\leq\frac{\sqrt{21}}{4\sqrt{2}}$

所以从快到慢为 b, d, a
***
## 2.2.19

![](../../../assets/Pasted%20image%2020250227221821.png)

（a）$g(x)=\frac{1}{2}x+\frac{1}{x},g'(x)=\frac{1}{2}-\frac{1}{x^2}\leq\frac{1}{2}$

那么由定理 2.3 得有唯一不动点

（b）$x_1=\frac{1}{2}x_0+\frac{1}{x_0}>\sqrt{2}$

（c）因为由 b 我们知道如果 $0<x_0<\sqrt{2}$，最终也会到 $x>\sqrt{2}$ 的情况，那么最后还是会收敛到 $\sqrt{2}$，所以对于任意 $x_0>0$，都会收敛到 $\sqrt{2}$