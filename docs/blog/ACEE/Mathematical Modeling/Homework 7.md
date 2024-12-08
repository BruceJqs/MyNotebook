---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 7

## Question 1

![](../../../assets/Pasted%20image%2020241208003910.png)


同 [Homework 5 Question 1](https://brucejqs.github.io/MyNotebook/blog/ACEE/Mathematical%20Modeling/Homework%205/#question-01)
***
## Question 2

![](../../../assets/Pasted%20image%2020241208005837.png)


（1）甲投注 $A$ 获胜的期望收益为 $pa+p(1-a)+2(1-p)a=p+2(1-p)a$

投注 $B$ 获胜的期望收益为 $2p(1-a)+(1-p)a+(1-p)(1-a)=1+p-2pa$

（2）除甲之外的其余 $N$ 人中，有 $k$ 人投注 $A$ 的概率为 $C_N^kp^k(1-p)^{N-k},0\leq k\leq N$


若甲投注 $A$ 获胜，当且仅当 $k=N$ 且 $B$ 获胜时甲才有收益，所以甲的期望收益为：

$$
\begin{aligned}
&a\sum\limits_{k=0}^NC_N^kp^k(1-p)^{N-k}·\frac{N+1}{k+1}+(1-a)p^N\\
=&a\sum\limits_{k=0}^N\frac{(N+1)!}{(k+1)!(N-k)!}p^k(1-p)^{N-k}+(1-a)p^N\\
=&a\sum\limits_{k=1}^{N+1}\frac{(N+1)!}{k!(N-k)!}p^{k-1}(1-p)^{N-k+1}+(1-a)p^N\\
=&a·\frac{1}{p}(\sum\limits_{k=0}^{N+1}C_{N+1}^kp^k(1-p)^{N-k+1}-(1-p)^{N+1})+(1-a)p^N\\
=&a·\frac{1}{p}(1-(1-p)^{N+1})+(1-a)p^N
\end{aligned}
$$

若甲投注 $B$ 获胜，当且仅当 $k=0$ 且 $A$ 获胜时甲才有收益，所以甲的期望收益为：

$$
\begin{aligned}
&a(1-p)^N+(1-a)\sum\limits_{k=0}^NC_N^kp^k(1-p)^{N-k}\frac{N+1}{N-k+1}\\
=&a(1-p)^N+(1-a)\sum\limits_{k=0}^N\frac{(N+1)!}{k!(N-k+1)!}(1-p)^{N-k}\\
=&a(1-p)^N+(1-a)\frac{1}{1-p}(\sum\limits_{k=1}^{N+1}\frac{(N+1)!}{k!(N-k+1)!}(1-p)^{N+1-k}-p^{N+1})\\
=&a(1-p)^N+\frac{1-a}{1-p}(1-p^{N+1})
\end{aligned}
$$

比较上面两式，当 $a\geq\frac{p-p^{N+1}}{1-(1-p)^{N+1}-p^{N+1}}$ 时，有：

$$
\frac{a}{p}(1-(1-p)^{N+1})+(1-a)p^N\geq a(1-p)^N+\frac{1-a}{1-p}(1-p^{N+1})
$$

此时甲的收益较大

（3）若甲投注 $A$ 获胜两场，收益约为 $\frac{1}{4}(N+1)+\frac{1}{2}·1+\frac{1}{4}·0\approx\frac{1}{4}N$

投注 $A$ 一胜一负，收益约为 $\frac{1}{4}(N+1)+\frac{1}{4}·0+\frac{1}{4}·(N+1)+\frac{1}{4}·0\approx\frac{1}{2}N$

投注 $B$ 获胜两场，收益约为 1。所以甲应当投注 $A$ 一胜一负。

