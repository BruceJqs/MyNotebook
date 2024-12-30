---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 07 : Divide and Conquer

## Introduction

>分治法(Divide-and-conquer algorithm)属于一种算法范型，它的基本思想是将一个问题分解为若干个规模较小的相同问题，然后递归地解决这些子问题，最后将这些子问题的解合并得到原问题的解，一个比较经典的案例就是归并排序和快速排序。

!!! Example "Closest Points Problem"

	二维最近点问题(Closest Points Problem)，指的是给定平面上的 n 个点，找出其中距离最近的两个点。
	
	=== "朴素方法"
	
		最朴素的做法当然是枚举所有的点对，一共需要 $C_N^2=\frac{N(N−1)}{2}$​ 即复杂度为 $O(N^2)$。
	
	=== "分治方法"
	
		现在我们类比最大子序列和问题的分治做法。
		
		!!! note "最大子序列和的分治做法"
		
			1. 将序列分为左右两部分，分别求解最大子序列和；
			2. 求解跨越中点的最大子序列和；
			3. 比较三者的大小，取最大值；
		
		我们可以将整个平面分为两个部分，即如图中绿色线将点对划分为两个部分。
		
		![](../../../assets/Pasted image 20241029105248.png)
		
		接下来我们同样分为这么三步：
		
		1. 将点对分为左右两部分，分别求解最近点对；
		2. 寻找跨越分界线的点对，从中寻找最近点对；
		3. 比较三者的大小，取最小值；
		
		显然，我们现在需要解决的就是要如何设计第二步的实现，以求更优的复杂度。
		
		首先我们假设在第一步中，我们求得两边求得的最小距离中较小的那个为 $\delta$，换句话来说，如果答案在第二步中被更新，那么它的距离需要小于 $\delta$。而我们知道，在第二步中被拿出来的点对，一定是一个在分界线左侧一个在分界线 L 右侧。朴素的来想，在距离分界线 $\delta$ 以外的点对中，我们是不需要考虑的。而在距离分界线 $\delta$ 以内的点，都存在成为答案点对的可能。
		
		![](../../../assets/Pasted image 20241029105421.png)
		
		如图，现在我们知道，只有落在两条深绿色之间的点才可能会更新答案。
		
		现在我们需要做的是，从分界线左侧的区域里拿一个点，和分界线右边的一个点做匹配，然后取所有结果中的最小点。不过这件事仍然可以优化——在二维的数据中，仅对 x 纬度做约束往往会导致事情变得不那么稳定，所以我们同样考虑在 y 方向做约束。
		
		也是基于范围约束的考虑。我们先对于两条深绿色之间的点关于 y 坐标从上到下排序，并且用一个宽为 $\delta$ 的分割线去划分区域，对于每个点，我们仅计算位于该点下方且距离该点小于等于 $\delta$ 的点和它之间的距离。
		
		因此，对于选定点 $p_{l_i}$，其所有可能导致答案更新的点都被框定在一个 $2\delta\times\delta$ 的矩形中。
		
		而更奇妙的是，这个由参数 $\delta$ 指定的矩形，巧妙地约束了落在矩形中的点的最大数量。
		
		![](../../../assets/Pasted image 20241029110835.png)
		
		在这样一个区域中，我们需要约束所有落在 $\delta\times\delta$ 的 L 区域中的点，互相的距离都大于等于 $\delta$（因为如果小于 $\delta$ 的话 $\delta$ 就不应该是当前这个数了应该是更小的这个值），对 R 区域中的点也有相同的约束。不难发现，在最理想最理想的情况下——闭区间、允许点重合的情况下，这个矩形最多也只能放八个点（两边各四个）：
		
		![](../../../assets/Pasted image 20241029111708.png)
		
		而更一般的情况下，最多也只能放六个点（两边各三个）。（这便是最坏的情况，也就是说在其他情况下这样的矩形内是塞不下更多的点的）
		
		因此我们可以得到结论，在这种情况下，对于每一个选定的 $p_{l_i}$，寻找其可能导致答案更新的点的复杂度都是常数级的。
		
		而枚举这些“选定点”，也就是枚举 $p_{l_i}$，其复杂度（撑死）是 $O(N)$。
		
		于是我们能得到这个分治的时间复杂度计算递推公式：
		
		$$
		T(N)=2T(\frac{N}{2})+O(N)=O(N\log N)
		$$
		

