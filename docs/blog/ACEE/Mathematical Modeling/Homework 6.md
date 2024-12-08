---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 6

### Question 01

![](../../../assets/Pasted%20image%2020241128171701.png)

（1）上升阶段受力分析可得：

$$
\begin{gather}
-mg-f(v)=ma=m\frac{dv}{dt}\\
\therefore \frac{dv}{dt}=-g-\frac{f(v)}{m}\\
\Rightarrow -\frac{dv}{g+\frac{f(v)}{m}}=dt
\end{gather}
$$

两边积分可得 $t_a=\int_0^{v_0}\frac{mdv}{mg+f(v)}$

下降阶段同理受力分析得 $t_d=\int_0^{v_f}\frac{mdv}{mg-f(v)}$

考虑上升距离：

$$
\begin{gather}
(mg+f(v)dx=\frac{1}{2}m[(v-dv)^2-v^2]\\
\Rightarrow -mvdv=(mg+f(v))dx
\end{gather}
$$

两边积分可得 $h=\int_0^{v_0}\frac{mvdv}{mg+f(v)}$

下降阶段同理可得 $h=\int_0^{v_f}\frac{mvdv}{mg-f(v)}$

由上升下降距离相同有 $\int_0^{v_0}\frac{mvdv}{mg+f(v)}=\int_0^{v_f}\frac{mvdv}{mg-f(v)}$

（2）由 $mg+f(v)>mg-f(v)$，所以 $v_0>v_f,t_a>t_d$
***
### Question 02

![](../../../assets/Pasted%20image%2020241128172341.png)

（1）易得在空中的时间为 $t=\frac{2v\sin\theta}{g}$，水平速度为 $v_x=v\cos\theta$，竖直速度为 $v_y=v\sin\theta-gt$

所以长度为 $L(v,\theta)=2\int_0^{\frac{v\sin\theta}{g}}\sqrt{(v\cos\theta)^2+(v\sin\theta-gt)^2}dt$

令 $s=\sqrt{(v\cos\theta)^2+(v\sin\theta-gt)^2}$

则 $L(v,\theta)=(gt-v\sin\theta)s+(\frac{v\cos\theta}{g})^2\ln[(gt-v\sin\theta)+s]|_0^{\frac{v\sin\theta}{g}}=\frac{v^2\sin\theta}{g}+\frac{v^2\cos^2\theta}{g}\ln\frac{\cos\theta}{1-\sin\theta}$

（2）$L(v,\frac{\pi}{4})=\frac{\sqrt{2}v^2}{2g}+\frac{v^2}{2g}\ln\frac{\sqrt{2}}{2-\sqrt{2}}\approx 1.1\frac{v^2}{g}$

$L(v,\frac{\pi}{2})=\frac{v^2}{g}$

$\therefore L(v,\frac{\pi}{4})>L(v,\frac{\pi}{2})$

（3）$\frac{\partial L}{\partial\theta}=\frac{v^2\cos\theta}{g}-\frac{2v^2\sin\theta\cos\theta}{g}\ln\frac{\cos\theta}{1-\sin\theta}+\frac{v^2\cos\theta}{g}=0$

$\therefore\sin\theta\ln\frac{\cos\theta}{1-\sin\theta}=1$

