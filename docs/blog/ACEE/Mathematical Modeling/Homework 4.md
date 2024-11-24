---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 4

## Question 01

![](../../../assets/Pasted%20image%2020241122173905.png)

由定义，$L_i=\frac{\sum\limits_{j=1}^iy_j}{\sum\limits_{j=1}^ny_j},i=1,...,n$

则有：

$$
\begin{aligned}
S_B&=\sum\limits_{j=1}^n\frac{L_{i-1}+L_i}{2}·\frac{1}{n}=\frac{1}{2n}(2\sum\limits_{i=1}^nL_i-L_n)\\
&=\frac{1}{n}\sum\limits_{i=1}^n L_i-\frac{1}{2n}=\frac{1}{n\sum\limits_{j=1}^ny_j}\sum\limits_{i=1}^n(n-i+1)y_i-\frac{1}{2n}\\
\end{aligned}
$$

因此 $G=2(\frac{1}{2}-S_B)=\frac{n+1}{n}-\frac{2}{n\sum\limits_{j=1}^ny_j}\sum\limits_{i=1}^n(n-i+1)y_i$

由于 $y_1\leq y_2\leq ...\leq y_n$ ，因此 $L_i\leq\frac{i}{n}$ ,即 $L$ 总在直线 $y = x$ 的下方，$G$ 越大，$L$ 在横坐标较小时增长较慢，在横坐标较大时增长迅速，说明少部分人占有收入比例很高，家庭收入差异大。
***
## Question 02

![](../../../assets/Pasted%20image%2020241122232340.png)

（1）若进入会场时有 n 个座位可供选择，与会者选择每个座位的概率均为 $\frac{1}{n}$。若他选择了第 $i$ 个座位,下一个进入会场者只有其左侧的 $i − 1$ 个座位可供选择。因此，可得递推关系：$E_n=1+\frac{1}{n}\sum\limits_{i=1}^nE_{i-1}$，即 $nE_n=n+\sum\limits_{i=1}^nE_{i-1}$，再写一项我们有 $(n+1)E_{n+1}=n+1+\sum\limits_{i=1}^{n+1}E_{i-1}$，两式相减即得 $(n+1)E_{n+1}-nE_n=1+E_n$，即 $E_{n+1}=E_n+\frac{1}{n+1}$，由 $E_1=1$，则 $E_n=\sum\limits_{i=1}^n\frac{1}{i}$

（2）记 $G_n$ 为只有一侧有入口时最终入座人数的期望，则 $G_n$ 满足递推关系 $G_n=1+pG_{n-1}+(1-p)·\frac{1}{n}\sum\limits_{i=1}^nG_{i-1}$，则 $F_n$ 满足递推关系 $F_n=1+pF_{n-1}+(1-p)·\frac{1}{n}\sum\limits_{i=1}^n(G_{i-1}+G_{n-i})$
