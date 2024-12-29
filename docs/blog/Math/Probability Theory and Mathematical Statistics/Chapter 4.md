---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  
# Chapter 04 : 随机变量的数字特征

## 数学期望

### 离散型随机变量的数学期望

设离散型随机变量 $X$ 的概率分布率为 $P\{X=x_i\}=p_i,i=1,2,..$.，若级数 $\sum\limits_{i=1}^{+\infty}=|x_i|p_i<+\infty$（绝对收敛），则称级数 $\sum\limits_{i=1}^{+\infty}=|x_i|p_i$ 为 $X$ 的数学期望（Mathematical Expectation）或均值（Mean），简称为期望，记 $E(X)=\sum\limits_{i=1}^{+\infty}x_ip_i$。

如果 $\sum\limits_{i=1}^{+\infty}=|x_i|p_i=+\infty$ 则称随机变量 $X$ 的数学期望不存在。
***
#### 0-1 分布的数学期望

设随机变量 $X$ 服从 0-1 分布 $B(1,p)(0<p<1)$，则：

$$
E(X)=\sum\limits_{k=0}^1k·P\{X=k\}=0·P\{X=0\}+1·P\{X=1\}=0·(1-p)+1·p=p
$$

***
#### 二项分布的数学期望

设随机变量 $X$ 服从二项分布 $B(n,p)(n\in\mathbb{N}^∗,0<p<1)$，则：

$$
E(X)=\sum\limits_{k=0}^nk⋅P\{X=k\}=\sum\limits_{k=0}^nk⋅C_n^kp^k(1−p)^{n−k}=np\sum\limits_{k=1}^nC_{n−1}^{k−1}p^{k−1}(1−p)^{n−k}=np
$$


或者，我们引入随机变量 $X_i=\begin{cases}1,第i次试验成功\\0,第i次试验失败\end{cases}$，则 $X=\sum\limits_{i=1}^nX_i$，且 $X_i$ 相互独立，且 $X_i∼B(1,p)$，则：

$$
E(X)=E(\sum\limits_{i=1}^nX_i)=\sum\limits_{i=1}^nE(X_i)=\sum\limits_{i=1}^np=np
$$

***
#### 泊松分布的数学期望

设随机变量 $X$ 服从泊松分布 $P(\lambda)(\lambda>0)$，则：

$$
E(X)=\sum\limits_{k=0}^{+\infty}k⋅P\{X=k\}=\sum\limits_{k=0}^{+\infty}k⋅\frac{\lambda ^k}{k!}e^{−\lambda}=\lambda e^{−\lambda}\sum\limits_{k=1}^{+\infty}\frac{\lambda^{k−1}}{(k−1)!}=\lambda
$$

由此式可知，已知泊松分布的数学期望可以确定泊松分布。
***
### 连续型随机变量的数学期望

设连续型随机变量 $X$ 的密度函数为 $f(x)$，若 $\int_{−\infty}^{+\infty}|x|f(x)dx<+\infty$，则称积分$\int_{−\infty}^{+\infty}xf(x)dx$ 为 $X$ 的数学期望或均值，简称为期望，记 $E(X)=\int_{−\infty}^{+\infty}xf(x)dx$。

如果 $\int_{−\infty}^{+\infty}|x|f(x)dx=+\infty$ 则称随机变量 $X$ 的数学期望不存在。
***
#### 均匀分布的数学期望

设随机变量 $X$ 服从均匀分布 $U(a,b)(a<b)$，则：

$$
E(X)=\int_{−\infty}^{+\infty}xf(x)dx=\int_{−\infty}^{+\infty}x\frac{1}{b−a}dx=\frac{1}{b−a}\int_{−\infty}^{+\infty}xdx=\frac{1}{b−a}⋅\frac{x^2}{2}|_a^b=\frac{a+b}{2}
$$

***
#### 指数分布的数学期望

设随机变量 $X$ 服从指数分布 $E(\lambda)(\lambda>0)$，则：

$$
E(X)=\int_{−\infty}^{+\infty}xf(x)dx=\int_0^{+\infty}x\lambda e^{−λx}dx=−\int_0^{+\infty}xd(e^{−\lambda x})=−(xe^{−\lambda x})|_0^{+\infty}+\int_0^{+\infty}e^{−\lambda x}dx=\frac{1}{\lambda}
$$

由此式可知，已知指数分布的数学期望可以确定指数分布。
***
#### 标准正态分布的数学期望

