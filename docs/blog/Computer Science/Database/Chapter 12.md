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

对于单条件选择来看，有两种情况：

- $\sigma_{A=V}(r)$
	- $n_r/V(A,r)$：满足选择条件要求的记录数量
	- 若 A 为键：大小为 1
- $\sigma_{A\leq V}(r)$
	- 记 $c$ 为符合条件的元组数量
	- 如果 $\min(A,r)$ 和 $\max(A,r)$ 存在：
		- 如果 $V<\min(A,r)$，那么 $c=0$
		- $c=n_r$，$\frac{v-\min(A,r)}{\max(A,r)-\min(A,r)}$
	- 如果没有统计信息，$c$ 被假定为 $\frac{n_r}{2}$
***
### Size Estimation of Complex Selections

我们定义条件 $\theta_i$ 的中选率（Selectivity）为关系 $r$ 中元组满足条件 $\theta_i$ 的概率，如果记 $s_i$ 为 $r$ 中满足条件 $\theta_i$ 的元组数量，那么有 $\text{Selectivity}=\frac{s_i}{n_r}$

- 对于一个合取条件选择 $\sigma_{\theta_1\land\theta_2\land\cdots\land\theta_n}(r)$，假设它们互相独立，那么结果当中预计的元组数量为 $n_r\times\frac{s_1\times s_2\times\cdots\times s_n}{n_r^n}$
- 对于一个析取条件选择 $\sigma_{\theta_1\lor\theta_2\lor\cdots\lor\theta_n}(r)$，假设它们互相独立，那么结果当中预计的元组数量为 $n_r\times\big[1-(1-\frac{s_1}{n_r})(1-\frac{s_2}{n_r})\cdots(1-\frac{s_n}{n_r})\big]$
- 对于条件选择 $\sigma_{\neg\theta}(r)$ ，预计的元组数量为 $n_r-\text{size}(\sigma_{\theta}(r))$
***
### Estimation of the Size of Joins

- 笛卡尔积 $r\times s$ 包含 $n_r\times n_s$ 个元组，每个元组占据 $s_r+s_s$ 字节
- 如果 $R\cap S=\phi$，那么 $r\Join s$ 和 $r\times s$ 相同
- 如果 $R\cap S$ 是 $R$ 的一个主键，那么 $s$ 的一个元组最多会跟 $r$ 的一个元组连接
	- 因此，$\text{The Number of Tuples in }r\Join s\leq n_s$
	
	![](../../../assets/Pasted%20image%2020250428192732.png)
	
- 如果 $R\cap S$ 在 $S$ 中是 $S$ 引用 $R$ 的外键，那么 $r\Join s$ 中元组的数量和 $s$ 中的元组数量相同
	
	![](../../../assets/Pasted%20image%2020250428193039.png)
	
- 如果 $R\cap S=\{A\}$ 并不是 $R$ 或是 $S$ 的键，那么如果我们假设每个 $R$ 中的元组 $t$ 都会在 $R\Join S$ 中产生元组，那么 $R\Join S$ 中元组的个数估计为 $\frac{n_r*n_s}{V(A,s)}$；同理如果 $S$ 中的元组 $t$ 都会在 $R\Join S$ 中产生元组，那么 $R\Join S$ 中元组的个数估计为 $\frac{n_r*n_s}{V(A,r)}$
***
### Size Estimation for Other Operations

- 投影操作：$\prod_A(r)$ 的估计大小为 $V(A,r)$
- 聚合操作：$\text{}_A\mathcal{G}_F(r)$ 的估计大小为 $V(A,r)$
- 集合操作：
	- 对于交和并在同一关系的选择操作，可以通过等价规则将其转化为单一条件的选择操作的大小估计，例如 $\sigma_{\theta_1}(r)\cup\sigma_{\theta_2}(r)$ 可以被重写为 $\sigma_{\theta_1\lor\theta_2}(r)$
	- 对于在不同关系的选择操作：
		- $r\cup s$ 的估计大小为 $r$ 的大小与 $s$ 的大小之和
		- $r\cap s$ 的估计大小为 $r$ 和 $s$ 的大小的最小值
		- $r-s$ 的估计大小为 $r$ 的大小
		- 所有的估计大小可能并不准确，但是至少提供了大小的上界
