---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 02 : Solutions of Equations in One Variable

> 这一整章核心要解决的问题就是如何求一个一元方程 $f(x)=0$ 的根，下面介绍了几种方法

## The Bisection Method

!!! note "Intermediate Value Theorem"

	介值定理：如果 $f\in C[a,b]$（$C$ 表示连续函数）且 $K$ 是介于 $f(a)$ 和 $f(b)$ 之间的任意值，那么存在一个数 $p\in (a,b)$，使得 $f(p)=K$
	
	![](../../../assets/Pasted image 20250227103955.png)

根据上面的介值定理，我们可以通过二分法，不断逼近真正的根，我们还有以下定理：

!!! note "Theorem"

	假设 $f\in C[a,b]$ 且满足 $f(a)⋅f(b)<0$，那么二分法将产生一个序列 ${p_n}(n=1,2,…)$，用于逼近 $f$ 的一个零点 $p$，并满足 $|p_n−p|\leq\frac{b−a}{2^n},n\geq 1$
	
	??? note "Proof"
	
		当 $n\geq 1$ 时，有 $b_n−a_n=\frac{1}{2^{n−1}}(b−a)\text{ and }p\in (a_n,b_n)$ 成立。
		
		因为 $n\geq 1$ 时，有 $p_n=\frac{1}{2}(a_n+b_n)$，所以 $|p_n−p|\leq\frac{1}{2}(b_n−a_n)=\frac{b−a}{2^n}$ 成立

在连续函数 $f$ 的区间 $[a,b]$ 上寻找 $f(x)=0$ 的解，其中 $f(a),f(b)$ 符号相反

- 输入：端点 $a,b$；容忍值（Tolerance）TOL；最大迭代次数 $N_{\max}$
- 输出：$p$ 的近似解或失败信息

```c title="Bisection Method.c"
Step 1  Set i = 1;
            FA = f(a);
Step 2  while (i <= N_max) do steps 3-6
        Step 3  Set p = a + (b - a) / 2;  /*computer p_i*/
                FP = f(p);
        Step 4  if (FP == 0) or (b - a) / 2 < TOL then Output(p);
                STOP;  /*successful*/
        Step 5  Set i++;
        Step 6  if sign(FA) * sign(FP) > 0 then Set a = p; FA = FP;
                else set b = p;  /*update a_i, b_i*/
Step 7  Output(Method failed after N_max iterations);  /*unsuccessful*/
		Stop.
```

!!! question "Question"

	=== "Question"
	
		在 Step 3 当中，为什么不是 `p = (a + b) / 2`；在 Step 6 当中，为什么不是 `FA * FP > 0`
	
	=== "Answer"
	
		两个问题的答案是一致的，是为了防止溢出（Overflow），无论是 `a + b` 还是 `FA * FP`，如果它们的符号一致，且数值特别大的时候，它们的和或积可能是计算机无法表示出来的东西，也就是产生了溢出的问题，此时该算法可能返回的是一个意料之外的结果，而不产生报错
		
		另外对于 Step 3 有特殊的一点，如果 $a$ 和 $b$ 都是很小的数，相加可能会产生舍入误差。用 `a+(b-a)/2` 可以确保 $p$ 落在 $a$ 和 $b$ 之间
		
		例如，用截断保留 2 位有效数字，$a=0.91$，$b=0.93$，$(a+b)/2=1.8/2=0.9$，而 $a+(b-a)/2=0.91+(0.93-0.91)/2=0.92$

对于二分法来说，其优点在于：

- 该方法简单，只要求函数 $f$ 是连续的
- 结果总是会收敛到真正的解

但其缺点在于：

- 收敛速度过慢，并且在计算过程中，更好的中间值近似可能在不经意间被抛弃掉了
- 不适用于寻找多根和复数根的情况

!!! tip "Tips"

	实际上，我们可以在使用二分法之前先画一幅 $f(x)$ 的草图，观察二分法是否可行，或者用一个子程序将完整的区间划分为多个子区间 $[a_k,b_k]$，这样的话即使 $f(a)⋅f(b)$，也可以保证 $f(a_k)⋅f(b_k)<0$