## Solving Recurrences

在开始接下来的内容之前，我们需要给出更一般的，我们想要解决的问题，即求解时间复杂度递推公式形如下式的算法的时间复杂度：

$$
T(N)=aT(\frac{N}{b})+f(N),a,b\in\mathbb{Z}^+
$$

例如，上面的最近点对问题，就是 $a=2,b=2,f(N)=O(N)$ 的情况。
***
### Substitution Method

> 代换法（Substitution Method）的思路非常直白，首先我们通过某些手段（~~比如大眼观察法👀~~）来得到一个预设的结果，接下来通过代入、归纳的方法来证明这个结果。

简单来说，就是大胆猜测，小心求证（先猜后证）！

!!! Example

	=== "Question"
	
		求解复杂度：
		
		$$
		T(N)=2T(\frac{N}{2})+N
		$$
		
	
	=== "Answer"
	
		大胆猜测 $T(N)=O(N\log N)$
		
		对于足够小的 $m<N$，有：
		
		$$
		T(\frac{m}{2})=O(\frac{m}{2}\log\frac{m}{2})\leq c\frac{m}{2}\log\frac{m}{2}
		$$
		
		将上式代入得：
		
		$$
		T(m)=2T(\frac{m}{2})+m\leq c\frac{m}{2}\log\frac{m}{2}+m\leq cm\log m\text{ for }c\geq 1
		$$
		
		对于足够小的 $m=2$ 式子就可以成立，由归纳法得结论成立
		
		!!! failure "错误的猜测"
		
			如果我们猜测 $T(N)=O(N)$，那么会有以下证明：

			- 假设对于 $m<N$，该结论成立
			- 取 $m=\lfloor\frac{N}{2}\rfloor$，那么存在一个常数 $c>0$，使得$T(\lfloor\frac{N}{2}\rfloor)≤c\lfloor\frac{N}{2}\rfloor$
			    
			- 将这个式子代入递推公式，得：
			
			$$
			T(N)=2T(\lfloor\frac{N}{2}\rfloor)+N\leq 2c\lfloor\frac{N}{2}\rfloor+N\leq cN+N=O(N)
			$$
			
			这样的证明看起来没什么问题，但错误发生在最后一个不等式上：我们得到了 $cN+N=(c+1)N$，虽然它的时间复杂度确实是 $O(N)$，但在形式上它是错误的，因为我们预先假设正确的结论是 $T(m)≤cm$，要根据这个条件证明出 $T(N)≤cN$，而不是 $(c+1)N$。换句话说，我们必须证明出**精确的形式**，连常数也必须保持一致。

不过很显然，在某些情况下我们求证了一个复杂度的假设成立，但它并不一定足够紧，这是猜解法的通病。

!!! tip "小技巧"

	- 如果时间复杂度的递推关系式中出现类似 $T(\sqrt{N})$ 等形式，可以考虑**换元法**：
	    - 令 $m=\log⁡ n$，那么 $T(\sqrt{n})=T(2^{\frac{m}{2}}),T(n)=T(2^m)$
	    - 再令 $S(m)=T(2^m)$，那么 $S(\frac{m}{2})=T(2^{\frac{m}{2}})$，这样整个递推关系式就被转化为一般的形式了
	- 如果出现形如 $T(f(N)+c)$ 的形式（$c$ 为常数），由于 $N$ 足够大，因此可以忽略常数 $c$
***
### Recursion-tree Method

>递归树法(Recursion-tree Method)的思路是，我们通过画出递归树来分析算法的时间复杂度，实际上和直接数学推理的区别不是很大，主要就是通过观察递归过程中数据增长的模式来进行分析。

就类似于直接展开式子，只不过通过树状图的形式或许更加直观。

对于一个递推式，我们将它不断展开以后，其形式大概会是这样：

