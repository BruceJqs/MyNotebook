---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 12 : Query Optimization

## Introduction

查询优化的主要思想就是寻求执行给定查询的替代方法，例如等效表达式、针对每个操作的不同算法等

!!! example "Example"

	例如我们有如下查询：
	
	```sql
	select name, title
	from instructor natural join (teaches natural join course)
	where dept_name=‘Music’ ;
	```
	
	化成关系代数即 $\prod_{\text{name,title}}(\sigma_{\text{dept\_name}=\text{music}}(\text{instructor}\Join(\text{teaches}\Join(\text{course}))))$，我们有两种方法来执行这个查询：
	
	![](../../../assets/Pasted%20image%2020250428101521.png)
	
	显然右边的查询开销更小

- 查询的评估计划之间的成本差异可能非常巨大

基于成本的查询优化步骤：

1. 使用等价规则生成逻辑上等价的表达式
2. 以不同的方式注释生成的等价表达式，以获得不同的查询计划
3. 根据估计的成本选择最便宜的计划

根据以下内容估算查询成本：

1. 关系的统计信息。例如：元组数量、某个属性的不同值数量。
2. 对中间结果的统计估计（基数估计），以计算复杂表达式的成本。
3. 使用统计信息计算的算法成本公式
***
## Generating Equivalent Expressions

### Transformation of Relational Expressions

- 如果两个关系代数表达式在每个合法的数据库实例上都能生成相同的元组集合，则称这两个表达式等价
- 在 SQL 中，输入和输出是元组的多重集
	- 如果在多重集版本的关系代数中，两个表达式在每个合法的数据库实例上都能生成相同的元组多重集，则称这两个表达式等价
- 一个等价规则表明，两种形式的表达式是等价的  
	- 可以将第一种形式的表达式替换为第二种形式，反之亦然
***
### Equivalence Rules

我们有如下常见的等价规则：

- 合取的选择操作可以被分解为一系列单独的选择操作：$\sigma_{\theta_1\land \theta_2}(\text{R})=\sigma_{\theta_1}(\sigma_{\theta_2}(\text{R}))$
- 选择操作是可交换的（Commutative）：$\sigma_{\theta_1}(\sigma_{\theta_2}(\text{R}))=\sigma_{\theta_2}(\sigma_{\theta_1}(\text{R}))$
- 如果只需要序列中的最后一个投影操作，其他的可以省略：$\prod_{L_1}(\prod_{L_2}(\cdots\prod_{L_n}(\text{R})\cdots))=\prod_{L_1}(\text{R})$
- 选择操作可以和笛卡尔积与 Theta 连接结合：
	- $\sigma_{\theta}(E_1\times E_2)=E_1\Join_{\theta}E_2$
	- $\sigma_{\theta_1}(E_1\Join_{\theta_2}E_2)=E_1\Join_{\theta_1\land\theta_2}E_2$
- Theta 连接（和自然连接）操作是可交换的：$E_1\Join_{\theta}E_2=E_2\Join_{\theta}E_1$

![](../../../assets/Pasted%20image%2020250428102911.png)

- 自然连接操作是可结合的（Associative）：$E_1\Join E_2\Join E_3=(E_1\Join E_2)\Join E_3=E_1\Join(E_2\Join E_3)$

![](../../../assets/Pasted%20image%2020250428102923.png)

- Theta 连接在如下方式当中被称为可结合的：$(E_1\Join_{\theta_1}E_2)\Join_{\theta_2\land\theta_3}E_3=E_1\Join_{\theta_1\land\theta_3}(E_2\Join_{\theta_2}E_3)$，其中 $\theta_2$ 只包含 $E_2$ 和 $E_3$ 的属性
- 选择操作在以下两个条件下对 Theta 连接操作可以分配（Distribute）
	- 当 $\theta_0$ 中的所有属性仅涉及正在连接的其中一个表达式（E1）的属性时：$\sigma_{\theta_0}(E_1\Join_{\theta}E_2)=\sigma_{\theta_0}(E_1)\Join_{\theta}E_2$
	
	![](../../../assets/Pasted%20image%2020250428103233.png)
	
	- 当 $\theta_1$ 仅涉及 $E_1$ 的属性，且 $\theta_2$ 仅涉及 $E_2$ 的属性时：$\sigma_{\theta_1\land\theta_2}(E_1\Join_{\theta}E_2)=(\sigma_{\theta_1}(E_1))\Join_{\theta}(\sigma_{\theta_2}(E_2))$
- 投影操作在以下条件对 Theta 连接操作可以分配
	- 如果 $\theta$ 只包含 $L_1\cup L_2$ 的属性：$\prod_{L_1\cup L_2}(E_1\Join_{\theta}E_2)=\prod_{L_1}(E_1)\Join_{\theta}\prod_{L_2}(E_2)$
	- 考虑一个连接 $E_1\Join_{\theta}E_2$
		- 让 $L_1$ 和 $L_2$ 分别为 $E_1$ 和 $E_2$ 的属性集合
		- 让 $L_3$ 为 $E_1$ 当中属于连接条件 $\theta$ 但是不属于 $L_1\cup L_2$ 的属性集合
		- 让 $L_4$ 为 $E_2$ 当中属于连接条件 $\theta$ 但是不属于 $L_1\cup L_2$ 的属性集合
		- $\prod_{L_1\cup L_2}(E_1\Join_{\theta}E_2)=\prod_{L_1\cup L_2}((\prod_{L_1\cup L_3}(E_1))\Join_{\theta}(\prod_{L_2\cup L_4}(E_2)))$