***
## Fixed-Point Iteration

不动点迭代方法将 $f(x)$ 的根看成一个函数 $g(x)$ 的不动点，即 $f(x)=0\stackrel{\text{equivalent}}{\Leftrightarrow}x=g(x)$

基本思路是：从初始的近似值 $p_0$ 开始，通过 $p_n=g(p_{n−1})$（其中 $n\geq 1$），产生序列 $\{p_n\}_{n=0}^{\infty}​$。如果该序列能收敛到 $p$，且 $g$ 是一个连续函数，那么：

$$
p=\lim\limits_{n\rightarrow\infty}p_n=\lim\limits_{n\rightarrow\infty}g(p_{n-1})=g(\lim\limits_{n\rightarrow\infty}p_{n-1})=g(p)
$$

!!! question "这个方法适用所有方法吗？"

	看起来貌似只需要不断的迭代，我们总能找到解。但实际上，并不是所有的 $g(x)$ 都能做到让序列收敛，具体来看下面几个例子：
	
	!!! example "Example"
	
		=== "Question"
		
			判断以下几种 $g(x)$ 中，哪个能做到收敛，为什么？
			
			![](../../../assets/Pasted image 20250227111421.png)
		
		=== "Answer"
		
			想必高中应该都被蛛网图祸害过吧（bushi）
			
			![](../../../assets/Pasted image 20250227111618.png)

那么怎样才能准确判断 $g(x)$ 能让序列收敛有不动点呢？我们有定理如下：