$$
T(N)=...=\underbrace{\sum\limits_{leaf_i}^{leaves}T(N_{leaf_i})}_{conquer}+\underbrace{\sum\limits_{node_i}^{non-leaf-nodes}f(N_{node_i})}_{combine}
$$

其中，由于末端子问题的规模一般都足够小，可以认为 $T(N_{leaf_i})$ 都是常数，于是上式又可以变化为：

$$
T(N)=...=\underbrace{cN_{leaves}}_{conquer}+\underbrace{\sum\limits_{node_i}^{non-leaf-nodes}f(N_{node_i})}_{combine}
$$

具体来说解释其含义，combine 部分就是在每一次“分治”的处理时间，如合并当前的子问题分治后的结果，体现在递推式的 $f(N)$ 部分；而 conquer 部分指的是当“分治”的“治”在“分”的末端的体现，即对于足够小的规模的问题，不再需要继续“分”的时候，对其处理的开销。

实际上在代码层面这两部分可能区别不大（可能就是一个分支的事情），不过在数学意义上，对于一个递推式子求解我们一般是需要“首项”的，或者说是“最底层”的，而这个“最底层”的部分就是 conquer 部分。

!!! Example

	![](../../../assets/Pasted image 20241029114339.png)
	
	!!! note "对于 $3^{\log_{4}N}=N^{\log_{4}3}$ 的证明"
	
		一般化这个问题，我们有 $a^{\log_{b}N}=e^{\frac{\ln N}{\ln b}\ln a}=e^{\frac{\ln a}{\ln b}\ln N}=N^{\log_{b}a}$
	
	可以发现，此情况下 $a=3,b=4,f(N)=\Theta(N^2)$，也就是说每次分为 3 个子问题，子问题的规模是 $\frac{N}{4}$​，而合并开销为 $\Theta(N^2)$。
	
	此时由于分治的策略是相对均匀的，所以我们可以认为得到的是一个完美三叉树。
	
	显然，树高为 $\log_{⁡4}N$，根记为 0，每个分治节点的 combine 开销已经标注在图的节点位置，横向箭头标记的是对该层所有节点的开销的求和。特别的，对于最底层，即叶子层，它表示的是 conquer 部分的开销。
	
	于是我们可以根据 $T(N)=...=\underbrace{cN_{leaves}}_{conquer}+\underbrace{\sum\limits_{node_i}^{non-leaf-nodes}f(N_{node_i})}_{combine}$ 的形式，对其进行求和，得到图片中下方的式子。
	
	最后我们有：
	
	$$
	\begin{aligned}
	T(N)​&=\sum\limits_{i=0}^{\log_{4}^​N−1}​(\frac{3}{16}​)^icN^2+\Theta(N^{\log_{4}​3})\\
	&<\sum\limits_{i=0}^{+\infty}​(\frac{3}{16}​)^icN^2+\Theta(N^{\log_{4​}3})\\
	&=\frac{cN^2}{​1−\frac{3}{16}​}+\Theta(N^{\log_{4}​3})=O(N^2)
	\end{aligned}​
	$$
	
	- 第 2 行到第 3 行的等式中，用到了一个常用的幂级数展开公式：
	
	$$
	\frac{1}{1−x}=\sum\limits_{n=0}^{+\infty}x^n,∣x∣<1
	$$
    
***
### Master Method

> 主方法(Master Method)之所以叫“主”，是因为它分析的是 combine 和 conquer 部分孰为主导。

需要注意的是，主定理并不是万金油，它没有覆盖所有的情况。
***
#### Form 1

!!! note "Form 1"

	对于形如 $T(N)=aT(\frac{N}{b})+f(N)$ 的递推式：
	
	1. 若 $f(N)=O(N^{\log_{⁡b}a−\epsilon}),\text{ for }\epsilon>0$，那么 $T(N)=\Theta(N^{\log_{⁡b}a})$；
	2. 若 $f(N)=\Theta(N^{\log_{⁡b}a})$，那么 $T(N)=\Theta(N^{\log_{b}a}\log ⁡N)$；
	3. 若 $f(N)=\Omega(N^{log⁡_{b}a+\epsilon}),\text{ for }\epsilon>0$ 且 $af(\frac{N}{b})<cf(N),\text{ for }c<1\text{ and }\forall N>N_0$，那么 $T(N)=\Theta(f(N))$；
	
	其中 $af(\frac{N}{b})<cf(N),\text{ for }c<1\text{ and }\forall N>N_0$ 又叫 Regularity Condition.

