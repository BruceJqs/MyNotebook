---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 14 : Parallel Algorithms

## Introduction

> 我们先前学的所有算法均为顺序算法（Sequencial Algorithm），这类算法的特点是每步只完成一个操作。要想提升算法的速度，除了可以设计更快的算法（降低时间复杂度）外，还可以采用**并行**的方法。

所谓**并行**（Parallelism），就是指每一步能够同时完成多个操作。可以分为以下几类并行方式：

- 机器并行（硬件层面）：包括了处理器并行、流水线、超长指令字 (VLIW) 等方法（详情请见[计组 Chapter 4](https://brucejqs.github.io/MyNotebook/blog/Computer%20Science/Computer%20Organization/Chapter%204/)
- **并行算法**（Parallel algorithms）（软件层面）：
	- 并行算法中常用的模型有：
	    - **并行随机访问机**（Parallel Random Access Machine, PRAM）
	    - **工作 - 深度**（Work-Depth, WD）
***
### PRAM

PRAM 模型的图示如下：

![](../../../assets/Pasted%20image%2020241217111446.png)

- $P_1​,…,P_n​$ 表示 $n$ 个处理器，它们同时访问一块共享内存
- 每个处理器与共享内存间的双向箭头表示**单位时间内对内存的访问**（包括读、写、计算等操作）
    - 具体来说，向上的箭头表示读取，向下的箭头表示写入

!!! example "Examples"

	=== "Example 01"
	
		当处理器 $i$ 执行操作 `c:=a+b`：
		
		![](../../../assets/Pasted%20image%2020241217112858.png)
	
	=== "Example 02"
	
		如果我们想要执行多个写入语句，伪代码如下：
		
		```c title="PRAM.c"
		// 将每个处理器的结果写入到内存对应位置上
		for P_i, 1 <= i <= n pardo
		    A(i) := B(i)
		// pardo: do parallelly，即并行执行循环
		// 因此实际上执行这个循环所需时间为 O(1)
		```
		
		![](../../../assets/Pasted%20image%2020241217112708.png)	


不难发现，这个模型存在一个问题：如果多个处理器同时访问同一块内存，改如何处理冲突呢？下面给出几种解决方案：

- 专一读取-专一写入（Exclusive-Read Exclusive-Write, EREW）
- 并发读取-专一写入（Concurrent-Read Exclusive-Write, CREW）
- 并发读取-并发写入（Concurrent-Read Concurrent-Write, CRCW）
	- 并发写入会造成冲突，我们有三种不同的写入规则：
	    - **任意**（Arbitrary）规则：任意选择一个处理器进行写入操作
	    - **优先级**（Priority）规则：选择优先级最高的处理器（一般规定编号越小优先级越高）进行写入操作
	    - **共同**（Common）规则：只有当所有处理器的写入数据是一致的时候，才会执行写入操作

!!! example "求和问题"

	=== "Question"
	
		- 输入：$A(1),A(2),…,A(n)$（来自内存的数据）
		- 输出：$A(1)+A(2)+⋯+A(n)$
	
	=== "Answer"
	
		PRAM 模型计算此题的过程如下图所示：
		
		![](../../../assets/Pasted%20image%2020241217114550.png)
		
		- 最底层表示初始情况，每层表示并行算法的每个步骤
		- 每层都有 8 个处理器，空白圆圈表示空闲的处理器
		- 观察发现，整个过程中所有工作的处理器构成了一棵满二叉树
		    - 因此层数为 $\log ⁡n$，即该算法在 $\log⁡ n$ 时间内完成
		- $B(h,i)$ 表示第 $h$ 步中第 $i$ 个处理器的计算结果
		    - 有以下关系式成立：$B(h,i)=B(h−1,2i−1)+B(h−1,2i)$
		
		伪代码如下所示：
		
		```c title="Sum-PRAM.c"
		for P_i, 1 <= i <= n pardo
		    B(0, i) := A(i)
		for h = 1 to log(n) do
		    if i <= n / 2^h
		        B(h, i) := B(h - 1, 2 * i - 1) + B(h - 1, 2 * i)
		    else
		        stay idle
		for i = 1:
		    output B(log(n), 1)
		for i > 1:
		    stay idle
		```
		
		时间复杂度为 $T(n)=\log n + 2$

根据上面对例子的分析，我们可以得出关于操作数量和时间之间的关系图：

![](../../../assets/Pasted%20image%2020241217120011.png)

- 横轴上的最大值为 $p$，等于用到过的处理器的最大数量
- 纵轴上的最大值为 $t$，表示总的运行时间
- 每个横条表示一个阶段（单位时间），蓝色部分表示工作的处理器，灰色部分表示空闲的处理器

!!! warning "PRAM 模型的缺陷"

	- 该模型无法揭示算法和实际使用的处理器个数之间的关系
	    - 对于上面的例子，假如有 100 个处理器，但实际上只用了 8 个处理器，所以更多的处理器并不能使执行速度进一步加快
	- 该模型需要指定哪个处理器处理哪部分的指令，这些详细信息其实是非并行算法所不需要的
***
### Work-Depth

> 相比于 PRAM，WD 的每个时钟内，不一定所有 CPU 都在工作

Work-Depth 模型对应的操作数量和时间之间的关系图如下：

![](../../../assets/Pasted%20image%2020241217122040.png)

由于没有了那些灰色区域（不工作的处理器），因此这张图更清楚地反映了真实情况下各个时间段内的用到的处理器数量。对于更一般的情况，如下所示：

![](../../../assets/Pasted%20image%2020241217122100.png)

!!! example "求和问题 WD 版本"

	WD 模型的伪代码如下所示：
	
	```c title="Sum-WD.c"
	for P_i, 1 <= i <= n pardo
	    B(0, i) := A(i)
	for h = 1 to log(n) do
	    for P_i, i <= n / 2^h pardo
	        B(h, i) := B(h - 1, 2 * i - 1) + B(h - 1, 2 * i)
	for i = 1 pardo
	    output B(log(n), 1)
	```
	
	和 PRAM 的区别就在于第 4 行和第 6 行，这里用到的是并行处理的方式（`pardo`），而且不再显式指出不工作的处理器。
***
### Measuring the Performance

衡量并行算法的性能有如下指标：

- $W(n)$：工作量，即运行并行算法所需的总操作数目
- $T(n)$：最坏情况下的运行时间，包括计算时间和并行时间两部分

!!! tip

	对于上面 WD 版本的求和问题，$T(n)=\log n+2,W(n)=n+\frac{n}{2}+\frac{n}{2^2}+...+\frac{n}{2^k}+1=2n$，其中 $2^k=n$
	
	![](../../../assets/Pasted%20image%2020241217142523.png)
***
对 PRAM 模型来说，如果有 $W(n)$ 次操作，需要花费 $T(n)$ 时间：

- 当使用处理器数量为 $P(n)=\frac{W(n)}{T(n)}$ 时，所需时间为 $T(n)$
- 当使用处理器数量为 $P(n)\leq\frac{W(n)}{T(n)}$ 时，所需时间为 $\frac{W(n)}{P(n)}$（对应处理器不足的情况）
- 当使用任意数量为 $P(n)$ 的处理器时，所需时间为 $\frac{W(n)}{P(n)}+T(n)$（对应处理器冗余的情况）

这三个指标实际上是**渐进等价的**（Asymptotically Equivalent），即对于任意大的 $n$，这三者位于同一复杂度下。
***
对 WD 模型来说，有如下定理：

- **WD 表示法充分性定理**（WD-Presentation Sufficiency Theorem）：用 WD 模型表示的算法能够被任意 $P(n)$ 个处理器在 $O(\frac{W(n)}{P(n)}+T(n))$ 时间内实现，此时采用并发写入规则。

虽然 PRAM 模型和 WD 模型本质上没有太大的区别，但是 WD 模型可以反映算法与处理器数量之间的关系，因此表现会更好。
***
## Examples

### Prefix-Sums

!!! question "问题描述"

	- 输入：$A(1),A(2),…,A(n)$
	- 输出：$\sum\limits_{i=1}^1A(i),\sum\limits_{i=1}^2A(i),…,\sum\limits_{i=1}^nA(i)$

解决这个问题的方法与前面的求和问题是类似的，首先还是借助一棵平衡二叉树模型来分析：

![](../../../assets/Pasted%20image%2020241217143216.png)

可以看到，这里还是先计算了求和问题，为之后前缀和问题的解决打下基础。

接下来，我们规定**前缀和** $C(h,i)=\sum\limits_{k=1}^{\alpha}A(k)$，其中 $(0,\alpha)$ 表示二叉树的节点 $(h,i)$ 最右侧路径上的叶子节点的位置。要得到 $C(h,i)$ 的值，需要分以下情况讨论：

- 最左边路径上的节点：

```c
if (i == 1)
	C(h, i) := B(h, i)
```

- 每一层偶数位上的节点：

```c
if (i % 2 == 0)
    C(h, i) := C(h + 1, i / 2)
```

- 除最左边路径外每一层奇数位上的节点：

```c
if (i % 2 == 1 && i != 1)
    C(h, i) := C(h + 1, (i - 1) / 2) + B(h, i)
```

??? question "思考"

	=== "Question"
	
		或许会有人注意到，第三种情况还有一种算法，利用 $i-1$ 为偶数套用第二种情况，就是 $C(h,i)=C(h,i-1)+B(h,i)$，为什么不这么算呢？
	
	=== "Answer"
	
		这是因为每层都是并行计算的，因此只能利用上一级的计算值以及自身的值。（而且不觉得上面这个式子长得跟正常前缀和公式一模一样嘛）

总结一下：我们先**自底向上**计算求和问题，然后根据求和问题的结果**自顶向下**计算前缀和问题，这两趟计算都用到了并行算法。伪代码如下所示：

```c title="Prefix-Sums.c"
// Same as summation problem
for P_i, 1 <= i <= n pardo
    B(0, i) := A(i)
for h = 1 to log(n)
    for i, 1 <= i <= n / 2^h pardo
        B(h, i) := B(h - 1, 2 * i - 1) + B(h - 1, 2 * i)

// Now calculate the prefix sum problem
for h = log(n) to 0
    for i even, 1 <= i <= n / 2^h pardo
        C(h, i) := C(h + 1, i / 2)
    for i = 1 pardo
        C(h, 1) := B(h, 1)
    for i odd, 3 <= i <= n / 2^h pardo
        C(h, i) := C(h + 1, (i - 1) / 2) + B(h, i)
for P_i, 1 <= i <= n pardo
    Output C(0, i)
```

性能分析如下所示：

![](../../../assets/Pasted%20image%2020241217144803.png)

- 时间复杂度：$T(n)=O(\log ⁡n)$
- 工作量：$W(n)=O(n)$
***
### Merging

??? question "问题描述"

	合并两个非递减的数组 $A(1),A(2),…,A(n)$ 和数组 $B(1),B(2),…,B(m)$ 至另一个非递减的数组 $C(1),C(2),…,C(n+m)$。

为了简化后面的分析，我们规定：

- 数组 $A,B$ 之间没有重复元素
- 令 $n=m$
- $\log ⁡n,\frac{n}{\log⁡ n}$ 的结果均为整数

> 事实上，即使没有这个规定，后面的分析也同样适用于一般的情况。

解决该问题用到的关键方法：**划分**（Partition）。其范式（Paradigm）如下：

- **划分**：将输入数据划分为 $p$（很大的数字）个独立的小任务，每个小任务的规模大致为 $\frac{n}{p}$
- **实际的工作**：并发执行这些小任务，对于每个小任务使用（顺序）算法来解决

我们可以将合并问题进一步转化为**排行**问题（Ranking），本质是需要知道 $A$ 中的每个元素在 $B$ 中的排序位置/$B$ 中的每个元素在 $A$ 中的排序位置，方便之后直接可以放入 $C$，我们规定：

$$
\text{RANK}(j,A)=\begin{cases}
i & \text{if } A(i)<B(j)<A(i+1),\text{for }1\leq i<n\\
0 & \text{if } B(j)<A(1)\\
n & \text{if } B(j)<A(n)
\end{cases}
$$

那么排行问题可以被记为 $\text{RANK}(A,B)$，此时需要计算的东西为：$\forall 1\leq i\leq n$，计算 $\text{RANK}(i,B)$ 和 $\text{RANK}(i,A)$。伪代码如下所示：

```c title="Merging.c"
for P_i, 1 <= i <= n pardo
    C(i + RANK(i, B)) := A(i)
for P_i, 1 <= i <= n pardo
    C(i + RANK(i, A)) := B(i)
```

!!! example "Example"

	=== "Question"
	
		$A=[11,12,15,17],B=[13,14,16,18]$
	
	=== "Answer"
	
		![](../../../assets/Pasted%20image%2020241217150236.png)

那么该如何求出这些 Ranking 呢？我们先来通过比较看看一些求 Ranking 的方法：

!!! note "求 Ranking 的一些方法"

	=== "顺序排行"
	
		```c title="Serial Ranking.c"
		i = j = 0
		while (i <= n || j <= m)
		    if (A(i + 1) < B(j + 1))
		        RANK(++i, B) = j;
		    else 
		        RANK(++j, A) = i;
		```
		
		时间复杂度为 $T(n)=O(n+m)$，工作量为 $W(n)=O(n+m)$
	
	=== "二分查找"
	
		```c title="Binary Search.c"
		for P_i, 1 <= i <= n pardo
		    RANK(i, B) := BS(A(i), B)
		    RANK(i, A) := BS(B(i), A)
		```
		
		此时时间复杂度为 $T(n)=O(\log n)$，工作量为 $W(n)=O(n\log n)$（相当于是 $n$ 个二分查找并行）
		
		相较于普通的顺序排行来讲，时间复杂度降低了但是工作量变大了

上面这两个方法都有一定的缺陷，相较来说，我们还有改进方法：并行排行（Parallel Ranking），其思想有点像分治，大致如下：

- 假设 $n=m$，且确保 $A(n+1),B(n+1)$ 比 $A(n),B(n)$ 都要大
- 第一步：划分，令处理器数量 $p=\frac{n}{\log ⁡n}$，对 $1\leq i\leq p$，每 $\log n$ 个数据设置一个 Select（相当于组标志），有：
    - $A_{\text{Select}}(i)=A(1+(i−1)\log⁡ n)$
    - $B_{\text{Select}}(i)=B(1+(i−1)\log ⁡n)$
    - 计算每一个（根据上面两个式子）被选中的排行
    
    ![](../../../assets/Pasted%20image%2020241217152801.png)
    
	- 此时我们有 $T_1(n)=O(\log n),W_1(n)=O(p\log n)=O(n)$（相当于是 $p$ 个二分查找并行）
    
- 第二步：实际排行
    - 划分以后，整个问题被分为至多有 $2p$ 个规模为 $O(\log⁡ n)$ 的子问题，对每个子问题采用顺序排行
    
    ![](../../../assets/Pasted%20image%2020241217153606.png)
    
    - 此时我们有 $T_2(n)=O(\log n),W_2(n)=2p\times O(\log n)=O(p\log n)=O(n)$

综上所述整个并行排行的 $T(n)=O(\log n),W(n)=O(n)$

解决 Ranking 求解之后，整个 Merging 问题就可以在 $T(n)=O(1)$ 和 $W(n)=O(n+m)$ 下求解了
***
### Maximum Finding

> 即为从 $n$ 个元素中找到最大值

对于这个问题我们有四种解法：

#### Summation Algorithm

一种最简单的想法就是把上面的求和问题修改一下，把加号改成 max 即可

此时 $T(n)=O(\log n),W(n)=O(n)$
***
#### Compare All Pairs

伪代码如下所示：

```c title="Compare All Pairs.c"
for P_i, 1 <= i <= n pardo
    B(i) := 0
for i and j, 1 <= i, j <= n pardo
    if (A(i) < A(j) || A(i) == A(j) && i < j)
        B(i) = 1
    else
        B(j) = 1
for P_i, 1 <= i <= n pardo
    if B(i) == 0
        A(i) is a maximum in A
```

此时 $T(n)=O(1),W(n)=O(n^2)$

需要注意的是，这里会不可避免地发生多个处理器访问相同元素的冲突，这里我们可以采用 CRCW 策略当中的共同规则进行写入
***
#### Doubly-Logarithmic Paradigm

!!! note "Doubly-Logarithmic Paradigm"

	可以看到 Compare All Pairs 算法的时间复杂度已经讲到常数级别了，但是工作量却变成二次，所以我们通过划分来降低工作量。
	
	=== "$\sqrt{n}$ 划分"
	
		我们先尝试将问题划分为 $\sqrt{n}$​ 个规模为 $\sqrt{n}$ 的子问题：
		
		- $A_1=A(1),…,A(\sqrt{n})\Rightarrow M_1$
		- $A_2​=A(\sqrt{n}​+1),…,A(2\sqrt{n}​)\Rightarrow M_2​$
		- ......
		- $A_n=A(n−\sqrt{n}+1),…,A(n)\Rightarrow M_n$
		
		最后从每个子问题得到的最大值 $M_1,M_2,…M_n$ 中选取最大值为 $A_{\text{max}}$
		
		分析：
		
		- 对于每个子问题，所需时间为 $T(n)$，工作量为 $W(n)$
		- 从这些子问题的最大值寻找整个问题的最大值时，采用的是前一种算法，因此所需时间为 $T(1)$，工作量为 $W((\sqrt{n})^2)=O(n)$
		- 由于是并行解决 $n$ 个子问题，因此对于总问题而言，有以下递推式成立：
			- $T(n)\leq T(\sqrt{n})+c_1$
		    - $W(n)\leq\sqrt{n}W(\sqrt{n})+c_2n$
		- 根据递推式，最终解得：
		    - 时间：$T(n)=O(\log⁡\log ⁡n)$
		    - 工作量：$W(n)=O(n\log\log⁡ n)$
		
		可以看到，虽然工作量下降了，但是所需时间还是变多了，因此这种改进方法还是不太好。
	
	=== "$\log\log n$ 划分"
	
		我们假设 $h=\log\⁡log ⁡n$ 为整数，此时 $n=2^{2^h}$。现在将问题划分为 $\frac{n}{h}$ 个规模为 $j$ 的子问题：
		
		- $A_1=A(1),…,A(h)\Rightarrow M_1​$
		- $A_2=A(h+1),…,A(2h)\Rightarrow M_2$
		- ......
		- $A_{\frac{n}{h}}=A(n−h+1),…,A(n)\Rightarrow M_{\frac{n}{h}}$
		
		最后从每个子问题得到的最大值 $M_1,M_2,…M_{\frac{n}{h}}$​​ 中选取最大值为 $A_{\text{max}}$
		
		分析：
		
		- 对于每个子问题，所需时间为 $T(h)$，工作量为 $W(h)$
		- 根据对之前划分的分析，最终解得：
		    - 时间：$T(n)=O(h+\log\log\frac{⁡n}{h})=O(\log\log ⁡n)$
		    - 工作量：$W(n)=O(h⋅\frac{n}{h}+\frac{n}{h}\log\log⁡\frac{n}{h})=O(n)$
		
		相比前一种划分而言，这次终于将工作量压到了线性复杂度，但是还是没能保住原来常数级的时间。
***
#### Random Sampling

具体步骤如下：

- 这里采用的是 CRCW 策略（任意规则写入）
- 先从数组 $A$ 中的 $n$ 个元素中挑选 $n^{\frac{7}{8}}$ 个元素出来，形成数组 $B$
- 将数组 $B$ 划分为多个大小为 $n^{\frac{1}{8}}$ 的小块，因此有 $n^{\frac{3}{4}}$​ 个这样的小块。然后对每个小块求出最大值，得到了 $n^{\frac{3}{4}}​$ 局部最大值（使用 Compare All Pairs 方法计算）
- 接下来将这些最大值划分为 $n^{\frac{1}{2}}​$ 个大小为 $n^{\frac{1}{4}}$ 的小块，然后对每个小块求出最大值，进而求出所有 $n^{\frac{7}{8}}​$ 个元素的最大值（使用 Compare All Pairs 方法计算）

![](../../../assets/Pasted%20image%2020241217163742.png)

复杂度分析如下：

- 第 1 次划分：
    - 时间：$M_i^{(1)}∼T=O(1)\Rightarrow T(n)=O(1)$
    - 工作量：$W_i=O((n^{\frac{1}{8}})^2)=O(n^{\frac{1}{4}})\Rightarrow W(n)=O(n)$
- 第 2 次划分：
    - 时间：$M_i^{(2)}∼T=O(1)\Rightarrow T(n)=O(1)$
    - 工作量：$W_i=O((n^{\frac{1}{4}})^2)=O(n^{\frac{1}{2}})\Rightarrow W(n)=O(n)$
- 总结：
    - 时间：$M(n^{\frac{7}{8}})∼T=O(1)$
    - 工作量：$W_i=O(n)$

伪代码如下：

```c title="Random Sampling.c"
while (there is an element larger than M) {
    for (each element larger than M)
        Throw it into random place in new B(n^{7/8})
    Compute a new M;
}
```

值得注意的是，这个算法并不保证始终得到正确结果（因为解出的是 $n^{\frac{7}{8}}$ 中最大的），但是得到正确结果的概率相当大（失败概率为 $O(\frac{1}{n^c})$），其中 $c$ 为一个正常数。