---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 07 : Relational Database Design

## Introduction

!!! example "Example"

	我们有如下关系模式：
	
	![](../../../assets/Pasted%20image%2020250407100719.png)
	
	如果我们想合并 instructor 和 department 呢？我们会得到如下信息：
	
	![](../../../assets/Pasted%20image%2020250407100807.png)
	
	这导致了数据冗余和重复的问题（因为 ID 和 dept_name 同样都能决定 building 和 budget，而 dept_name 并非主键），这样合并而成的关系是不好的，因为重复信息有可能会造成冲突不一致的问题
	
	简单总结来说，非候选键（Candidate Key）最好不要能决定其他属性

一个不好的关系模式有如下特征：

- 信息重复（Information Repetition）
- 插入异常（Insertion Anomalies）
- 更新困难（Update Difficulty）
***
### Decomposition

**分解**（Decomposition）就是将一个（往往包含冗余信息的）模式拆分成几个更小的模式。我们希望通过这样的分解，将一个包含冗余信息的模式分为多个没有冗余信息的小模式。但这个过程并不总是一帆风顺的——

- 有时经过一次乃至多次分解后，得到的模式可能还是包含冗余信息的；
- 即使分解得到的模式都是不冗余的，但通过自然连接将它们拼好得到的模式包含了更多冗余的，甚至是没有意义的信息。我们称这样的分解为**有损分解**（Lossy Decomposition），相对应的就是**无损分解**（Lossless Decomposition）

!!! example "Examples"

	=== "Lossy Decomposition"
	
		![](../../../assets/Pasted%20image%2020250407101758.png)
		
		可以看到，分解过后的结果自然连接得到了非常多冗余甚至是错误的信息
	
	=== "Lossless-Join Decomposition"
	
		![](../../../assets/Pasted%20image%2020250407101918.png)

我们还可以用形式化的语言来描述无损分解：令 $R$ 为一个关系模式，$R_1,R_2​$ 是 分解 $R$ 得到的模式，也就是说 $R=R_1\cup R_2$。如果用 $R_1,R_2$ 替代 $R$ 后没有出现信息的损失，即 $\prod_{R_1}(r)\Join\prod_{R_2}(r)=r$，那么这种分解称为无损分解

相反地，如果有 $r\subset\prod_{R_1}(r)\Join\prod_{R_2}(r)$，那么称这种分解为有损分解（直观上理解，更多的元组会带来更多的不确定性，意味着更少的信息）

- 如果满足 $R_1\cap R_2\rightarrow R_1$ 或 $R_1\cap R_2\rightarrow R_2$，那么关系 $R$ 分解为 $R_1$ 和 $R_2$ 是无损分解
***
### Devise a Theory for the Following

> 这个准则能帮助我们判断什么样的关系是否是好的

- 如果关系 R 不是好的形式，则将其分解为一组关系 $\{R_1,R_2,\cdots,R_n\}$，满足：
	- 每一个关系 $R_i$ 都是好的形式
	- 分解为无损分解
- 这个理论基于：
	- 函数依赖关系
	- 多值依赖关系
- 范式（Normal Form）：
	- 1 NF $\rightarrow$ 2 NF $\rightarrow$ 3 NF $\rightarrow$ BCNF $\rightarrow$ 4 NF
***
## Functional Dependencies

**函数依赖**（Functional Dependencies）是用于识别关系中唯一特定属性值的**一组约束**。对于关系模式 $r(R)$ 及其属性 $\alpha,\beta\subseteq R$：

- 对于 $r(R)$ 的一个实例，如果对于其所有的元组对 $t_1,t_2$​，当 $t_1[\alpha]=t_2[\alpha]$ 时，$t_1[\beta]=t_2[\beta]$，那么称该实例满足函数依赖 $\alpha\rightarrow\beta$
- 若 $r(R)$ 上所有的实例均满足函数依赖 $\alpha\rightarrow\beta$，那么称该依赖在 $r(R)$ 上**有效**（Hold）
    - 所以可能会存在某个实例满足一些不在整个关系模式中有效的函数依赖的情况

