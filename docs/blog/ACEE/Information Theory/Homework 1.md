---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 01

## 2.1

![](../../../assets/Pasted%20image%2020250322170634.png)

设 $y_1$ 表示说真话，$y_2$ 表示说假话，$y_3$ 表示拒绝回答，那么有：

$$
\begin{aligned}
P(y_1)&=0.5p+0.3(1-p)\\
P(y_2)&=0.3p+0.5(1-p)\\
P(y_3)&=0.2p+0.2(1-p)=0.2\\
H(Y)&=-\sum\limits_{i=1}^3P(y_i)\log P(y_i)\\
H(Y|X)&=P(A)H(Y|X=A)+P(B)H(Y|X=B)\\
&=-0.5\log 0.5-0.3\log 0.3-0.2\log 0.2=1.485\text{ bit}\\
I(X;Y)&=H(Y)-H(Y|X)
\end{aligned}
$$

要想让 $I(X;Y)$ 最大，即让 $H(Y)$ 最大：

$$
H(Y)=-(0.3+0.2p)\log(0.3+0.2p) - (0.5-0.2p)\log(0.5-0.2p) - 0.2\log 0.2
$$

求导：

$$
\begin{aligned}
\frac{dH(Y)}{dp} &=\log e(0.2\ln\frac{5-2p}{3+2p})=\log e(0.2\ln(\frac{8}{3+2p}-1))
\end{aligned}
$$


当导数为 0，即当 $p=0.5$ 时，$I(X;Y)$ 最大，此时：

$$
\begin{aligned}
H(Y)&=0.4\log 0.4+0.4\log 0.4+0.2\log 0.2=1.522\text{ bit}\\
I(X;Y)&=H(Y)-H(Y|X)=0.037\text{ bit}
\end{aligned}
$$

***
## 2.2

![](../../../assets/Pasted%20image%2020250322170715.png)

设 $X=x_1$ 表示抛掷骰子出现 1,2,3,4 点；$X=x_2$ 表示抛掷骰子出现 5,6 点；$Y=y_i$ 表示投掷硬币正面的出现次数，那么有：

$$
\begin{aligned}
P(X=x_1)&=\frac{2}{3},P(X=x_2)=\frac{1}{3}\\
P(Y=y_0)&=\frac{5}{12},P(Y=y_1)=\frac{1}{2},P(Y=y_2)=\frac{1}{12}\\
\end{aligned}
$$

所以：

$$
\begin{aligned}
I(X;Y)&=H(Y)-H(Y|X)\\
&=H(\frac{5}{12},\frac{1}{2},\frac{1}{12})-\frac{2}{3}H(\frac{1}{2},\frac{1}{2})-\frac{1}{3}H(\frac{1}{4},\frac{1}{2},\frac{1}{4})\\
&=0.158\text{ bit}
\end{aligned}
$$
***
## 2.4

![](../../../assets/Pasted%20image%2020250322170748.png)

设第 $i$ 个骰子的结果为 $X_i$

$$
\begin{aligned}
H(X)&=H(X_1)=H(X_2)=H(X_3)=\log_2 6=2.585\text{ bit}\\
H(Y)&=H(X_1+X_2)=\sum\limits_{y_i}P(y_i)\log P(y_i)=3.274\text{ bit}\\
H(Z|Y)&=H(X_3)=2.585\text{ bit}
\end{aligned}
$$

- $H(X|Y)=H(X)+H(Y|X)-H(Y)=H(X)+H(X_2)-H(Y)=1.896\text{ bit}$
- $H(Y|X)=H(X_2)=2.585\text{ bit}$
- $H(Z|X,Y)=H(X_3)=2.585\text{ bit}$
- $H(X,Z|Y)=H(X|Y)+H(Z|X,Y)=4.481\text{ bit}$
- $H(Z|X)=H(X_2+X_3)=H(Y)=3.274\text{ bit}$
***
## 2.5

![](../../../assets/Pasted%20image%2020250322170847.png)