设随机变量 $X$ 服从标准正态分布 $N(0,1)$，注意到其密度函数 $\varphi(x)=\frac{1}{\sqrt{2\pi}}e^{−\frac{x^2}{2}},x\in\mathbb{R}$ 为偶函数，那么$x\varphi(x)$ 是奇函数，所以 $E(X)=0$
***
#### 正态分布的数学期望

设随机变量X服从正态分布 $N(\mu,\sigma^2)(\sigma>0)$，则：

$$
\begin{gather}
Z=\frac{X−\mu}{\sigma}∼N(0,1)\\
E(X)=E(\sigma Z+\mu)=\sigma E(Z)+\mu=\mu
\end{gather}
$$

***
### 随机变量函数的数学期望

对于随机变量函数，在保证期望存在的情况下，只需要将定义中 $x_i$ 换为 $g(x_i)$ 即可，但我们不需要计算 $g(x_i)$ 的概率分布率：

离散型：$Z=g(X)$，则 $E(Z)=E[g(X)]=\sum\limits_{i=1}^{+\infty}g(x_i)p_i$

连续型：$Z=g(X)$，则 $E(Z)=E[g(X)]=\int g(x)f(x)dx$

二元离散型：$Z=h(X,Y)$，则 $E(Z)=E[h(X,Y)]=\sum\limits_{i=1}^{+\infty}\sum\limits_{j=1}^{+\infty}h(x_i,y_j)p_{ij}$

二元连续型：$Z=h(X,Y)$，则 $E(Z)=E[h(X,Y)]=\int_{−\infty}^{+\infty}\int_{−\infty}^{+\infty}h(x,y)f(x,y)dxdy$

!!! tip

	以上所有的 $p_i,p_{ij},f(x),f(x,y)$ 均为 $X,Y$ 本来的联合分布率，而不是 $Z$ 的联合分布率
***
### 数学期望的性质

除了使用定义计算，还有一些性质可以简化计算：

- 若 $C$ 是常数，则 $E(C)=C$；
- 设 $X$ 是随机变量，$C$ 是常数，则 $E(C⋅X)=C⋅E(X)$；
- 设 $X,Y$ 是两个随机变量，则 $E(X+Y)=E(X)+E(Y)$； 
	- 这一性质可以推广到任意有限个随机变量线性组合的情况：$E(\sum\limits_i^nc_i⋅X_i)=\sum\limits_i^nc_i⋅E(X_i)$；

!!! tip

	上述三条合并起来就是 $E(aX+bY+c)=aE(X)+bE(Y)+c$

- 设 $X,Y$ 是相互独立的随机变量，则 $E(X⋅Y)=E(X)⋅E(Y)$，但**逆命题不成立**；
	- 更一般地，对于任意有限个独立的随机变量，$E(\prod\limits_i^nX_i)=\prod\limits_i^nE(X_i)$

!!! note "证明"

	$$
	\begin{aligned}
	E(XY)&=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}xyf(x,y)dxdy=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}xyf_X(x)f_Y(y)dxdy\\
	&=\int_{-\infty}^{+\infty}xf_X(x)dx\int_{-\infty}^{+\infty}yf_Y(y)dy=E(X)E(Y)
	\end{aligned}
	$$
	
***
## 方差

设 $X$ 为随机变量，若 $E\{[X−E(X)]^2\}$ 存在，则称其为 $X$ 的**方差**，记作 $Var(X)$ 或 $D(X)$，即$Var(X)=E\{[X−E(X)]^2\}$

记 $\sigma(X)=\sqrt{Var(X)}$ 为 $X$ 的**标准差**或**均方差**。

- 数学期望存在是方差存在的必要但不充分存在。

方差刻画了 $X$ 取值的**分散程度**：

- 若 $X$ 取值集中，则 $Var(X)$ 较小；
- 若 $X$ 取值分散，则 $Var(X)$ 较大；

而其计算方法可以利用随机变量函数的数学期望，记 $g(X)=(X−E(X))^2$ ，然后计算 $E(g(X))$ 。具体的，有：

- 离散型：$Var(X)=E\{[X−E(X)]^2\}=\sum\limits_{i=1}^{+\infty}[x_i−E(X)]^2p_i$；
- 连续型：$Var(X)=E\{[X−E(X)]^2\}=\int_{−\infty}^{+\infty}[x−E(X)]^2f(x)dx$；
- 利用期望的性质，可以得到 $Var(X)=E(X^2)−E^2(X)$；
***
### 常见随机变量的方差

