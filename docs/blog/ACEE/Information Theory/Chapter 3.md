---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 3 : 连续随机变量的互信息和微分熵

> 之前讲的主要在离散随机变量，这一章主要介绍的是连续随机变量

## 连续随机变量的概率密度

- $p_{XY}(x,y)$ 是连续随机变量 $XY$ 的联合概率密度函数
- $p_X(x)$ 是 $X$ 的边际概率密度
- $p_Y(y)$ 是 $Y$ 的边际概率密度

则：

$$
\begin{aligned}
p_X(x)&=\int_{-\infty}^{+\infty}p_{XY}(x,y)dy\\
p_Y(y)&=\int_{-\infty}^{+\infty}p_{XY}(x,y)dx\\
p_{Y|X}(y|x)&=\frac{p_{XY}(x,y)}{p_X(x)}
\end{aligned}
$$
***
## 连续随机变量的离散化

![](../../../assets/Pasted%20image%2020250322153124.png)
***
## 连续随机变量的互信息

联合连续随机变量 $((X,Y),R^2,p_{XY}(x,y))$ 之间的互信息：

$$
\begin{aligned}
I(X;Y)&=\sum\limits_{i=-\infty}^{+\infty}\sum\limits_{j=-\infty}^{+\infty}[p_{XY}(x_i,y_j)\Delta x_i\Delta y_j]\log\frac{[p_{XY}(x_i,y_j)\Delta x_i\Delta y_j]}{[p_X(x_i)\Delta x_i][p_Y(y_j)\Delta y_j]}\\
&=\sum\limits_{i=-\infty}^{+\infty}\sum\limits_{j=-\infty}^{+\infty}(p_{XY}(x_i,y_j)\log\frac{p_{XY}(x_i,y_j)}{p_X(x_i)p_Y(y_j)})\Delta x_i\Delta y_j\\
&\stackrel{\Delta x_i\rightarrow 0,\Delta y_j\rightarrow 0}{\rightarrow} \iint p_{XY}(x,y)\log\frac{p_{XY}(x,y)}{p_X(x)p_Y(y)}dxdy\\
I(X;Y|Z)&=\iiint p_{XYZ}(x,y,z)\log\frac{p_{XY|Z}(x,y|z)}{p_{X|Z}(x|z)p_{Y|Z}(y|z)}dxdydz\\
I(X;YZ)&=\iiint p_{XYZ}(x,y,z)\log\frac{p_{XYZ}(x,y,z)}{p_{X}(x)p_{YZ}(yz)}dxdydz
\end{aligned}
$$

性质：

- $I(X;Y)\geq 0$
- $I(X;Y)=I(Y;X),I(X;Y|Z)=I(Y;X|Z)$
- $I(X;YZ)=I(X;Y)+I(X;Z|Y)=I(X;Z)+I(X;Y|Z)$
- 如果 $X\rightarrow Y\rightarrow Z$，那么 $I(X;Y)\geq I(X;Z)$，$I(X;Y)\geq I(X;Y|Z)$
***
## 连续随机变量的微分熵

连续随机变量 $(X,R,p_X(x))$ 的离散化熵值：

$$
\begin{aligned}
H_{\Delta}(X)&=-\sum\limits_{i=-\infty}^{+\infty}p_X(x_i)\Delta x_i\log(p_X(x_i)\Delta x_i)\\
&=-\sum\limits_{i=-\infty}^{+\infty}[p_X(x_i)\log p_X(x_i)]\Delta x_i-\sum\limits_{i=-\infty}^{+\infty}p_X(x_i)\Delta(X_i)\log\Delta x_i\\
&\stackrel{\Delta x_i\rightarrow 0}{\rightarrow}-\int p_X(x)\log p_X(x)dx+\infty
\end{aligned}
$$

直接采用离散化进行推广会出现问题，所以我们简单地略去无穷大项，我们定义连续随机变量 $X$ 的微分熵为：

$$
H_C(X)=h(X)\stackrel{\Delta}{=}-\int p_X(x)\log p_X(x)dx
$$
***
### 微分熵的本质和性质

1. 微分熵 $H_C(X)$ 不反应连续随机变量 $X$ 的不确定性，连续随机变量的不确定性一般都是无穷大。单微分熵的确在一定程度上反映了该连续随机变量的相对不确定性
2. $H_C(X)$ 可正，可负，可为 0
***
### 条件微分熵和联合微分熵及其性质

