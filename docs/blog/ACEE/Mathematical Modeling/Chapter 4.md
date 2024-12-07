---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 
# Chapter 04 :  图论模型

## 图

- **图**是一个有序二元组 $G=(V,E)$，其中 $V$ 是顶点（Vertex）集合，$E$ 是边（Edge）的集合。$E$ 中每条边 $e$ 与 $V$ 中两个顶点关联（Incident）。
	- 若与边关联的两个顶点有序，则称图为有向图（Digraph），否则称为无向图
	- 图可以用以点表示顶点，以曲线段表示边的图形来表示，但图与图形表示（Diagrammatic Representation）中点和曲线段在图形中的相对位置无关
	
	![](../../../assets/Pasted%20image%2020241204165609.png)
	![](../../../assets/Pasted%20image%2020241204165635.png)
	
- **度**：无向图 $G$ 中与顶点 $v$ 关联的边的数目称为 $v$ 的度，记为 $d(v)$ 或 $deg_G(v)$
	- 图的所有顶点的度的最大值与最小值分别称为最大度和最小度， 记为 $\Delta(G)$ 和 $\delta(G)$
	- （握手定理）所有顶点的度之和等于边数的两倍，即 $\sum\limits_{v\in V}d(v)=2|E|$
- 子图
	- 图 $G'=(V',E')$ 称为图 $G=(V,E)$ 的一个子图（Subgraph），若 $V'\subseteq V,E'\subseteq E$，且 $G'$ 中边的关联关系在 $G'$ 中保持不变
		- 生成子图：$V'=V$
		- 导出子图：$G(V'),G\textbackslash V',G(E'),G\textbackslash E'$
	
	![](../../../assets/Pasted%20image%2020241204165859.png)
	
- 树
	- 连通的无圈图称为树（Tree）
	- 图 $G$ 的生成子图称为生成树（Spanning Tree）
		- 最小生成树（MST）是赋权图所有生成树中总权和最少的生成树
		- 可以用 Kruskal 和 Prim 算法解决
***
### 简单图

两端点相同的边称为环（Loop），两端点分别相同的多条边称为平行边（Parallel Edges）

既没有环，也没有平行边的图称为简单图（Simple Graph）。不是简单图的图称为多重图（Multigraph）

- 完全图
	- 任何两个不同顶点之间都有边相连的简单图称为完全图（Complete Graph）
	- $n$ 个顶点的完全图记为 $K_n$， $K_n$ 的边数为 $\frac{n(n−1)}{2}$
- 简单图的顶点数与边数
	- 若 $G=(V,E)$ 为简单图，则边数的上下界为 $|V|−1\leq |E|\leq\frac{|V|(|V|−1)}{2}$
	- 边数接近上界的称为稠密图（Dense Graph），边数远离上界的称为稀疏图（Sparse Graph）

![](../../../assets/Pasted%20image%2020241204165348.png)
***
### 路

- 顶点和边交替出现的序列 $v_{i_0}e_{i_1}v_{i_1}e_{i_2}...e_{i_k}v_{i_k}$，且序列中与每条边相邻的两个顶点为该边的两个端点，称为连接顶点 $v_{i_0}$ 和 $v_{i_k}$ 的途径（Walk）
	- 若图为简单图，可省略途径中边的符号
	- 经过边互不相同的途径称为迹（Trail）
		- 起点和终点相同的迹称为闭迹
	- 经过顶点互不相同的途径称为路（Path）
		- 起点和终点相同，其余顶点互不相同，也不与起点和终点相同的途径称为圈（Cycle）
		- 边赋权图中一条路所含边的权之和称为它的长度
		- 最短路：图 $G=(V,E)$ 中起点为 $s$，终点为 $t$ 的长度最短的路称为 $s$ 到 $t$ 的最短路（Shortest Path），可以用 Bellman-Ford（无负权圈）、Dijkstra（非负权图，时间复杂度 $O(|E|+|V|\log|V|)$）、Floyd-Warshall（无负权圈）算法解决

![](../../../assets/Pasted%20image%2020241204165308.png)
***
### 二部图与连通

- 二部图
	- 若图的顶点集可以划分为两个非空集合 $X$ 和 $Y$，使得图中任一条边的两个端点分属 $X,Y$ 两个集合，则称该图为二部图（Bipartite Graph），记为 $G=(X\bigcup Y,E)$
		- $X$ 中所有顶点与 $Y$ 中所有顶点都有边相连的二部图称为完全二部图
	- $G$ 是二部图当且仅当 $G$ 中不存在奇圈
- 连通
	- 若无向图中两顶点 $u,v$ 之间有路相连，则称 $u,v$ 连通（Connected）
	- 无向图中任意两顶点均连通的图称为连通图（Connect Graph）

![](../../../assets/Pasted%20image%2020241204165212.png)
***
### 最短连接

给定 Euclidean 平面上 $n$ 个点，如何用总长度最短的若干条线段将它们连接起来？

用最小生成树解决最短连接问题：构造 $n$ 个顶点的赋权完全图 $K_n$，边的权为它的两个端点的Euclidean 距离。问题的解即为 $K_n$ 的最小生成树

#### 最小 Steiner 树

允许增加任意多个 Steiner 点的最短连接（就是说，可以在原有的点集中增加任意多个点，使得最后的连接线段总长度最短）

![](../../../assets/Pasted%20image%2020241204230135.png)

- Gilbert-Pollak 猜想：最小 Steiner 树长度不小于最小生成树长度的 32 倍（当 $n=3,4,5,6$ 时结论是成立的）
***
#### Hamilton 圈与 Hamilton 图

经过图的所有顶点恰好一次的圈称为 Hamilton 圈（Hamiltion cycle）

存在 Hamilton 圈的图称为 Hamilton 图

!!! example "Examples"

	=== "Icosian Game"
	
		问题描述：一个正十二面体的二十个顶点各代表一个城市，是否有一条从某个城市出发，沿正十二面体的棱行走，经过每个城市恰好一次，最后回到出发城市的路线？
		
		![](../../../assets/Pasted image 20241208132611.png)
		
	=== "骑士环游（Knight's Tour）"
	
		在 $8\times 8$ 国际象棋棋盘上，马能否按其走子规则，从一个格子出发，经过其它格子恰好一次，最后回到起点？
		
		- 构造“跳马图”，每一格子为图的一个顶点，两个格子之间有 边相连当且仅当马可按走子规则从一个格子跳到另一个格子
		
		![](../../../assets/Pasted image 20241208132834.png)
		
		- 推广到一般情况，$m\times n(m\leq n)$ 方格棋盘对应的“跳马图”为 Hamilton 图，除非：
			- $m,n$ 均为奇数
			- 或 $m=1,2,4$
			- 或 $m=3,n=4,6,8$
***
### 特殊顶点集

