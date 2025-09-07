---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 
# Homework 03

## 4.1

![](../../../assets/Pasted%20image%2020250612135709.png)

（a）信道概率转移矩阵为 $P=\begin{pmatrix}1-\epsilon-\delta & \delta & \epsilon\\\epsilon & \delta & 1-\epsilon-\delta\end{pmatrix}$

该信道为准对称信道，取 $P(X=0)=P(X=1)=0.5$ 时达到信道容量，此时：

$$
\begin{aligned}
P(Y=0)&=0.5-0.5\delta\\
P(Y=1)&=\delta\\
P(Y=2)&=0.5-0.5\delta
\end{aligned}
$$

信道容量为：

$$
\begin{aligned}
C&=I(X=0;Y)=I(X=1;Y)\\
&=\sum\limits_{j=0}^2p(j|0)\log\frac{p(j|0)}{p(j)}\\
&=(1-\epsilon-\delta)\log\frac{1-\epsilon-\delta}{0.5-0.5\delta}+\delta\log\frac{\delta}{\delta}+\epsilon\log\frac{\epsilon}{0.5-0.5\delta}\\
&=(1-\epsilon-\delta)\log(1-\epsilon-\delta)+\epsilon\log\epsilon-(1-\delta)\log(0.5-0.5\delta)
\end{aligned}
$$

（b）信道概率转移矩阵为 $P=\begin{pmatrix}1 & 0 & 0\\0.5 & 0.25 & 0.25\\0 & 0.5 & 0.5\end{pmatrix}$

当 $P(X=0)=P(X=2)=0.5,P(X=1)=0$ 时，$P(Y=0)=0.5,P(Y=1)=P(Y=2)=0.25$，有：

$$
\begin{aligned}
I(X=0;Y)&=\sum\limits_{j=0}^2 p(j|0)\log\frac{p(j|0)}{p(j)}=1\\
I(X=2;Y)&=\sum\limits_{j=0}^2 p(j|2)\log\frac{p(j|2)}{p(j)}=1\\
I(X=1;Y)&=0\leq 1
\end{aligned}
$$

因此信道容量 $C=1$

（c）信道概率转移矩阵为 $P=\begin{pmatrix}1-\epsilon & \epsilon & 0\\0 & 1-\epsilon & \epsilon\\\epsilon & 0 & 1-\epsilon\end{pmatrix}$

这是一个对称信道，因此当输入为均匀分布时达到信道容量，$C=(1-\epsilon)\log 3(1-\epsilon)+\epsilon\log 3\epsilon=\log 3+\epsilon\log\epsilon+(1-\epsilon)\log(1-\epsilon)$

（d）信道概率转移矩阵为 $P=\begin{pmatrix}\frac{3}{4} & \frac{1}{4} & 0\\\frac{1}{3} & \frac{1}{3} & \frac{1}{3}\\0 & \frac{1}{4} & \frac{3}{4}\end{pmatrix}$

当 $P(X=0)=P(X=2)=0.5,P(X=1)=0$ 时，$P(Y=1)=\frac{1}{4},P(Y=0)=P(Y=2)=\frac{3}{8}$，有：

$$
\begin{aligned}
I(X=0;Y)&=\sum\limits_{j=0}^2 p(j|0)\log\frac{p(j|0)}{p(j)}=\frac{3}{4}\\
I(X=2;Y)&=\sum\limits_{j=0}^2 p(j|2)\log\frac{p(j|2)}{p(j)}=\frac{3}{4}\\
I(X=1;Y)&=\sum\limits_{j=0}^2 p(j|1)\log\frac{p(j|1)}{p(j)}=\frac{2}{3}\log\frac{8}{9}+\frac{1}{3}\log\frac{4}{3}\leq\frac{3}{4}
\end{aligned}
$$

因此信道容量 $C=\frac{3}{4}$

（e）信道概率转移矩阵为 $P=\begin{pmatrix}\frac{1}{3} & \frac{1}{3} & 0 & \frac{1}{3}\\0 & \frac{1}{3} & \frac{1}{3} & \frac{1}{3}\\\frac{1}{3} & 0 & \frac{1}{3} & \frac{1}{3}\end{pmatrix}$

这是一个准对称信道，取 $P(X=0)=P(X=1)=P(X=2)=\frac{1}{3}$ 时达到信道容量，此时 $P(Y=0)=P(Y=1)=P(Y=2)=\frac{2}{9},P(Y=3)=\frac{1}{3}$

信道容量为：