我们可以用函数依赖的概念重新定义超键：如果 $K\rightarrow R$ 在 $r(R)$ 上有效，那么 $K$ 就是 $r(R)$ 的超键（Superkey）

函数依赖的用途：

- 检验关系实例是否满足某个给定的函数依赖 $F$
- 为某组合法关系指明约束，这样我们仅需考虑那些满足函数依赖的关系实例即可

对于某个函数依赖 $\alpha\rightarrow\beta$，如果 $\beta\subseteq\alpha$，那么这个函数依赖是**平凡的**（Trivial）
***
### Closure

#### Closure of Functional Dependencies

> 给定一组函数依赖 $F$，$F$ 在逻辑上可能包含了其他的函数依赖项，例如，如果 $A\rightarrow B,B\rightarrow C$，那么 $A\rightarrow C$

我们定义 $F$ 在逻辑上隐含的所有函数依赖关系的集合是 $F$ 的闭包，记为 $F^+$，显然 $F^+$ 是 $F$ 的超集

例如，如果 $F=\{A\rightarrow B,B\rightarrow C\}$，那么 $F^+=\{A\rightarrow B,B\rightarrow C,A\rightarrow C,AB\rightarrow B,AB\rightarrow C,\cdots\}$

我们可以反复应用阿姆斯特朗公理（Armstrong Axioms）来获得 $F$ 的闭包：

- 自反率（Reflexivity）：如果 $\beta\subseteq\alpha$，那么 $\alpha\rightarrow\beta$
- 增补率（Augmentation）：如果 $\alpha\rightarrow\beta$，那么 $\gamma\alpha\rightarrow\gamma\beta$
- 传递率（Transitivity）：如果 $\alpha\rightarrow\beta,\beta\rightarrow\gamma$，那么 $\alpha\rightarrow\gamma$

!!! example "Example"

	我们有 $R=\{A,B,C,G,H,I\},F=\{A\rightarrow B,A\rightarrow C,CG\rightarrow H,CG\rightarrow I,B\rightarrow H\}$
	
	- 由传递率及 $A\rightarrow B,B\rightarrow H$ 我们可以很容易得到 $A\rightarrow H$
	- 由 $A\rightarrow C$ 以及增补率我们可以得到 $AG\rightarrow CG$，再由传递率及 $CG\rightarrow I$ 可以得到 $AG\rightarrow I$
	- 由 $CG\rightarrow I, CG\rightarrow H$ 及增补率我们可以得到 $CG\rightarrow CGI, CGI\rightarrow HI$，再由传递率可以得到 $CG\rightarrow HI$

除了阿姆斯特朗公理我们还可以衍生出其他规则：

- 合并（Union）：如果 $\alpha\rightarrow\beta,\alpha\rightarrow\gamma$，那么 $\alpha\rightarrow\beta\gamma$
- 分解（Decomposition）：如果 $\alpha\rightarrow\beta\gamma$，那么 $\alpha\rightarrow\beta,\alpha\rightarrow\gamma$
- 伪传递（Pseudotransitivity）：如果 $\alpha\rightarrow\beta,\gamma\beta\rightarrow\delta$，那么 $\alpha\gamma\rightarrow\delta$

我们可以用如下思路来计算 $F^+$：

![](../../../assets/Pasted%20image%2020250407120726.png)
***
#### Closure of Attribute Sets

给定一组属性 $a$，将 $F$ 下的 $a$ 的闭包（用 $a^+$ 表示）定义为由 $F$ 下的 $a$ 在函数下确定的属性集

例如，如果 $F=\{A\rightarrow B,B\rightarrow C,C\rightarrow D\}$，那么 $A^+=ABCD,B^+=BCD,C^+=C$

我们可以用如下思路来计算 $\alpha$ 的闭包：

![](../../../assets/Pasted%20image%2020250407120645.png)