观察三种情况的区分条件都是比较 $f(N)$（每一次的 combine 开销） 和 $N^{\log⁡_b a}$（即求和式中的 conquer 的开销），当 $f(N)$ 足够小时，以 conquer 开销为主（即 Case 1）；当足够大时，以 combine 为主（即 Case 3）；而其中还有一个中间状态（即 Case 2）。

!!! Example "Examples of Form 1"

	=== "Example 01"
	
		- $a=b=2,f(N)=N$；
			- $f(N)=N=\Theta(N^{\log_{⁡2}2})$，适用于情况 2；
			- 因此得到结果 $T(N)=\Theta(N\log ⁡N)$；
	
	=== "Example 02"
	
		- $a=b=2,f(N)=N\log ⁡N$；
			- $f(N)=N\log ⁡N$，虽然 $N\log ⁡N=\Theta(N^{\log_{2}2})$，但是 $N\log⁡ N\not=\Theta(N^{\log⁡_{2} 2+\epsilon})$，所以不适用于情况 3；
			- 具体来说，$\lim\limits_{⁡N\rightarrow\infty}\frac{N\log ⁡N}{N^{1+\epsilon}}=\lim\limits_{⁡N\rightarrow\infty}\frac{\log ⁡N}{N^\epsilon}=0\text{ for fixed }\epsilon>0$；
			- 这个例子体现出了 $\epsilon$ 的一定作用；

