---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 5

## Question 01

![](../../../assets/Pasted%20image%2020241128145500.png)

（1）对于每支球队来说，设先罚进球数为 $X$，其分布律如下：

$$
\begin{gather}
P\{X=0\}=(1-p)(1-q)=1-p-q+pq\\
P\{X=1\}=(1-p)q+p(1-q)=p+q-2pq\\
P\{X=2\}=pq
\end{gather}
$$

设后罚进球数为 $Y$，其分布律如下：

$$
\begin{gather}
P\{Y=0\}=(1-q)(1-p)=1-p-q+pq\\
P\{Y=1\}=(1-q)p+q(1-p)=p+q-2pq\\
P\{Y=2\}=pq
\end{gather}
$$

因此：

$$
\begin{aligned}
P\{\text{先罚获胜}\}&=(p+q-2pq+pq)(1-p-q+pq)+pq(p+q-2pq)\\
&=(1+3pq)(p+q-pq)-(p+q)^2\\
P\{\text{后罚获胜}\}&=(1-p-q+pq)(p+q-2pq+pq)+(p+q-2pq)pq\\
&=(1+3pq)(p+q-pq)-(p+q)^2\\
P\{\text{进球相同}\}&=(1-p-q+pq)^2+(p+q-2pq)^2+p^2q^2
\end{aligned}
$$

当 $p=\frac{3}{4},q=\frac{2}{3}$ 时，有 $P\{先罚获胜\}=P\{后罚获胜\}=\frac{41}{144},P\{进球相同\}=\frac{31}{72}$
***
（2）在现规则下：

$$
\begin{aligned}
P\{先罚获胜\}=p(1-q)+pq·p(1-q)+p^2q^2·p(1-q)+...=\frac{p-pq}{1-pq}\\
P\{后罚获胜\}=(1-p)q+pq·(1-p)q+p^2q^2·(1-p)q+...=\frac{q-pq}{1-pq}
\end{aligned}
$$

在新规则下：

$$
\begin{aligned}
P\{先罚获胜\}&=p(1-q)+pq·(1-p)q+p^2q^2·p(1-q)+...\\
&=\frac{p-pq}{1-p^2q^2}+pq\frac{q-pq}{1-p^2q^2}\\
&=\frac{p+pq^2-pq-p^2q^2}{1-p^2q^2}\\
P\{后罚获胜\}&=(1-p)q+pq·p(1-q)+p^2q^2(1-p)q+...\\
&=\frac{q-pq}{1-p^2q^2}+pq\frac{p-pq}{1-p^2q^2}\\
&=\frac{p^2q+q-pq-p^2q^2}{1-p^2q^2}
\end{aligned}
$$

***
## Question 02

![](../../../assets/Pasted%20image%2020241128152834.png)

（1）$P\{A\text{ 获得比赛胜利}\}=(\alpha+\beta)+\gamma^2(\alpha+\beta)+...=\frac{\alpha+\beta}{1-\gamma^2}$

（2）$P\{A\text{ 获得比赛胜利}\}=\alpha+\beta a+\gamma b$

（3）$a=\gamma + \beta\frac{\alpha+\beta}{1-\gamma^2},b=1-\frac{\alpha+\beta}{1-\gamma^2}$

$\therefore P\{A\text{ 获得比赛胜利}\}=\alpha+\beta\gamma+\beta^2\frac{\alpha+\beta}{1-\gamma^2}+\gamma-\gamma\frac{\alpha+\beta}{1-\gamma^2}=\frac{1-\beta+\beta\gamma^2+\beta^2}{1+\gamma}$

在旧赛制下，$P\{A\text{ 获得比赛胜利}\}=\frac{1}{1+\gamma}$

从公平性角度来看，一般来说 $-\beta+\beta\gamma^2+\beta^2<0$，所以新赛制更为公平一些