!!! example "Example"

	我们有 $R=\{A,B,C,G,H,I\},F=\{A\rightarrow B,A\rightarrow C,CG\rightarrow H,CG\rightarrow I,B\rightarrow H\}$
	
	计算 $(AG)^+$：
	
	1. $\text{result} = \text{AG}$
	2. $\text{result} = \text{ABCG}$（$A\rightarrow C,A\rightarrow B$）
	3. $\text{result} = \text{ABCGH}$（$CG\rightarrow H,CG\subseteq AGBC$）
	4. $\text{result} = \text{ABCGHI}$（$CG\rightarrow I,CG\subseteq AGBCH$）
***
#### Uses of Attribute Closure

在最坏情况下，属性闭包算法的时间复杂度是 $F$ 大小的二次方，通常会比直接计算 $F^+$ 更快。该算法有以下几种用途：

- 检验 $\alpha$ 是否为超键：计算 $\alpha^+$，然后看它是否包含了 $R$ 的所有属性
- 检验函数依赖 $\alpha\rightarrow\beta$ 是否有效：通过检查 $\beta\subseteq\alpha^+$ 实现
- 提供另一种计算 $F^+$ 的方法：$\forall\gamma\subseteq R$，找到其闭包 $\gamma^+$，然后 $\forall S\subseteq\gamma^+$，得到函数依赖 $\gamma\rightarrow S$

!!! example "Example"

	我们有 $R=\{A,B,C\},F=\{A\rightarrow B,B\rightarrow C\}$
	
	计算闭包：$A^+=ABC,B^+=BC,C^+=C,(AB)^+=ABC,(AC)^+=ABC,(BC)^+=ABC,(ABC)^+=ABC$
	
	$$
	\begin{aligned}
	F\Leftrightarrow\{&A\rightarrow ABC, B\rightarrow BC, C\rightarrow C, AB\rightarrow ABC, AC\rightarrow ABC, BC\rightarrow BC, ABC\rightarrow ABC\}\\
	\Leftrightarrow\{&A\rightarrow A, A\rightarrow B,A\rightarrow C, A\rightarrow AB,A\rightarrow AC,A\rightarrow BC,A\rightarrow ABC\\
	&B\rightarrow B,B\rightarrow C, B\rightarrow BC,\\
	&C\rightarrow C,\\
	&AB\rightarrow A, AB\rightarrow B,AB\rightarrow C, AB\rightarrow AB,AB\rightarrow AC,AB\rightarrow BC,AB\rightarrow ABC,\\
	&AC\rightarrow A, AC\rightarrow B,AC\rightarrow C, AC\rightarrow AB,AC\rightarrow AC,AC\rightarrow BC,AC\rightarrow ABC,\\
	&BC\rightarrow B, BC\rightarrow C, BC\rightarrow BC,\\
	&ABC\rightarrow A, ABC\rightarrow B,ABC\rightarrow C, ABC\rightarrow AB, ABC\rightarrow AC, ABC\rightarrow BC, ABC\rightarrow ABC\}\\
	=&F^+
	\end{aligned}
	$$
	
***
### Canonical Cover

函数依赖集当中可能会有冗余的一些依赖关系，可以从其他依赖关系推出来，例如在 $\{A\rightarrow B,B\rightarrow C,A\rightarrow C\}$ 中 $A\rightarrow C$ 就是冗余的；也有可能某些依赖关系还可以进行进一步简化，例如在 $\{A\rightarrow B,B\rightarrow C,A\rightarrow CD\}$ 中 $A\rightarrow CD$ 可以简化为 $A\rightarrow D$

我们定义 $F$ 的正则覆盖（Canonical Cover）为 $F$ 的“最小”功能依赖关系集，没有冗余的依赖关系或依赖关系的冗余部分

规范化来说，$F$ 的正则覆盖是一组依赖关系 $F_c$，满足：

- $F$ 逻辑蕴含 $F_c$ 中的所有依赖项
- $F_c$ 逻辑蕴含 $F$ 中的所有依赖项
- $F_c$ 中没有函数依赖项包含多余属性（Extraneous Attributes）
- $F_c$ 中函数依赖关系的左侧都是唯一的