- 外连接操作：
	- 对于左外连接 $r⟕s$，估计大小为 $r\Join s$ 的大小加上 $r$ 的大小，右外连接同理
	- 对于全外连接 $r⟗s$，估计大小为 $r\Join s$ 的大小加上 $r$ 和 $s$ 的大小
****
### Estimation of Number of Distinct Values

> 大小估计通常取决于某个属性不同值的数量。需要计算中间结果的不同值

- ​若 A 取特定值​：$V(A, \sigma_{\theta}(r)) = 1$
- ​若 A 取指定集合中的某个值：$V(A, \sigma_{\theta}(r)) =$ 指定值的数量
- ​若选择条件 $\theta$ 是 A op v 形式（如比较操作符）：估计 $V(A, \sigma_{\theta}(r)) = V(A, r) \times s$，其中 s 是选择条件的选择率
- ​其他所有情况，使用近似估计：$V(A, \sigma_{\theta}(r)) = \min(V(A, r),n_{\sigma_{\theta}(r)})$
	- 更准确的估计可以通过概率论获得，但这种估计通常效果良好
- 对投影的不同值的估计较为简单，它们在 $\prod_A(r)$ 中与在 $r$ 中是相同的
- 聚合的分组属性也是如此，对于聚合值：
	- $\min(A)$ 和 $\max(A)$，不同值的数量可以估计为 $\min(V(A,r), V(G,r))$，其中 $G$ 表示分组属性
	- 对于其他聚合函数，假设所有值都是不同的，使用 $V(G,r)$
***
## Choice of Evaluation Plans

### Cost-Based Optimizer

- 在选择评估计划时，必须考虑评估技术的相互作用
	- 独立地为每个操作选择最便宜的算法可能无法得到最佳的整体算法。例如：
		- 合并连接（Merge-Join）的成本可能高于哈希连接（Hash-Join），但可能提供排序输出，从而降低外层聚合的成本
		- 嵌套循环连接（Nested-Loop Join）可能为流水线处理提供机会
- 实用的查询优化器结合了以下两种广泛方法的要素：
	1. 搜索所有计划并以基于成本的方式选择最佳计划
	2. 使用启发式方法选择计划
***
### Join Order Optimization Algorithm

- 要为一组 n 个关系找到最佳连接树：
	- 要为一组 n 个关系的集合 S 找到最佳计划，考虑所有形式为：$S_1\Join(S - S_1)$的可能计划，其中 $S_1$ 是 S 的任意非空子集  
	- 递归计算将 S 的子集进行连接的代价，以找出每个计划的代价。从 $2^n- 2$ 种选择中选出成本最小的那个
	- 递归的基本情况：单个关系访问计划  
		- 使用 $R_i$ 上的最佳索引选择对 $R_i$ 应用所有选择操作  
	- 当计算出任何子集的计划时，存储该计划，并在再次需要时重用它，而不是重新计算它，这便是动态规划的思想

!!! note "Pseudo Code"

	![](../../../assets/Pasted%20image%2020250428204437.png)
	
	![](../../../assets/Pasted%20image%2020250428204449.png)
***
## Left Deep Join Trees

- 在左深连接树中，每个连接的右侧输入是一个关系，而不是中间连接的结果

![](../../../assets/Pasted%20image%2020250428204542.png)
***
## Cost of Optimization

- 使用动态规划
	- 对于茂密树的优化时间复杂度为 $O(3^n)$
	- 空间复杂度为 $O(2^n)$
- 为了找到一组 n 个关系的最佳左深连接树：  
	- 考虑 n 种选择，每次将一个关系作为右侧输入，其他关系作为左侧输入  
	- 修改优化算法：  
		- 将“对于 S 的每个非空子集 $S_1$，使得 $S_1\neq S$” 替换为：对于 S 中的每个关系 r，令 $S_1 = S - r$
- 如果只考虑左深树： 
	- 找到最佳连接顺序的时间复杂度为 $O(n\times 2^n)$
	- 空间复杂度仍为 $O(2^n)$  
- 基于成本的优化成本高昂，但对于大型数据集上的查询来说是值得的（典型查询的 n 较小，通常 < 10）
***
## Heuristic Optimization

