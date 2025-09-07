---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Chapter 06 : Backtracking

## Abstract

!!! Abstract

	回溯算法是一个非常常用的算法，在 OI 中是一个非常基本的内容，Bruce 和夏神都是一起打过 NOIP 的所以这里就不多赘述（Bruce 想偷懒），可转至：[夏神整理的资源](https://note.isshikih.top/cour_note/D2CX_AdvancedDataStructure/Lec06/)

需要补充的 $\alpha-\beta$ 剪枝，这篇知乎讲的非常清楚：[α-β Pruning](https://zhuanlan.zhihu.com/p/658351019)，还有 [OI Wiki](https://oi-wiki.org/search/alpha-beta/#alpha-beta-%E5%89%AA%E6%9E%9D)
***
## Homework

!!! question "Question 01"

	Given the following game tree, which node in the right subtree is the first node to be pruned with $\alpha-\beta$ pruning algorithm?
	
	![](../../../assets/Pasted%20image%2020241224212607.png)
	
	- A. d
	- B. b
	- C. c
	- D. a
	
	??? note "Answer"
	
		A. d。类似这样的 $\alpha-\beta$ 剪枝题，谨记一点，一开始非叶子节点是未知的，我们是先找到一条路径（即最左边的这个 65）再以此基础看其他有没有可能剪枝的
		
		在这里，我们必须先找到第五个叶子节点 65，同时 a 是肯定需要访问的，不然我们不会知道它的父亲是多少，这时其实就已经出问题了，我们可以看到 a 的父亲已经比左子树（即第二层的 68）小了，而 a 的爷爷又是通过 min 取得（这意味着 a 的爷爷必然 $\leq 65$），那么最终的根必然为 68 而非 a 的爷爷，所以右侧从 d 开始的所有搜索都是无意义的，可以剪枝