!!! note "Extraneous Attributes"

	考虑函数依赖集合 $F$ 以及其中的一个函数依赖 $\alpha\rightarrow\beta$
	
	- **左侧**属性的移除：对于属性 $A\in\alpha$，当 $F$ 逻辑蕴含 $(F−\{\alpha\rightarrow\beta\})\cup\{(\alpha−A)\rightarrow\beta\}$ 时，$A$ 是 $\alpha$ 内的多余属性
	- **右侧**属性的移除：对于属性 $A\in\beta$，当 $(F−\{\alpha\rightarrow\beta\})\cup\{(\alpha\rightarrow(\beta−A))\}$ 逻辑蕴含 $F$ 时，$A$ 是 $\beta$ 内的多余属性
	- 上述关于逻辑蕴含的语句倒过来表述也是对的（因为有自反律）
	
	!!! example "Examples"
	
		=== "Example 01"
		
			给定 $F=\{A\rightarrow C,AB\rightarrow C\}$，那么 $B$ 在 $AB\rightarrow C$ 中是多余的，因为 $\{A\rightarrow C,AB\rightarrow C\}$ 逻辑蕴含 $A\rightarrow C$
		
		=== "Example 02"
		
			给定 $F=\{A\rightarrow C,AB\rightarrow CD\}$，那么 $C$ 在 $AB\rightarrow CD$ 中是多余的

我们可以使用如下思路来计算 $F$ 的正则覆盖：

![](../../../assets/Pasted%20image%2020250407120739.png)

- 因为该算法允许选择任意的多余属性，因此可能会得到多种正则覆盖，而这些正则覆盖都是等价的

!!! example "Example"

	我们有 $R=\{A,B,C\},F=\{A\rightarrow BC,B\rightarrow C,A\rightarrow B,AB\rightarrow C\}$
	
	- 首先，$A\rightarrow BC$ 和 $A\rightarrow B$ 是重复的，可以去掉 $A\rightarrow B$
	- $A$ 在 $AB\rightarrow C$ 中是多余的
	- $C$ 在 $A\rightarrow BC$ 中是多余的
	
	最后整合正则覆盖为 $F_c=\{A\rightarrow B,B\rightarrow C\}$
***
## Normal Forms

### Boyce-Codd Normal Form

**Boyce-Codd 范式**（Boyce-Codd Normal Form，简称 **BCNF**）能够基于函数依赖消除全部的冗余。关于函数依赖集合 $F$ 的关系 $R$，对于所有的在 $F^+$ 的函数依赖 $\alpha\rightarrow\beta$，其中 $\alpha\subseteq R,\beta\subseteq R$，至少满足以下条件之一时，称 $R$ 遵循 BCNF：

- $\alpha\rightarrow\beta$ 是一个平凡的函数依赖
- $\alpha$ 是模式 $R$ 的超键

显然，任意只有两个属性的模式必然遵守 BCNF，对于不遵守 BCNF 的模式（即至少有一个非平凡的函数依赖 $\alpha\rightarrow\beta$，$\alpha$ 不是 $R$ 的超键），我们需要对其进行分解为：

- $(\alpha\cup\beta)$
- $(R−(\beta−\alpha))$

当然，可能分解一次还是会出现不遵守 BCNF 的模式，那就对其再次分解，直到结果都遵循 BCNF 为止

我们使用如下思路来计算 BCNF：

![](../../../assets/Pasted%20image%2020250407133225.png)

- 其中每一个 $R_i$ 都是遵守 BCNF 的，且分解均为无损分解

!!! example "Example"

	对于关系 $R=\{A,B,C,D\}$ 有函数依赖集 $F=\{A\rightarrow B,B\rightarrow CD\}$
	
	（a）列出所有关系的候选键
	
	（b）将关系分解为一些 BCNF 关系的集合，且分解为无损分解
	
	??? note "Answer"
	
		![](../../../assets/Pasted%20image%2020250407134537.png)
		
		（a）由图可得候选键为 $A$
		
		（b）分解为 $R_1=\{B,C,D\},R_2=\{A,B\},F_1=\{B\rightarrow CD\},F_2=\{A\rightarrow B\}$
