---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Quiz

## Quiz 1

![](../../../assets/Pasted%20image%2020250619174812.png)

（a）Exact：$\frac{4}{5}\times\frac{1}{3}=\frac{4}{15}$

Three-Digit Chopping：$\frac{4}{5}=0.800,\frac{1}{3}\approx 0.333,\frac{4}{5}\times\frac{1}{3}=0.8\times 0.333=0.2664\approx 0.266$

Three-Digit Rounding：$\frac{4}{5}=0.800,\frac{1}{3}\approx 0.333,\frac{4}{5}\times\frac{1}{3}=0.8\times 0.333=0.2664\approx 0.266$

Relative Error：$e=\frac{|p-p^*|}{|p|}=\frac{|\frac{4}{15}-0.266|}{\frac{4}{15}}=0.0025$

（b）Exact：$(\frac{1}{3}+\frac{3}{11})-\frac{3}{20}=\frac{301}{660}$

Three-Digit Chopping：$\frac{1}{3}\approx 0.333,\frac{3}{11}\approx 0.272,\frac{3}{20}=0.150,0.333+0.272-0.150=0.455$

Three-Digit Rounding：$\frac{1}{3}\approx 0.333,\frac{3}{11}\approx 0.273,\frac{3}{20}=0.150,0.333+0.272-0.150=0.456$

Chopping Error：$e=\frac{|p-p^*|}{|p|}=\frac{|\frac{301}{660}-0.455|}{\frac{301}{660}}=0.002325$

Rounding Error：$e=\frac{|p-p^*|}{|p|}=\frac{|\frac{301}{660}-0.456|}{\frac{301}{660}}=0.000133$
***
## Quiz 2

![](../../../assets/Pasted%20image%2020250619202212.png)

构造 $g(x)=x=(x+1)^{\frac{1}{3}},g'(x)=\frac{1}{3(x+1)^{\frac{2}{3}}}$，在 $[1,2]$ 中 $|g'(x)|\leq|g'(1)|\approx 0.21<1$，所以存在不动点且可以迭代计算

$$
\begin{aligned}
p_1=g(p_0)=2^{\frac{1}{3}}\approx 1.2599&,p_2=g(p_1)=(1+1.2599)^{\frac{1}{3}}\approx 1.3123\\
\Rightarrow e\leq\frac{0.21}{1-0.21}|1.3123&-1.2599|=0.0139>10^{-2}\\
p_3=g(p_2)&=(1+1.3123)^{\frac{1}{3}}\approx 1.3224\\
\Rightarrow e=\frac{0.21^2}{1-0.21}|1.3123&-1.2599|=2.925\times 10^{-3}<10^{-2}
\end{aligned}
$$

综上计算答案为 $1.3224$
***
## Quiz 3

![](../../../assets/Pasted%20image%2020250619204910.png)

（a）

$$
\begin{aligned}
\overline{A}=\begin{bmatrix}
1 & 1 & 0 & 1 & 2\\
2 & 1 & -1 & 1 & 1\\
4 & -1 & -2 & 2 & 0\\
3 & -1 & -1 & 2 & -3
\end{bmatrix}
\Rightarrow\begin{bmatrix}
1 & 1 & 0 & 1 & 2\\
0 & 1 & 1 & 1 & 3\\
0 & 0 & 3 & 3 & 7\\
0 & 0 & 0 & 0 & -4
\end{bmatrix}
\end{aligned}
$$

可以看到方程无解，不需要行交换

（b）

$$
\begin{aligned}
\overline{A}=\begin{bmatrix}
1 & 1 & 0 & 1 & 2\\
2 & 1 & -1 & 1 & 1\\
-1 & 2 & 3 & -4 & 4\\
3 & -1 & -1 & 2 & -3
\end{bmatrix}
\Rightarrow\begin{bmatrix}
1 & 1 & 0 & 1 & 2\\
0 & 1 & 1 & 1 & 3\\
0 & 0 & 0 & -6 & -3\\
0 & 0 & 3 & 3 & 3\\
\end{bmatrix}
\Rightarrow\begin{bmatrix}
1 & 1 & 0 & 1 & 2\\
0 & 1 & 1 & 1 & 3\\
0 & 0 & 1 & 1 & 1\\
0 & 0 & 0 & -6 & -3
\end{bmatrix}
\end{aligned}
$$

