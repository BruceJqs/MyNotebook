---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 
## Homework 02

### Mooc

#### Question 01

![](../../../assets/Pasted%20image%2020241021230242.png)

（1）策略：每一位同学数自己能看见的 ”淙淙”，“宸宸”和“莲莲”的个数，设为 $k_1,k_2,k_3$，那么设 $t=|k_2-k_1| \text{ mod } 3$  那么有 $t=\begin{cases}0\Rightarrow 站左边\\1\Rightarrow 站中间\\2\Rightarrow 站右边\end{cases}$
证明：假设场上的”淙淙”，“宸宸”和“莲莲”的个数分别为 $n_1,n_2,n_3$，不妨设 $n_1\leq n_2\leq n_3$ ，设 $M=n_2-n_1$
- 第一种情况：若该同学背后是"淙淙"，那么他看到的是 $n_1-1,n_2,n_3$，此时 $t=|n_2-n_1+1|\text{ mod } 3=|M+1|\text{ mod } 3$
- 第二种情况：若该同学背后是"宸宸"，那么他看到的是 $n_1,n_2-1,n_3$，此时 $t=|n_2-n_1-1|\text{ mod } 3=|M-1|\text{ mod } 3$
- 第三种情况：若该同学背后是"莲莲"，那么他看到的是 $n_1,n_2,n_3-1$，此时 $t=|n_2-n_1|\text{ mod } 3=|M|\text{ mod } 3$
因为 $|M+1|\text{ mod } 3,|M-1|\text{ mod } 3,|M|\text{ mod } 3$ 三者必然互不相同且必为 0,1,2，因此实现了一一对应。
（2）
***
#### Question 02

![](../../../assets/Pasted%20image%2020241022000045.png)

（1）设 $W^*$ 为伪币的质量，由题意我们有 $\begin{cases}NW+|I|(W^*-W)=M_1\\(\sum\limits_{i=1}^n p^i) W+(\sum\limits_{i\in I}p^i)(W^*-W)=M_2\end{cases}$，因此消去 $W^*$ 我们有 $\frac{M_1-NW}{|I|}=\frac{M_2-(\sum\limits_{i=1}^np^i)W}{\sum\limits_{i\in I}p^i}$，定义函数 $f(M_1,M_2,W)=\frac{M_2-(\sum\limits_{i=1}^np^i)W}{M_1-NW}=\frac{\sum\limits_{i\in I}p^i}{|I|}$，此函数值仅与 $I,p$ 有关。
（2）假设伪币质量比真币轻，考虑函数： 

$$
\begin{aligned}
F(M_1,M_2,W)&=(p-1)(M_1-NW)f(M_1,M_2,W)\\
&=(p-1)(M_2-\sum\limits_{i=1}^np^iW)\\
&=(p-1)(M_2-\frac{p^{N+1}-p}{p-1}W)\\
&=(p-1)M_2-p^{N+1}W+pW\\
&=\frac{(p-1)(M_1-NW)\sum\limits_{i\in I}p^i}{|I|}
\end{aligned}
$$

对于最后一个等号，只要函数值唯一，由于 $p,M_1,N,W$ 已知，可以唯一确定指标集 $I$，对其求导：

$$
F'_p(M_1,M_2,W)=M_2-(N+1)p^NW+W
$$

注意到当 $p=1$ 时 $F(M_1,M_2,W)=0,F'_p(M_1,M_2,W)=M_2-NW=M_1-NW<0$，