设 $X$ 表示发送的数字，$Y$ 表示接收的数字，那么有：

$$
I(X;Y)=\sum\limits_{x\in\mathcal{X}}\sum\limits_{y\in\mathcal{Y}}p(x,y)\log\frac{p(x|y)}{q(x)}
$$

（1）如果发送的是偶数，那么有：

$$
I(X;Y)_{\text{even}}=5\times\frac{1}{10}\log\frac{1}{0.1}=1.661\text{ bit}
$$

（2）如果发送的是奇数，且接收正确，有：

$$
I(X;Y)_{\text{right odd}}=5\times 0.05\log\frac{0.5}{0.1}=0.581\text{ bit}
$$

（3）如果发送的是奇数，且接收错误，有：

$$
I(X;Y)_{\text{wrong odd}}=20\times 0.0125\log\frac{0.125}{0.1}=0.08\text{ bit}
$$

所以总信息量为 $2.322\text{ bit}$
***
## 2.6

![](../../../assets/Pasted%20image%2020250322170924.png)

![](../../../assets/Pasted%20image%2020250322170950.png)

（a）$\text{LHS}\geq H(X|Y,Z)+H(Y|Z)=H(X,Y|Z)\geq H(X|Z)$

（b）由 $H(X|Y)=H(X,Y)-H(Y)\geq H(X,Y)-H(Y|Z)-H(Z)\Leftrightarrow H(X,Y)\leq H(X|Y)+H(Y|Z)+H(Z)$

同理，有 $H(Y,Z)\leq H(X|Y)+H(Y|Z)+H(Z)$

所以有 $LHS\geq\frac{H(X|Y)+H(Y|Z)}{H(X|Y)+H(Y|Z)+H(Z)}\geq\frac{H(X|Z)}{H(X|Z)+H(Y|Z)}\geq\frac{H(X|Z)}{H(X,Z)}$
***
## 2.9

![](../../../assets/Pasted%20image%2020250322171050.png)

（a）

$$
\begin{aligned}
H(Z)&=H(X,Y)-H(X,Y|Z)=H(X)+H(Y)-H(X,Y|Z)\\
&=H(X)+H(Y)-H(Y|Z)-H(X|Z,Y)\\
&=H(X)+H(Y)-H(Y|Z)=H(X)+I(Y;Z)\geq H(X)
\end{aligned}
$$

（b）同（a）类似

（c）由 $H(Z)=H(X,Y)-H(X,Y|Z)$ 有 $H(X,Y)\geq H(Z)$

（d）

$$
\begin{aligned}
H(Z)&=H(X)+H(Y)-H(X,Y|Z)\\
&=H(X)+H(Y)-H(X|Z)-H(Y|Z,X)\\
&=H(X)+H(Y)-H(X|Z)=H(Y)+I(X;Z)\\
\therefore I(X;Z)&=H(Z)-H(Y)
\end{aligned}
$$

（e）$I(X,Y;Z)=H(Z)-H(Z|X,Y)=H(Z)$

（f）$I(X;Y,Z)=H(X)-H(X|Y,Z)=H(X)$

（g）$I(Y;Z|X)=H(Y|X)-H(Y|Z,X)=H(Y|X)=H(Y)$

（h）$I(X;Y|Z)=H(X|Z)-H(X|Y,Z)=H(X|Z)=H(Y|Z)$
***
## 2.12

![](../../../assets/Pasted%20image%2020250322171129.png)

（a）

