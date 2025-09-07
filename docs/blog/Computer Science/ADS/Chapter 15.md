---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Chapter 15 : External Sorting

## Introduction

> 我们先前所学的所有排序算法，都是利用主存 (Main Memory) 运行的内部排序，在数据量不大（即主存能够容纳所有待排序数据）可以顺利地完成排序工作。

然而，一旦数据量很大，主存无法容下所有待排序数据时，就需要用到**外部排序**(External Sorting) 算法。所谓“外部”，即用到磁盘的空间。我们在[计算机组成](https://brucejqs.github.io/MyNotebook/blog/Computer%20Science/Computer%20Organization/Chapter%205/#memory-hierarchy-introduction)中也学过，磁盘相比主存空间更大，但访问速度更慢。举个例子：若要访问数组的某个元素 `a[i]`，它们所需的时间分别为：

- 主存：$O(1)$（用索引寻找，随机访问）
- 磁盘：找到元素所在的迹（Track）$\rightarrow$ 找到对应的区（Sector）（磁盘存储信息的最小单位）$\rightarrow$ 找到元素 `a[i]` 并传输数据
    - 这一过程的快慢还取决于设备的性能
    - 要想提升访问速度，我们应尽可能让磁盘读写头沿着一个方向移动，以避免磁盘频繁的旋转

我们将归并排序（MergeSort）作为外部排序的算法。为了简化后续的分析过程，我们假定：

- 存储数据集的容器称为**磁带**（Tape），里面的元素只能按顺序访问（这符合磁盘读写头的特性）
- 至少需要使用 3 个磁带（2 个子序列合并成 1 个更大的序列）

!!! example "Example"

	=== "Question"
	
		假设主存一次最多只能处理 $M=3$ 条记录，请通过外部排序算法（归并排序）来实现对以下序列的排序：
	
		![](../../../assets/Pasted%20image%2020241224101750.png)
	
	=== "Answer"
	
		我们称在主存中排好序的一组数据称为 **Run**，用趟（Pass）来表示归并排序合并两个子序列，形成一个更大子序列的过程
		
		=== "Pass 1"
		
			- 由于一次最多只能对 3 条记录进行排序，所以将原序列分为若干组，每组有 3 条记录，一组组地进行排序（排序算法任意）
			- 由于归并排序至少需要 3 条磁带，因此不能将排好序的组放入同一个磁带内，要分开来放，这里规定相邻的两个组放在不同的磁带里
			
			![](../../../assets/Pasted%20image%2020241224102145.png)
		
		=== "Pass 2"
		
			将两个 Tape 进行归并排序，放在两个不同的磁带里（可以使用原有空闲的磁带）
			
			![](../../../assets/Pasted%20image%2020241224102306.png)
		
		=== "Pass 3"
		
			进一步归并排序，最后就可以排序完成（最后一步略）
			
			![](../../../assets/Pasted%20image%2020241224102359.png)
		
		因此我们一共用了 $1+3=4$ 趟

- 一般情况下，若要对 $N$ 条记录进行外部排序，且主存最多对 $M$ 条记录进行排序，需要的趟数为 $1+\lceil\log_{2}\frac{N}{M}\rceil$（这里 1+ 表示数据分配到磁带的过程）

在设计外部排序的时候，我们会关心以下问题：

- **寻找**时间——$O(\text{Number of Passes})$
- **读 / 写**一个记录**块**（一组记录集）的时间
- 对 $M$ 条记录进行**内部排序**的时间
- 从输入缓存（就是磁带）**合并** $N$ 条记录到输出缓存所需的时间

要实现外部排序，需要解决以下问题：

- 减少趟的数量
- 合并 Run（一组排好序的记录）
- 用并行算法处理缓存
    - 注意：计算机可以并行处理 I/O 和 CPU
- 生成 Run
***
## Pass Reduction

### k-Way Merge

根据前面关于趟数的结论，要想减少趟数，一种很自然的想法便是增大对数函数的底数 $k$（原来 $k=2$），也就是增加子序列的个数，以 $k=3$ 为例：

!!! example "k-Way Merge"

	和上面的例子需要排序的数据一样：
	
	=== "Pass 1"
	
		![](../../../assets/Pasted%20image%2020241224103500.png)
	
	=== "Pass 2"
	
		![](../../../assets/Pasted%20image%2020241224103559.png)
		
		需要注意的是，由于需要同时比较三个数据，因此这里用到了**最小堆**，便于随时取出最小的数据，并加入下一个待排序的数据。
		
		本例中，第 3 个子序列为空，但为了一般性的解释，我们还是为第 3 个子序列预留了一个磁带。

有了以上的优化，我们的趟数就能降到 $1+\lceil\log_{k}\frac{N}{M}\rceil$，但是所需的磁带数升至 $2k$ 个，这样的开销有点难以接受，因为 $k$ 的增加也会导致内排序的复杂度增加，也会增加 pass 内的 seek 次数。
***
### Polyphase Merge

我们希望在降低趟数的同时能够尽可能避免磁带数的提升，因此尝试一下在保持子序列个数不变的情况下减少所需磁带数，下面以 $k=2$，磁带数 $=3$ 为例进行分析：

!!! example "Example"

	如果原序列已经排成了 34 个 run：
	
	![](../../../assets/Pasted%20image%2020241224105736.png)
	
	我们将原来的 34 个 run 均分为包含 17 个 run 的两个子序列，然后对它们进行合并，形成一个 17 个 run 的完整序列，此时每个 run 会包含更多排好序的记录。
	
	![](../../../assets/Pasted%20image%2020241224105910.png)
	
	- 由于这么一趟下来后只有一条磁带里包含记录，为了继续合并，还是需要将所有的 run 一分为二。因此在进入下一趟操作前，需要将包含记录的磁带的一半的 run 拷贝到另一个空磁带上。
	- 但是对于磁盘来说，拷贝所需成本有些大，所以如果像这样简单地减少磁带数量，可能会带来更大的成本损耗（像这个例子就需要 6 个 Pass，5 次拷贝）

这里给出一种更聪明的算法——**多相合并**（Polymerge Sort），它的改进之处在于：在起始步的时候，对原序列进行**不均等的分割**，形成大小不一的子序列。这样可以确保在每一趟结束后，（除了最后阶段外）始终会有多个包含记录的子序列，因此无需额外高昂的拷贝操作。照着上面的例子来看：

!!! example "Polymerge Sort"

	=== "Pass 1"
	
		我们将原序列（34 runs）划分为大小不一的两个子序列（21 runs + 13 runs）
		
		![](../../../assets/Pasted%20image%2020241224110041.png)
		
		合并两个子序列后，还会剩下两个子序列：
		
		- 其中一个是刚合并好的结果序列（13 runs）
		- 另一个是剩下未进行合并的子序列（8 runs）
		
		![](../../../assets/Pasted%20image%2020241224110353.png)
	
	=== "Pass 2"
	
		按 Pass 1 类似的方法进行合并，变成合并后的 8 runs 子序列和剩下的 5 runs 子序列：
		
		![](../../../assets/Pasted%20image%2020241224110440.png)
	
	=== "Pass 3"
	
		按 Pass 1 类似的方法进行合并，变成合并后的 5 runs 子序列和剩下的 3 runs 子序列：
		
		![](../../../assets/Pasted%20image%2020241224110556.png)
	
	=== "Pass 4"
	
		按 Pass 1 类似的方法进行合并，变成合并后的 3 runs 子序列和剩下的 2 runs 子序列：
		
		![](../../../assets/Pasted%20image%2020241224110650.png)
	
	=== "Pass 5"
	
		按 Pass 1 类似的方法进行合并，变成合并后的 2 runs 子序列和剩下的 1 run 子序列：
		
		![](../../../assets/Pasted%20image%2020241224110756.png)
	
	=== "Pass 6"
	
		按 Pass 1 类似的方法进行合并，变成合并后的 1 run 子序列和剩下的 1 run 子序列：
		
		![](../../../assets/Pasted%20image%2020241224110840.png)
	
	=== "Pass 7"
	
		最后合并完成：
		
		![](../../../assets/Pasted%20image%2020241224110927.png)
	
	一共需要 7 个 Pass

当然，这个方法非常吃分割的方法，如果我们将 34 个分割成 22 和 12，就会出现下面的情况：

![](../../../assets/Pasted%20image%2020241224111201.png)

需要 10 个 Run，还外带一次拷贝，就非常难蚌，那么怎么分才能达到上例呈现的效果呢？或许有人根据上面的例子能看出猫腻了，`13,8,5,3,2...` ，这难道不是 Fibonacci 数列嘛？下面给出结论：

- 对于两路归并排序，如果序列中 Run 的数量是一个**斐波那契数** $F_N$​，那么最好的分割情况是将它分成包含 $F_{N−1}$ 个 run 和 $F_{N−2}$ 个 run 的子序列。
    - 如果初始 run 的数量不是一个斐波那契数的话也没有问题，只需找到离该数最接近的斐波那契数，然后按照这个斐波那契数的递推式将其分成两个子序列（注意其中一个子序列可能也不是斐波那契数）
- 对于 $k$ 路归并排序，$F_N(k)=F_{N−1}(k)+⋯+F_{N−k}(k)$，其中 $F_N(k)=0(0\leq N\leq k−2),F_{k−1}(k)=1$
    - 因此，对于 $k$ 路归并排序，只需要 $k+1$ 个磁带就够了
    - 一般情况下，可能很难做到将 Run 的数量划分为多个斐波那契数，但我们应确保有尽可能多的斐波那契数
***
### Replacement Selection

> FDS Bonus 第二道题就是这个算法（回过头才发现原来第一道是计组学的 LRU hhh）

除了提升 $k$ 值外，我们还可以尝试通过生成更长的 Run 来减小趟数，这里我们用到一个称为**置换选择**（Replacement Selection）的算法来实现这一目标

!!! example "Example"

	我们基于以下序列生成一个更长的 Run：
	
	![](../../../assets/Pasted%20image%2020241224114442.png)
	
	我们还是使用大小为 3 的最小堆来选取数据，遵循一个原则：
	
	每次从堆中删除元素时，需要比较这个被删除的元素与下一个进入堆的元素：
	
	- 如果前者更小，说明后者将会与前者处于同一个 Run 内
	- 否则的话，后者要放在与前者不同的 Run 内，且它不会与堆内和它处于不同 Run 下的元素进行堆排序
	
	=== "Step 1"
	
		![](../../../assets/Pasted%20image%2020241224114850.png)
		
		前 4 个数据正常进堆
	
	=== "Step 2"
	
		![](../../../assets/Pasted%20image%2020241224115206.png)
		
		当 12 进入的时候发现出堆的 94 比它大，说明它们俩不会在同一个 Run 内，须新开一个 Run，标记为红
	
	=== "Step 3"
	
		![](../../../assets/Pasted%20image%2020241224154253.png)
		
		同理，35 比要出堆的 96 小，说明它们俩不会在同一个 Run 内，标记为红
	
	=== "Step 4"
	
		![](../../../assets/Pasted%20image%2020241224154509.png)
		
		这时候 17 入堆，新开一个 Run
	
	=== "Step 5"
	
		![](../../../assets/Pasted%20image%2020241224154651.png)
		
		一直正常进堆出堆直到 15 的出现，此时它比出堆的 75 小，不会在同一个 Run 内，标记为红
	
	=== "Step 6"
	
		![](../../../assets/Pasted%20image%2020241224154818.png)
		
		最后直到只剩 15，新开一个 Run

结论：

- 用这种算法生成得到的 Run 的平均长度 $L_{avg}=2M$
- 当序列的数据处于接近排好序的状态时，这种算法的表现就很不错
***
## Buffer Handling

那么我们该如何并行地处理缓存呢？在了解并行的做法前，我们不妨先来看一下串行的做法：

!!! example "Example"

	=== "Question"
	
		对一个包含 3250 份记录的文件排序，限制条件为：
		
		- 用于排序的计算机的主存最多能容纳 750 份记录
		- 单个的输入文件是一个包含 250 份记录的记录块
		
		可以看到，题目的模型与前面的例子是类似的，但这里我们要重点分析这个主存是如何输入和输出数据的。
	
	=== "Analysis"
	
		- 首先，我们需要将主存划分为**输入缓冲**和**输出缓冲**两个部分（此时内部排序应为归并排序）
		- 然后从两个子序列中分别读出一个记录块到输入缓存中，开始进行内部排序
		
		![](../../../assets/Pasted%20image%2020241224161424.png)
		
		- 对于输入缓存的记录，我们需要逐条记录地进行比较和排序，最后得到一部分答案
		
		![](../../../assets/Pasted%20image%2020241224161745.png)
		
		- 由于输出缓存空间有限，所以还没排完序输出缓存空间已满。因此不得不暂停排序过程，将输出缓存排好序的部分记录块丢给空闲的磁带，然后清空缓存的内容，以迎接之后的排序结果。

对于并行的情况来说：

- 修改输出缓存：
    - 在上面的例子中，我们看到，当输出缓存空间爆满时，排序就得暂时中止，这样有些浪费时间。
    - 为了让主存在清空输出缓存的同时还能继续对输入缓存的记录进行排序，我们可以将输出缓存**一分为二**（请注意，<font color="red">这并不是增加额外的空间</font>）。当其中一个输出缓存爆满，需要清空时，另一个闲置的输出缓存可以接替后续的排序任务，也就是两个输出缓存轮流保存排序结果，这样就可以确保排序的不间断进行
- 修改输入缓存：
    - 我们貌似还忽略了一个问题，输入缓存读取子序列的记录块也要时间，所以如果输入缓存的记录都排完后，那么就要到子序列读取新的记录块，这个过程也需要一定的时间，那么排序过程就又一次中断了。
    - 解决方案是借鉴输出缓存的做法，对于 $k$ 路归并排序，我们将输入缓存划分为 $2k$ 个子空间。其中的 $k$ 个子空间用于容纳正在进行排序的记录，而另外 $k$ 个子空间用于读取子序列的记录块，这样的话一半空间的记录排完后，可以紧接着对另一半的记录进行排序，不会被读取给耽搁
    - $k\uparrow\Rightarrow \text{number of input buffers}\uparrow\Rightarrow\text{buffer size}\downarrow\Rightarrow\text{block size on disk}\downarrow\Rightarrow\text{seek time}\uparrow$（即 I/O 时间的增加），因此这种划分方法对于更大的 $k$ 而言效果可能不是特别好。为了取得最佳效果，我们需要综合磁盘参数和用于缓存的主存空间容量来选择合适的 $k$ 值
***
## Minimizing the Merge Time

另一种提升外部排序的速度的想法是：令合并时间最小化。这里我们借助哈夫曼编码——在合并数个长度不一的 run 时，我们应避免多次合并长度较长的 run，而哈夫曼编码的贪心策略正符合我们的需求。下面来看个例子，以便更清楚地了解该算法在合并过程中的应用：

!!! example "Example"

	=== "Question"
	
		假设我们有 4 个 Run，长度分别为 2, 4, 5, 15。请计算最小的合并时长。
	
	=== "Answer"
	
		最小时间 $= 2 * 3 + 4 * 3 + 5 * 2 + 15 * 1 = 43$

结论：最小合并时间 $= O(\text{the weighted external path length})$（哈夫曼树的带权路径和）
***
## Homework

!!! question "Question 01"

	If only one tape drive is available to perform the external sorting, then the tape access time for any algorithm will be $\Omega(N^2)$.
	
	??? note "Answer"
	
		True. 因为只有一个 Tape Drive，那么寻迹时间会增加

!!! question "Question 02"

	Suppose we have the internal memory that can handle 12 numbers at a time, and the following two runs on the tapes:
	
	**Run 1**: 1, 3, 5, 7, 8, 9, 10, 12
	
	**Run 2**: 2, 4, 6, 15, 20, 25, 30, 32
	
	Use 2-way merge with 4 input buffers and 2 output buffers for parallel operations. Which of the following three operations are NOT done in parallel?
	
	- A. 1 and 2 are written onto the third tape; 3 and 4 are merged into an output buffer; 6 and 15 are read into an input buffer
	- B. 3 and 4 are written onto the third tape; 5 and 6 are merged into an output buffer; 8 and 9 are read into an input buffer
	- C. 5 and 6 are written onto the third tape; 7 and 8 are merged into an output buffer; 20 and 25 are read into an input buffer
	- D. 7 and 8 are written onto the third tape; 9 and 15 are merged into an output buffer; 10 and 12 are read into an input buffer
	
	??? note "Answer"
	
		D. 7 and 8 are written onto the third tape; 9 and 15 are merged into an output buffer; 10 and 12 are read into an input buffer
		
		模拟一下整个过程：
		
		=== "Step 1"
		
			- 1,3 写入 Input Buffer 1，此时没有 Merge 条件
			
			| B1  | B2  | B3 | B4 | B5 | B6 |
			|-----|-----|----|----|----|----|
			| 1,3 | -  | -  | -  | -  | -  |
		
		=== "Step 2"
		
			- 2,4 写入 Input Buffer 2，此时没有 Merge 条件
			
			| B1  | B2  | B3 | B4 | B5 | B6 |
			|-----|-----|----|----|----|----|
			| 1,3 | 2,4 | -  | -  | -  | -  |
		
		=== "Step 3"
		
			- 5,7 写入 Input Buffer 3
			- 1,2 Merge，写入 Output Buffer 1
			
			| IB1  | IB2  | IB3 | IB4 | OB1 | OB2 |
			|-----|-----|----|----|----|----|
			| 3 | 4 | 5,7 | -  | 1,2 | -  |
		
		=== "Step 4（对应 A 选项）"
		
			- 6,15 写入 Input Buffer 4
			- 3,4 Merge，写入 Output Buffer 2
			- 1,2 输出到 Tape
			
			| IB1  | IB2  | IB3 | IB4 | OB1 | OB2 |
			|-----|-----|----|----|----|----|
			| -  | -  | 5,7 | 6,15 | -  | 3,4 |
		
		=== "Step 5（对应 B 选项）"
		
			- 8,9 写入 Input Buffer 1
			- 5,6 Merge，写入 Output Buffer 1
			- 3,4 输出到 Tape
			
			| IB1  | IB2  | IB3 | IB4 | OB1 | OB2 |
			|-----|-----|----|----|----|----|
			| 8,9  | -  | 7 | 15 | 5,6 | -  |
		
		=== "Step 6（对应 C 选项）"
		
			- 20,25 写入 Input Buffer 2
			- 7,8 Merge，写入 Output Buffer 2
			- 5,6 输出到 Tape
			
			| IB1  | IB2  | IB3 | IB4 | OB1 | OB2 |
			|-----|-----|----|----|----|----|
			| 9  | 20,25 | -  | 15 | -  | 7,8 |
		
		=== "Step 7（对应 D 选项）"
		
			- 10,12 写入 Input Buffer 3
			- 9,10 Merge，写入 Output Buffer 1
			- 7,8 输出到 Tape
			
			| IB1  | IB2  | IB3 | IB4 | OB1 | OB2 |
			|-----|-----|----|----|----|----|
			| -  | 20,25 | 12 | 15 | 9,10 | -  |
			
			- 事实上，写入和输出是可以并行的，但是 Merge 还是有时序性的，这里 D 选项就错在此时 10 有被读进来，所以就紧随着去 Merge 了
		
		=== "Step 8"
		
			- 30,32 写入 Input Buffer 1
			- 12,15 Merge，写入 Output Buffer 2
			- 9,10 输出到 Tape
			
			| IB1  | IB2  | IB3 | IB4 | OB1 | OB2 |
			|-----|-----|----|----|----|----|
			| 30,32 | 20,25 | -  | -  | -  | 12,15 |
		
		=== "Step 9 & 10"
		
			分别完成 20,25，30,32 的 Merge 与输出



