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
	
		在插入一个 5 之后，可以看到，这使得 8 的平衡因子变成了 2，不再符合 AVL 树的要求，这样因为某个点的插入导致平衡因子不再符合 AVL 树要求的点被称为 **Trouble Finder**（即这里的 8），而引起这个 “Trouble” 的点被称为 **Trouble Maker**（即这里的 5）。
	
!!! note "Rotation Operations"

	值得注意的是，在实际情况中可能会出现多个 "Trouble Finder",但我们只关注 **"距离案发现场最近的 Trouble Finder"** 为根的子树。
	
	=== "LL"
	
		![](../../../assets/Screenshot14.png)
	
	=== "RR"
	
		![](../../../assets/Screenshot15.png)
	
	=== "LR"
	
		![](../../../assets/Screenshot16.png)
	
	=== "RL"
		
		![](../../../assets/Pasted image 20240910153653.png)
		
	稍作解释：例如 "LL"，指 "Trouble Maker" 位于 "Trouble Finder" 左孩子的左子树中的情况.
***
>接下来我们从两个视角来理解 Rotate Operation：

!!! note "从旋转视角来理解"

	以 LL Rotation 为例（RR Rotation 类似）
	 
	![](../../../assets/Pasted image 20240910195353.png)
	 
	我们可以得到当下有如下性质：
	 
	- $BF(Trouble Finder)=h(New Left Subtree)−h(Right Subtree)=2$
	- $h(New L Left Subtree)−h(L Right Subtree)=1$
		- 如果此差为 0，则不应当成为 Trouble Maker，若此差为 2，则 Left Child 应当为 Trouble Finder；
	
	现在我们希望在保留二叉搜索树的性质下，要让 $∣BF(Trouble Finder)∣$ 变小，一个很自然的想法就是让 $h(New Left Subtree)$ 减 1，让 $h(Right Subtree)$ 加 1。那么我们可以有如下操作：
	
	=== "Initial"
	
		![](../../../assets/Pasted image 20240910204504.png)
	
	=== "Connect"
	
		![](../../../assets/Pasted image 20240910204608.png)
	
	=== "Rotate"
	
		![](../../../assets/Pasted image 20240910204657.png)
	
	=== "Final"
	
		![](../../../assets/Pasted image 20240910204745.png)

!!! note "从换根视角来理解（推荐）"
	
	以 LL Rotation 为例：（RR Rotation 类似）
		
	=== "Initial"
		
		![](../../../assets/Pasted image 20240910205532.png)
		
	=== "Cut"
		
		![](../../../assets/Pasted image 20240910205605.png)
		
	=== "Move"
		
		![](../../../assets/Pasted image 20240910205655.png)
		
	=== "Connect"
		
		![](../../../assets/Pasted image 20240910205733.png)
		
	当插入 "Trouble Maker" 时，"Trouble Finder" 发现左子树太高了，因此我们不希望让左子树成为某个节点的子树，如 "Cut" 操作割裂其与 "Trouble Finder" 的关系。
	
	我们仍然需要让这个森林重新变回一个树，所以就需要重新从里面找到根节点，显然，只能选择 Trouble Finder 旁边的 Left Child。但是为了继续维护二叉搜索树的性质，所以我们需要将 L Right Subtree 移植到 Trouble Finder 必定空缺（因为这里原先是 Left Child）的左指针上。
	
	再以 LR Rotation 为例：(RL Rotation 类似)：
	
	=== "Initial"
	
		![](../../../assets/Pasted image 20240910213533.png)
	
	=== "Connect"
	
		![](../../../assets/Pasted image 20240910213627.png)
		
	=== "Cut"
	
		![](../../../assets/Pasted image 20240910213812.png)
		
	=== "Final"
	
		![](../../../assets/Pasted image 20240910213910.png)
		
	找到关键的三个点（Left Child, Trouble Finder, L Right Child），然后把最下面的顶到上面去，剩下两个作为左右子树，原先的那个点的左右子树则对应地，左子树接到左边空缺的右子树上，右子树接到右边空缺的左子树上。
***
!!! question "如果出现多个 Trouble Finder 该怎么办？"

	之前我们提到过，我们关注的是 **"距离案发现场最近的 Trouble Finder"** 为根的子树，并以此作出 Rotation 操作，这也会导致其所有父节点的平衡因子都会相应发生变化。
***
## Splay Tree
### Definition

- Splay 树，即伸展树，想要解决的问题和 AVL 树类似，只不过 Splay 树希望达到的目标是在摊还(Amortized) 复杂度 $O(\log⁡N)$ 的情况下完成大部分对点操作。

- 为使 AVL 保持平衡，我们需要维护从根节点到 Trouble Maker 这条路径上所有点的平衡因子。而 Splay 则不再维护这些信息，这意味着我们无法保证 Splay 树的状态都是平衡的，但是我们希望它尽可能平衡。具体来说就是对于 $M$ 次任意操作，其时间复杂度都为 $O(M\log⁡N)$，均摊下来这 $M$ 个操作每一个都需要 $O(\log⁡N)$。

- Splay 的核心思想就是，每当我们访问一个节点（比如查询某个点、插入某个点，删除某个点）时，我们就通过一系列操作将目标点转移到根部，形象上理解就是不断旋转整个树的构造，直到把点转到根部。
***
### Operations

> 对于某个节点 X，我们记其父节点为 P(Parent)，其父节点的父节点为 G(Grandparent)。

- 当我们访问到 X 时：
	- 如果 P 是根节点，则直接进行一次 Single Rotation（即类似 AVL Tree 中的 LL / RR Rotation）
	- 如果 P 不是根节点：
		- 当情况为 LR / RL 时，进行一次 LR Rotation 或 RL Rotation，称该操作为 Zig-Zag
		- 当情况为 LL / RR 时，进行两次 Single Rotation，使得 X、P、G 的顺序逆转，像跷跷板一样，称该操作为 Zig-Zig
	- 不断对 X 进行 Splay 操作，直到 X 成为根节点

![](../../../assets/Pasted%20image%2020240910222750.png)
