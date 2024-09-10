# Chapter 01 : AVL trees, Splay Trees, and Amortized Analysis

## AVL Trees

### Why?

>对于一棵二叉搜索树，其对点的操作代价为 $O(\log⁡\space n)$。然而在最坏情况下，它会退化成 $O(n)$。

>如果我们想让一棵二叉树好维护（即时间复杂度低），那么就希望它的高度尽可能低，而在点数固定的情况下，一种朴素的思想是让节点尽可能“均匀”地分布在树上。
***
### Definition

!!! note "AVL Trees"

	- 一个空二叉搜索树是平衡的
	- 如果一个树 $T$ 是一个非空二叉搜索树，其左子树为 $T_L$ ，右子树为 $T_R$ ，那么树 $T$ 是平衡的当且仅当：
		- $T_L$ 和 $T_R$ 是平衡的
		- $|h_L-h_R|\leq 1$ ，其中 $h_L$ 为 $T_L$ 的高度，$h_R$ 为 $T_R$ 的高度	

	!!! note "Balance Factor"

		- 一个节点的平衡因子被用来描述一个节点的平衡状态，对于节点 $T_P$，它的左子树为 $T_L$​，右子树为 $T_R$​，则 $BF(T_P)=h(T_L)-h(T_R)$
	
		- 在一个 AVL 树中，其每一个节点的平衡因子均为 -1 或 0 或 1

在如此定义之下，可以证明 AVL Trees 的高度为 $O(\log\space N)$：

!!! note "Height of AVL Trees"
	我们记 $n_h$ 是高度为 $h$ 的 AVL 树所包含的最少节点数，则有如下递推关系：
	
	$$
	n_h = \left\{
	\begin{array}{}
	1 & & (n=0)\\
	2 & & (n=1)\\
	n_{h-1}+n_{h-2}+1 & & (n>1)
	\end{array}
	\right.
	$$
	
	可以发现 $n_h$ 非常像 Fibonacci 的递推公式，因此我们用 Fibonacci 进行一个估计，对于 Fibonacci 数列：
	
	$$
	\begin{aligned}
	F_n & = \frac{1}{\sqrt{5}}((\frac{1+\sqrt{5}}{2})^n-(\frac{1-\sqrt{5}}{2})^n) \\
	& \approx\frac{1}{\sqrt{5}}(\frac{1+\sqrt{5}}{2})^n \\
	\end{aligned}
	$$
	
	由此我们可以得到 $\log(F_n)\approx n$ ，而 $n_h+1\approx F_{h+2}$，所以 $h\approx\log(n_h)$，即 $h\approx\log N$

***
### The Rotation Operations on BST

> 为了时刻能维护 AVL 树的平衡，我们需要引入“旋转”这一操作，首先我们需要定义两个概念：

!!! note "Trouble Maker & Trouble Finder"

	=== "Initial"
	
		![](../../../assets/Screenshot12.png)
	
	=== "After Insertion"
	
		![](../../../assets/Screenshot13.png)
	
		在插入一个 5 之后，可以看到，这使得 8 的平衡因子变成了 2，不再符合 AVL 树的要求，这样因为某个点的插入导致平衡因子不再符合 AVL 树要求的点被称为 **Trouble Finder**（即这里的 8），而引起这个“Trouble” 的点被称为 **Trouble Maker**（即这里的 5）。
	
!!! Rotation Operations

	=== "LL"
	
		![](../../../assets/Screenshot14.png)
	
	=== "RR"
	
		![](../../../assets/Screenshot15.png)
	
	=== "LR"
	
		![](../../../assets/Screenshot16.png)
	
	=== "RL"
		
		![[Pasted image 20240910153653.png]]
		
	稍作解释：例如 "LL"，指 "Trouble Maker" 位于 "Trouble Finder" 左孩子的左子树中的情况.