$$
\begin{aligned}
H(Y,Z|X)&=-\sum_{i,j,k}p(x_i,y_j,z_k)\log p(y_j,z_k|x_i)\\
&=-\sum_{i,j,k}p(x_i,y_j,z_k)\log p(y_j|x_i)p(z_k|x_i,y_j)\\
&=-\sum_{i,j,k}p(x_i,y_j,z_k)\log p(y_j|x_i)+\sum_{i,j,k}p(x_i,y_j,z_k)\log p(z_k|x_i,y_j)\\
&=-\sum_{i,j,k}p(x_i,y_j,z_k)\log p(y_j|x_i)+\sum_{i,j,k}p(x_i,y_j)p(z_k|x_i,y_j)\log p(z_k|x_i,y_j)\\
&\leq-\sum_{i,j,k}p(x_i,y_j,z_k)\log p(y_j|x_i)+\sum_{i,j,k}p(x_i,y_j)p(z_k|x_i,y_j)\log p(z_k|x_i)\\
&=-\sum_{i,j,k}p(x_i,y_j,z_k)\log p(y_j|x_i)+\sum_{i,j,k}p(x_i,y_j,z_k)\log p(z_k|x_i)\\
&=-\sum_{i,j}p(x_i,y_j)\log p(y_j|x_i)+\sum_{i,k}p(x_i,z_k)\log p(z_k|x_i)\\
&=H(Y|X)+H(Z|X)
\end{aligned}
$$

当且仅当 $p(y_j,z_k|x_i)=p(y_j|x_i)p(z_k|x_i)$ 成立时，等号成立

（b）

$$
\begin{aligned}
H(Y, Z | X) &=-\sum_{i,j,k}p(x_i,y_j,z_k)\log p(y_j,z_k|x_i)\\
&=-\sum_{i,j,k}p(x_i,y_j,z_k)\log p(y_j|x_i)p(z_k|x_i,y_j)\\
&=-\sum_{i,j,k}p(x_i,y_j,z_k)\log p(y_j|x_i)+\sum_{i,j,k}p(x_i,y_j,z_k)\log p(z_k|x_i,y_j)\\
&=H(Y|X)+H(Z|X, Y)
\end{aligned}
$$

（c）由（a）和（b）可得等号成立的充要条件为对一切 $i, j, k$ 有 $p(y_j,z_k|x_i)=p(y_j|z_k)p(z_k| x_i)$ 成立
***
## 2.13

![](../../../assets/Pasted%20image%2020250322171228.png)

![](../../../assets/Pasted%20image%2020250322171251.png)

（a）$H(X)=H(\alpha,1-\alpha)+\alpha H(X_1)+(1-\alpha)H(X_2)$

（b）

$$
\begin{aligned}
H(X)&=H(\alpha,1-\alpha)+\alpha H(X_1)+(1-\alpha)H(X_2)\\
&=-\alpha\log\alpha-(1-\alpha)\log(1-\alpha)+\alpha H(X_1)+(1-\alpha)H(X_2)\\
\end{aligned}
$$

求导：

$$
\begin{aligned}
\frac{dH(X)}{d\alpha}&=\log e(-\ln\alpha+\ln(1-\alpha))+H(X_1)-H(X_2)\\
&=\log\frac{1-\alpha}{\alpha}+H(X_1)-H(X_2)
\end{aligned}
$$

令导数为 0，底数为 2，有 $\log\frac{1-\alpha}{\alpha}=H(X_2)-H(X_1)$，解得 $\alpha=\frac{1}{1+2^{H(X_2)-H(X_1)}}$

$$
\begin{aligned}
H(X)_{max}&=-\alpha\log\alpha-(1-\alpha)\log(1-\alpha)+\alpha H(X_1)+(1-\alpha)H(X_2)\\
&=-\log(1-\alpha)+\alpha\log(\frac{1-\alpha}{\alpha})+\alpha H(X_1)+(1-\alpha)H(X_2)\\
&=-\log(1-\frac{1}{1+2^{H(X_2)-H(X_1)}})+\alpha(H(X_2)-H(X_1))+\alpha H(X_1)+(1-\alpha)H(X_2)\\
&=-\log(\frac{2^{H(X_2)-H(X_1)}}{1+2^{H(X_2)-H(X_1)}})+H(X_2)\\
&=\log(\frac{2^{H(X_1)}+2^{H(X_2)}}{2^{H(X_2)}})+H(X_2)\\
&=\log(2^{H(X_1)}+2^{H(X_2)})\\
\end{aligned}
$$