!!! note "Proof of Form 1"

	对于形如 $T(N)=aT(\frac{N}{b})+f(N)$ 的递推式，我们需要依次证明，此处我们使用递归树法进行证明。

	=== "Case 1"
	
		树高 $\log_⁡{b}N$，共 $\log_⁡{b}N+1$ 层，则有：
		
		- 第 0 层（根）一共 1 项，combine 的开销为 $f(N)$；
		- 第 1 层一共 a 项，combine 的开销为 $a×f(\frac{N}{b})$；
		- 第 2 层一共 $a^2$ 项，combine 的开销为 $a^2×f(\frac{N}{b^2})$；
		- ......
		- 第 j 层一共 $a^j$ 项，combine 的开销为 $a^j×f(\frac{N}{b^j})$；
		- ......
		- 第 $\log_{⁡b}N−1$ 层一共 $a^{\log_{⁡b}N−1}$ 项，combine 的开销为 $a^{\log_{b}N−1}×f(\frac{N}{b^{\log_{b}N−1}})$；
		- 第 $\log_{⁡b}N$ 层，即为叶子层，一共 $a^{\log_{b}N}=N^{\log_{b}a}$ 项，conquer 的开销为 $N^{\log_⁡{b} a}×\Theta(1)=\Theta(N^{\log_{⁡b}a})$；
		
		得到求和式：
		
		$$
		T(N)=\Theta(N^{\log_{b}a})+\sum\limits_{j=0}^{\log_{b}N-1}a^jf(\frac{N}{b^j})
		$$
		
		而我们有条件 $f(N)=O(N^{\log_{b}a−\epsilon}),\text{ for }\epsilon>0$，将它代入到上式中得到：
		
		$$
		\begin{aligned}
		T(N)&=\Theta(N^{\log_{b}a})+\sum\limits_{j=0}^{\log_{b}N-1}a^jO((\frac{N}{b^j})^{\log_{b}a-\epsilon})\\
		&=\Theta(N^{\log_{b}​a})+O(​N^{\log_{b}​a−\epsilon}×\sum\limits_{j=0}^{\log_{b}​N−1}​(\frac{a}{b^{\log_{b}​a−\epsilon}}​)^j​)\\
		&=\Theta(N^{\log_{b}​a})+O(N^{\log_{b}​a−\epsilon}×\sum\limits_{j=0}^{\log_{b}​N−1}​(b^\epsilon)^j)\\
		&​=\Theta(N^{\log_{b}​a})+O(N^{\log_{b}​a−\epsilon}×\frac{1×(1−(b^\epsilon)^{\log_{b}​N})​}{1−b^\epsilon})\\
		&=\Theta(N^{\log_{b}​a})+O(N^{\log_{b}​a−\epsilon}×\frac{N^\epsilon-1}{b^\epsilon−1}​)\\
		&=\Theta(N^{\log_{b}​a})+O(N^{\log_{b}​a−\epsilon}×N^\epsilon)\\
		&=\Theta(N^{\log_{b}​a})+O(N^{\log_{b}​a})\\
		&=\Theta(N^{\log_{b}​a})​
		\end{aligned}
		$$
		
		证毕
	
	=== "Case 2"
	
		前面的部分和情况一的类似，我们通过相同的步骤得到相同的求和式：
		
		$$
		T(N)=\Theta(N^{\log_{b}a})+\sum\limits_{j=0}^{\log_{b}N-1}a^jf(\frac{N}{b^j})
		$$
		
		而我们有条件 $f(N)=\Theta(N^{\log_{⁡b}a})$，将它代入到上式中得到：
		
		$$
		\begin{aligned}
		T(N)&=\Theta(N^{\log_{⁡b}a})+\sum\limits_{j=0}^{\log⁡_{b}N−1}a^j\Theta((\frac{N}{b^j})^{\log⁡_{b}a})\\
		&=\Theta(N^{\log_{⁡b}a})+\Theta(N^{\log_{b}a}×\sum\limits_{j=0}^{\log_{⁡b}N−1}(\frac{a}{b^{\log_{b}a}})^j)\\
		&=\Theta(N^{\log_{⁡b}a})+\Theta(N^{\log_{b}a}×\log_{⁡b}N)\\
		&=Θ(N^{\log_{⁡b}a}\log⁡N)
		\end{aligned}
		$$
		
		​证毕
	
	=== "Case 3"
	
		情况三的证明，从条件的变化就可以看出来和前面稍许有些不同了。不过求和式的得到还是一样，通过和之前一样的方法，我们首先得到求和式：
		
		$$
		T(N)=\Theta(N^{\log_{b}a})+\sum\limits_{j=0}^{\log_{b}N-1}a^jf(\frac{N}{b^j})
		$$
		
		接下来的步骤和之前不同。在继续之前，我们首先观察不等式 $af(\frac{N}{b})<cf(N)$，在我们的求和式中，我们观察到我们有大量的形如 $a^jf(\frac{N}{b^j})$ 的项，而这些项都可以通过迭代上面那个不等式来实现，即：
		
		$$
		a^jf(\frac{N}{b^j}​)<c×a^{j−1}f(\frac{N}{b^{j−1}}​)<...<c^jf(N)
		$$
		
		将这个不等式应用于求和式中，我们能够得到：
		
		$$
		\begin{aligned}
		T(N)&<\Theta(N^{\log_{b}a})+\sum\limits_{j=0}^{\log_{b}N-1}c^jf(N)\\
		&=\Theta(N^{\log_{b}a})+f(N)\sum\limits_{j=0}^{\log_{b}N-1}c^j\\
		&=\Theta(N^{\log_{b}a})+f(N)\times\frac{1-c^{\log_{b}N}}{1-c}\\
		&=\Theta(N^{\log_{b}a})+f(N)\times\frac{1-N^{\log_{b}c}}{1-c}
		\end{aligned}
		$$
		
		而由于 $c<1$，所以 $\log_{⁡b}c<0$；而 $N>0$，而且一般非常大，所以 $N\log_{⁡b}c\in(0,1)$。因此，对于确定的常数 $c$，我们有 $\frac{1−N^{\log_{⁡b}c}}{1−c}\in(0,\frac{1}{1−c})$；
		
		因此，上式便能改变为：
		
		$$
		\begin{aligned}
		T(N)&<\Theta(N^{\log_{b}a})+f(N)\times\frac{1-N^{\log_{b}c}}{1-c}\\
		&<\Theta(N^{\log_{b}a})+f(N)\times\frac{1}{1-c}
		\end{aligned}
		$$
		
		并且，由于 $f(N)=\Omega(N^{\log_{⁡b}a+\epsilon}),\text{ for }\epsilon>0$，所以可以得到 $c_2N^{\log_{⁡b}a+\epsilon}<f(N)\Rightarrow N^{\log_{b}a}<\frac{1}{c_2N^\epsilon}f(N)$，因此 $T(N)<\Theta(N^{\log_{b}a})+f(N)\times\frac{1}{1-c}<c_1N^{\log_{b}a}+f(N)\times\frac{1}{1-c}<(\frac{c_1}{c_2N^\epsilon}+\frac{1}{1-c})f(N)=O(f(N))$
		
		而我们知道，要证明 $T(N)=\Theta(f(N))$ 还需要证明 $T(N)=\Omega(f(N))$：
		
		$$
		T(N)​=Θ(N^{\log_{b​}a})+\sum\limits_{j=0}^{\log_{b​}N−1}​a^jf(\frac{N}{b^j}​)​
		\geq\sum\limits_{j=0}^{\log_{b}​N−1}​a^jf(\frac{N}{b^j}​)\geq f(N)
		$$
		
		由此得到 $T(N)=\Omega(f(N))$，最终证得 $T(N)=\Theta(f(N))$，至此证毕。

