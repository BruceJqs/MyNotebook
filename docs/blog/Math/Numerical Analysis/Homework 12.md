---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 12

## 8.3.3

![](../../../assets/Pasted%20image%2020250619134405.png)

![](../../../assets/Pasted%20image%2020250619135253.png)

根据公式计算 $\tilde{T_4}$ 的 4 个零点：$x_1=\cos(\frac{1}{8}\pi),x_2=\cos(\frac{3}{8}\pi),x_3=\cos(\frac{5}{8}\pi),x_4=\cos(\frac{7}{8}\pi)$

（a）$c_0=f[x_1]=y_1=e^{x_1}=2.519,c_1=\frac{y_2-y_1}{x_2-x_1}=1.945,c_2=0.705,c_3=0.176$

（b）$c_0=f[x_1]=0.798,c_1=0.786,c_2=-0.144,c_3=-0.156$

（c）$c_0=1.073,c_1=0.379,c_2=-0.096,c_3=0.051$
***
## 8.3.7

![](../../../assets/Pasted%20image%2020250619134435.png)

六阶麦克劳林多项式为 $\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}+\frac{1}{7!}\sin^7(\xi)x^7$

对于切比雪夫多项式，$T_0(x)=1,T_1(x)=x,T_2(x)=2x^2-1,T_3(x)=4x^3-3x$,$T_4(x)=8x^4-8x^2+1,T_5(x)=16x^5-20x^3+5x$

尝试降到三阶：$P_3(x)=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{1}{5!}\times\frac{1}{2^4}T_5(x)=09973958x-0.15625x^3$

误差 $\max_{[-1,1]}|\sin x-P_3(x)|<\max_{[-1,1]}|\sin x-P_4(x)|+\frac{1}{5!*2^4}\max_{[-1,1]}|T_5(x)|$ $=\frac{1}{7!}+\frac{1}{5!*16}=7.19*10^{-4}$
***
## 8.3.9

![](../../../assets/Pasted%20image%2020250619134448.png)

$$
\begin{aligned}
LHS&=\int_{-1}^1\frac{[\cos(n\arccos x)]^2}{\sqrt{1-x^2}}dx\\
&=\int_{-1}^1[\cos(n\arccos x)]^2d(\arccos x)\\
&=\int_0^{\pi}[\cos ny]^2dy=\int_0^{\pi}\frac{\cos 2ny+1}{2}dy=\frac{\pi}{2}
\end{aligned}
$$