#### 均匀分布的方差

设随机变量X服从均匀分布 $U(a,b)(a<b)$，则：

$$
\begin{aligned}
&\because E(X)=\frac{a+b}{2}\\
&\therefore Var(X)=E(X^2)−E^2(X)=\int_{−\infty}^{+\infty}x^2f(x)dx−\frac{(a+b)^2}{4}=\int_{−\infty}^{+\infty}x^2\frac{1}{b−a}dx−\frac{(a+b)^2}{4}\\
&=\frac{1}{b−a}\int_{−\infty}^{+\infty}x^2dx−\frac{(a+b)^2}{4}=\frac{1}{b−a}⋅\frac{x^3}{3}|_a^b−\frac{(a+b)^2}{4}=\frac{(b−a)^2}{12}
\end{aligned}
$$

***
#### 0-1 分布的方差

设随机变量 $X$ 服从 0-1 分布 $B(1,p)(0<p<1)$，则：

$$
\begin{aligned}
&\because E(X)=p\\
&\therefore Var(X)=E(X^2)−E^2(X)=\sum\limits_{k=0}^1k^2⋅P\{X=k\}−p^2=p(1−p)
\end{aligned}
$$

***
#### 二项分布的方差

设随机变量 $X$ 服从二项分布 $B(n,p)(n\in\mathbb{N}^∗,0<p<1)$

引入随机变量 $X_i=\begin{cases}1,第i次试验成功\\0,第i次试验失败\end{cases}$，则 $X=\sum\limits_{i=1}^nX_i$，且 $X_i$ 相互独立，且 $X_i∼B(1,p)$，则：

$$
Var(X)=Var(\sum\limits_{i=1}^nX_i)=\sum\limits_{i=1}^nVar(X_i)=np(1−p)
$$

***
#### 泊松分布的方差

设随机变量 $X$ 服从泊松分布 $P(\lambda)(\lambda>0)$，则：

$$
\begin{aligned}
&\because E(X^2)=E(X(X−1)+X)=E(X(X−1))+E(X)=\sum\limits_{k=0}^{+\infty}k(k−1)\frac{\lambda^ke^{−\lambda}}{k!}+\lambda=\lambda^2+\lambda\\
&\therefore Var(X)=E(X^2)−E^2(X)=\lambda^2+\lambda−\lambda^2=\lambda
\end{aligned}
$$

***
#### 指数分布的方差

设随机变量 $X$ 服从指数分布 $E(\lambda)(\lambda>0)$，则：

$$
\begin{aligned}
&\because E(X^2)=\int_{-\infty}^{+\infty}x^2f(x)dx=\int_0^{+\infty}x^2\lambda e^{−\lambda x}dx=−x^2e^{−\lambda x}|_0^{+\infty}+\int_0^{+\infty}2xe^{−\lambda x}dx=\frac{2}{\lambda^2}\\
&\therefore Var(X)=E(X^2)−E^2(X)=\frac{2}{λ^2}−\frac{1}{λ^2}=\frac{1}{λ^2}
\end{aligned}
$$

***
#### 标准正态分布的方差

设随机变量 $X$ 服从标准正态分布 $N(0,1)$，因为 $E(X)=0$，所以：

$$
\begin{aligned}
Var(X)&=E(X^2)=\int_{−\infty}^{+\infty}x^2\varphi(x)dx=\int_{−\infty}^{+\infty}x^2\frac{1}{\sqrt{2\pi}}e^{−\frac{x^2}{2}}dx\\
&=\frac{1}{\sqrt{2\pi}}\int_{−\infty}^{+\infty}xd(−e^{−\frac{x^2}{2}})=\frac{1}{\sqrt{2\pi}}⋅(−xe^{−\frac{x^2}{2}})|_{−\infty}^{+\infty}+\frac{1}{\sqrt{2\pi}}\int_{−\infty}^{+\infty}e^{−\frac{x^2}{2}}dx\\
&=\frac{1}{\sqrt{2\pi}}\int_{−\infty}^{+\infty}e^{−\frac{x^2}{2}}dx=\frac{1}{\sqrt{2\pi}}⋅2\pi=1
\end{aligned}
$$

***
#### 正态分布的方差

设随机变量 $X$ 服从正态分布 $N(\mu,\sigma^2)(\sigma>0)$，则：