方程有唯一解 $x_1=-\frac{1}{2},x_2=2,x_3=\frac{1}{2},x_4=\frac{1}{2}$，需要进行行交换
***
## Quiz 4

![](../../../assets/Pasted%20image%2020250619210621.png)

能观察到第一次消元第二行前三个元素均为 0，所以需要进行行交换

$$
\begin{aligned}
P&=\begin{bmatrix}
1 & 0 & 0 & 0\\
0 & 0 & 0 & 1\\
0 & 0 & 1 & 0\\
0 & 1 & 0 & 0
\end{bmatrix}
\Rightarrow PA=\begin{bmatrix}
1 & -2 & 3 & 0\\
2 & 1 & 3 & -1\\
1 & -2 & 2 & -2\\
1 & -2 & 3 & 1
\end{bmatrix}\\
L_1&=\begin{bmatrix}
1 & 0 & 0 & 0\\
-2 & 1 & 0 & 0\\
-1 & 0 & 1 & 0\\
-1 & 0 & 0 & 1
\end{bmatrix}
\Rightarrow L_1PA=\begin{bmatrix}
1 & -2 & 3 & 0\\
0 & 5 & -3 & -1\\
0 & 0 & -1 & -2\\
0 & 0 & 0 & 1
\end{bmatrix}=U\\
\Rightarrow A&=P^{-1}L_1^{-1}U,P'=P^{-1}=\begin{bmatrix}
1 & 0 & 0 & 0\\
0 & 0 & 0 & 1\\
0 & 0 & 1 & 0\\
0 & 1 & 0 & 0
\end{bmatrix}\\
L&=L_1^{-1}=\begin{bmatrix}
1 & 0 & 0 & 0\\
2 & 1 & 0 & 0\\
1 & 0 & 1 & 0\\
1 & 0 & 0 & 1
\end{bmatrix},U=\begin{bmatrix}
1 & -2 & 3 & 0\\
0 & 5 & -3 & -1\\
0 & 0 & -1 & -2\\
0 & 0 & 0 & 1
\end{bmatrix}
\end{aligned}
$$
***
## Quiz 5

![](../../../assets/Pasted%20image%2020250619212641.png)

$$
\begin{aligned}
x_1^{(1)}&=x_1^{(0)}+\frac{1.1}{3}(1-3x_1^{(0)}+x_2^{(0)}-x_3^{(0)})=\frac{1.1}{3}\approx 0.367\\
x_2^{(1)}&=x_2^{(0)}+\frac{1.1}{6}(0-3x_1^{(1)}-6x_2^{(0)}-2x_3^{(0)})=-\frac{1.21}{6}\approx -0.202\\
x_3^{(1)}&=x_3^{(0)}+\frac{1.1}{7}(0-3x_1^{(1)}-3x_2^{(1)}-7x_3^{(0)})\approx 0.551\\
\therefore x^{(1)}&=\begin{bmatrix}
0.367\\
-0.202\\
0.551
\end{bmatrix}
\end{aligned}
$$
***
## Quiz 6

![](../../../assets/Pasted%20image%2020250619213945.png)

（a）

$$
\begin{aligned}
\det(A)&=\frac{1}{2}\times\frac{1}{4}-\frac{1}{3}\times\frac{1}{3}=\frac{1}{72}\\
A^{-1}&=72\times\begin{bmatrix}
\frac{1}{4} & -\frac{1}{3}\\
-\frac{1}{3} & \frac{1}{2}
\end{bmatrix}=\begin{bmatrix}
18 & -24\\
-24 & 36
\end{bmatrix}\\
K(A)&=\|A\|\|A^{-1}\|=\frac{5}{6}\times 60=50
\end{aligned}
$$