***
#### Dependency Preservation

令 $F$ 为模式 $R$ 的一个函数依赖集合，$R_1,R_2,\cdots,R_n$​ 为 $R$ 的一个分解，那么针对 $R_i$ 的 $F$ 的**限制**（Restriction）$F_i$​ 是一个来自 $F^+$ 的集合，但仅包含 $R_i$ 中出现的属性。检查这些限制集合 $F_1,F_2,\cdots,F_n$ 相比检查 $F$ 会更高效。令 $F'=F_1\cup F_2\cup\cdots\cup F_n$，通常来说 $F'\neq F$，但即便确实如此，也很有可能满足 $F'^+=F^+$，那么此时在 $F$ 中的每个依赖都被 $F'$ 逻辑蕴含，所以验证 $F'$ 就相当于验证 $F$ 了。我们称具备这种性质的分解为**依赖保留分解**（Dependency-Preserving Decomposition）

!!! example "Example"

	我们有 $R=\{A,B,C\},F=\{A\rightarrow B,B\rightarrow C\}$，主键为 A
	
	显然 $R$ 是不符合 BCNF 的，我们分解 $R_1=\{A,B\},R_2=\{B,C\}$，$F_1=\{A\rightarrow B\},F_2=\{B\rightarrow C\}$，此时 $R_1$ 和 $R_2$ 都符合 BCNF 且分解为无损分解，又因为 $(F_1\cup F_2)^+=F^+$，所以该分解是依赖保留分解
	
	但如果我们换一种分解方式 $R_1=\{A,B\},R_2=\{A,C\}$，$F_1=\{A\rightarrow B\},F_2=\{A\rightarrow C\}$，此时 $R_1$ 和 $R_2$ 都符合 BCNF 且分解为无损分解，但 $(F_1\cup F_2)^+\neq F^+$，所以该分解不是依赖保留分解

我们可以使用如下思路来检验依赖保留：

![](../../../assets/Pasted%20image%2020250407143154.png)

- 值得注意的是，我们并不总是能够获得保留依赖关系的 BCNF 分解
***
### Third Normal Form

关于函数依赖集合 $F$ 的关系 $R$，对于所有的在 $F^+$ 的函数依赖 $\alpha\rightarrow\beta$，其中 $\alpha\subseteq R,\beta\subseteq R$，至少满足以下条件之一时，称 $R$ 遵循**第三范式**（Third Normal Form，以下简称 **3NF**）：

- $\alpha\rightarrow\beta$ 是一个平凡的函数依赖
- $\alpha$ 是模式 $R$ 的超键
- 在 $\beta−\alpha$ 内的每个属性 $A$ 是 $R$ 的（可能是不同的）候选键的一个成员

可以看到，3NF 的前两个条件和 BCNF 相同，只是新增了第 3 个条件，可以让那些左侧不是超键的非平凡函数依赖也有机会符合这个范式。这个更为松弛的条件使得 3NF 能够确保模式分解时仍然保留了原有的依赖。

对比 BCNF，3NF 的优劣有：

- 优点：可以让关系模式在不牺牲无损或依赖保留的情况下遵循 3NF
- 缺点：可能会带来 null 值，说明存在信息重复的问题

对 3NF 下的依赖保留分解算法如下：

![](../../../assets/Pasted%20image%2020250407144959.png)

借助该算法，我们还可以重新设计 BCNF 分解算法：首先使用 3NF 算法，然后对于分解中不是 BCNF 的模式再次使用 BCNF 算法，如果得到的结果没能保留依赖，那就回退到 3NF 的设计

3NF 算法得到的结果是不唯一的，因为一个函数依赖集合里面可能包含多个正则覆盖。而且该算法可能会分解那些已经遵守 3NF 的关系，但它能够保证分解的结果还是遵守 3NF 的