#### Form 2

!!! note "Form 2"

	对于形如 $T(N)=aT(\frac{N}{b})+f(N)$ 的递推式：
	
	1. 若 $af(\frac{N}{b})=\kappa f(N)\text{ for fixed }\kappa <1$，那么 $T(N)=\Theta(f(N))$；
	2. 若 $af(\frac{N}{b})=\kappa f(N)\text{ for fixed }\kappa >1$，那么 $T(N)=\Theta(N^{\log_{⁡b}a})=\Theta(a^{\log_{⁡b}N})$；
	3. 若 $af(\frac{N}{b})=f(N)$，那么 $T(N)=\Theta(f(N)log_{⁡b}N)$；

!!! note "Proof of Form 2"

	对于形如 $T(N)=aT(\frac{N}{b})+f(N)$ 的递推式，基于线性关系的形式二的证明实际上和形式一的第三种情况的证明非常相像。
	
	假设我们有 $af(\frac{N}{b})=cf(N)$，只需要讨论 c 的取值范围对结果的影响，就可以一次性得到结果。
	
	类似于形式一的第三种情况的证明，我们迭代该关系式，得到关系：
	
	$$
	a^jf(\frac{N}{b^j})=c^jf(N)
	$$
	
	于是，我们有：
	
	$$
	\begin{aligned}
	T(N)&<\Theta(N^{\log_{b}a})+\sum\limits_{j=0}^{\log_{b}N-1}c^jf(N)\\
	&=\Theta(N^{\log_{b}a})+f(N)\sum\limits_{j=0}^{\log_{b}N-1}c^j\\
	&=\Theta(N^{\log_{b}a})+f(N)\times\frac{1-c^{\log_{b}N}}{1-c}\\
	&=\Theta(N^{\log_{b}a})+f(N)\times\frac{1-N^{\log_{b}c}}{1-c}
	\end{aligned}
	$$
	
	我们现在并不像 Form 1 有显式的 $f(N)=\Omega(N^{\log_{⁡b}a+\epsilon})$ 的条件，而这个条件最终决定 conquer 部分和 combine 部分谁占主导地位。但是，我们实际上只需要得到 $f(N) = \Omega(N^{\log_{⁡b}a})$ 就够了。其实 $af(\frac{N}{b})∼cf(N)$ 这件事本身就暗含了它与 $N^{\log_{⁡b}a}$ 的关系：
	
	$$
	cf(N)∼af(\frac{N}{b}​)∼...∼a^Lf(\frac{N}{b^L}​)
	$$
	
	可以发现，这一步还是和 Form 1 的第三种情况的证明过程高度相似。只不过现在我们要更进一步地看这个式子。
	
	当 $c<1$ 时，实际上有 $f(N)>af(\frac{N}{b})$；当 $c=1$ 时，实际上有 $f(N)=af(\frac{N}{b})$；当 $c>1$ 时，实际上有 $f(N)<af(\frac{N}{b})$；
	
	我们假设 $\frac{N}{b^L}$ 足够小（即递归到最末端，只需要进行 conquer 的时候），即 $\frac{N}{b^L}=\Theta(1)$，那么就有 $L=\Theta(\log_{⁡b}N)$。于是，我们有：
	
	$$
	f(N)∼Θ(a^{\log_{⁡b}N})=Θ(N^{\log_{⁡b}a})
	$$
	
	剩下的证明就跟 Form 1 的第三种情况一样了。

