---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 02 : Red-Black Trees and B+ Trees

## Red-Black Trees

### Why?

> 跟 AVL 树和 Splay 树一样，红黑树被发明出来也是希望能维护一个相对平衡的二叉搜索树

### Definition

!!! Definition "Red-Black Tree"

	红黑树是满足如下性质的一种二叉搜索树：
	
	- 每个节点不是红色就是黑色
	- 根节点为黑色
	- NIL 节点（空叶子节点）为黑色
	- 如果一个节点是红色，那么它的两个子节点都是黑色
	- 从根节点到 NIL 节点的每条路径上的黑色节点数量相同
	
	下图为一合法的红黑树：
	
	![](../../../assets/Pasted image 20240921110036.png)