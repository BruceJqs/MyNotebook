---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 10 : NP Completeness

## Abstract

!!! Abstract

	正巧，Bruce 在数模课上面学过一点 NP 完全性了（虽然一点都没学懂），ADS 再来一遍，数模有关的笔记可转至 [数模 NP 笔记](https://brucejqs.github.io/MyNotebook/blog/ACEE/Mathematical%20Modeling/Chapter%203/#_9)

## Introduction

根据问题的难度，由不同的定义划分，问题可以分为：

- **P** 问题（Polynomial Time）
- **NP** 问题（Nondeterministic Polynomial Time）
- **NPC** 问题（NP Complete）
- **NPH** 问题（NP Hard）

除此之外 ，我们还需要额外了解不可计算问题（Undecidable）。

!!! note "Undecidable Problem"

	**不可判定问题（Undecidable Problem）**是一类特殊的[决定性问题](https://en.wikipedia.org/wiki/Decision_problem)，它的特点是我们无法设计一个算法来求解它的结果。
	
	其中一个比较典型的例子就是[图灵停机问题](https://en.wikipedia.org/wiki/Halting_problem)。
	
	!!! note "图灵停机问题"
	
		停机问题是一个典型的不可计算问题，它指的是，对于任意一个程序，我们无法设计一个算法来判断它是否会在有限时间内停机（即判断程序是否会死循环）。
		
		我们通过反证法可以证明：
		
		假设存在函数 `willHalt(func F)` 可以判断函数 F 是否会停机，如果会，则返回 `true`，否则返回 `false`。那么我们可以构造一个这样的函数 `foo()`：
		
		```c
		void foo() {
		    if ( willHalt(foo) ) {
		        while (true) {} // Endless loop.
		    }
		    return;
		}
		```

		接下来，如果我们想知道 `foo()` 是否会停机，就会执行 `willHalt(foo)`。然而在 `foo()` 内部也有一个 `willHalt(foo)`，如果它认为 `foo()` 会停机，则构造一个死循环；而如果它认为 `foo()` 不会停机，则选择让它立刻停机，于是这里就产生了矛盾。

		理解上面这段内容的关键就是，这里虽然不存在事实意义上的“死循环”，但可以理解为这里存在一个逻辑上的递归，而这种“逻辑上的递归”，正是导致停机问题成为一个不可计算问题的原因。

!!! note "P"

	P 取自 polynomial time，指的是可以用**确定型图灵机**在**多项式**时间内**解决**的问题。
	
	也就是我们通常意义下所说的，可以在**多项式**时间内**解决**的问题。
	
	!!! note "Turing Machine"
	
		图灵机有一些变体，而我们在这里引入图灵机是为了介绍 P/NP，只介绍**[确定型图灵机](https://en.wikipedia.org/wiki/Turing_machine)**和**[非确定型图灵机](https://en.wikipedia.org/wiki/Nondeterministic_Turing_machine)**。

> 		图灵机由一个**无限长的纸带**和一个**读写头**组成。纸带被划分为一个个**格子**，每个格子上有一个**符号**，读写头可以在纸带上移动，读写头可以读取当前格子上的符号，也可以改变当前格子上的符号。图灵机的**状态**是一个有限集合，每个状态都有一个**转移函数**，转移函数的输入是当前状态和当前格子上的符号，输出是下一个状态、下一个格子上的符号和读写头的移动方向。
		
		确定型图灵机每次都能执行一个指令，并且<font color="red">根据当前指令跳转到下一个唯一的指令</font>，非确定型图灵机<font color="red">可以从有限集中随意选择下一步</font>，如果当前得到了一个答案，那么<font color="red">它一直都会选择正确的那一步</font>。
		
		更本质的来说，图灵机是一种**计算模型**，我们可以用它来表示任何有限逻辑数学过程。确定型图灵机与我们常规理解的计算机逻辑类似，即下一步要做什么可以根据当前状态确定。而非确定型图灵机则类似于能够进行无限并行，并且最终总是选择通向正确答案的方向的那条路（有点类似于它能开平行宇宙，并且总是让你观测到正确的那一个平行宇宙）。
		

我们可以用这样一张图来表示后四个概念的关系：

![](../../../assets/Pasted%20image%2020241119105739.png)

这体现了 NP–hard 可以是 NP 问题，也可以不是 NP 问题。