$$
\begin{gather}
Z=\frac{X−\mu}{\sigma}∼N(0,1)\\
Var(X)=Var(\sigma Z+\mu)=\sigma^2Var(Z)=\sigma^2
\end{gather}
$$

***
### 方差的性质

- 若 $C$ 是常数，则 $Var(C)=0$ ；
- 设 $X$ 是随机变量， $C$ 是常数，则 $Var(C⋅X)=C^2⋅Var(X)$；
- 设 $X,Y$ 是两个随机变量，则 $Var(X\pm Y)=Var(X)+Var(Y)\pm 2E\{[X−E(X)][Y−E(Y)]\}=Var(X)+Var(Y)\pm 2Cov(X,Y)$
	- $Cov(X,Y)$ 为协方差，后面会讲到
	- 更一般地，$Var(\sum\limits_{i=1}^nX_i)=\sum\limits_{i=1}^nVar(X_i)+2\sum\limits_{1\leq i<j\leq n}Cov(X_i,X_j)$
		- 特别地，如果 $X,Y$ 相互独立，则 $Var(X±Y)=Var(X)+Var(Y)$；进一步地，如果$X_i(i=1,2,...,n)$ 彼此独立，则 $Var(c_1X_1±c_2X_2±...±c_nX_n)=c_1^2Var(X_1)+c_2^2Var(X_2)+...+c_n^2Var(X_n)$

!!! tip

	综合上述三条，若 $X,Y$ 独立，则有 $Var(aX+bY+c)=a^2Var(X)+b^2Var(Y)$；


- $Var(X)\leq E((X−c)^2)$，并且当且仅当 $E(X)=c$ 时等号成立；
- $Var(X)=0\Leftrightarrow P(X=c)=1\text{ and }c=E(X)$；
***
## 标准化变量

设随机变量 $X$ 的数学期望 $E(X)=\mu$，方差 $Var(X)=\sigma^2\not=0$

中心化：使随机变量 $X$ 的数学期望为0，则称随机变量 $X−\mu$ 为 $X$ 的**中心化变量**。

标准化：使随机变量 $X$ 的数学期望为0，方差为1，则称随机变量 $\frac{X−\mu}{\sigma}$ 为 $X$ 的**标准化变量**。

- 标准化变量的数学期望为 $E(X^∗)=0$，方差为 $Var(X^∗)=1$。
***
### 变异系数

**变异系数**(Coefficient of Variation)又叫“**标准差率**”，是衡量资料中各观测值变异程度的一个数字特征。它可以消除单位或平均数不同对两个或多个资料变异程度比较的影响。

设随机变量 $X$ 具有数学期望 $E(X)=\mu$，方差 $Var(X)=\sigma^2\not=0$，则称 $C_v=\frac{\sigma}{\mu}$ 为 $X$ 的变异系数。
***
## 协方差与相关系数

定义：$E\{[X-E(X)][Y-E(Y)]\}$ 称为随机变量 $X$ 与 $Y$ 的协方差，记为 $Cov(X,Y)$，即 $Cov(X,Y)=E\{[X-E(X)][Y-E(Y)]\}$，称 $\rho_{XY}=\frac{Cov(X,Y)}{\sqrt{D(X)D(Y)}}$ 为随机变量 $X$ 和 $Y$ 的相关系数，$\rho_{XY}$ 是一个无量纲的量。

- 协方差其实就是把 $X$ 和 $Y$ 都中心化后的期望成绩
***
### 协方差的性质

协方差具有线性性：

- $Cov(X,X)=Var(X)$；
- $Cov(X,Y)=Cov(Y,X)$；
- $Cov(aX,bY)=abCov(X,Y),a,b\in\mathbb{R}$；
- $Cov(X+Y,Z)=Cov(X,Z)+Cov(Y,Z)$；

- $Cov(X,Y)=E(XY)−E(X)E(Y)$；
- $Cov(aX+bY,cX+dY)=acVar(X)+bdVar(Y)+(ad+bc)Cov(X,Y)$；
- $Cov(c,Y)=E(cY)−E(c)E(Y)=0,c\in\mathbb{R}$；
- $Cov(X+Y,X−Y)=Cov(X,X)−Cov(Y,Y)=Var(X)−Var(Y)$；
- $D(aX+bY)=a^2Var(X)+b^2Var(Y)+2abCov(X,Y)$；
***
### 相关系数的性质

