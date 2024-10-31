---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  
# Chapter 03 : 多元随机变量及其分布

## 二元离散型随机变量

### 联合分布律

设 $(X,Y)$ 所有可能取值为 $(x_i,y_j),P(X=x_i,Y=y_j)=p_{ij},i,j=1,2,…$ 为二元离散型随机变量 $(X,Y)$ 的联合分布律（Joint Mass Function），可以用如下表格表示：

![](../../../assets/Pasted%20image%2020241017112253.png)
***
### 边际分布律

对于离散型随机变量 $(X,Y)$，分布律为 $P(X=x_i,Y=y_j)=p_{ij},i,j=1,2,...$

$X,Y$ 的边际（边缘）分布律（Marginal Mass Function）为：

- $P(X=x_i)=P(X=x_i,Y<+\infty)=\sum\limits_{j=1}^\infty p_{ij}$，记为 $p_{·i},i=1,2,...$；
-  $P(Y=y_j)=P(X<+\infty,Y=y_j)=\sum\limits_{i=1}^\infty p_{ij}$，记为 $p_{·j},j=1,2,...$；

边际分布律本质是联合分布律的行/列求和。
***
### 条件分布律

对于两个事件 $A,B$，若 $P(A)>0$，可以考虑条件概率 $P(B|A)$，对于二元离散型随机变量 $(X,Y)$，设其分布律为 $P(X=x_i,Y=y_j)=p_{ij},i,j=1,2,...$

若 $P(Y=y_j)=p_{·j}>0$，条件概率 $P(X=x_i|Y=y_j)=\frac{P(X=x_i​,Y=y_j​)}{​P(Y=y_j​)}=\frac{p_{ij}}{p_{⋅j}},​​​i,j=1,2,...$

$P(X<x∣Y<y)=\frac{P(X<x,Y<y)}{P(Y<y)}​$，然后根据联合分布律和边际分布律读表计算；
***
## 二元随机变量的分布函数

### 分布函数

定义：设 $(X,Y)$ 是二元随机变量，对于任意实数 $x,y$，二元函数 $F(x,y)=P\{(X\leq x)\bigcap (Y\leq y)\}$ ，记为 $P(X\leq x,Y\leq y)$ ，称为二元随机变量 $(X,Y)$ 的分布函数。

分布函数 $F(x,y)$ 具有如下性质：

- **固定**其中一个变量，则该二元函数关于另外一个变量单调**不减**；
- $0\leq F(x,y)\leq 1$，且 $F(x,−\infty)=F(−\infty,y)=F(−\infty,−\infty)=0,F(+\infty,+\infty)=1$；
- $F(x,y)$ 关于 $x$ 和 $y$ **分别**右连续（离散），即 $\lim\limits_{\epsilon\rightarrow 0^+}F(x+\epsilon,y)=F(x,y),\lim\limits_{\epsilon\rightarrow 0^+}F(x,y+\epsilon)=F(x,y)$； 
- $x_1<x_2,y_1<y_2​$ 时，有： $P\{x_1<X\leq x_2,y_1<Y\leq y_2\}=F(x_2,y_2)−F(x_1,y_2)−F(x_2,y_1)+F(x_1,y_1)\geq 0$
***
### 边际（边缘）分布函数

二元随机变量 $(X,Y)$ 作为整体，有分布函数 $F(x,y)$，其中 $X$ 和 $Y$ 都是随机变量，它们的分布函数，记为 $F_X(x),F_Y(y)$ 称为边际分布函数。

由定义我们容易得：$F_X(x)=P(X\leq x)=P(X\leq x,Y\leq +\infty)=F(x,+\infty),F_Y(y)=P(Y\leq y)=P(X\leq +\infty,Y\leq y)=F(+\infty,y)$
***
### 条件分布函数