$$
\begin{aligned}
C=I(X=0;Y)=I(X=1;Y)=I(X=2;Y)&=\sum\limits_{j=0}^3 p(j|0)\log\frac{p(j|0)}{p(j)}\\
&=2\times\frac{1}{3}\log\frac{3}{2}=\frac{2}{3}\log\frac{3}{2}
\end{aligned}
$$

（f）信道概率转移矩阵为 $P=\begin{pmatrix}1-\epsilon & \epsilon\\\delta & 1-\delta\end{pmatrix}$

转移矩阵可逆，设 $P(X=0)=p,P(X=1)=1-p,0<p<1,\alpha=\begin{bmatrix}-H(\epsilon)\\-H(\delta)\end{bmatrix}$

解方程 $P\beta=\alpha$，得到 $\beta=\begin{bmatrix}\frac{\epsilon H(\delta)-(1-\delta)H(\epsilon)}{1-\epsilon-\delta}\\\frac{\delta H(\epsilon)-(1-\epsilon)H(\delta)}{1-\epsilon-\delta}\end{bmatrix}$

$$
\therefore C=\log[2^{\frac{\epsilon H(\delta)-(1-\delta)H(\epsilon)}{1-\epsilon-\delta}}+2^{\frac{\delta H(\epsilon)-(1-\epsilon)H(\delta)}{1-\epsilon-\delta}}]
$$

***
## 4.2

![](../../../assets/Pasted%20image%2020250612165206.png)

信道可视为一个无噪信道 $C_1$ 和一个二元对称信道 $C_2$ 的和信道

有 $C_1=0,C_2=1-H(\epsilon)$,则总信道为 $C=\log[1+2^{1-H(\epsilon)}]$
***
## 4.9

![](../../../assets/Pasted%20image%2020250612165832.png)

该信道是对称信道，取 $P(X=0)=P(X=1)=P(X=2)=P(X=3)=\frac{1}{4}$

信道容量为：

$$
\begin{aligned}
C&=I(X=0;Y)=I(X=1;Y)=I(X=2;Y)=I(X=3;Y)\\
&=\sum\limits_{j=0}^3 p(j|0)\log\frac{p(j|0)}{p(j)}\\
&=2-H(p)
\end{aligned}
$$

***
## 4.13

![](../../../assets/Pasted%20image%2020250612170148.png)
（a） $C=\max\limits_{f(x)}I(X;Y)=\max\limits_{f(x)}[H(Y)-H(Y|X)]$

因为 $Y=(X+Z)\text{ mod }2\pi$，当 $X$ 确定时 $H(Y|X)$ 仅由噪声 $Z$ 确定，即 $H(Y|X)=H(Z\text{ mod }2\pi)$

对于 $H(Y)$ 来说，当 $Y$ 为均匀分布时最大， $H(Y)_{\max}=\log 2\pi$

当 $a>\pi$ 时，噪声是均匀的，因此 $H(Y|X)=\log 2\pi,C=0$

（b）当 $a\leq\pi$ 时，噪声也是均匀的，因此 $H(Y|X)=\log 2a,C=\log(\frac{\pi}{a})$
***
## 4.14

![](../../../assets/Pasted%20image%2020250612170535.png)


传输每比特的平均能量为 $\epsilon_b=\frac{P}{R}$

由容量公式可得 $\eta=\frac{R}{W}=\log(1+\frac{\epsilon_bR}{N_0W})$

所以在频谱效率为 $\eta$ 时，$\epsilon_b^*(\eta)=\frac{N_0}{\eta}(2^{\eta}-1)$

由于是 $\eta$ 的严格单调增函数，所以传输 1 比特的最小能量为 $\epsilon_b^*(0)=\lim\limits_{R\rightarrow 0}\epsilon_b^*(\eta)=N_0\ln 2=0.693N_0$

设用 $T_b$ 时间传送 1 bit 信息，由 Shannon 公式：

$$
\begin{aligned}
C_{T_b}=T_b\cdot W\log(1+\frac{P}{N_0W})=1\\
\Rightarrow T_bW=\frac{1}{\log(1+\frac{P}{N_0W})}
\end{aligned}
$$

要求 $\frac{P}{N_0W}>4000$，那么有 $\epsilon_b=PT_b>4000N_0WT_b=\frac{4000N_0}{\log(1+\frac{P}{N_0W})}$

因此：

$$
\frac{\epsilon_b}{\epsilon_{\min}}\geq\frac{4000N_0}{0.693N_0\times\log 4001}=482
$$