- $|\rho_{XY}|\leq 1$；

!!! note "证明"

	我们有：
	
	$$
	\begin{aligned}
	D(\frac{X-E(X)}{\sqrt{D(X)}}\pm\frac{Y-E(Y)}{\sqrt{D(Y)}})&=D(\frac{X-E(X)}{\sqrt{D(X)}})+D(\frac{Y-E(Y)}{\sqrt{D(Y)}})\pm2Cov(\frac{X-E(X)}{\sqrt{D(X)}},\frac{Y-E(Y)}{\sqrt{D(Y)}})\\
	&=2(1\pm\rho_{XY})\geq 0
	\end{aligned}
	$$
	

- $|\rho_{XY}|=1\Leftrightarrow\exists a,b\in\mathbb{R}$，使得 $P(Y=a+bX)=1$；
    - $\rho_{XY}=+1$ 时，$b>0$；
    - $\rho_{XY}=−1$ 时，$b<0$；

上述两条性质可以合并写成：

当 $Var(X)Var(Y)\not=0$ 时，有 $Cov(X,Y)^2\leq Var(X)Var(Y)$，其中等号当且仅当 $X,Y$ 之间有严格的线性关系，即存在常数 $a,b$，使 $P(Y=a+bx)=1$；

相关系数 $\rho_{XY}$ 是用来表征 $X,Y$ 之间**线性关系紧密程度**的量。此外，考虑以 $X$ 的线性函数 $a+bX$ 来近似表示 $Y$，**均方误差** $e(a,b)=E\{[Y−(a+bX)]^2\}$ 也可以用来衡量 $X,Y$ 之间线性关系紧密程度。

!!! note "最佳近似值"

	由两个偏导数为 0 可得最佳近似值：
	
	$$
	a_0=E(Y)−b_0E(X),b_0=Cov(X,Y)Var(X)
	$$
	
	于是有：
	
	$$
	e(a_0,b_0)=Var(Y)-\frac{[Cov(X,Y)]^2}{Var(X)}=Var(Y)[1-\rho_{XY}^2]
	$$
	

- $|\rho_{XY}|$ 比较大时，误差较小，表示 $X,Y$ 线性关系的程度好；
- $|\rho_{XY}|=1$ 时，误差为 0，表示 $X,Y$ 之间以概率 1 存在线性关系；
- $|\rho_{XY}|$比较小时，误差较大，表明 $X,Y$ 线性关系的程度差；
- $\rho_{XY}>0$ 时，$X,Y$ 正相关；
- $\rho_{XY}<0$ 时，$X,Y$ 负相关；
- $\rho_{XY}=0$ 时，称 $X,Y$ **不相关**或**零相关**（仅仅对于线性关系来说，与**独立**的含义不同）；

!!! note ""

	  $\rho_{XY}=0$ 时:
	  
	  - $Cov(X,Y)=0$；
	  - $E(XY)=E(X)E(Y)$；
	  - $Var(X\pm Y)=Var(X)+Var(Y)$；
	  
	  于是有结论：
	  
	  - $X,Y$ 互相独立 $\Rightarrow$ $X,Y$ 不相关
	  - $X,Y$ 相关 $\Rightarrow$ $X,Y$ 不独立
	
	<font color="red">反之不一定成立</font>

***
## 二维正态分布

### 参数含义

参数 $\mu_1,\mu_2$ 分别表示 $X,Y$ 的数学期望，$σ_1^2,σ_2^2$ 分别表示 $X,Y$ 的方差，$\rho$ 表示 $X,Y$ 的相关系数。

当 $\rho=0$ 时，称 $X,Y$ 不相关，而此时可推出 $X,Y$ 独立。因此对于二维正态分布，$X,Y$ 独立与不相关是等价的。
***
### 二元正态变量性质

- 二元随机变量 $X,Y$ 服从二元正态分布 $\Leftrightarrow X,Y$ 的任意线性组合 $aX+bY$ 服从一元正态分布，其中 $a,b$ 均为不为 0 的参数，且 $aX+bY~N(E(aX+bY),D(aX+bY))$
- 正态变量的线性变换不变性：若 $X,Y$ 服从二元正态分布，设 $Z_1,Z_2$ 是 $X,Y$ 的线性函数，则 $Z_1,Z_2$ 也服从二元正态分布
***
## 其他数字特征

### 矩