若 $P(Y=y)>0$，则在 $Y=y$ 条件下，$X$ 的条件分布函数为：$F_{X|Y}(x|y)=P(X\leq x|Y=y)=\frac{P(X\leq x,Y=y)}{Y=y}$，若 $P(Y=y)=0$，但对任给 $\epsilon>0,P(y<Y<y+\epsilon)>0$，则在 $Y=y$ 条件下，$X$ 的条件分布函数为：$F_{X|Y}(x|y)=\lim\limits_{\epsilon\rightarrow 0^+}P(X\leq x|y<Y\leq y+\epsilon)$
***
## 二元连续型随机变量

### 联合概率密度

对于二元随机变量 $(X,Y)$ 的联合分布函数为 $F(x,y)$，若存在二元函数 $f(x,y)\geq 0$，则对于任意的实数 $x,y$ 有 $F(x,y)=\int_{−\infty}^x\int_{−\infty}^yf(u,v)dudv$，则称 $(X,Y)$ 为**二维连续型随机变量（Bivariate Continuous Random Variable）**，称 $f(x,y)$ 为 $(X,Y)$ 的联合概率密度。其具有以下性质：

- $f(x,y)\geq 0$；
- $F(+\infty,+\infty)=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}f(u,v)dudv=1$；
- 在 $f(x,y)$ 的连续点 $(x,y)$ 上有 $\frac{\partial^2F(x,y)}{\partial x\partial y}=f(x,y)$；
- $(X,Y)$ 落入 $xOy$ 平面任意区域 $D$ 的概率为：$P\{(X,Y)\in D\}=\iint\limits_D f(x,y)dxdy$；
- 由于其几何意义为落在以 $D$ 为底，以曲面 $z=f(x,y)$ 为顶面的柱体体积，所以当 $D$ 面积为 $0$ 时概率为 $0$；
- `eg`：$P(X=1,Y=1)=0,P(X+Y=1)=0,P(X^2+Y^2=1)\not=0$；
***
### 边际（边缘）概率密度

对于连续型随机变量 $(X,Y)$，概率密度为 $f(x,y)$，$X,Y$ 的边际概率密度为 $f_X(x)=\int_{-\infty}^{+\infty}f(x,y)dy,f_Y(y)=\int_{-\infty}^{+\infty}f(x,y)dx$
***
### 条件概率密度

设二元随机变量 $(X,Y)$ 的概率密度为 $f(x,y)$，$(X,Y)$ 关于 $Y$ 的边际概率密度为 $f_Y(y)$，若对于固定的 $y,f_Y(y)>0$，且 $f_Y(y)$ 连续，则 $\frac{f(x,y)}{f_Y(y)}$ 为在 $Y=y$ 的条件下，$X$ 的条件概率密度记为 $f_{X|Y}(x|y)=\frac{f(x,y)}{f_Y(y)}$，对 $Y$ 同理。

事实上，$F_{X|Y}(x|y)=\lim\limits_{\Delta y\rightarrow 0^+}\frac{P(X\leq x,y<Y\leq y+\Delta y)}{P(y<Y\leq y+\Delta y)}=\lim\limits_{\Delta y\rightarrow 0^+}\frac{\frac{1}{\Delta y}\int_{-\infty}^xds\int_y^{y+\Delta y}f(s,t)dt}{\frac{1}{\Delta y}\int_y^{y+\Delta y}f_Y(t)dt}=\frac{\int_{-\infty}^xf(s,y)ds}{f_Y(y)}=\int_{-\infty}^x\frac{f(s,y)}{f_Y(y)}ds$

也就是，由 $f_{X|Y}(x|y)=\frac{\partial}{\partial x}F_{X|Y}(x|y)\Rightarrow f_{X|Y}(x|y)=\frac{f(x,y)}{f_Y(y)}$，证明如下：