- $H_C(X,Y)=-\iint p_{XY}(x,y)\log p_{XY}(x,y)dxdy$
- $H_C(X|Y)=-\iint p_{XY}(x,y)\log p_{X|Y}(x|y)dxdy$
- $H_C(X,Y)=H_C(X)+H_C(Y|X)=H_C(Y)+H_C(X|Y)$
- $H_C(U^N)=H_C(U_1,U_2,...,U_N)=\sum\limits_{i=1}^{N}H_C(U_i|U_1,U_2,...,U_{i-1})=\sum\limits_{i=1}^{N}H_C(U_i|U^{i-1})$
- $I(X,Y)=H_C(X)-H_C(X|Y)=H_C(Y)-H_C(Y|X)=H_C(X)+H_C(Y)-H_C(X,Y)$
***
### 微分熵的线性变性

对于离散随机变量 $X$，令 $Y=f(X)$ 是 $X\rightarrow Y$ 上的一对一函数，则 $H(X)=H(Y)$

但对于连续随机变量：$H_C(Y)=-\int p(y)\log p(y)dy=-\int p(x)\log p(x)f'(x)dx\neq H_C(X)$

即使对于线性变换，微分熵也不具有不变性
***
### 微分熵的极大化

#### 峰值受限

定理：设 $X$ 取值限于 $(-M,M)$，即 $\int_{-M}^Mp(x)dx=1$，这时微分熵 $H_C(X)\leq\ln 2M$，等号在均匀分布时达到

??? note "Proof"

	使用 Lagrange 乘子法：
	
	$$
	\begin{aligned}
	J(p(x))&\stackrel{\Delta}{=}H_C(X)-\lambda\int_{-M}^Mp(x)dx\\
	&=-\int_{-M}^Mp(x)\ln p(x)dx-\lambda\int_{-M}^Mp(x)dx\\
	&=-\int_{-M}^Mp(x)\ln (e^{\lambda}p(x))dx\\
	&\leq-\int_{-M}^Mp(x)(\frac{1}{e^{\lambda}p(x)}-1)dx\\
	&=\frac{2M}{e^{\lambda}}-1
	\end{aligned}
	$$
	
	等号成立的条件为 $\frac{1}{e^{\lambda}p(x)}=1$，即 $p(x)=e^{-\lambda}$ 为常数，即 $p(x)$ 是均匀分布
	
	由约束条件 $\int_{-M}^Mp(x)dx=1$，得到 $p(x)=\frac{1}{2M}$，所以 $H_C(X)\leq\ln 2M$
***
#### 平均功率受限

定理：在方差 $\sigma^2$ 一定条件下，当 $X$ 服从正态分布时，微分熵最大，即 $H_C(X)\leq\ln\sqrt{2\pi e}\sigma$

??? note "Proof"

	使用 Lagrange 乘子法：
	
	$$
	\begin{aligned}
	J(p(x))&\stackrel{\Delta}{=}H_C(X)-\lambda_1\int_{-\infty}^{+\infty}p(x)dx-\lambda_2\int_{-\infty}^{+\infty}p(x)(x-m)^2dx\\
	&=-\int_{-\infty}^{+\infty}p(x)\ln(\frac{e^{\lambda_1e^{-\lambda_2}(x-m)^2}}{p(x)})dx\\
	&\leq-\int_{-\infty}^{+\infty}p(x)(\frac{e^{\lambda_1}e^{-\lambda_2}(x-m)^2}{p(x)}-1)dx
	\end{aligned}
	$$
	
	等号成立的条件为 $p(x)=e^{\lambda_1}e^{-\lambda_2(x-m)^2}$
	
	根据约束条件 $\int_{-\infty}^{+\infty}p(x)dx=1$ 以及 $\int_{-\infty}^{+\infty}p(x)(x-m)^2dx=\sigma^2$
	
	得 $p(x)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-m)^2}{2\sigma^2}}$，所以 $H_C(X)\leq\ln\sqrt{2\pi e}\sigma$
***
### 熵功率

定义熵功率：

$$
\overline{\sigma_x}^2=\frac{1}{2\pi e}e^{2H_C(X)}
$$

高斯随机变量 $X\sim p(x)=\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{1}{2\sigma^2}x^2}$ 的微分熵为 $H_C(X)=\frac{1}{2}\ln 2\pi e\sigma^2$，其熵功率为 $\overline{\sigma_x}^2=\frac{1}{2\pi e}e^{2H_C(X)}=\sigma^2$ 刚好为高斯随机变量的方差
***
#### 熵功率不等式

$$
\begin{gather*}
H_C(X)\leq\ln(\sqrt{2\pi e}\sigma)\\
\Updownarrow\\
\overline{\sigma_x}^2=\frac{1}{2\pi e}e^{2H_C(X)}\leq\sigma^2\\
\end{gather*}
$$

1. 随机变量的熵功率一般不大于功率，只有高斯变量其熵功率与功率相等
2. 功率一定时，高斯变量的熵功率最大，与功率相等