（b）

$$
\begin{aligned}
\det(A)&=1\times 2-1.00001\times 2=-0.00002\\
A^{-1}&=-50000\times\begin{bmatrix}
2 & -2\\
-1.00001 & 1
\end{bmatrix}=\begin{bmatrix}
-100000 & 100000\\
50000.5 & -50000
\end{bmatrix}\\
K(A)&=\|A\|\|A^{-1}\|=3.00001\times 200000=600002
\end{aligned}
$$
***
## Quiz 7

![](../../../assets/Pasted%20image%2020250619214800.png)

| $x_0=0.0$ | 1.0000  |        |         |         |          |
| --------- | ------- | ------ | ------- | ------- | -------- |
| $x_1=0.2$ | 1.22140 | 1.1070 |         |         |          |
| $x_2=0.4$ | 1.49182 | 1.3521 | 0.61275 |         |          |
| $x_3=0.6$ | 1.82212 | 1.6515 | 0.7485  | 0.22625 |          |
| $x_4=0.8$ | 2.22554 | 2.0171 | 0.914   | 0.27583 | 0.061975 |

$$
\begin{aligned}
\therefore f(0.05)&=f(0)+1.1070*(0.05-0)+0.61275*(0.05-0)*(0.05-0.2)\\
&+0.22625*(0.05-0)*(0.05-0.2)*(0.05-0.4)\\
&+0.061975*(0.05-0)*(0.05-0.2)*(0.05-0.4)*(0.05-0.6)\approx 1.0513
\end{aligned}
$$

***
## Quiz 8

![](../../../assets/Pasted%20image%2020250619214916.png)

| $F(l)$ | $l$  | $x=  l-E$ |
| ------ | ---- | --------- |
| 2      | 7.0  | 1.7       |
| 4      | 9.4  | 4.1       |
| 6      | 12.3 | 7.0       |

对误差 $S=\sum\limits_{n=1}^3[F-kx]^2$ 求偏导得 $\frac{\partial S}{\partial k}=\sum\limits_{i=1}^3-2x(F-kx)=0\Rightarrow k=\frac{\sum\limits_{i=1}^nFx}{\sum\limits_{i=1}^nx^2}\approx 0.89956$
***
## Quiz 9

![](../../../assets/Pasted%20image%2020250619220228.png)

$\int_{-1}^1 1dx=2,\int_{-1}^1 x^2dx=\frac{2}{3},\int_{-1}^1(x^2-2x+3)dx=\frac{20}{3},\int_{-1}^1(x^2-2x+3)xdx=-\frac{4}{3}$

$\therefore f(x)\approx \frac{10}{3}-2x=3.33333-2x$
***
## Quiz 10

![](../../../assets/Pasted%20image%2020250619220340.png)

$$
\begin{aligned}
LHS&=\int_{-1}^1\frac{[\cos(n\arccos x)]^2}{\sqrt{1-x^2}}dx\\
&=\int_{-1}^1[\cos(n\arccos x)]^2d(\arccos x)\\
&=\int_0^{\pi}[\cos ny]^2dy=\int_0^{\pi}\frac{\cos 2ny+1}{2}dy=\frac{\pi}{2}
\end{aligned}
$$

或者换元 $\theta=\arccos(x)$ 也可
***
## Quiz 11

![](../../../assets/Pasted%20image%2020250619220432.png)

![](../../../assets/Pasted%20image%2020250619220442.png)

根据题目条件我们得到方程组：

$$
\begin{cases}
2f(0)=12\\
1\times (f(-0.5)+f(0.5))=5\\
\frac{1}{3}[f(-1)+4f(0)+f(1)]=6\\
f(-1)=f(1)\\
f(-0.5)=f(0.5)-1
\end{cases}
$$