这个形式虽然简单，但是能够计算的时间复杂度相当有限，一些能由前一种形式的主定理解决的问题，用这种形式的主定理无法解决；前一种形式的主定理无法解决的问题，这种形式的主定理更无法解决。

!!! Example

	$a=4,b=2,f(N)=N\log N$
	
	- 先计算 $af(\frac{N}{b})=4(\frac{N}{2})\log⁡(\frac{N}{2})=2N\log ⁡N−2N$
	- 显然找不到任何常数 $c$ 满足 $cf(N)=2N\log⁡ N−2N$，因此无法用这种主定理计算
	- 然而，用前一种主定理是可以算出来的：发现 $O(N^{\log⁡_{b}a−\epsilon})=O(N^{2−\epsilon})=f(N)$，符合第 1 类情况，那么时间复杂度为 $T=O(N^2)$

***
#### Form 3

> 个人认为 Form 3 更为强大更为常用。

!!! note "Form 3"

	当递推关系满足：
	
	$$
	T(N)=aT(\frac{N}{b})+\Theta(N^k\log^{p}N)\text{ Where }a\geq 1,b>1,p\geq 0
	$$
	
	其复杂度有结论：
	
	$$
	T(N)=
	\begin{cases}
	O(N^{\log_{⁡b}a}),a>b^k\\
	O(N^k\log⁡^{p+1}N),a=b^k\\
	O(N^k\log^{p}N),a<b^k
	\end{cases}
	$$
	

!!! Example "Examples of Form 3"

	=== "Example 01"
	
		对于归并排序，$a=b=2,p=0,k=1$，满足第 2 种情况（$a=b^1$），因此 $T(N)=O(N^k\log^{⁡p+1} N)=O(N\log ⁡N)$。
		
	
	=== "Example 02"
	
		假设某种分治算法中，对于每次递归，$a=3,b=2$，且合并操作的时间复杂度为 $O(N)$，即 $k=1,p=0$。
		
		不难发现，它符合第 1 种情况，因此 $T(N)=O(N^{\log_{⁡2}3})=O(N^{1.59})$。
		
		- 如果合并时间复杂度为 $O(N^2)$，那么 $T(N)=O(N^2)$。
	
	=== "Example 03"
	
		再来解决前两种形式都没法计算的问题：$a=b=2,f(N)=N\log ⁡N$（即 $k=p=1$）。此时满足第 2 种情况，因此时间复杂度 $T(N)=O(N^k\log^{⁡p+1}N)=O(N\log^2N)$。
***
## Homework

!!! question "Question 01"

	Which one of the following is the lowest upper bound of $T(n)$ for the following recursion $T(n)=2T(n​)+\log n$?
	
	- A. $O(\log n\log\log n)$
	- B. $O(\log^2 n)$
	- C. $O(n\log n)$
	- D. $n^2$
	
	??? note "Answer"
	
		A. $O(\log n\log\log n)$
		
		这就需要用到我们之前提到的小技巧，我们令 $m=\log n$，那么有 $T(\sqrt{n})=T(2^{\frac{m}{2}})$，此时 $T(n)=T(2^m)$
		
		再令 $S(m)=T(2^m)$，原递推公式就变为 $S(m)=2S(\frac{m}{2})+m$，根据主定理 3 我们可以得到 $S(m)=O(m\log m)$，即 $T(n)=T(2^m)=S(m)=O(m\log m)=O(\log n\log\log n)$