!!! note "Fixed-Point Theorem"

	- 令 $g\in C[a,b]$，且满足 $\forall x\in [a,b]$，有 $g(x)\in [a,b]$，那么 $g$ 在 $[a,b]$ 上有不动点
	- 一阶导函数 $g'$ 存在于区间 $(a,b)$，且满足 $\forall x\in (a,b)$，$\exists$ 常数 $k\in (0,1)$ 使得 $|g'(x)|\leq k$ 成立，那么该不动点是唯一的，且 $\forall p_0\in [a,b]$，由 $p_n=g(p_{n−1}),n\geq 1$ 定义的序列会收敛到位于区间 $[a,b]$ 上的唯一不动点。
	
	??? note "Proof"
	
		- “不动点”：令 $f(x)=g(x)−x$，因为 $a\leq g(x)\leq b$，所以 $f(a)=g(a)−a\geq 0$ 且 $f(b)=g(b)−b\leq 0$。由介值定理知，$f$ 一定有一个根，因此 $g$ 有一个不动点
		- “唯一”：（用反证法证明）
			- 假设 $p,q$ 都是 $g$ 在区间 $[a,b]$ 上的两个不同的不动点
			- 根据均值定理（Mean Value Theorem），存在一个位于 $p,q$ 的数 $\xi$，满足 $g(p)−g(q)=g'(\xi)(p−q)$
			- 因为 $g(p)=p,g(q)=q$，所以可以得到 $(1−g'(\xi))(p−q)=0$，和已知条件矛盾，因此假设不成立，即“不动点是唯一的”结论成立
		- “收敛”：即证明 $\lim\limits_{⁡n\rightarrow\infty}|p_n−p|=0$
			- 因为 $\forall x\in [a,b]$，$g(x)\in [a,b]$，所以 $\forall n\geq 0$，$p_n$ 都是有定义的
			- 因此：
				
				$$
				\begin{aligned}
				∣p_n−p∣&=∣g(p_{n−1})−g(p)∣=∣g'(\xi)∣∣p_{n−1}−p∣\leq k∣p_{n−1}−p∣\\
				& \leq k^2∣p_{n−2}−p∣\leq...\leq k^n∣p_0−p∣
				\end{aligned}
				$$
				
			- 根据条件，$k∈(0,1)$，所以 $k^n\rightarrow 0$，因此 $\lim\limits_{n\rightarrow\infty}|p_n-p|=0$ 成立

!!! note "推论"

	如果 $g$ 满足不动点定理的假设，那么用 $p_n​$（$\forall n\geq 1$）近似表示 $p$ 所产生的误差边界为：
	
	$$
	|p_n−p|\leq\frac{1}{1−k}|p_{n+1}−p_n|\text{ and }|p_n−p|\leq\frac{k^n}{1−k}|p_1−p_0|
	$$
	
	??? note "Proof"
	
		- $|p_{n+1}−p_n|\geq |p_n−p|−|p_{n+1}−p|\geq|p_n−p|−k|p_n−p|$
		- $|p_{n+1}−p_n|=|g(x_n)−g(x_{n−1})|=|g'(\xi_n)(p_n−p_{n−1})|\leq k|p_n−p_{n−1}|\leq ... \leq k^n|p_1−p_0|$
	
	这两个不等式，前者可以用来控制计算的精度，而后者说明了 $k$ 越小收敛速度越快

给定一个初始近似值 $p_0$，找到 $p=g(p)$ 的一个解。

- 输入：初始近似值 $p_0​$；容忍值 TOL；最大迭代次数 $N_{\max}$
- 输出：近似解 $p$ 或错误信息

```c title="Fixed-Point Iteration.c"
Step 1  Set i = 1;
Step 2  while (i <= N_max) do steps 3-6
        Step 3  Set p = g(p_0);  /*compute p_i*/
        Step 4  if |p - p_0| < TOL then Output(p);  /*successful*/
            STOP;
        Step 5  Set i++;
        Step 6  Set p_0 = p;  /*update p_0*/
Step 7  Output(The method failed after N_max iterations);  /*unsuccessful*/
```

!!! example "例题"

	=== "Question"
	
		使用以下 $p_0=1.5$ 的等价不动点形式在 $[1,2]$ 中找到方程 $x^3+4x^2–10=0$ 的唯一根，哪一种方式是最好的？（根的准确值约为 $1.365230013$）
		
		![](../../../assets/Pasted image 20250228010444.png)
	
	=== "Answer"
	
		如果无脑迭代的话，会得到以下结果：
		
		![](../../../assets/Pasted image 20250227133802.png)
		
		可以看到 $a,b$ 不符合要求，而 $c,d,e$ 都可以迭代下去。$a,b$ 不符合的原因分别是一个不收敛，另一个出现对负数开根号的情况。但即使是可以迭代的 $c,d,e$，也有一些小小的差别：
		
		- c：在区间 $[1,1.5]$ 时，$k\approx 0.66$
		- d：$k\approx 0.15$
		- e：$k$ 更小，表现最好
***
## Newton's Method

牛顿法的基本思想即使用泰勒展开（Taylor's Expansion）来线性化一个非线性的函数

具体来说，令 $p_0\in [a,b]$ 为 $p$ 的一个近似值，满足 $f'(p)\not=0$。考虑以下 $f(x)$ 关于 $p_0$ 的泰勒多项式：

$$
f(x)=f(p_0)+f'(p_0)(x−p_0)+\frac{f''(\xi_x)}{2!}(x−p_0)^2\text{ where }\xi_x\text{ lies between }p_0\text{ and }x
$$

假设 $|p−p_0|$ 很小，那么 $(p−p_0)^2$ 会更小，有：

$$
0=f(p)\approx f(p_0)+f'(p_0)(p−p_0)\Rightarrow p\approx p_0−\frac{f(p_0)}{f'(p_0)}
$$

我们不难得到以下递推关系式：