设 $X, Y$ 是随机变量，$k, l$ 是正整数，若以下期望存在，则称它们为 $X, Y$ 的 $k$ 阶原点矩和 $k$ 阶中心矩：

- $X$ 的 $k$ 阶原点矩：$E(X^k)$；
    - 1 阶原点矩为数学期望；
- $X$ 的 $k$ 阶中心矩：$E\{[X-E(X)]^k\}$；
    - 1 阶中心矩为 0；
    - 2 阶中心矩为方差；
- $X, Y$ 的 $k+l$ 阶混合（原点）矩：$E(X^kY^l)$；
- X, Y 的 $k+l$ 阶混合中心矩：$E\{[X-E(X)]^k[Y-E(Y)]^l\}$；
***
### 分位数

$X$ 为连续型随机变量， 其分布函数和概率密度函数分别为 $F(x)$ 和 $f(x)$ 称满足条件 $P\{X>x_{\alpha}\}=1-F(x_{\alpha})=\int_{x_{\alpha}}^{+\infty}f(x)\mathrm dx=\alpha,\alpha\in(0,1)$ 的 $x_{\alpha}$ 为 $X$ 的 $\alpha$ 分位数

- $x_{1/2}$ 称为 $X$ 的中位数；
- $x_{1/4}$ 称为 $X$ 的上 $\frac{1}{4}$ 分位数；
- $x_{3/4}$ 称为 $X$ 的上 $\frac{3}{4}$ 分位数；
***
## 多元随机变量的数字特征

设 $n$ 元随机变量 $X=(X_1,X_2,...,X_n)^T$，若每一个分量的数学期望都存在，则称$E(X)=(E(X_1),E(X_2),...,E(X_n))^T$ 为 **$n$ 元随机变量** $X$ **的数学期望（向量）**。

设 $n$ 维随机变量 $\vec{X}=(X_1,X_2,...,X_n)^T$，$Cov(X_i,X_j)(i,j=1,2,...,n)$ 都存在，则：

$$
\begin{bmatrix}
Var(X_1) & Cov(X_1,X_2) & ... & Cov(X_1,X_n)\\
Cov(X_2,X_1) & Var(X_2) & ... & Cov(X_2,X_n)\\
... & ... & ... & ... \\
Cov(X_n,X_1) & Cov(X_n,X_2) & ... & Var(X_n)
\end{bmatrix}
$$

称之为 $\vec{X}$ 的**协方差矩阵**。它是一个**对称**的**非负定矩阵**。
***
### n 维正态变量重要性质

- $n$ 维正态变量 $(X_1,X_2,...,X_n)^T$ 中的任意子向量 $(X_{i_1},X_{i_2},...,X_{i_k})^T$，$1\leq k\leq n$ 也服从 $k$ 元正态分布；
    - 特别地，每一个分量 $X_i,i=1,2,...,n$ 都是正态变量；
    
    !!! note ""
    
		联合正态可以推出边际正态，但边际正态不一定能推出联合正态。  
		
		如函数 $f(x,y)=\frac{1}{2\pi}e^{-\frac{1}{2}(x^2+y^2)}(1+\sin x\sin y)$，边际分布都是标准正态分布，但是联合分布不是正态分布。  
		
		我们需要加条件。
    
    - 反之，若每个 $X_i$ 都是正态变量，且相互独立，则 $(X_1,X_2,...,X_n)$ 是 $n$ 维正态 
- n 维随机变量 $(X_1,X_2,...,X_n)$ 服从 $n$ 维正态分布的**充要条件**是 $X_1,X_2,...,X_n$ 的任意线性组合 $\sum_{i}^{n} l_iX_i$ 服从一维正态分布，其中 $l_1,l_2,...,l_n$ 不全为 $0$；
- 若 $(X_1,X_2,...,X_n)$ 服从 $n$ 维正态分布，设 $Y_1,Y_2,...,Y_k$ 是 $X_i$ 的线型函数，则 $(Y_1,Y_2,...,Y_k)$ 也服从多维正态分布，这一性质被称为正态变量的线性变换不变性；
- 若 $(X_1,X_2,...,X_n)$ 服从 $n$ 维正态分布，则 $X_1,X_2,...,X_n$ 互相独立的**充要条件**是 $X_i$ 两两不相关，也等价于协方差矩阵为对角矩阵；
***
## 总结

![](../../../assets/Pasted%20image%2020241114101630.png)

