# Chapter 01 : AVL trees, Splay Trees, and Amortized Analysis

## AVL Trees

### Why?

- 对于一棵二叉搜索树，其对点的操作代价为 $O(\log⁡\space n)$。然而在最坏情况下，它会退化成 $O(n)$

- 如果我们想让一棵二叉树好维护，那么就希望它的高度尽可能低，而在点数固定的情况下，一种朴素的思想是让节点尽可能“均匀”地分布在树上。
***
### Definition

!!! "AVL Trees"

	- 一个空二叉搜索树是平衡的
	- 如果一个树 $T$ 是一个非空二叉搜索树，其左子树为 $T_L$ ，右子树为 $T_R$ ，那么树 $T$ 是平衡的当且仅当：
		- $T_L$ 和 $T_R$ 是平衡的
		- $|h_L-h_R|\leq 1$ ，其中 $h_L$ 为 $T_L$ 的高度，$h_R$ 为 $T_R$ 的高度	
***
!!! "Balance Factor"

	一个节点的平衡因子被用来描述一个节点的平衡状态，对于节点 $T_P$，它的左子树为 $T_L$​，右子树为 $T_R$​，则 $BF(T_P)=h(T_L)-h(T_R)$
	
	在一个 AVL 树中，其每一个节点的平衡因子均为 -1 或 0 或 1
***
在如此定义之下，可以证明 AVL Trees 的高度为 $O(\log\space N)$：

!!! "Height of AVL Trees"
	我们记 $n_h$ 是高度为 $h$ 的 AVL 树所包含的最少节点数，则有如下递推关系：
	$$
	n_h = \begin{cases}
	1 (n=0)\\
	2 (n=1)\\
	n_{h-1}+n_{h-2}+1(n>1)
	\end{cases}
	$$

### The Rotation Operations on BST