$$
p_n=p_{n−1}−\frac{f(p_{n−1})}{f'(p_{n−1})}\text{ for }n\geq 1
$$

!!! note "Theorem"

	令 $f\in C^2[a,b]$（即函数具有二阶连续导数）。如果 $p\in [a,b]$ 满足 $f(p)=0$ 且 $f'(p)\not=0$，那么存在一个 $\delta>0$，使得牛顿法产生一个序列 $\{p_n\}(n=1,2,…)$，对任意近似值 $p_0\in [p−\delta,p+\delta]$，该序列收敛于 $p$
	
	??? note "Proof"
	
		牛顿法就是：$p_n=g(p_{n−1}),n\geq 1$，满足 $g(x)=x−\frac{f(x)}{f'(x)}$。我们需要回答以下问题：
		
		- $g(x)$ 是否在 $p$ 的邻近区域内连续
		    - 因为 $f'(p)\not=0$ 且连续，所以在 $p$ 的邻近区域内，$f'(x)\not=0$
		- $g'(x)$ 是否在 $p$ 的邻近区域内被 $0<k<1$ 约束
		    - 因为 $g'(x)=\frac{f(x)f''(x)}{[f'(x)]^2}$，所以 $g'(p)=0$
		    - 又因为 $f''(x)$ 连续，所以 $g'(x)$ 很小，且在 $p$ 的邻近区域内连续
		- $g(x)$ 是否将 $[p−\delta,p+\delta]$ 映射到自身
			- $|g(x)−p|=|g(x)−g(p)|=|g'(\xi)||x−p|\leq k|x−p|<|x−p|<\delta$

!!! warning "注意"

	牛顿法的收敛性取决于初始近似值的选择。如下图所示，如果选择不当的话，牛顿法就会失效：
	
	![](../../../assets/Pasted image 20250227213636.png)
***
## Error Analysis for Iterative Methods

假设 $\{p_n\}_{n=0}^\infty$ 收敛于 $p$，其中对 $\forall p_n \neq p$。如果存在正数 $\lambda$ 和 $\alpha$，使得：

$$
\lim_{n\to\infty}\frac{|p_{n+1}-p|}{|p_n-p|^\alpha} = \lambda
$$

则称 $\{p_n\}_{n=0}^\infty$ 是 $\alpha$ 阶收敛的（Converges to p of Order $\alpha$），$\lambda$ 称为**渐进误差常数**（Asymptotic Error Constant）

- $\alpha$ 值越大，收敛速度越快
	- 如果 $\alpha=1$，则该序列是**线性收敛**的（Linearly Convergent）
	- 如果 $\alpha=2$，则该序列是**二次收敛**的（Quadratically Convergent）
***
### Fixed-Point Iteration

我们有不动点法的收敛阶和渐进误差常数：

$$
\begin{aligned}
p_{n+1}-p = g(p_n)-g(p) = g'(\xi)(p_n-p) &\Rightarrow \frac{|p_{n+1}-p|}{|p_n-p|} = |g'(\xi)|\\
&\Rightarrow \lim_{n\to\infty}\frac{|p_{n+1}-p|}{|p_n-p|} = \lim_{n\to\infty}|g'(\xi)| = |g'(p)|
\end{aligned}
$$

因此，如果$g'(p)\neq 0$，则不动点迭代法是线性收敛的，且渐进误差常数为$|g'(p)|$
***
### Newton's Method

由泰勒展开，我们有牛顿迭代法的收敛阶和渐进误差常数：

$$
\begin{aligned}
0 &= f(p) = f(p_n) + f'(p_n)(p-p_n) + \frac{f''(\xi)}{2}(p-p_n)^2\\
&\Rightarrow p =     p_n-\frac{f(p_n)}{f'(p_n)} - \frac{f''(\xi)}{2f'(p_n)}(p-p_n)^2\\
&\Rightarrow \lim_{n\to\infty}\frac{|p_{n+1}-p|}{|p_n-p|^2} = \lim_{n\to\infty}\frac{|f''(\xi)|}{2|f'(p_n)|} = \frac{|f''(p)|}{2|f'(p)|}
\end{aligned}
$$

