---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Chapter 05: Induction and Recursion

## Mathematical Induction

### Principle of Mathematical Induction

第一数学归纳法（The First Principle of Mathematical Induction）：$(P(1)\land\forall k(P(k)\rightarrow P(k+1)))\rightarrow\forall nP(n)$，更一般地，$\forall n[n\geq k\rightarrow P(n)]$

![image-20240412082030935](../../assets/image-20240412082030935.png)

![image-20240412082052928](../../assets/image-20240412082052928.png)

### Guidelines:Mathmatical Induction Proofs

![image-20240412084214784](../../assets/image-20240412084214784.png)

## Strong Induction and Well-ordering

第二数学归纳法/强归纳法/完全归纳法（The Second Principle of Mathematical Induction/Strong Induction/Complete Induction）：$(P(n_0)\land\forall k(k\geq n_0\land P(n_0)\land P(n_0+1)\land...\land P(k)\rightarrow P(k+1)))\rightarrow\forall nP(n)$

## Recursive Definition and Structural Induction

### Lame's Theorem

拉梅定理（Lame's Theorem）：设 $a$ 和 $b$ 是满足 $a\geq b$ 的正整数。则欧几里得算法为了求出 $\gcd(a,b)$ 而使用的除法的次数小于等于 $b$ 的十进制位数的 5 倍。

### Recursively Defined Sets

集合可以以递归的形式定义：

- 基础步骤：规定一些初始的元素。
- 递归步骤：给出用来从已知属于集合的元素来构造集合的新元素的规则。

### Strings

字母表 $\Sigma$ 上的字符串的集合 $\Sigma^*$ 递归的定义为：

- 基础步骤：$\lambda\in\Sigma^*$（其中 $\lambda$ 是不包含任何符号的空串）
- 递归步骤：若 $\omega\in\Sigma^*$ 且 $x\in\Sigma$ 则 $\omega x\in\Sigma^*$

通过连接运算可以组合两个字符串。设 $\Sigma$ 是符号的集合，$\Sigma^*$ 是 $\Sigma$ 中符号形成的字符串的集合。可以如下定义两个字符串的连接，用 $·$ 表示：

- 基础步骤：若 $\omega\in\Sigma^*$，则 $\omega·\lambda=\omega$，其中 $\lambda$ 是空串。
- 递归步骤：若 $\omega_1\in\Sigma^*$ 且 $\omega_2\in\Sigma^*$ 以及 $x\in\Sigma$ ，则 $\omega_1·(\omega_2x)=(\omega_1·\omega_2)x$

### Rooted Trees

根树（Rooted Trees）：由一个顶点集合和连接这些顶点的边组成的，顶点集合包含的一个特殊顶点称为树根。

- 基础步骤：单个顶点 $r$ 是根树。
- 递归步骤：假设 $T_1,T_2,...,T_n$ 是根树，分别带有树根 $r_1,r_2,...,r_n$。则如下形成的图也是根树：从树根 $r$ 开始，$r$ 不属于根树 $T_1,T_2,...,T_n$ 中的任何一个，从 $r$ 到顶点 $r_1,r_2,...,r_n$ 中的每个都加入一条边。

![image-20240413164928150](../../assets/image-20240413164928150.png)

### Full Binary Trees

以下这些步骤可以递归地定义满二叉树的集合：

- 基础步骤：存在一个只含有单个顶点的满二叉树。
- 递归步骤：如果 $T_1$ 和 $T_2$ 都是满二叉树，则存在一个表示为 $T_1·T_2$ 的满二叉树，它包含树根 $r$ 和连接从 $r$ 到左子树 $T_1$ 和右子树 $T_2$ 各自的根的边。

![image-20240413165412790](../../assets/image-20240413165412790.png)

### Structural Induction

结构归纳法（Structural Induction）包含如下两个部分：

- 基础步骤：证明对于递归定义的基础步骤所规定的属于该集合的所有元素来说，结果成立。
- 递归步骤：证明如果对于定义的递归步骤中用来构造新元素的每个元素来说命题为真，则对于这些新的元素来说结果成立。

e.g. 递归地定义满二叉树 $T$ 的高度 $h(T)$。

- 基础步骤：只含有树根 $r$ 的满二叉树 $T$ 的高度是 $h(T)=0$。
- 递归步骤：如果 $T_1$ 和 $T_2$ 都是满二叉树，则满二叉树 $T=T_1·T_2$ 有高度 $h(T)=1+max\{h(T_1),h(T_2)\}$

用结构归纳法证明如果 $T$ 是满二叉树，则 $n(T)\leq 2^{h(T)+1}-1$。

![image-20240413170211549](../../assets/image-20240413170211549.png)