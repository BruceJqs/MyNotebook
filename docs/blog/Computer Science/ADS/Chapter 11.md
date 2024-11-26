---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 11 : Approximation

## Introduction

在上一章中我们介绍了 P/NP 问题，而大家普遍认为 $P \not= NP$，这就意味着对于某些问题，我们无法使用多项式时间解决，而在问题规模变大时，越发不可接受。

因此，我们考虑能否退而求其次，在多项式时间内求一个**比较优**的解。更具体的来说，我们尝试寻找一种多项式算法，使得其结果始终在关于准确解的可接受偏差范围内，对于这种算法，我们称之为**近似算法（Approximation Algorithm）**。

我们设 $f(n,x)$ 是对输入大小为 $n$ 的情况下，对结果 $x$ 的**最坏情况**的一个直观量化（例如 dist, weight...），若设 $x^∗$ 为准确解，$x$ 为给定算法结果，则我们定义**近似比（Approximation Ratio）**$\rho$：

$$
\forall n,\rho = \max\bigg\{\frac{f(n,x)}{f(n,x^*)},\frac{f(n,x^*)}{f(n,x)}\bigg\}
$$

则称给定算法为 $\rho$ 近似算法（$\rho$-approximation Algorithm）。
***
### Approximation Scheme

近似范式（Approximation Scheme）指的是对于某个优化问题的一族相同模式的算法，它们满足对于确定的 $\epsilon>0$，算法的近似比为 $1+\epsilon$。

>可以粗糙地理解为：“范式”是一个输出为算法的特殊函数，而 $\epsilon$ 是“范式”的一个参数，对于特定的 $\epsilon$，“范式”输出一个特定的算法（这些算法有着相同的模式），而这些“范式”输出的算法，都解决同一个问题，并且对于任意固定的 $\epsilon$ 其近似比为 $1+\epsilon$。
>
>而关于 $\epsilon>0$ 这个约束，是因为近似比必定大于 1。

而此时，这一族的算法的复杂度可以表示为 $O(f(n,\epsilon))$，如 $O(n^{\frac{2}{\epsilon}}),O((\frac{1}{\epsilon})^2n^3)$。当 $f(n,\epsilon)$ 关于 $n$ 是多项式时，我们称其为**多项式时间近似范式（Polynomial-time Approximation Scheme, PTAS）**，时间复杂度可以记为 $O(n^{f(\frac{1}{\epsilon})})$；当 $f(n,\epsilon)$ 关于 $n$ 和 $\frac{1}{\epsilon}$​ 都是多项式时，我们称其为**完全多项式时间近似范式（Fully Polynomial-Time Approximation Scheme, FPTAS）**，时间复杂度可以记为 $O(n^{O(1)}(\frac{1}{\epsilon})^{O(1)})$。

??? question "为什么要区分 PTAS 和 FPTAS？"

	我们观察 $\epsilon$ 对算法的影响：随着 $\epsilon$ 的减小，近似比逐渐变小，即准确度提高；而 $\frac{1}{\epsilon}$​ 变大，而通常来说 $\frac{1}{\epsilon}$​ 与算法复杂度都是正相关的，因此会导致算法复杂度升高。如果说这个近似范式是 FPTAS，那么为了提高准确度而缩小 $\epsilon$，导致的复杂度变化是相对可接受的（多项式级的变化，如 $(\frac{1}{\epsilon})^2n^3$ 关于 $\frac{1}{\epsilon}$​ 是多项式级的）；然而如果它不是 FPTAS，那么 $\epsilon$ 的缩小可能带来恐怖的复杂度增加（如 $n^{\frac{2}{\epsilon}}$ 关于 $\epsilon$ 是指数级的）。
***
## Examples

### Bin Packing

装箱问题指的是，给定 $N$ 个 item，第 $i\in[1,N]$ 个 item 的 size 为 $S_i\in(0,1]$，一个 bin 的大小为 1，尝试寻找最少的，能够装载所有 item 的 bin 的数量。

!!! example "Example"

	给定 7 个 item，size 分别为 0.2,0.5,0.4,0.7,0.1,0.3,0.8，则最少需要 3 个 bin（准确解）：
	
	- bin 1: 0.2+0.8;
	- bin 2: 0.7+0.3;
	- bin 3: 0.4+0.1+0.5;

这是一个 NP Hard 问题，我们一共有四种近似解法。需要注意的是，前三种都是在线（Online）解法，即处理 $item_i$ 时我们不知道 $item_{i+1}∼item_N$ 的情况。最后一个则是一种离线（Offline）解法，也就是我们知道所有 item 的情况以后再给出策略。

> 该问题的变种（决策问题）：给定 $K$ 个桶，我们能否装下 $N$ 个物品。这是个 NP Complete 问题。
***
#### Online Algorithm

!!! note "Online Algorithm"

	=== "Next Fit(NF)"
	
		NF 策略总是选择当前最后一个 bin，若能够容纳，则将当前 item 放入其中，否则新开一个 bin。
		
		```c title="Pseudo Code"
		void NextFit() {
		    read item1;
		    while (read item2) {
		        if (item2 can be packed in the same bin as item1)
		            place item2 in the bin;
		        else
		            create a new bin for item2;
		        item1 = item2;
		    } // end-while
		}
		```
		
		- 时间复杂度：$O(N)$
		- NF 策略总是使用不超过 $2M−1$ 个 bin，其中 $M$ 表示准确解的 bin 个数。因此该算法是一个 2-近似算法。
		
		!!! note "Proof"
		
			我们从 NF 的结果出发，证明当 NF 的结果为需要 $2M−1$ 或 $2M$ 个 bin 时，准确解为至少需要 $M$ 个 bin。
			
			假设 $S(B_i)$ 表示第 $i$ 个 bin 的 size，则根据 NF 的定义，有：$S(B_i)+S(B_{i+1})>1$（是 NF 的必要不充分条件）。稍作解释，使用反证法，假设 $S(B_i)+S(B_{i+1})\leq 1$，这说明无论 $B_{i+1}$​ 中有多少 item，都一定能放进 $B_i$​，而这与 NF “$B_i$​ 放不下了才开始放 $B_{i+1}$​” 的性质相违背。于是我们将所有桶两两配对：
			
			1.当 NF 的结果是需要 $2M−1$ 个 bin 时：
			
			$$
			\begin{cases}
			S(B_1)+S(B_2)>1\\
			S(B_3)+S(B_4)>1\\
			\vdots\\
			S(B_{2M-3})+S(B_{2M-2})>1\\
			S(B_{2M-1})\leq 1
			\end{cases}
			$$
			
			$$
			\begin{gather}
			\therefore\sum\limits_{i=1}^{2M-1}S(B_i)>\sum\limits_{i=1}^{2M-2}S(B_i)>M-1\\
			\therefore\sum\limits_{i=1}^{2M-1}S(B_i)\geq M
			\end{gather}
			$$
			
			即 item 的总 size 至少为 M，即至少需要 M 个 bin。
			
			2.而当 NF 的结果是需要 $2M$ 个 bin 时，可以转化为 $2M−1$ 的情况，至少需要 $M+1$ 个 bin。