因此，牛顿迭代法是二次收敛的，且渐进误差常数为$\frac{|f''(p)|}{2|f'(p)|}$

!!! question "我们如何一般性地求出 $\alpha$ 和 $\lambda$ ？"

	我们有如下定理：令 $p$ 是 $g(x)$ 的不动点。如果存在一些常量 $\alpha\geq 2$，使得 $g\in C^\alpha[p−\delta,p+\delta]$，<font color="red">$g'(p)=...=g^{(\alpha−1)}(p)=0$</font> 且 $g^{(\alpha)}(p)\not=0$。那么关于 $p_n=g(p_{n−1}),n\geq 1$ 的迭代是 $α$ 阶收敛的
	
	??? note "Proof"
	
		$$
		p_{n+1}=g(p_n))=\underbrace{g(p)}_{=p}+\frac{g'(p)}{1!}(p_n-p)+...+\underbrace{\frac{g^{(\alpha)}(\xi_n)}{\alpha!}}_{=\lambda(n\rightarrow\infty)}(p_n-p)^\alpha
		$$
		

!!! question "如果根**不是**简单的，那么牛顿法的收敛阶数是多少？"

	如果 $p$ 是 $f$ 中的一个根，且重数（Multiplicity）为 $m$，那么 $f(x)=(x-p)^mq(x)$ 且 $q(p)\not=0$
	
	根据牛顿法，$p_n=g(p_{n-1})\text{ for }n\geq 1\text{ with }g(x)=x-\frac{f(x)}{f'(x)}$，得到：
	
	$$
	\begin{align*}
	g'(x) &= 1-\frac{f'(x)^2-f(x)f''(x)}{(f'(x))^2} = \frac{f(x)f''(x)}{(f'(x))^2} \\
	&= \frac{(x-p)^mq(x)(m(m-1)(x-p)^{m-2}q(x)+2m(x-p)^{m-1}q'(x)+q''(x)(x-p)^m)}{(m(x-p)^{m-1}q(x)+q'(x)(x-p)^m)^2} \\
	&= \frac{(x-p)^{2m-2}q(x)(m(m-1)q(x)+2m(x-p)q'(x)+q''(x)(x-p)^2)}{(x-p)^{2m-2}(mq(x)+q'(x)(x-p))^2} \\
	&= \frac{q(x)(m(m-1)q(x)+2m(x-p)q'(x)+q''(x)(x-p)^2)}{(mq(x)+q'(x)(x-p))^2}
	\end{align*}
	$$
	
	所以 $g'(p)=\frac{q(p)m(m-1)q(p)}{(mq(p))^2}=1-\frac{1}{m}<1$，此时牛顿法收敛，但不是二次收敛
***
幸运的是，存在一种可以加快收敛速度的方法：将有重根的 $f$ 转换为等价的另一个有**简单根**的函数，在这个新的函数上使用牛顿法。具体来说，定义 $\mu(x)=\frac{f(x)}{f'(x)}$

如果 $p$ 是 $f$ 的 $m$ 重零点，$f(x)=(x-p)^mq(x)$，则

$$\mu(x)=\frac{(x-p)^mq(x)}{m(x-p)^{m-1}q(x)+q'(x)(x-p)^m}=\frac{(x-p)q(x)}{mq(x)+q'(x)(x-p)}$$

又因为 $q(p)\neq 0$，且

$$\frac{q(p)}{mq(p)+q'(p)(p-p)}=\frac{1}{m}\neq 0$$

所以 $p$ 是 $\mu(x)$ 的单根，那么我们对 $\mu$ 应用牛顿迭代法，就有

$$
\begin{align*}
p_{n+1}=g(p_n) &= p_n-\frac{\mu(p_n)}{\mu'(p_n)} \\
&= p_n-\frac{\frac{f(p_n)}{f'(p_n)}}{\frac{f'(p_n)f'(p_n)-f(p_n)f''(p_n)}{(f'(p_n))^2}} \\
&= p_n-\frac{f(p_n)f'(p_n)}{f'(p_n)^2-f(p_n)f''(p_n)} \\
\end{align*}
$$

这就是让有多重根的牛顿法二次收敛的方法，但是其也有优劣：

- 优点：二次收敛，收敛速度快
- 缺点：
	- 计算量大，因为需要计算 $f'(x)$ 和 $f''(x)$
	- 分母由两个接近于 0 的数相减，会引起严重的舍入误差
***
## Accelerating Convergence

### Aitken's $\Delta^2$ Process

!!! note "Definition"

	对于给定的序列，向前差分（Forward Difference）定义为 $\Delta p_n = p_{n+1}-p_n$，对于更高的幂，我们有 $\Delta^k p_n = \Delta(\Delta^{k-1}p_n)$，比如 $\Delta^2 p_n = \Delta(\Delta p_n)= \Delta(p_{n+1}-p_n) = (p_{n+2}-p_{n+1}) -(p_{n+1}-p_n)$

假设 $\{p_n\}_{n=0}^\infty$ 是线性收敛的，其极限为 $p$，为了便于构造比$\{p_n\}_{n=0}^\infty$收敛更快的序列$\{\hat{p}_n\}_{n=0}^\infty$，我们假设$p_n-p, p_{n+1}-p, p_{n+2}-p$的符号一致，又假设$n$足够大，有

$$
\frac{p_{n+1}-p}{p_n-p} \approx \frac{p_{n+2}-p}{p_{n+1}-p}
$$

从而

$$
p_{n+1}^2-2p_{n+1}p+p^2 \approx p_{n+2}p_n-(p_n+p_{n+2})p+p^2
$$

解出 $p$，得到：

$$
p \approx \frac{p_{n+2}p_{n}-p_{n+1}^2}{p_{n+2}-2p_{n+1}+p_n} \approx p_n - \frac{(p_{n+1}-p_n)^2}{p_{n+2}-2p_{n+1}+p_n}
$$

于是，我们可以构造序列$\{\hat{p}_n\}_{n=0}^\infty$，其中

$$
\hat{p}_n = p_n - \frac{(p_{n+1}-p_n)^2}{p_{n+2}-2p_{n+1}+p_n}=p_n -\frac{(\Delta p_n)^2}{\Delta^2 p_n}
$$

这样定义序列的方法就是 AITKEN$\Delta^2$ 法

!!! question "为什么这样的序列收敛更快？"

	我们有如下定理：假设序列 $\{p_n\}(n=1,2,...)$ 线性收敛到 $p$；且对于充分大的数 $n$，有 $(p_{n+1}-p)(p_n-p)>0$，则 $\{\hat{p}_n\}(n=1,2,...)$ 收敛到 $p$ 的速度快于 $\{p_n\}(n=1,2,...)$，即：
	
	$$
	\lim_{n\to\infty}\frac{\hat{p}_n-p}{p_n-p} = 0
	$$
	

!!! question "如何迭代？"

	其实还是用序列本身的迭代法，不过在计算值的时候采取了AITKEN$\Delta^2$法。
	
    构造按如下顺序：
	
    $$
    \begin{aligned}
    p_0, p_1 &= g(p_0), p_2 = g(p_1)  \\
    \hat{p_0} &= \{\Delta^2\}(p_0)\\
    p_3 &= g(p_2) \\
    \hat{p_1} &= \{\Delta^2\}(p_1)\\
    \vdots
    \end{aligned}
    $$
    
*** 
### Steffensen's Method

> 若 $g'(p)\not=1$，那么可以做到**局部二次收敛**。

这个方法假设 $\hat{p_0}$ 比 $p_2$ 更好地逼近 $p$，从而把上述过程第三行的不动点迭代应用到 $\hat{p_0}$ 上

$$
\begin{aligned}
p_0^{(0)}, p_1^{(0)} &= g(p_0^{(0)}), p_2^{(0)} = g(p_2^{(0)})  \\
p_0^{(1)} &= \{\Delta^2\}(p_0^{(0)}),p_1^{(1)} = \{\Delta^2\}(p_0^{(1)}),p_2^{(1)} = \{\Delta^2\}(p_1^{(1)}) \\
p_0^{(2)} &= \{\Delta^2\}(p_0^{(1)}) \\
&\vdots
\end{aligned}
$$