- 集合操作交和并是可交换的：
	- $E_1\cap E_2=E_2\cap E_1$
	- $E_1\cup E_2=E_2\cup E_1$
	- 集合差操作是不可交换的
- 集合操作交和并是可结合的：
	- $(E_1\cap E_2)\cap E_3=E_1\cap(E_2\cap E_3)$
	- $(E_1\cup E_2)\cup E_3=E_1\cup(E_2\cup E_3)$
- 选择操作在交、并、差操作当中是可分配的：
	- $\sigma_{\theta}(E_1-E_2)=\sigma_{\theta}(E_1)-\sigma_{\theta}(E_2)$
	- $\sigma_{\theta}(E_1\cap E_2)=\sigma_{\theta}(E_1)\cap\sigma_{\theta}(E_2)$
	- $\sigma_{\theta}(E_1\cup E_2)=\sigma_{\theta}(E_1)\cup\sigma_{\theta}(E_2)$
	- $\sigma_{\theta}(E_1-E_2)=\sigma_{\theta}(E_1)-E_2$
	- $\sigma_{\theta}(E_1\cap E_2)=\sigma_{\theta}(E_1)\cap E_2$
- 投影操作在并操作当中是可分配的：$\prod_{L_1}(E_1\cup E_2)=\prod_{L_1}(E_1)\cup\prod_{L_1}(E_2)$
- 选择操作在聚合操作当中是可分配的：$\sigma_{\theta}(\text{}_G\gamma_A(E))=\text{}_G\gamma_A(\sigma_{\theta}(E))$
- 完全外连接是可交换的：$E_1⟗E_2=E_2⟗E_1$
- 左外连接和右外连接是不可交换的，但是我们有：$E_1⟕E_2=E_2⟖E_1$
- 只要 $\theta_1$ 仅涉及 $E_1$ 的属性，选择操作就会如下分配在左外连接和右外连接上：
	- $\sigma_{\theta_1}(E_1⟕_{\theta}E_2)=(\sigma_{\theta_1}(E_1))⟕_{\theta}E_2$
	- $\sigma_{\theta_1}(E_2⟖_{\theta}E_1)=E_2⟖_{\theta}(\sigma_{\theta_1}(E_1))$
- 外连接在某些条件下（$\theta_1$ 在 $E_2$ 上拒绝空值（Null Rejecting），即如果 $\theta_1$ 具有当 $E_2$ 的属性为空值时，其结果为假或未知的属性）可以被内连接替代：
	- $\sigma_{\theta_1}(E_1⟕_{\theta}E_2)=\sigma_{\theta_1}(E_1\Join_{\theta}E_2)$
	- $\sigma_{\theta_1}(E_2⟖_{\theta}E_1)=\sigma_{\theta_1}(E_1\Join_{\theta}E_2)$
***
### Enumeration of Equivalent Expressions

查询优化器使用等价规则系统地生成与给定表达式等价的表达式

- 我们可以重复以下步骤生成所有等价表达式：  
	- 对迄今为止找到的每个等价表达式的每个子表达式应用所有适用的等价规则
	- 将新生成的表达式添加到等价表达式集合中
	- 直到不再生成新的等价表达式为止

上述方法在空间和时间上代价非常高，我们有以下两种方法：  

- 基于转换规则的优化计划生成
- 针对仅包含选择、投影和连接的查询的特殊情况方法——启发式方式
***
### Implementing Transformation Based Optimization

我们可以通过共享公共子表达式减少空间需求：

- 当根据等价规则从 $E_2$ 生成 $E_1$ 时，通常只有两者的顶层不同，下方的子树是相同的，可以使用指针进行共享

![](../../../assets/Pasted%20image%2020250428110309.png)

- 相同的子表达式可能会被多次生成  
	- 检测重复的子表达式并共享一份副本
- 通过不生成所有表达式来减少时间需求，即动态规划
***
## Statistics for Cost Estimation

我们定义如下符号：

- $n_r$：关系 $r$ 的元组数量
- $b_r$：包含关系 $r$ 元组的块数量
- $I_r$：关系 $r$ 的元组大小
- $f_r$：关系 $r$ 的块因子——例如每个块中包含的元组数量
	- 如果 $r$ 的元组保存在一个文件当中，那么有 $b_r=\lceil\frac{n_r}{f_r}\rceil$
- $V(A,r)$：关系 $r$ 中属性 $A$ 的不同值数量，和 $\prod_A(r)$ 的大小相同
***
### Selection Size Estimation


