---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 04 : Leftist Heaps and Skew Heaps

## Leftist Heap

### Why?

> 对于普通的两个堆合并操作，我们都需要将其中一个堆的每个元素一个一个地拷贝到某一个地方（无论是拷贝到另一个堆里面还是拷贝到一个新的堆里面），这样的时间复杂度为 $O(N)$，那有没有方法或者一个新的堆结构能让其合并地快一些呢？
***
### Definition

!!! Definition

	**左偏堆(Leftist Heap)**，它相比于普通的堆，更好的一点在于它支持快速的堆合并操作。“左偏”，并不断将新的东西往右侧合并（来更好实现堆的平衡），来实现每次都是往相对小的那一侧塞进东西。
	
	由于左偏堆不再是一个完全二叉树，所以我们不能再像维护大根堆小根堆那样用数组来维护它了。
	
	一个左偏堆的结点维护了左右子堆的地址、自身的键值、和一个“空路径距离（Null Path Length）”。

!!! note "Null Path Length"

	- 如果一个结点的左孩子或右孩子为空结点，则该结点的 NPL 为 $0$，这种结点被称为外结点
	
	- 如果一个结点的左孩子和右孩子都不为空，则该结点的 NPL 为 $\min⁡\{NPL(left child),NPL(right child)\}+1$；
	
	或者更为直接地，定义 $NPL(NULL)=-1$，那么有 $NPL(X)=\min\{NPL(C)+1\},C为X的孩子$
	
	![](../../../assets/Pasted image 20241008102305.png)

- 有了空路径距离这个定义，我们也可以得到左偏堆的一个性质：对于堆中的每一个节点 $X$，其左孩子的空路径距离一定不小于其右孩子的空路径距离。

![](../../../assets/Pasted%20image%2020241008102805.png)

我们还可以得到如下扩展性质：

!!! Properties

	- 结点的 NPL 等于 $NPL(right child)+1$（假设 $NPL(NULL)=−1$）

	- 如果 $NPL(i)=N$，则以 $i$ 为根的子树**至少**是一个 $N+1$ 层的满二叉树，则这个子树至少有 $2^{N+1}−1$ 个结点；
	
	![](../../../assets/Pasted image 20241008103628.png)

为什么左偏堆会这么设计呢？实际上，合并堆需要考虑的非常重要的一个点就是要能在之后的操作中尽可能地维护堆的“平衡”，否则我们把堆维护成了一个链，那显然是非常糟糕的。

而左偏堆通过维护整个堆“左偏”，并不断往右侧合并，来实现每次都是往 NPL 相对小的那一侧塞进东西，进而保证了这个堆的相对平衡性。
***
### Operations

左偏堆的核心操作就是合并。而其它操作都可以看作是合并的特殊情况。因此我们首先讨论任意两个左偏堆的合并。
***
#### Merge

作为左偏堆的核心操作，合并操作自然就是要在满足性质的条件下，合并两个左偏堆。大致思路就是**先维护堆的性质**，在**回溯时维护左偏性质**，所以实际上它是一个先自上而下再自下而上的过程。

按照实现方法，左偏堆的合并可以分为**递归式**和**迭代式**两种。其中前者可能更为直觉，而后者可视化后则更为直观。

!!! Merge

	=== "递归式"
	
		递归式先比较当前两个待合并子树的根结点的键值，选择较小（较大）的那个作为根结点，其左子树依然为左子树，右子树更新为「右子树和另一个待合并子树的合并结果」。
		
		当然，在递归地更新完后，我们需要检查左子树和右子树是否满足 $NPL(left child)\geq NPL(right child)$ 的性质，如果不满足，我们则需要**交换左右子树**来维持性质。
		
		```c
		LeftistHeapNode * merge(LeftistHeapNode * x, LeftistHeapNode * y) {
		    // Recursive exit. If any is NULL, return the other as the new root of subtree.
		    if (x == NULL) return y;
		    if (y == NULL) return x;
		
		    // If x's val is smaller than y's, swap them, which means we always operates on x.
		    if (x->val > y->val) {
		        swap(x, y);
		    }
		
		    // Merge x's right subtree and y, and set x's right subtree to the result.
		    x->rs = merge(x->rs, y);
		
		    // If x's left subtree's dist is smaller than x's right subtree's dist, swap them.
		    if (x->ls->dist == NULL || x->ls->dist < x->rs->dist) {
		        swap(x->ls, x->rs);
		    }
		
		    // Update x's dist.
		    x->dist = x->rs->dist + 1;
		
		    // Return x as the new root of subtree.
		    return x;
	    }
		```





