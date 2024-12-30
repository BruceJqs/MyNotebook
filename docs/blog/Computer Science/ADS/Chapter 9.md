---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 09 : Greedy Algorithms

## Abstract

!!! Abstract

	贪心算法是一个非常常用的算法，在 OI 中是一个非常基本的内容，Bruce 和夏神都是一起打过 NOIP 的所以这里就不多赘述（Bruce 想偷懒），贪心也是一个非常宽泛且非常多例子的算法，需要不断练习，见过才算会，可转至：[夏神的网站](https://note.isshikih.top/cour_note/D2CX_AdvancedDataStructure/Lec09/)
***
## Homework

!!! question "Question 01"

	Let S be the set of activities in Activity Selection Problem. Then the earliest finish activity $a_m$​ must be included in all the maximum-size subset of mutually compatible activities of S.
	
	??? note "Answer"
	
		False. 这题有点 Tricky，我们贪心的最优解确实是包含了最早结束的活动，但是也有可能会有其他和贪心同样优且并不包含最早结束的活动的方案
		
		简单来说，贪心出来的最优解只是最优解的一种，换个说法 "There must be some maximum-size subset of mutually compatible activities of S that includes the earliest finish activity." 这就对了

!!! question "Question 02"

	Let $C$ be an alphabet in which each character $c$ in $C$ has frequency $c.\text{freq}$. If the size of $C$ is $n$, the length of the optimal prefix code for any character $c$ is not greater than $n−1$.
	
	??? note "Answer"
	
		True. 哈夫曼树的性质，哈夫曼编码最短长度为 $1$ 最长长度为 $n-1$

!!! question "Question 03"

	Consider the problem of making change for $n$ cents using the fewest number of coins. Assume that each coin's value is an integer.  
	
	The coins of the lowest denomination（面额） is the cent.
	
	(I) Suppose that the available coins are quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent). The greedy algorithm always yields an optimal solution.
	
	(II) Suppose that the available coins are in the denominations that are powers of c, that is, the denominations are $c^0, c^1, ..., c^k$ for some integers $c>1$ and $k>=1$. The greedy algorithm always yields an optimal solution.
	
	(III) Given any set of $k$ different coin denominations which includes a penny (1 cent) so that there is a solution for every value of $n$, greedy algorithm always yields an optimal solution.
	
	Which of the following is correct?
	
	- A. Statement (I) is false.
	- B. Statement (II) is false.
	- C. Statement (III) is false.
	- D. All of the three statements are correct.
	
	??? note "Answer"
	
		C. Statement (III) is false.
		
		=== "选项 I"
		
			对于第一个选项来说，较大的硬币面额是较小面额的整数倍（例如，$10 = 2 \times 5，25 = 2.5 \times 10$）。贪心算法每次选择当前最大的可用硬币时，剩余金额可以通过较小面额的硬币精确表示。因此，无论需要找零的总金额 $n$ 是多少，贪心算法都能找到最少硬币数的最优解。
		
		=== "选项 II"
		
			当硬币面额为 $c$ 的幂次方时，每个更高面额都是前一面额的 $c$ 倍（如 $c=2$ 时，面额为 $1, 2, 4, 8, ...$）。这种递增关系确保了贪心算法的选择总是最优的，因为每次选择最大的面额时，剩余金额也能通过较小面额的组合精确表示。
		
		=== "选项 III"
		
			虽然包含 1 美分可以确保任何金额 $n$ 都有解，但并不保证贪心算法总是能够得到最优解。存在一些硬币面额的组合，包含 1 美分，但贪心算法无法找到最少硬币数的最优解。
			
			例如：硬币面额为1美分、3美分和4美分，需要找零6美分
			
			- **贪心算法选择：**
				- 选择 1 个 4 美分，剩余 2 美分
				- 选择 2 个 1 美分
			- **最优解：**2 个 3 美分
			
			因此，贪心算法未能找到最优解