解得 $f(-1)=-3,f(-0.5)=2,f(0)=6,f(0.5)=3,f(1)=-3$
***
## Quiz 12

![](../../../assets/Pasted%20image%2020250619222942.png)

给定节点 $x_1,x_2,\cdots,x_n$，构造 $w(x)=\prod_{i=1}^n(x-x_i),P(x)=w^2(x)=(x-x_1)^2(x-x_2)^2\cdots(x-x_n)^2$

计算 $P(x)$ 在区间 $[a,b]$ 上的精确积分值 $I=\int_a^bP(x)dx=\int_a^b[w(x)]^2dx>0$

应用到公式当中，$Q(P)=\sum\limits_{i=1}^nc_iP(x_i)=0\neq I$

所以存在一个 2n 次多项式使得求积公式不精确
***
## Quiz 13

![](../../../assets/Pasted%20image%2020250619225221.png)

对于中点法：

$$
\begin{aligned}
w_{i+1}&=w_i+h[-w_i-\frac{h}{2}(-w_i+t_i+1)+t_i+\frac{h}{2}+1]\\
&=w_i(1-h+\frac{h^2}{2})+t_ih(1-\frac{h}{2})+h
\end{aligned}
$$

对于改进欧拉法：

$$
\begin{aligned}
w_{i+1}&=w_i+\frac{h}{2}\cdot[f(t_i,w_i)+f(t_i+h,w_i+h\cdot f(t_i,w_i))]\\
&=w_i+\frac{h}{2}\cdot[-w_i+t_i+1+-w_i-h(-w_i+t_i+1)+t_i+h+1]\\
&=w_i(1-h+\frac{h^2}{2})+t_ih(1-\frac{h}{2})+h
\end{aligned}
$$

所以两者迭代公式相同，对任意 $h$ 估计也相同
***
## Quiz 14

![](../../../assets/Pasted%20image%2020250620102453.png)

使用牛顿向后差分公式，在 $(t_i,f_i),(t_{i-1},f_{i-1})$ 上对 $f$ 插值：

$$
P_1(t_i+sh) = f_i + s \nabla f_i = f_i + s(f_i - f_{i-1})
$$

得到 $w_{i+1} = w_i + h \int_0^1 [f_i + s(f_i - f_{i-1})]ds = w_i + \frac{h}{2}(3f_i - f_{i-1})$ 
***
## Quiz 15

![](../../../assets/Pasted%20image%2020250620103846.png)

对于测试方程 $f(t,y)=\lambda y$，代入梯形方法公式：

$$
\begin{aligned}
w_{i+1}&=w_i+\frac{h}{2}(\lambda w_i+\lambda w_{i+1})\\
\Rightarrow w_{i+1}-\frac{h\lambda}{2}w_{i+1}&=w_i+\frac{h\lambda}{2}w_i\\
\Rightarrow w_{i+1}&=\frac{1+\frac{h\lambda}{2}}{1-\frac{h\lambda}{2}}w_i
\end{aligned}
$$

令 $z=h\lambda$，则解得比例因子为 $R(z)=\frac{1+\frac{z}{2}}{1-\frac{z}{2}}$，由稳定性要求 $|R(z)|\leq 1$：

$$
\begin{aligned}
\bigg|\frac{1+\frac{z}{2}}{1-\frac{z}{2}}\bigg|&\leq 1\\
\bigg|1+\frac{z}{2}\bigg|^2&\leq\bigg|1-\frac{z}{2}\bigg|^2\\
(1+\frac{z}{2})(1+\frac{\overline{z}}{2})&\leq(1-\frac{z}{2})(1-\frac{\overline{z}}{2})\\
\Rightarrow\frac{z+\overline{z}}{2}&\leq -\frac{z+\overline{z}}{2}\\
\Rightarrow Re(z)&\leq 0
\end{aligned}
$$

因此稳定性要求 $Re(\lambda)\leq 0$