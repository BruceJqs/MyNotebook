# 搜索引擎中的 PageRank 模型

## 搜索引擎

### 搜索引擎（search engine）

- 一种用于帮助用户查找因特网信息的技术工具。其工作原理是先以一定的策略在因特网中搜索，发现信息，然后对信息进行理解、提取、组织和处理，最后为用户提供信息和服务。
***
### 互联网信息获取的特点与难点

- 互联网上有海量信息，网页及其内容处于动态变化中，缺乏统一管理
- 具有相同关键词的网页数量众多，如何展示搜索结果，提升用户搜索体验
- 如何给出一种<font color="red">合理、客观、定量、可操作</font>的网页排序规则，使“重要”的网页在搜索结果中靠前显示
***
### PageRank 的网页排序机制

- 互联网中的网页通过超链接（hyperlink）关联
- 网页的重要程度由网页之间的链接关系决定
***
## 网页重要度

### 网页重要度的原则与假设

- <font color="pink">某网页重要，是因为有重要的网页链接到它</font>
	- 对任一网页 A，确定一数值为其<font color="blue">重要度</font>，作为网页排序的依据
	- 链接到网页 A 的所有网页对网页 A 的重要度均有贡献，贡献大小与这些网页自身的重要度有关
- <font color="blue">传递性</font>：重要度大的网页链接到网页 A 时对网页 A 的重要度的贡献比重要度小的网页链接到网页 A 时对网页 A 的重要度的贡献大
	- 某网页对其他网页重要度的贡献之和等于它的重要度
- <font color="blue">等效性</font>：网页对它所链接的每个网页的重要度的贡献相等
	- 某网页对其他网页的重要度贡献与它所链接的网页数量呈反比
- <font color="blue"> 叠加性</font>：链接到网页 A 的网页越多，网页 A 越重要
	- 网页 A 的重要度是所有链接到 A 的网页对网页 A 的重要度的贡献之和
- <font color="blue">无关性</font>：网页链接其他网页的多少，与其本身的重要度无关
***
### 网络链接图

- 互联网中网页之间的链接关系可用<font color="red">图</font>表示，称为<font color="blue">网络链接图</font>
	- 顶点：网页 $v_1,v_2,...,v_n$
	- 弧：网页间的链接关系
		- 若网页 $v_i$ 上有链接指向网页 $v_j$，则网络链接图中有一条以 $v_i$ 为起点，$v_j$ 为终点的弧
	- 出度：以某顶点为起点的弧的总数，即该网页链接的网页数量

![](../../../assets/Pasted%20image%2020240915160217.png)
***
### 网页重要度

- 网页 $v_i$ 的重要度记为 $x_i$，出度记为 $q_i$
	- 网页 $v_i$ 对其它网页重要度贡献之和为 $x_i$（传递性）
	- 网页 $v_i$ 与它链接的 $q_i$ 个网页中的任一个的重要度贡献为 $\frac{x_i}{q_i}$（等效性）
	- 若链接到网页 $v_j$ 的网页有 $v_{j_1},v_{j_2},...,v_{j_k}$，则 $x_j=\frac{x_{j_1}}{q_{j_1}}+\frac{x_{j_2}}{q_{j_2}}+...+\frac{x_{j_k}}{q_{j_k}}$（叠加性、无关性）
- 线性方程组

	$$
	\begin{aligned}
	x_j &= \frac{x_{j_1}}{q_{j_1}}+\frac{x_{j_2}}{q_{j_2}}+...+\frac{x_{j_k}}{q_{j_k}},j = 1,...,n\\
	&= p_{i1}x_1 + p_{i2}x_2 + ... + p_{in}x_n = \sum\limits_{j=1}^np_{ij}x_j
	\end{aligned}
	$$
***
## 随机矩阵

### 随机矩阵

- 各行（列）元素之和均为 1 的<font color="red">非负方阵</font>称为<font color="blue">行（列）随机矩阵</font>（row(column) strochastic matrix）
- 各行与各列元素之和均为 1 的<font color="red">非负方阵</font>称为<font color="blue">双随机矩阵</font>（doubly strochastic matrix）
***
### 随机矩阵的特征值