- 基于成本的优化即使采用动态规划也会耗费大量资源
- 系统可能会使用启发式方法来减少必须以基于成本的方式进行选择的次数
- 启发式优化（Heuristic Optimization）通过使用一组规则来转换查询树，这些规则通常（但并非在所有情况下）能提高执行性能：  
	- 尽早执行选择操作（减少元组数量）  
	- 尽早执行投影操作（减少属性数量）  
	- 在其他类似操作之前执行最具限制性的选择和连接操作（即结果集最小的操作）
	- 采用左深连接顺序  
	- 有些系统仅使用启发式方法，而另一些系统则将启发式方法与部分基于成本的优化相结合
***
## Additional Optimization Techniques

### Optimizing Nested Subqueries

- SQL 在概念上将从句中的嵌套子查询视为函数，这些函数接收参数并返回单个值或一组值
	- 参数是来自外层查询的变量，在嵌套子查询中使用；这样的变量被称为相关变量（Correlation Variables）  
- 从概念上讲，对于外层 FROM 子句生成的笛卡尔积中的每个元组，嵌套子查询会执行一次
	- 这种求值方式称为相关执行（Correlated Evaluation） 
	- 注意：在 WHERE 子句中的其他条件可能会用于在执行嵌套子查询之前计算连接（而不是笛卡尔积）
- 相关性评估可能效率极低，因为可能会对嵌套查询进行大量调用，从而可能导致不必要的随机 I/O
- SQL 优化器会尝试在可能的情况下将嵌套子查询转换为连接操作，以便使用高效的连接技术

!!! example "Example"

	对于一个嵌套查询：
	
	```sql
	select name from instructor
	where exists (select * from teaches where instructor.ID=teaches.ID and teaches.year=2022)
	```
	
	也可以重写为：
	
	```sql
	select name from instructor, teaches
	where instructor.ID = teaches.ID and teaches.year=2022
	```
	
	关系代数为 $\prod_{\text{name}}(\text{instructor}\Join_{\text{instructor.ID}=\text{teaches.ID}\land\text{teaches.year}=2022}\text{teaches})$
	
	可以看到，两个查询会产生不同数量的重复项，这是因为 teaches 可能会有重复的 ID，我们可以使用半连接运算符进行修改，以正确处理重复项
	
	修改关系代数为 $\prod_{\text{name}}(\text{instructor}⋉_{\text{instructor.ID}=\text{teaches.ID}\land\text{teaches.year}=2022}\text{teaches})$，甚至为 $\prod_{\text{name}}(\text{instructor}⋉_{\text{instructor.ID}=\text{teaches.ID}}(\sigma_{\text{teaches.year}=2022}\text{teaches}))$，这样重复项数量就是正确的了
	
	- 事实上，上面的关系代数还等价于 `select name from instructor where ID in (select teaches.ID from teaches where teaches.year=2022)`

