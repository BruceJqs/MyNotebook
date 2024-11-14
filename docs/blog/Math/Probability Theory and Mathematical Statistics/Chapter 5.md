---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  
# Chapter 05 : 大数定律和中心极限定理

## 大数定律

### 依概率收敛

设 $\{Y_n,n\geq 1\}$ 为一**随机变量序列**，若对于 $\forall\epsilon>0$，均有 $\lim\limits_{n\rightarrow+\infty}P{|Y_n−Y|\geq\epsilon}=0$（或者 $\lim\limits_{n\rightarrow +\infty}P{|Y_n−c|<\epsilon}=1$），则称 $\{Y_n,n\geq 1\}$ **依概率收敛(Convergence in Probability)** 于 $Y$，记做 $Y_n→P_Y,n\rightarrow+\infty$。

特别地，当 $Y=c$ 为一常数时，称 $\{Y_n,n\geq 1\}$ 依概率收敛于常数 $c$。

- 这种收敛不是数学意义上的一般收敛，而是概率意义下的一种收敛；
- 其含义是：$Y_n$ 对 $Y$ 的绝对偏差不小于任何一个给定量的可能性随 $n$ 的增大而越来越小；或者绝对偏差 $|Y_n−Y|$ 小于任何一个给定量的可能性随 $n$ 的增大时而越来越接近于 1；

***
依概率收敛有如下重要**性质**：

若 $X_n\stackrel{P}{\rightarrow}a，Y_n\stackrel{P}{\rightarrow}b$，当 $n\rightarrow+\infty$ 时，函数 $g(x,y)$ 在点 $(a,b)$ 连续，则：$g(X_n,Y_n)\stackrel{P}{\rightarrow}g(a,b),n\rightarrow+\infty$；特别地，若 $X_n\stackrel{P}{\rightarrow}a$，$f(x)$ 在点 $a$ 连续，则：$f(X_n)\stackrel{P}{\rightarrow}f(a),n\rightarrow+\infty$
***
### 两个重要不等式

#### 马尔可夫（Markov）不等式

若随机变量 $Y$ 的 $k$ 阶（原点）矩存在（$k\geq 1$），即 $E(Y_k)$ 存在，则对 $\forall\epsilon>0$，均有：

$P\{|Y|\geq\epsilon\}\leq \frac{E(|Y|^k)}{\epsilon^k}\text{ or }P\{|Y|<\epsilon\}\geq 1−\frac{E(|Y|^k)}{\epsilon^k}$；特别地，当 $Y$ 取非负值的随机变量且它的 $k$ 阶矩存在时，有：$P\{Y\geq\epsilon\}\leq \frac{E(Y^k)}{\epsilon^k}$

---

#### 切比雪夫（Chebyshev）不等式

若随机变量 $X$ 具有数学期望 $E(X)=\mu$，方差 $Var(X)=\sigma^2$，则对 $\forall\epsilon>0$，均有：

$P\{|X−\mu|\geq\epsilon\}\leq\frac{\sigma^2}{\epsilon^2}\text{ or }P\{|X−μ|<\epsilon\}\geq 1−\frac{\sigma^2}{\epsilon^2}$

- 切比雪夫不等式是马尔可夫不等式的推论；
- 切比雪夫不等式应用范围更广，但是计算结果更粗糙；
