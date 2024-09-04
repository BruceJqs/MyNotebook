---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Chapter 11: Trees

## Introduction to Trees

### Tree

> 定义 1：<font color="red">树（Tree）</font>是没有简单回路的连通无向图。

因为树没有简单回路，所以树不含多重边或环。因此任何树都必然是简单图。

> 定义 2：不含简单回路但不一定连通的图是<font color="red">森林（Forest）</font>。

森林的每个连通分支都是树。

> 定理 1：一个无向图是树当且仅当在它的每对顶点之间存在唯一简单通路。

### Root Tree

> 定义：<font color="red">有根树（Root Tree）</font>是指定一个顶点作为根并且每条边的方向都离开根的树。

#### Parent VS Child

若 $v$ 是 $T$ 中的非根顶点，则 $v$ 的<font color="red">父母（Parent）</font>是从 $u$ 到 $v$ 存在有向边的唯一的顶点 $u$ 。当 $u$ 是 $v$ 的父母时，$v$ 称为 $u$ 的<font color="red">孩子（Child）</font>。

#### Sibling

具有相同父母的顶点称为<font color="red">兄弟（Sibling）</font>。

#### Ancestors VS Descendants

非根顶点的<font color="red">祖先（Ancestors）</font>是从根到该顶点通路上的顶点，不包括该顶点自身但包括根。顶点 $v$ 的<font color="red">后代（Descendants）</font>是以 $v$ 作为祖先的顶点。

#### Leaf

树的顶点若没有孩子，则该顶点称为<font color="red">树叶（Leaf）</font>。

#### Internal Vertex

有孩子的顶点称为<font color="red">内点（Internal Vertex）</font>。

#### Subtree

若 $a$ 是树中的顶点，则以 $a$ 为根的<font color="red">子树（Subtree）</font>是由 $a$ 和 $a$ 的后代以及这些定点所关联的边所组成的该树的子图。

### m-ary Rooted Trees

若有根树的每个内点都有不超过 $m$ 个孩子，则称它为<font color="red"> $m$ 叉树（m-ary Rooted Trees）</font>。若该树的每个内点都恰好有 $m$ 个孩子，则称它为<font color="red">满 $m$ 叉树（Full m-ary Tree）</font>。把 $m=2$ 的 $m$ 叉树称为二叉树。

### Ordered Rooted Tree

> 定义：<font color="red">有序根树（Ordered Rooted Tree）</font>是把每个内点的孩子都排序的有根树。

画有序根树时，以从左向右的顺序来显示每个内点的孩子。

在有序二叉树（通常只称为二叉树）中，若一个内点有 $2$ 个孩子，则第一个孩子称为<font color="red">左子（Left Child）</font>而第二个孩子称为<font color="red">右子（Right Child）</font>。以一个顶点的左子为根的树称为该顶点的<font color="red">左子树（Left Subtree）</font>，而以一个顶点的右子为根的树称为该顶点的<font color="red">右子树（Right Subtree）</font>。

### Properties of Trees

> 定理 1：带有 $n$ 个顶点的树含有 $n-1$ 条边。

> 定理 2：带有 $i$ 个内点的满 $m$ 叉树含有 $n=mi+1$ 个顶点。

> 定理 3：一个满 $m$ 叉树若有：
>
> (i) $n$ 个顶点，则有 $i=\frac{n-1}{m}$ 个内点和 $l=\frac{(m-1)n+1}{m}$ 个树叶。
>
> (ii) $i$ 个内点，则有 $n=mi+1$ 个顶点和 $l=(m-1)i+1$ 个树叶。
>
> (iii) $l$ 个树叶，则有 $n=\frac{ml-1}{m-1}$ 个顶点和 $i=\frac{l-1}{m-1}$ 个内点。

### Level of Vertices and Height of Trees

根树中的一个顶点 $v$ 的<font color="red">等级（Level）</font>是从根到 $v$ 的唯一通路的长度。

一个根树的<font color="red">高度（Height）</font>是其所有顶点的等级的最大值。

### Balanced m-ary Trees

若一颗高度为 $h$ 的 $m$ 叉树的所有树叶都在 $h$ 层或 $h-1$ 层，则这棵树是<font color="red">平衡的（Balanced）</font>。

### The Bound for the Number of Leaves in an m-ary Tree

定理：在高度为 $h$ 的 $m$ 叉树中至多有 $m^h$ 个树叶。

## Applications of Trees

二叉搜索树与决策树与 fds 讲述内容相同。

### Prefix Codes

为了保证没有比特串对应着多个字母的序列，可以令一个字母 de 比特串永远不出现在另一个字母的比特串的开头部分，具有这个性质的编码称为<font color="red">前缀码（Prefix Codes）</font>，可以用任何二叉树来构造一个前缀码，其中每个内点的左边都用 0 标记，而右边都用 1 标记，树叶都用字符标记。字符都用从根到这个树叶的唯一通路中的边的标记所组成的比特串来编码。

e.g. 把 e 编码成 0，把 a 编码成 10，把 t 编码成 110，把 n 编码成 1110，把 s 编码成 1111（如下图），则编码为 11111011100 的单词为 sane。

![](../../assets/image-20240606111441491.png)

### Huffman Coding

## Tree Traversal

与 fds 所讲前中后序遍历、表达式树相同。

## Spanning Trees

深度宽度优先搜索、回溯等算法均在 fds 讲解过。

### The Definition of Spanning Tree

定义：设 $G$ 是简单图，$G$ 的生成树是包含 $G$ 的每个顶点的 $G$ 的一颗树。

定理：简单图是连通的当且仅当它有生成树。

## Minimum Spanning Trees

与 fds 中所讲最小生成树算法（Prim、Kruskal）相同。
