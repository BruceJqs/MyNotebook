# Chapter 01 : AVL trees, Splay Trees, and Amortized Analysis

## AVL Trees

### Why?



### Definition

!!! "AVL Trees"

	- 一个空二叉搜索树是平衡的
	- 如果一个树 $T$ 是一个非空二叉搜索树，其左子树为 $T_L$ ，右子树为 $T_R$ ，那么树 $T$ 是平衡的当且仅当：
		- $T_L$ 和 $T_R$ 是平衡的
		- $|h_L-h_R|\leq 1$ ，其中 $h_L$ 为 $T_L$ 的高度，$h_R$ 为 $T_R$ 的高度	

!!! "Balance Factor"

	一个节点的平衡因子被用来描述一个节点的平衡状态，对于节点 $T_P$，它的左子树为 $T_L$​，右子树为 $T_R$​，则 $BF(T_P)=h(T_L)-h(T_R)$
	
	在一个 AVL 树中，其每一个节点的平衡因子均为 -1 或 0 或 1