$$
\begin{aligned}
f_{X|Y}(x|y)&=\frac{\partial}{\partial x}F_{X|Y}(x|y)=\frac{\partial}{\partial x}\lim\limits_{\Delta y\rightarrow 0^+}\frac{P(X\leq x,y<Y\leq y+\Delta y)}{P(y<Y\leq y+\Delta y)}\\
&=\frac{\partial}{\partial x}\lim\limits_{\Delta y\rightarrow 0^+}\frac{F(x,y+\Delta y)-F(x,y)}{F_Y(y+\Delta y)-F_Y(y)}=\frac{\partial}{\partial x}\frac{\lim\limits_{\Delta y\rightarrow 0^+}\frac{F(x,y+\Delta y)-F(x,y)}{\Delta y}}{\lim\limits_{\Delta y\rightarrow 0^+}\frac{F_Y(y+\Delta y)-F_Y(y)}{\Delta y}}\\
&=\frac{\partial}{\partial x}\frac{\frac{\partial F(x,y)}{\partial y}}{\frac{dF_Y(y)}{dy}}=\frac{\frac{\partial^2F(x,y)}{\partial x\partial y}}{f_Y(y)}=\frac{f(x,y)}{f_Y(y)}
\end{aligned}
$$
***
### 二元均匀分布与二元正态分布

#### 二元均匀分布

若二元随机变量 $(X,Y)$ 在二维有界区域 $D$ 上取值，且具有概率密度 $f(x,y)=\begin{cases}\frac{1}{D的面积},(x,y)\in D\\0,其他\end{cases}$，则称 $(X,Y)$ 服从 $D$ 上的均匀分布。

若 $D_1$ 是 $D$ 的子集，则 $P\{(X,Y)\in D_1\}=\iint\limits_{D_1}f(x,y)dxdy$，即 $P\{(X,Y)\in D_1\}=\frac{D_1的面积}{D的面积}$
***
#### 二元正态分布

设二元随机变量 $(X,Y)$ 的概率密度为：

$$
\begin{aligned}
f(x,y)=\frac{1}{2\pi\sigma_1\sigma_2\sqrt{1-\rho^2}}\times\exp\{\frac{-1}{2(1-\rho^2)}[\frac{(x-\mu_1)^2}{\sigma_1^2}-2\rho\frac{(x-\mu_1)(y-\mu_2)}{\sigma_1\sigma_2}+\frac{(y-\mu_2)^2}{\sigma_2^2}]\}\\
(-\infty<x<+\infty,-\infty<y<+\infty)
\end{aligned}
$$

其中 $\mu_1,\mu_2,\sigma_1,\sigma_2,\rho$ 都是常数，且 $\sigma_1>0,\sigma_2>0,-1<\rho<1$，称 $X,Y$ 为服从参数为 $\mu_1,\mu_2,\sigma_1,\sigma_2,\rho$ 的二元正态分布，记为 $(X,Y)∼N(\mu_1,\mu_2,\sigma_1^2,\sigma_2^2,\rho)$

$$
\begin{aligned}
f_X(x)&=\int_{-\infty}^{+\infty}f(x,y)dy\\
&=\int_{-\infty}^{+\infty}\frac{1}{2\pi\sigma_1\sigma_2\sqrt{1-\rho^2}}\times\exp\{\frac{-1}{2(1-\rho^2)}[\frac{(x-\mu_1)^2}{\sigma_1^2}-2\rho\frac{(x-\mu_1)(y-\mu_2)}{\sigma_1\sigma_2}+\frac{(y-\mu_2)^2}{\sigma_2^2}]\}dy\\
&=\int_{-\infty}^{+\infty}\frac{1}{2\pi\sigma_1\sigma_2\sqrt{1-\rho^2}}e^{-\frac{(x-\mu_1)^2}{2\sigma_1^2}}e^{-\frac{1}{2(1-\rho^2)}[\frac{y-\mu_2}{\sigma_2}-\rho\frac{x-\mu_1}{\sigma_1}]^2}dy\\
&=\frac{1}{\sqrt{2\pi}\sigma_1}e^{-\frac{(x-\mu_1)^2}{2\sigma_1^2}}\int_{-\infty}^{+\infty}\frac{1}{\sqrt{2\pi}\sigma_2\sqrt{1-\rho^2}}e^{-\frac{1}{2\sigma_2^2(1-\rho^2)}\{y-[\mu_2+\rho\frac{\sigma_2}{\sigma_1}(x-\mu_1)]\}^2}dy\\
&=\frac{1}{\sqrt{2\pi}\sigma_1}e^{-\frac{(x-\mu_1)^2}{2\sigma_1^2}},-\infty<x<+\infty
\end{aligned}
$$

