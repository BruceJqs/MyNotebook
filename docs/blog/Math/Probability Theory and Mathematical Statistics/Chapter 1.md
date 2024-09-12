# Chapter 01 : 概率论的基本概念

!!! Abstracts

	本章和离散数学集合知识非常相似，具体也可请移步：[Discrete mathmatics notes-Chapter 02: The Basic Structures:Sets,Functions,Sequences,Sums and Matrices](https://brucejqs.github.io/MyNotebook/blog/Math/Discrete%20mathmatics/Discrete%20mathmatics%20notes-Ch02/)

## 随机试验

自然界与社会生活中有两类现象：

- 确定性现象：结果确定
- 不确定性现象：结果不确定
	- 个别现象
	- 随机现象：在个别试验中其结果呈现出不确定性，但在大量重复试验中其结果又具有统计规律性

!!! Definition

	对随机现象的观察、记录、实验统称为<font color="red">随机试验</font>。它具有以下特性：
	
	- 可以在相同的条件下重复进行
	- 每次试验可能出现的结果是不确定的, 但能事先知道试验的所有可能结果
	- 每次试验完成前不能预知哪一个结果会发生

## 样本空间 · 随机事件

### 样本空间

!!! Definition

	随机试验 E 的所有结果构成的集合称为 E 的<font color="red">样本空间</font>，记为 $S={e}$，称 S 中的元素 e 为<font color="red">样本点</font>。
	
	!!! Examples
	
		- 一枚硬币抛一次
			- $S={正面，反面}$
		- 记录一城市一日中发生交通事故次数
			- $S={0,1,2,...}$

### 随机事件

!!! Definition

	一般我们称 S 的子集 A 为 E 的<font color="red">随机事件</font> A，简称为<font color="red">事件</font> A。当且仅当 A 所包含的一个样本点发生称<font color="red">事件 A 发生</font>。它具有如下特征：
	
	- 事件 A 是相应的样本空间 S 的一个子集，其关系可以用维恩（Venn）图来表示
	- 事件 A 发生当且仅当 A 中的某个样本点出现
	- 事件 A 的表示可用集合，也可用语言来表示

特别地：

- 一个样本点组成的单点集称为<font color="red">基本事件</font>。
- 如果每次试验事件 S 总是发生，那么称 S 为<font color="red">必然事件</font>
- 记 $\Phi$ 为空集，不包含任何样本点，即每次试验 $\Phi$ 都不发生，则称 $\Phi$ 为<font color="red">不可能事件</font>

## 事件的关系及运算

### 事件的关系（包含、相等）

- 包含（$A\subset B$）：事件 A 发生一定导致 B 发生

![](../../../assets/Pasted%20image%2020240912110309.png)

- 相等（$A=B$）$\Leftrightarrow\begin{cases}A\subset B\\ B\subset A\end{cases}$ 

### 事件的运算

!!! 事件的运算

	=== "和事件"
	
		- A 与 B 的和事件，记为 $A\bigcup B$
		- $A\bigcup B = {x|x\in A 或 x\in B}$
		- A 与 B 至少有一个发生
	
		![](../../../assets/Pasted image 20240912110819.png)
	
		- $\bigcup\limits_{i=1}^n A_i : A_1, A_2,..., A_n$ 至少有一发生
	
	=== "积事件"
	
		- A 与 B 的积事件，记为 $A\bigcap B, A·B, AB$
		- $A\bigcap B = {x|x\in A 且 x\in B}$
		- A 与 B 同时发生
		
		![](../../../assets/Pasted image 20240912111046.png)
		
		- $\bigcap\limits_{i=1}^n A_i : A_1, A_2,..., A_n$ 同时发生
		- 当 $AB=\Phi$ 时，称事件 A 和 B 是<font color="red">不相容的
		  </font>，或<font color="red">互斥的</font>。
	
	=== "逆事件"
	
		- A 的逆事件记为 $\overline{A}$，有 $\begin{cases}A\bigcup\overline{A}=S\\ A\overline{A} = \emptyset \end{cases}$
		- 若 $\begin{cases}A\bigcup B=S\\ AB = \emptyset \end{cases}$，则称 A, B 互逆（互为对立事件）。
		
		![](../../../assets/Pasted image 20240912111911.png)
	
	=== "差事件"
	
		- 事件 A 对事件 B 的差事件：$A - B = A\overline{B} = {x|x\in A 且 x\not\in B$
	
		![](../../../assets/Pasted image 20240912112118.png)
	
	=== "德摩根定律"
	
		- $\overline{\bigcap\limits_{i=1}^n A_i} = \bigcup\limits_{i=1}^n \overline{A_i} = \overline{A_1}\bigcup\overline{A_2}\bigcup\overline{A_3}\bigcup...\bigcup\overline{A_n}$
		- $\overline{\bigcup\limits_{i=1}^n A_i} = \bigcap\limits_{i=1}^n \overline{A_i} = \overline{A_1}\overline{A_2}\overline{A_3}...\overline{A_n}$