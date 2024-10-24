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

事实上，$F_{X|Y}(x|y)=\lim\limits_{\Delta y\rightarrow 0^+}\frac{P(X\leq x,y<Y\leq y+\Delta y)}{P(y<Y\leq y+\Delta y)}$
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

若二元随机变量 $(X,Y)$ 在二维有界区域 $D$ 上取值，且具有概率密度 $f(x,y)=\begin{cases}\frac{1}{D的面积},(x,y)\in D\\0,其他\end{cases}$
若 $D_1$ 是 $D$ 的子集，则 $P\{(X,Y)\in D_1\}=\iint\limits_{D_1}f(x,y)dxdy$，即 $P\{(X,Y)\in D_1\}=\frac{D_1的面积}{D的面积}$
 