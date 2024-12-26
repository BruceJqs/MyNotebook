---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Final Review

!!! abstract "Abstract"

	这里是 Bruce 期末刷历年卷遇到的各种各样的稀奇古怪的题目合集～

## Question 01

![](../../../assets/Pasted%20image%2020241226105538.png)

??? note "Answer"

	True. 有意思，其实就是问 $x^n$ 该怎么求，我想到的想法是类似 [求和问题](https://brucejqs.github.io/MyNotebook/blog/Computer%20Science/ADS/Chapter%2014/#__tabbed_2_1)，并行计算，可以得到 $O(\log n)$ 复杂度
***
## Question 02

![](../../../assets/Pasted%20image%2020241226110631.png)

??? note "Answer"

	True. 补天还真补到不知道的东西了，这句话对应的完整定理为：对于右路径上有 $l$ 个轻结点的斜堆，整个斜堆至少有 $2l−1$ 个结点，这意味着一个 $n$ 结点的斜堆右路径上的轻结点个数为 $O(\log n)$
	
	证明：
	
	- 对 $l = 1$ 显然成立
	- 假设对小于等于 $l$ 都成立。对于 $l+1$ 情况，我们找到右路径上的第二个轻结点，以它为根节点的子树至少有 $2^l−1$ 个结点。 现在考虑第一个轻结点，根据定义，**轻结点的左子树更大**，而右路径上的第二个轻结点在右子树中。所以第一个轻结点的左子树至少有 $2^l−1$ 个结点。 所以整个堆有$1+2^l−1+2^l−1=2^{l+1}−1$ 个结点