总的来说，形如 `select A from r1, r2, ..., rn where P1 and exists(select * from s1, s2, ..., sm where P21 and P22)` 的 sql 语句可以被复写为 $\prod_{A}(\sigma_{P_1}(r_1\times r_2\times\cdots\times r_n)⋉_{P_2^2}\sigma_{P_2^1}(s_1\times s_2\times\cdots\times s_m)$

- 其中 $P_2^1$ 包含不涉及任何相关变量的谓词，$P_2^2$ 包含涉及相关变量的谓词
- 将嵌套查询替换为使用连接或半连接（可能涉及临时关系）的过程称为**去除相关**​（Decorrelation）
	- 在某些情况下，可以通过分组/聚合来实现标量聚合子查询的去除相关操作
- 在嵌套子查询涉及聚合操作，或者当嵌套子查询是标量子查询时，去除相关操作变得更加复杂，在这些情况下，系统会采用**关联式评估**​（Correlated Evaluation）
***
### Materialized Views

- 物化视图（Materialized Views）是一个预先计算的查询结果集，可以存储在数据库中以供后续查询使用，节省了查找多个元组的开销
- 保持物化视图与底层数据同步的任务被称为物化视图维护
- 物化视图可以通过每次更新时重新计算来维护，但是更好的选择是使用增量视图维护（Incremental View Maintenance），通过数据库关系的变更来计算物化视图的变更，然后对其进行更新
- 视图维护可以通过以下方式实现：  
	- 手动在视图定义中每个关系的插入、删除和更新操作上定义触发器  
	- 手动编写代码，在数据库关系更新时更新视图
	- 定期重新计算（例如每天一次）
	- 上述方法许多数据库系统直接支持，且避免了手动操作/正确性问题

对关系或表达式进行的插入和删除操作被称为其**差分**​（Differential）。插入到关系 r 中的元组集合记为 $i_r​$，从 r 中删除的元组集合记为 $d_r​$。为简化描述，我们仅考虑插入和删除操作，而将**元组的更新**​（Update）操作拆分为两步：先删除原元组，再插入更新后的新元组
***
#### Join Operation

考虑物化视图 $v=r\Join s$ 以及对 $r$ 的更新：

- 记 $r^{\text{old}}$ 和 $r^{\text{new}}$ 为关系 $r$ 前后的状态
- 考虑对 $r$ 的一次插入：
	- 我们可以将 $r^{\text{new}}\Join s$ 写为 $(r^{\text{old}}\cup i_r)\Join s$
	- 然后将其重写为 $(r^{\text{old}}\Join s)\cup(i_r \Join s)$
	- 可以看到，$r^{\text{old}}\Join s$ 和原来的视图一模一样，因此增量变化就是 $i_r\Join s$
- 因此，对于插入操作 $v^{\text{new}}=v^{\text{old}}\cup(i_r\Join s)$；相似地对于删除操作 $v^{\text{new}}=v^{\text{old}}-(d_r\Join s)$

![](../../../assets/Pasted%20image%2020250428221442.png)
***
#### Selection and Projection Operations

对于选择操作我们考虑一个视图 $v=\sigma_{\theta}(r)$：

- $v^{\text{new}}=v^{\text{old}}\cup\sigma_{\theta}(i_r)$
- $v^{\text{new}}=v^{\text{old}}-\sigma_{\theta}(d_r)$

对于投影操作，对于投影 $\prod_A(r)$ 中的每个元组，我们将记录它被获取的次数

- 当向 $r$ 中插入一个元组时，如果结果元组已存在于 $\prod_A(r)$ 中，我们就增加其计数；否则，我们添加一个计数为 1 的新元组
- 当从 $r$ 中删除一个元组时，我们减少 $\prod_A(r)$ 中相应元组的计数。如果计数变为 0，我们就从 $\prod_A(r)$ 中删除该元组
***
#### Aggregation Operations

- count：考虑视图 $v=\text{}_A\mathcal{G}_{\text{count}(B)}(r)$
	- 当每个元组 $i_r$ 被插入时，对于每一个元组 $r$，如果对应的组已经存在于 $v$ 当中，我们只需要增加计数器，否则我们需要添加一个新的组并将其计数器设置为 1
	- 当每个元组 $d_r$ 被删除时，我们寻找 $v$ 当中的组 $t.A$，减少计数器，如果计数器变为 0，则删除该组
- sum：考虑视图 $v=\text{}_A\mathcal{G}_{\text{sum}(B)}(r)$
	- 我们可以用类似计数器的方式来维护 sum 的值
	- 当然我们也需要维护 count 来检测没有元组的组，这样的组需要被删除
- avg：我们只需要分别维护 sum 和 count 的值，最后将其相除即可
- min/max：考虑视图 $v=\text{}_A\mathcal{G}_{\text{min}(B)}(r)$
	- 插入操作相对简单，我们只需要比较新元组的值和当前最小值，如果新元组的值更小，我们就更新最小值
	- 删除操作开销比较大，我们需要遍历所有元组，找到最小值并更新

!!! quesion "为什么我们在 sum 中还需要维护一个 count，而不是直接检测 sum=0 的情况？"

	这是因为即使一个组还存在元组，这些元组的 $B$ 值加起来也有可能恰好为 0
***
#### Other Operations

- 集合交集：考虑视图 $v=r\cap s$
	- 当一个元组插入 $r$ 时，我们需要检查它是否在 $s$ 中，如果在，我们就将其插入到 $v$ 当中
	- 当一个元组从 $r$ 中删除时，我们需要检查它是否在交集当中，如果在，我们就将其从 $v$ 中删除
- 其他集合操作类似
***
#### Handling Expressions

要处理整个表达式，我们从最小的子表达式开始，推导出用于计算每个子表达式结果的增量变化的表达式