综上 $2^{H(X)}\leq 2^{H(X_1)}+2^{H(X_2)}$
***
## 2.19

![](../../../assets/Pasted%20image%2020250322171348.png)

$p(x)=\frac{1}{2}, x\in[-1,1]$，因此：

$$
H_C(X)=-\int p_X(x)\log p_X(x)dx=[-\frac{1}{2}\log\frac{1}{2}]·2=1\text{ bit}
$$

令 $Y=X^2$，有 $F_Y(y)=P(Y\leq y)=P(X^2\leq y)=P(-\sqrt{y}\leq X\leq \sqrt{y})=\int_{-\sqrt{y}}^{\sqrt{y}}\frac{1}{2}dx=\sqrt{y}$

$P(Y=y)=F_Y'(y)=\frac{1}{2\sqrt{y}}, y\in[0,1]$

$\therefore H_C(X^2)=-\int_{0}^{1}\frac{1}{2\sqrt{y}}\log\frac{1}{2\sqrt{y}}dy=\log 2-\log e\text{ bit}$
***
## 2.20

![](../../../assets/Pasted%20image%2020250322171417.png)

（a）

$$
p(y)=\sum_{x\in X}p(x)p(y|x)=\begin{cases}
\frac{1}{8}, & -3<y\leq -1\\
\frac{1}{4}, & -1<y\leq 1\\
\frac{1}{8}, & 1<y\leq 3\\
0, & y\leq -3 \text{ or } y>3
\end{cases}
$$

（b）

$$
\begin{aligned}
H(Y)&=-\int_{-3}^{-1}\frac{1}{8}\log\frac{1}{8}dy-\int_{-1}^{1}\frac{1}{4}\log\frac{1}{4}dy-\int_{1}^{3}\frac{1}{8}\log\frac{1}{8}dy\\
&=\frac{1}{4}\log 8 + \frac{1}{2}\log 4 + \frac{1}{4}\log 8\\
&=\frac{5}{2}\log 2
\end{aligned}
$$

$$
\begin{aligned}
H(Y|X)=\sum_{x\in X}p(x)H(Y|X=x)&=\frac{1}{2}H(Y|X=1)+\frac{1}{2}H(Y|X=-1)\\
&=\frac{1}{2}\left[-\int_{-1}^{3}\frac{1}{4}\log\frac{1}{4}dy-\int_{-3}^{1}\frac{1}{4}\log\frac{1}{4}dy\right]\\
&=2\log2\\
\end{aligned}
$$

$\therefore I(X;Y)=H(Y)-H(Y|X)=\frac{5}{2}\log2-2\log2=\frac{1}{2}\log2$

（c）

$$
P(V)=\begin{cases}
\frac{1}{4}, &-3<y\leq -1,V=-1\\
\frac{1}{2}, &-1<y\leq 1,V=0\\
\frac{1}{4}, &1<y\leq 3,V=1\\
0, & \text{otherwise}
\end{cases}
$$

$\therefore H(V)=-\frac{1}{4}\log\frac{1}{4}-\frac{1}{2}\log\frac{1}{2}-\frac{1}{4}\log\frac{1}{4}=1.5\log2$

$$
P(V,X)=\begin{cases}
\frac{1}{2}, &V=0,X=-1\\
\frac{1}{2}, &V=-1,X=-1\\
\frac{1}{2}, &V=0,X=1\\
\frac{1}{2}, &V=1,X=1\\
0, & \text{otherwise}
\end{cases}
$$

$\therefore H(V|X)=\frac{1}{2}H(V|X=1)+\frac{1}{2}H(V|X=-1)=\log2$

$I(V;X)=H(V)-H(V|X)=0.5\log2$
***
## 2.23

![](../../../assets/Pasted%20image%2020250325203123.png)

![](../../../assets/Pasted%20image%2020250325203253.png)

（a）


***
## 2.25

![](../../../assets/Pasted%20image%2020250325203143.png)

![](../../../assets/Pasted%20image%2020250325203154.png)