那么我们就可以得到 $X∼N(\mu_1,\sigma_1^2)$，同理也可以得到 $Y∼N(\mu_2,\sigma_2^2$)，即二维正态分布的两个边际分布都是**对应参数的一维正态分布**，与 $\rho$ 无关。

$$
\begin{aligned}
f_{Y∣X}​(y∣x)=\frac{f(x,y)}{f_X(x)}=\frac{1}{\sqrt{2\pi}\sqrt{1-\rho^2}\sigma_2}\exp\{-\frac{1}{2(1-\rho^2)\sigma_2^2}[y-(\mu_2+\rho\frac{\sigma_2}{\sigma_1}(x-\mu_1))]^2\}\\​
f_{X∣Y}​(x∣y)=\frac{f(x,y)}{f_Y(y)}=\frac{1}{\sqrt{2\pi}\sqrt{1-\rho^2}\sigma_1}\exp\{-\frac{1}{2(1-\rho^2)\sigma_1^2}[x-(\mu_1+\rho\frac{\sigma_1}{\sigma_2}(y-\mu_2))]^2\}
\end{aligned}
$$

***
### 随机变量的独立性

如果对于任意的两个实数集合 $D_1,D_2​$，有 $P\{X\in D_1,Y\in D_2\}=P\{X\in D_1\}·P\{Y\in D_2\}$，则称随机变量 $X,Y$ **相互独立**，即 $X,Y$ **独立**。  

也可以说，当 $P\{X\leq x,Y\leq y\}=P\{X\leq x\}⋅P\{Y\leq y\}$，即 $F(x,y)=F_X(x)⋅F_Y(y)$ 时，$X,Y$ 独立。

- 若 $(X,Y)$ 是离散型随机变量，则 $X,Y$ 相互独立等价于 $p_{ij}=p_i⋅p_{⋅j}$对一切 $i,j$ 都成立
- 若 $(X,Y)$ 是连续型随机变量，则 $X,Y$ 相互独立等价于 $f(x,y)=f_X(x)f_Y(y)$ 总是成立，平面上“面积”为零的集合除外（可以在不连续点上不相等）
- 对于二维正态随机变量 $(X,Y)$，$X$ 与 $Y$ 相互独立的充要条件是参数 $\rho=0$。

n 维随机变量独立性相关定理：

- 设 $(X_1,X_2,⋯,X_m)$ 与 $(Y_1,Y_2,⋯,Y_n$) 相互独立，则 $X_i(i=1,2,⋯,m)$ 与 $Y_j(j=1,2,⋯,n)$ 相互独立
- 设 $(X_1,X_2,⋯,X_m)$ 与 $(Y_1,Y_2,⋯,Y_n)$ 相互独立，若 $h(x_1,x_2,⋯,x_m)$ 与 $g(y_1,y_2,⋯,y_n)$ 是连续函数，则 $h(X_1,X_2,⋯,X_m)$ 与 $g(Y_1,Y_2,⋯,Y_n)$ 相互独立
***
## 多元随机变量函数的分布

### 卷积公式

这里讨论连续型，离散型只需把积分符号换成求和符号即可，当 $X$ 和 $Y$ 相互独立时，$Z=X+Y$ 的条件下：

