---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 08

## Question 01

![](../../../assets/Pasted%20image%2020241212172110.png)

本题没有明确定义“夹角”，这里直接视为函数看待

（1）$x_a(t),y_a(t),x_b(t),y_b(t)$ 满足以下微分方程组：

$$
\begin{cases}
\frac{dx_a(t)}{dt}=v_a(t)\cos\alpha(t)\\
\frac{dy_a(t)}{dt}=v_a(t)\sin\alpha(t)\\
\frac{dx_b(t)}{dt}=v_b(t)\cos\beta(t)\\
\frac{dy_b(t)}{dt}=v_b(t)\sin\beta(t)
\end{cases}
$$

（2）令 $X(t)=x_b(t)-x_a(t), Y(t)=y_b(t)-y_a(t)$，则有 $r(t)=\sqrt{X^2(t)+Y^2(t)}$

则 $\frac{dr(t)}{dt}=\frac{X(t)(v_b(t)\cos\beta(t)-v_a(t)\cos\alpha(t))+Y(t)(v_b(t)\sin\beta(t)-v_a(t)\sin\alpha(t))}{r(t)}$

我们又有 $X(t)=r(t)\cos\theta(t),Y(t)=-r(t)\sin\theta(t)$，代入可得：

$$
\begin{aligned}
\frac{dr(t)}{dt}&=\cos\theta(t)(v_b(t)\cos\beta(t)-v_a(t)\cos\alpha(t))-\sin\theta(t)(v_b(t)\sin\beta(t)-v_a(t)\sin\alpha(t))\\
&=v_b(t)cos(\theta(t)+\beta(t))-v_a(t)cos(\theta(t)+\alpha(t))
\end{aligned}
$$

因为 $\alpha(t)$ 是未定的，想要让 $r(t)$ 下降的最快即使前一项绝对值最大，即 $\theta(t)=\pi-\beta(t)$，即海盗应选择始终朝着商船的方向

（3）代入即可得 $\frac{dr(t)}{dt}=-\lambda v_a-v_a\cos(\theta(t)+\alpha(t))$

由 $\cos\theta(t)=\frac{x_b(t)-x_a(t)}{r(t)}$，有 $-\sin\theta(t)·\frac{d\theta(t)}{dt}=\frac{\lambda v_a\cos\beta(t)-v_a\cos\alpha(t)-\cos\theta(t)\frac{dr(t)}{dt}}{r(t)}$

同理由 $\sin\theta(t)=\frac{y_b(t)-y_a(t)}{r(t)}$，有 $cos\theta(t)·\frac{d\theta(t)}{dt}=\frac{\lambda v_a\sin\beta(t)-v_asin\alpha(t)-\sin\theta(t)\frac{dr(t)}{dt}}{r(t)}$

消去 $\frac{dr}{dt}$ 即可得 $\frac{d\theta(t)}{dt}=\frac{\lambda v_a\sin(\beta(t)-\theta(t))-v_a\sin(\alpha(t)-\theta(t))}{r(t)}=\frac{v_a\sin(\theta(t)-\alpha(t))}{r(t)}$

（4）代入 $\alpha(t)=0$，有 $\frac{dr(t)}{dt}=-\lambda v_a-v_a\cos\theta(t)$，$\frac{d\theta(t)}{dt}=\frac{v_a\sin\theta(t)}{r(t)}$

两式相除有 $\frac{dr(t)}{d\theta(t)}=\frac{r(t)(-\lambda-\cos\theta(t))}{\sin\theta(t)}$，即 $\frac{1}{r(t)}dr(t)=-\frac{\lambda+\cos\theta(t)}{\sin\theta(t)}d\theta(t)$

两边积分，有 $\ln r(t)-\ln r_0=-\lambda\ln|\frac{\tan\frac{\theta(t)}{2}}{\tan\frac{\theta_0}{2}}|-\ln\frac{\sin\theta(t)}{\sin\theta_0}$

即 $r(t)=\frac{r_0}{(|\frac{\tan\frac{\theta(t)}{2}}{\tan\frac{\theta_0}{2}}|)^{\lambda}\frac{\sin\theta(t)}{\sin\theta_0}}$，其中 $\tan\theta_0=\frac{y_0}{x_0},r_0=\sqrt{x_0^2+y_0^2}$

当 $\lambda=1$ 时，$r(t)=\frac{r_0}{|\frac{\tan\frac{\theta(t)}{2}}{\tan\frac{\theta_0}{2}}|\frac{\sin\theta(t)}{\sin\theta_0}}=r_0\frac{\sin^2\frac{\theta_0}{2}}{\sin^2\frac{\theta(t)}{2}}=r_0\frac{1-\cos\theta_0}{1-\cos\theta(t)}=\frac{r_0-x_0}{1-\cos\theta(t)}$

代入 $\frac{d\theta(t)}{dt}=\frac{v_a\sin\theta(t)(1-\cos\theta(t))}{r_0-x_0}$，积分解得 $t=\frac{r_0-x_0}{2v_a}(\ln|\frac{\tan\frac{\theta(t)}{2}}{\tan\frac{\theta_0}{2}}|-\frac{1}{4\sin^2\frac{\theta(t)}{2}}+\frac{1}{4\sin^2\frac{\theta_0}{2}})$，其中 $\tan\theta_0=\frac{y_0}{x_0}$
***
## Question 02

![](../../../assets/Pasted%20image%2020241212172141.png)

（1）$\frac{dx}{d\theta}=\frac{dx}{dt}\times\frac{dt}{d\theta}=\frac{nv_A\cos\omega}{\frac{v_A}{a}}=na\cos\omega$，同理 $\frac{dy}{d\theta}=na\sin\omega$

（2）切线方程 $y=\tan\omega(x-x(t))+y(t)$，法线方程 $y=-\frac{1}{\tan\omega}(x-x(t))+y(t)$

（3）令 $X=a\cos\theta-x,Y=a\sin\theta-y$，$\rho=\sqrt{X^2+Y^2}$，则：

$$
\begin{aligned}
\frac{d\rho}{d\theta}&=\frac{(a\cos\theta-x)(-a\sin\theta-na\cos\omega)+(a\sin\theta-y)(a\cos\theta-na\sin\omega)}{\rho}\\
&=\frac{xa\sin\theta-ya\cos\theta-na^2cos(\theta+\omega)+xna\cos\omega+yna\sin\omega}{\rho}
\end{aligned}
$$

由 $\cos\omega=\frac{X}{\rho}$，有 $-\sin\omega\frac{d\omega}{d\theta}=\frac{-a\sin\theta-na\cos\omega-\cos\omega\frac{d\rho}{d\theta}}{\rho}$

同理 $\sin\omega=\frac{Y}{\rho}\Rightarrow \cos\omega\frac{d\omega}{d\theta}=\frac{a\cos\theta-na\sin\omega-\sin\omega\frac{d\rho}{d\theta}}{\rho}$

两式联立消去 $\frac{d\rho}{d\theta}$ 可得 $\frac{d\omega}{d\theta}=\frac{a\cos(\theta-\omega)}{\rho}$


