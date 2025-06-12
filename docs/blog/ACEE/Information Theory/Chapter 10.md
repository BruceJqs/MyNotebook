---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 10 :  加性高斯噪声（AWGN）信道

## 时间离散的加性高斯信道

![](../../../assets/Pasted%20image%2020250612105930.png)

$$
\begin{aligned}
Y_i=X_i+Z_i\\
\frac{1}{n}\sum\limits_{i=1}^nX_i^2\leq P\\
\end{aligned}
$$

***
### 幅度离散化

![](../../../assets/Pasted%20image%2020250612110121.png)

$$
\begin{aligned}
Y_i&=X_i+Z_i\\
X_i&\in\{+\sqrt{P},-\sqrt{P}\}
\end{aligned}
$$

二元对称信道：

$$
\begin{aligned}
P_e&=P\{Y<0|X=\sqrt{P}\}\\
&=P\{Y>0|X=-\sqrt{P}\}\\
&=P\{Z<-\sqrt{P}|X=\sqrt{P}\}\\
&=P\{Z>\sqrt{P}\}=1-\Phi\left(\sqrt{\frac{P}{N}}\right)\\
\end{aligned}
$$

二元除删信道
***
### 容量

$$
\begin{aligned}
C&=\max\limits_{p(x):EX^2\leq P}I(X;Y)\\
I(X;Y)&=h(Y)-h(Y|X)\\
&=h(Y)-h(X+Z|X)\\
&=h(Y)-h(Z|X)\\
&=h(Y)-h(Z)\\
h(Z)&=\frac{1}{2}\log(2\pi e N)\\
E(Y^2)&=P+N\\
h(Y)&\leq\frac{1}{2}\log(2\pi e (P+N))\\
\therefore I(X;Y)&\leq\frac{1}{2}\log 2\pi e(P+N)-\frac{1}{2}\log(2\pi e N)=\frac{1}{2}\log(1+\frac{P}{N})
\end{aligned}
$$

- 当输入 $X$ 为高斯分布时等号成立，说明发送信号采用高斯分布时，互信息最大
- 干扰信道（噪声信号）为高斯分布时，互信息最小，即高斯干扰最有效
***
## 高斯信道编码定理

- 高斯信道编码定理：在噪声方差为 $N$，信号功率限制为 $P$ 的加性高斯信道上，任何速率小于 $C$ 的码率 $R$，是可达的，即总存在一种编码方法，使信息在该信道上无错误地可靠传播
	- 逆定理：任何 $R<C$ 是不可达的
	- $\frac{A_n(n(P+N))^{\frac{n}{2}}}{A_n(nN)^{\frac{n}{2}}}=2^{\frac{n}{2}\log(1+\frac{P}{N})}$

![](../../../assets/Pasted%20image%2020250612111503.png)

!!! note "逆定理证明"

	利用 Fano 不等式 $H(W|Y^n)\leq 1+nRP_e^{(n)}\stackrel{\Delta}{=}n\epsilon_n$
	
	因为 $P_e^{(n)}\rightarrow 0$，所以当 $n\rightarrow\infty$ 时 $\epsilon_n\rightarrow 0$。因而
	
	$$
	\begin{aligned}
	nR=H(W)&=I(W;Y^n)+H(W|Y^n)\\
	&\leq I(X^n;Y^n)+n\epsilon_n\\
	&=h(Y^n)-h(Y^n|X^n)+n\epsilon_n\\
	&=\sum\limits_{i=1}^n\{h(Y_i)-h(Z_i)\}+n\epsilon_n\\
	h(Y_i)&\leq\frac{1}{2}\log(2\pi e (P_i+N))\\
	\therefore nR&\leq\sum\limits_{i=1}^n\{h(Y_i)-h(Z_i)\}+n\epsilon_n\\
	&\leq \frac{1}{2}\log(1+\frac{P_i}{N})+n\epsilon_n\\
	\frac{1}{n}\sum\limits_{i=1}^n\frac{1}{2}\log(1+\frac{P_i}{N})&\leq\frac{1}{2}\log(1+\frac{1}{n}\sum\limits_{i=1}^n\frac{P_i}{N})\leq\frac{1}{2}\log(1+\frac{P}{N})=C 
	\end{aligned}
	$$
	
***
### 高斯平行信道

- 物理意义：OFDM; CDMA; MIMO

![](../../../assets/Pasted%20image%2020250612112451.png)

$$
\begin{aligned}
Y_i&=X_i+Z_i,i=1,2,\cdots,k\\
Z_i&=N(0,N_i),i=1,2,\cdots,k\\
E&\bigg\{\sum\limits_{i=1}^kX_i^2\bigg\}\leq P\\
I(X_1,X_2,\cdots,X_k;Y_1,Y_2,\cdots,Y_k)&=h(Y_1,Y_2,\cdots,Y_k)-\sum\limits_{i=1}^kh(Z_i)\\
&\leq\sum\limits_{i=1}^k h(Y_i)-\sum\limits_{i=1}^k h(Z_i)\\
&\leq\frac{1}{2}\sum\limits_{i=1}^k\log(1+\frac{P_i}{N_i})\\
\end{aligned}
$$