- 1 是随机矩阵的特征值

!!! 证明

	- 对行随机矩阵，我们很容易就能取到特征向量为全为1的列向量，此时特征值为1。
	- 对列随机矩阵，因为转置前后特征值相同，所以也是1。

- 任一随机矩阵的<font color="blue">模最大特征值</font>为 1

!!! 证明

	- 设 $\lambda$ 是行随机矩阵 $P = (p_{ij})_{n\times n}$ 的特征值，非零向量 $X = (x_1,...,x_n)^T$ 为属于特征值 $\lambda$ 的特征向量。设 $|x_i|=max(|x_j|)>0(1\leq j \leq n)$
	- 由 $PX=\lambda X$，可得 $\lambda x_i = \sum\limits_{j=1}^n p_{ij}x_j$
	- 两边取<font color="red">模</font>，$|\lambda||x_i|=|\lambda x_i|= |\sum\limits_{j=1}^{n} p_{ij}x_j|\leq\sum\limits_{j=1}^{n}|p_{ij}||x_j|\leq|x_i|\sum\limits_{j=1}^n|p_{ij}|=|x_i|$，即 $|\lambda|\leq 1$


***
## 链接矩阵

- 令 $p_{ij} = \begin{cases}\frac{1}{q_j}\space,若有链接自  v_j 链向 v_i\\\space 0\space\space,其他\end{cases}$
	- 记矩阵 $P = (p_{ij})_{n\times n}$ 为（初始）<font color="blue">链接矩阵</font>，$X = (x_1,...,x_n)^T$ 为网页<font color="blue">重要度向量</font>
	- $X$ 为线性方程组 $X=PX$ 的解
		- $rank(I-P)<n$
		- 矩阵 $P$ 有特征值 1
		- 矩阵 $P$ 的每列元素之和为 1，为列随机矩阵

!!! Example 

	=== "Question"
	
		![](../../../assets/Pasted image 20240915161607.png)
	
	=== "Answer"
	
		有线性方程组：
		
		$$
		\left\{
		\begin{array}{}
		x_1= \space\space\space\space\space\space\space& & x_3 & +\frac{1}{2}x_4\\
		x_2= \frac{1}{3}x_1& & &\\
		x_3= \frac{1}{3}x_1& +\frac{1}{2}x_2& & +\frac{1}{2}x_4\\
		x_4 = \frac{1}{3}x_1& +\frac{1}{2}x_2
		\end{array}
		\right.
		$$
		
		其中：
		
		$$
		P = \begin{pmatrix}
		0 & 0 & 1 & \frac{1}{2}\\
		\frac{1}{3} & 0 & 0 & 0\\
		\frac{1}{3} & \frac{1}{2} & 0 & \frac{1}{2}\\
		\frac{1}{3} & \frac{1}{2} & 0 & 0
		\end{pmatrix}
		$$
		
		$$
		I - P = \begin{pmatrix}
		1 & 0 & -1 & -\frac{1}{2}\\
		-\frac{1}{3} & 1 & 0 & 0\\
		-\frac{1}{3} & -\frac{1}{2} & 1 & -\frac{1}{2}\\
		-\frac{1}{3} & -\frac{1}{2} & 0 & 1
		\end{pmatrix}
		$$
		
		解得 $x_1 = \frac{12}{31},x_2 = \frac{4}{31},x_3 = \frac{9}{31},x_4 = \frac{6}{31}$

- 但是，线性方程组 $X=PX$ 还会有特殊情况：

??? Question1

	=== "Question"
	
		- 节点没有出度
		
		![](../../../assets/Pasted image 20240915172214.png)
	
	=== "Solution"
	
		- 悬挂网页（dangling link）
			- 若某网页不链接任意其它网页，我们称之为**悬挂网页**。显然，悬挂网页的出度为 0，但它的重要度不为 0。将链接矩阵 $P$ 中对应列的所有元素由 0 修改为 $\frac{1}{n}$ ，得到（修正）链接矩阵 $\overline{P}$  

??? Question2

	- 线性方程组有多个解

