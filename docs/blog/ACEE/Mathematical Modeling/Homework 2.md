---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 
## Homework 02

### Question 01

![](../../../assets/Pasted%20image%2020241021230242.png)

（1）策略：每一位同学数自己能看见的 ”淙淙”，“宸宸”和“莲莲”的个数，设为 $k_1,k_2,k_3$，那么设 $t=|k_2-k_1| \text{ mod } 3$  那么有 $t=\begin{cases}0\Rightarrow 站左边\\1\Rightarrow 站中间\\2\Rightarrow 站右边\end{cases}$

证明：假设场上的”淙淙”，“宸宸”和“莲莲”的个数分别为 $n_1,n_2,n_3$，不妨设 $n_1\leq n_2\leq n_3$ ，设 $M=n_2-n_1$

- 第一种情况：若该同学背后是"淙淙"，那么他看到的是 $n_1-1,n_2,n_3$，此时 $t=|n_2-n_1+1|\text{ mod } 3=|M+1|\text{ mod } 3$
- 第二种情况：若该同学背后是"宸宸"，那么他看到的是 $n_1,n_2-1,n_3$，此时 $t=|n_2-n_1-1|\text{ mod } 3=|M-1|\text{ mod } 3$
- 第三种情况：若该同学背后是"莲莲"，那么他看到的是 $n_1,n_2,n_3-1$，此时 $t=|n_2-n_1|\text{ mod } 3=|M|\text{ mod } 3$

因为 $|M+1|\text{ mod } 3,|M-1|\text{ mod } 3,|M|\text{ mod } 3$ 三者必然互不相同且必为 0,1,2，因此实现了一一对应。

（2）不妨设 $n=3k+m(0\leq m<3)$ 设第 $i$ 位同学的图案为 $h_i(h_i=0,1,2)$，则 $\sum\limits_{i=1}^n h_i\text{ mod } 3$ 的值为一确定值。策略如下：

将 $n$ 名同学平均分为三组，安排第一组猜测自己的图案为 $x_1$ ，使得 $(x_1+\sum\limits_{j\not=i}h_i)\text{ mod } 3=0$；安排第二组猜测自己的图案为 $x_2$ ，使得 $(x_2+\sum\limits_{j\not=i}h_i)\text{ mod } 3=1$；安排第三组猜测自己的图案为 $x_3$ ，使得 $(x_3+\sum\limits_{j\not=i}h_i)\text{ mod } 3=2$。

由于$\sum\limits_{i=1}^n h_i\text{ mod } 3$ 的值为一确定值，那么可以保证有 $\lfloor\frac{n}{3}\rfloor$ 名同学猜对。 
***
### Question 02

![](../../../assets/Pasted%20image%2020241022000045.png)

（1）设 $W^*$ 为伪币的质量，由题意我们有 $\begin{cases}NW+|I|(W^*-W)=M_1\\(\sum\limits_{i=1}^n p^i) W+(\sum\limits_{i\in I}p^i)(W^*-W)=M_2\end{cases}$，因此消去 $W^*$ 我们有 $\frac{M_1-NW}{|I|}=\frac{M_2-(\sum\limits_{i=1}^np^i)W}{\sum\limits_{i\in I}p^i}$，定义函数 $f(M_1,M_2,W)=\frac{M_2-(\sum\limits_{i=1}^np^i)W}{M_1-NW}=\frac{\sum\limits_{i\in I}p^i}{|I|}$，此函数值仅与 $I,p$ 有关。

（2）设 $I=\{i_1,i_2,...,i_m\}$ ，为能求出指标集 $I$ ，即满足唯一性，即不存在 $m\not=n,\{i_1,i_2,...,i_m\}\not=\{j_1,j_2,...,j_n\}$ ，使得 $\frac{p^{i_1}+p^{i_2}+...+p^{i_m}}{m}=\frac{p^{j_1}+p^{j_2}+...+p^{j_n}}{n}$，由于整数的 $p$ 进制的表示是唯一的，当 $p > N$ 时，上式左右两边均可视作同一个整数在 p 进制下的一种表示。故任一 $p > N$ 的数均满足要求。但当 $p=2$ 时，会有特殊情况如下：

![](../../../assets/Pasted%20image%2020241106203405.png)

这样就无法求出 $I$ 。