其中，$P_i=EX_i^2,\sum\limits_{i=1}^kP_i\leq P$

用拉格朗日乘数法：

$$
\begin{aligned}
J&=\sum\limits_{i=1}^k\log(1+\frac{P_i}{N_i})-\lambda\sum\limits_{i=1}^k P_i\\
\frac{\partial J}{\partial P_i}&=\frac{1}{(1+\frac{P_i}{N_i})\cdot N_i}-\lambda=0\\
P_i&=\gamma-N_i\\
P_i&=(\gamma-N_i)^+
\end{aligned}
$$

根据 $\sum\limits_{i=1}^k P_i=P$ 可以算出 $\gamma$

注水（灌水，Water-filling，Water-Pouring）法则：

![](../../../assets/Pasted%20image%2020250612123201.png)
***
### 带限（模拟）高斯信道的容量

$$
y(t)=x(t)+z(t)
$$

$x(t),z(t)$ 的带宽均限制在 $[0,W]$ Hz 之内

- 连续信号的离散化表示（Nyquist 抽样）
	
	$$
	f(t)=\sum\limits_{n=-\infty}^{\infty}f(\frac{n}{2W})\text{sinc}2\pi W(t-\frac{n}{2W})
	$$
	
	- 其中，$\text{sinc}(x)=\frac{\sin x}{x}$
***
#### 连续信号的离散化

$$
\begin{aligned}
x(t)&=\sum\limits_{n=-\infty}^{\infty}x_n\varphi_n(t)=\sum\limits_{n=-\infty}^{\infty}x(\frac{n}{2W})\text{sinc}2\pi W(t-\frac{n}{2W})\\
z(t)&=\sum\limits_{n=-\infty}^{\infty}z_n\varphi_n(t)=\sum\limits_{n=-\infty}^{\infty}z(\frac{n}{2W})\text{sinc}2\pi W(t-\frac{n}{2W})\\
y(t)&=\sum\limits_{n=-\infty}^{\infty}y_n\varphi_n(t)=\sum\limits_{n=-\infty}^{\infty}(x_n+z_n)\varphi_n(t)\\
\end{aligned}
$$

***
#### 等效平行信道

![](../../../assets/Pasted%20image%2020250612133547.png)

若噪声 $z(t)$ 是均值为 0、单边带宽为 $W$、双边功率谱密度为 $\frac{N_0}{2}$ 的白高斯过程，其 Nyquist 采样序列 $\{z_n=z(\frac{n}{2W})\}$ 为均值为 0，方差为 $\frac{N_0}{2}$ 的独立随机序列
***
#### 模拟高斯信道的容量

考虑 $T$ 秒钟的模拟传输过程，它相当于 $2WT$ 次平行的传输。设每次传输时输入样本 $x_i$ 的方差分别为 $P_i$，则由功率限制：

$$
\sum\limits_{i=1}^{2WT}P_i\leq PT
$$

$T$ 秒钟的传输容量：$C_T=\frac{1}{2}\sum\limits_{i=1}^{2WT}\log(1+\frac{P_i}{N_i})$，$N_i\equiv\frac{N_0}{2},P_i\equiv\frac{P}{2W};C_T=WT\log(1+\frac{P}{N_0W})$

等效地，每秒钟的容量 $C=W\log(1+\frac{P}{N_0W})$
***
## 传输 1 比特需要的最小能量

传输每比特的平均能量为 $\epsilon_b=\frac{P}{R}$

由容量公式可得 $\eta=\frac{R}{W}=\log(1+\frac{\epsilon_bR}{N_0W})$

所以在频谱效率为 $\eta$ 时，$\epsilon_b^*(\eta)=\frac{N_0}{\eta}(2^{\eta}-1)$

由于是 $\eta$ 的严格单调增函数，所以传输 1 比特的最小能量为 $\epsilon_b^*(0)=\lim\limits_{R\rightarrow 0}\epsilon_b^*(\eta)=N_0\ln 2=0.693N_0$

- 推论
	- $\epsilon_b^*(R)=\frac{N_0}{R}(2^R-1)$ 是 $R$ 的增函数，令 $R=x\log e$
	- $P(W)=(2^{\frac{C}{W}}-1)N_0W$ 是 $W$ 的减函数，令 $W=\frac{C}{x\log e}$
***
### 功率与频率资源的互换

$$
C=W\log(1+\frac{P}{N_0W})\Rightarrow P(W)=(2^{\frac{C}{W}}-1)N_0W
$$

功率与频率资源的互换：所使用的带宽越宽，需要的功率越小

- 每比特需要的最少功率：$P_{\min}=\lim\limits_{W\rightarrow\infty}(2^{\frac{C}{W}}-1)N_0W=N_0C\ln 2$
- 功率效率的极限：$W\rightarrow\infty,C\rightarrow\frac{P}{N_0}\log e(\text{bps})$
***
### 对通信技术的启示

- 使用的带宽越大，系统功率效率越高，或者说传输同样信息，需要的功率越小。CDMA, OFDM... （不利因素）
- P 随 C 呈指数上升趋势
- 在 AWGN 信道上信息传输得越慢，则越节省能量