$$
\begin{aligned}
F_Z(z)&=\iint\limits_{x+y\leq z}f(x,y)dxdy=\int_{-\infty}^{+\infty}[\int_{-\infty}^{z-x}f(x,y)dy]dx,u=x+y\\
&=\int_{-\infty}^{+\infty}[\int_{-\infty}^{z}f(x,u-x)du]dx\\
&=\int_{-\infty}^{z}[\int_{-\infty}^{+\infty}f(x,u-x)dx]du\\
&=\int_{-\infty}^{z}f_Z(u)dy
\end{aligned}
$$

其密度函数公式：

- $f_Z​(z)=\int_{-\infty}^{+\infty}f(z−y,y)dy=\int_{-\infty}^{+\infty}f(x,z−x)dx$（$x,y$ 是对称的）
- 当 $X$ 和 $Y$ 相互独立时，$Z$ 的密度函数公式也称为**卷积公式**：$f_X∗f_Y=\int_{-\infty}^{+\infty}f_X(z−y)f_Y(y)dy=\int_{-\infty}^{+\infty}f_X(x)f_Y(z−x)dx$
***
### 常见分布的卷积

分布的卷积问题，也即是分布的可加性问题。

!!! note "常见分布的卷积"

	=== "二项分布"
	
		设 $X∼B(n,p),Y∼B(m,p)$，$0<p<1$，$m,n$ 均为正整数，若 $X$ 与 $Y$ 独立，则
		 $X+Y∼B(m+n,p)$
	
	=== "泊松分布"
	
		 设 $X∼P(\lambda_1),Y∼P(\lambda_2)$，$\lambda_i>0,i=1,2$，若 $X$ 与 $Y$ 独立，则 $X+Y∼P(\lambda_1+\lambda_2)$
	
	=== "正态分布"
	
		设 $X∼N(\mu_1,\sigma_1^2),Y∼N(\mu_2,\sigma_2^2),−\infty<\mu_i<+\infty,\sigma_i>0,i=1,2$，若 $X$ 与 $Y$ 独立，则 $aX+bY+c∼N(a\mu_1+b\mu_2+c,a^2\sigma_1^2+b^2\sigma_2^2)$
	
	=== "均匀分布"
	
		设 $X∼U(a_1,b_1)$，$Y∼U(a_2,b_2)$，若 $X$ 与 $Y$ 独立，则 $X+Y∼U([a_1,a_2]×[b_1,b_2])$

### $M=\max(X, Y), N=\min(X, Y)$ 的分布

设 $X,Y$ 是两个<font color="red">相互独立</font>的随机变量，他们的分布函数分别为 $F_X(x)$ 和 $F_Y(y)$ ，现在来求 $M,N$ 的分布函数 $F_{\text{max}}(z)$ 和 $F_{\text{min}}(z)$ 的值。

$$
\begin{gather}
F_{\max}(z)=P(M\leq z)=P(X\leq z,Y\leq z)=P(X\leq z)P(Y\leq z)\\
F_{\min}(z)=P(N\leq z)=1-P(N>z)=1-P(X>z,Y>z)=1-P(X>z)P(Y>z)
\end{gather}
$$

即 $F_{\max}(z)=F_X(z)F_Y(z),F_{\min}(z)=1-(1-F_X(z))(1-F_Y(z))$

一般地，推广到 $n$ 个相互独立的随机变量的情况，设 $X_1,X_2,...,X_n$ 是 $n$ 个<font color="red">相互独立</font>的随机变量，他们的分布函数分别为 $F_{X_i}(x_i),i=1,2,...,n$ ，则 $M=\max\limits_{1\leq i\leq n}X_i$ 和 $N=\min\limits_{1\leq i\leq n}X_i$ 的分布函数 $F_{\max}(z)$ 和 $F_{\min}(z)$ 为：

$$
\begin{gather}
F_{\max}(z)=F_{X_1}(z)F_{X_2}(z)...F_{X_n}(z)\\
F_{\min}(z)=1-[1-F_{X_1}(z)][1-F_{X_2}(z)]...[1-F_{X_n}(z)]
\end{gather}
$$



